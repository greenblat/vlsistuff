
import types,string
from logs import log_error,log_info

import traceback
from scan_rtl import  compute1

MathOptsStr = '~ ! & && ~& !& ^ !^ ~^ | || ~| !|'
MathOpts = MathOptsStr.split()

Between = '_HIER_'
def constant_inputs(Current,Env):
    Lits = []
    for Dst,Src,_,_ in Current.hard_assigns:
        if is_literal(Src,Current):
            Lits.append((Dst,Src))
    for Inst in Current.insts:
        Obj = Current.insts[Inst]
        for Pin in Obj.conns:
            Con = Obj.conns[Pin]
            for Lit,Repl in Lits:
                if same_expr(Con,Lit,Current):
                    print('replacement same input %s %s'%(Con,Repl))
                    Obj.conns[Pin]=Repl
                    

def remove_buffers(Current,Env):
    Renames=prepare_trans_table(Current)
    print('renames len=%d'%len(Renames.keys()))
    for ind,(Dst,Src,A,B) in enumerate(Current.hard_assigns):
        Src1 = translate_expr(Src,Renames)
        Current.hard_assigns[ind]=(Dst,Src1,A,B)
    for Inst in Current.insts:
        Obj = Current.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig1 = translate_expr(Sig,Renames)
            Obj.conns[Pin]=Sig1

def translate_expr(Src,Renames):
    if type(Src)is str:
        if Src in Renames:
            return Renames[Src][1]
        else:
            return Src
    if type(Src)is tuple:
        return Src
    if type(Src)is list:
        if Src[0]=='const':
            return Src
        if Src[0] in MathOpts:
            res=[Src[0]]
            for X in Src[1:]:
                Y = translate_expr(X,Renames)
                res.append(X)
            return res
    return Src


def output_sig(Dst,Current):
    if Dst not in Current.nets:
        return False
    Dir,Wid = Current.nets[Dst]
    return 'output' in Dir
        

def prepare_trans_table(Current):
    Holder={}
    Renames={}
    for Dst,Src,_,_ in Current.hard_assigns:
        if (type(Dst)is str) and (not output_sig(Dst,Current)) and simple_sig_source(Src):
            Holder[str(Dst)]=(Dst,Src)
    for Key in Holder:
        print('holder',Key,Holder[Key])
    for Key in Holder:
        Renames[Key]=Holder[Key]
    Hards=[]
    for Dst,Src,A,B in Current.hard_assigns:
        if str(Dst) not in Renames:
            Hards.append((Dst,Src,A,B))
    Current.hard_assigns=Hards

    Ok=True    
    while Ok:
        Ok=False    
        Keys = list(Renames.keys())
        for Key in Keys:
            (Dst,Src)=Renames[Key]
            Key1 = str(Src)
            if Key1 in Holder:
                (Dst1,Src1)=Holder[Key1]
                Renames[Key]=(Dst,Src1)    
                Ok=True
    return Renames


def simple_sig_source(Src):
    if not Src:
        return True
    if type(Src)is str:
        return True
    if type(Src)is tuple:
        return True
    if type(Src)is list:
        if Src[0] in ['const','subbit','subbus']:
            return True
    return False



def is_literal(Expr,Current):
    if type(Expr)is tuple:
        return True
    if type(Expr)is list:
        return Expr[0] in ['const','bin','hex']

    return False


def same_expr(Aex,Bex,Current):
    Alist = make_sig_list(Aex,Current)
    Blist = make_sig_list(Bex,Current)
    if len(Alist)!=len(Blist):
        return False
        
    return Alist==Blist

MoreDontFlattens = ['and','or','not','nand','nor','xor']
def flatten(Current,Whome,Env,load_module):
    Current.create_stat_types()
    if 'and' not in Env.DontFlattens:
        Env.DontFlattens.extend(MoreDontFlattens)
    dones = 0
    if (Whome in Current.insts):
        Type = Current.insts[Whome].Type
        if Type not in Env.Modules:
            load_module(Type,Env)
        if Type not in Env.Modules:
             Env.DontFlattens.append(Type)
             print('dont flatten %s (from %s) because not loaded'%(Type,Current.Module))
        else:
            flatten_inst(Current,Whome,Env.Modules)
    else:
        Insts= list(Current.insts.keys())
        for Inst in Insts:
            if (Whome=='*')or(Current.insts[Inst].Type==Whome)or(Current.insts[Inst].Type in Whome):
                 Type = Current.insts[Inst].Type
                 if (Type not in Env.DontFlattens):
                     if Type not in Env.Modules:
                         load_module(Type,Env)
                     if Type not in Env.Modules:
                         Env.DontFlattens.append(Type)
                         print('dont flatten %s (from %s) because not loaded'%(Type,Current.Module))
                     else:
                        flatten_inst(Current,Inst,Env.Modules)
                        print('FLATTEN',Inst,Type)
                        dones += 1
    return dones,(Inst,Type)


def flatten_deep(Current,Whome,Env,load_module):
    Dones=1
    Max = 30
    while (Dones>0) and (Max>0):
        Dones,Who = flatten(Current,Whome,Env,load_module)
        print('dones',Dones)
        Max -= 1
    

def flatten_inst(Current,InstName,modules):
    Type = Current.insts[InstName].Type
    Instobj = Current.insts[InstName]
    Conns = Instobj.conns
    Son = modules[Type]
    for Param in Son.parameters:
        Current.parameters[Param]=Son.parameters[Param]
    for Param in Son.localparams:
        Current.localparams[Param]=Son.localparams[Param]
    Translate = prepare_mapping_table(Current,Instobj,modules)
    for (Dst,Src,Dly,Stren) in Son.hard_assigns:
        Dst1 =  flatten_trans(InstName,Dst,Translate,Son)
        Src1 =  flatten_trans(InstName,Src,Translate,Son)
        Current.add_hard_assign(Dst1,Src1,Dly,Stren)
        Current.check_net_def(Dst1)
        Current.check_net_def(Src1)
    for Soninst in Son.insts:
        Sonobj = Son.insts[Soninst]
        Sontype = Sonobj.Type
        if (Soninst in Current.insts)or(Current.stat_types[Type]>1)or(Current.deepInstNames):
            Soninst = combine_inst_name(InstName,Sonobj.Name)
        Obj = Current.add_inst(Sontype,Soninst)
        for Sonprm in Sonobj.params:
            Val = Sonobj.params[Sonprm]
            Obj.add_param(Sonprm,Val)

        for Net in Son.nets:
            Dir,Wid = Son.nets[Net]
            if (Dir in ['wire','reg'])and(type(Wid)is tuple)and(Wid[0]=='double'):
                Current.nets['%s_%s'%(InstName,Net)]=(Dir,Wid)
        for Sonpin in Sonobj.conns:
            Sonsig = Sonobj.conns[Sonpin]
            Sonsig1 = flatten_trans(InstName,Sonsig,Translate,Son)
            Current.check_net_def(Sonsig1)
            Current.add_conn(Soninst,Sonpin,Sonsig1)
    if InstName not in Current.insts:
        logs.log_error('inst %s for flat is not in %s' % (InstName,Current.Module))
    Current.del_inst(InstName)
        

def combine_inst_name(Inst,Son):
    if (Son[0]=='\\'):
        Son=Son[1:]
    Soninst = '%s%s%s'%(Inst,Between,Son)
    Soninst = Soninst.replace('[','_')
    Soninst = Soninst.replace(']','_')
    Soninst = Soninst.replace('\\','')
    Soninst = Soninst.replace(' ','')
    return Soninst

def check_instance_against_module(Current,Instobj,modules):
    Type = Instobj.Type
    Son = modules[Type]

    Conns = list(Instobj.conns.keys())
    Conns.sort()
    Exts=[]
    for Net in Son.nets:
        (Dir,_)  = Son.nets[Net]
        if Dir not in ['wire','reg']:
            Exts.append(Net)
    Exts.sort()
    Bads=0
    for A1 in Conns:
        if A1 not in Exts:
            log_error('check_instance_against_module connected pin=%s of instance=%s of module=%s  not in definition of module %s'%(A1,Instobj.Name,Current.Module,Type))
            Bads += 1
    if (Bads>0):
        for Ext in Exts:
            log_info('ext: %s'%Ext)

    for A2 in Exts:
        if A2 not in Conns:
            print('check_instance_against_module external pin=%s of module %s not connected at instance=%s in module=%s'%(A2,Type,Instobj.Name,Current.Module))



def prepare_mapping_table(Current,Instobj,modules):
    check_instance_against_module(Current,Instobj,modules)
    Type = Instobj.Type
    Son = modules[Type]

    Translate={}
    for SonPin in Instobj.conns:
        SonSig = Instobj.conns[SonPin]
        try:
            (Dir,HsLs)=Son.nets[SonPin]
        except:
            print('prepare_mapping_table SonPin=%s (%s/%s) is not net in %s '%(SonPin,Instobj.Type,Instobj.Name,Current.Module))
            Dir='wire'
            HsLs=0,0
        if (type(HsLs)is tuple)and(HsLs[0]=='double'):
            H,L = total_width(Current,HsLs)
        elif type(HsLs) is tuple:
            H = Son.compute_int(HsLs[0])
            L = Son.compute_int(HsLs[1])
        else:
            H = HsLs
            L = HsLs
        
        Sigs = make_sig_list(SonSig,Current)
        Range = len(Sigs)
        if SonSig and (len(Sigs)!= (H-L+1)):
            log_error('wrong connection width for pin %s for sig %s lensigs=%d h=%d l=%d sontype=%s father=%s'%(SonPin,SonSig,len(Sigs),H,L,Type,Current.Module))
            Range = min(Range,(H-L+1))

        if not SonSig:
            Range=(H-L+1)
            Translate[SonPin]=False
            j=0
            for i in range(Range-1,-1,-1):
                PP = '%s[%d]'%(SonPin,i)
                Translate[PP]=False
                j+=1
        elif (len(Sigs)==1):
            Translate[SonPin]=Sigs[0]
        else:
            Translate[SonPin]=SonSig
            j=0
            for i in range(Range-1,-1,-1):
                PP = '%s[%d]'%(SonPin,i)
                Translate[PP]=Sigs[j]
                j+=1

    return Translate

def total_width(Son,HsLs):
    if type(HsLs)is tuple:
        return 1
    if type(HsLs)is tuple:
        if len(HsLs)==2:
            H = Son.compute_int(HsLs[0])
            L = Son.compute_int(HsLs[1])
            return H,L

    H = Son.compute_int(HsLs[1][0])
    L = Son.compute_int(HsLs[1][1])
    Wid0 = (H-L)+1
    H = Son.compute_int(HsLs[2][0])
    L = Son.compute_int(HsLs[2][1])
    Wid1 = (H-L)+1
    H = Wid0*Wid1-1
    L = 0
    return (H,L)

def make_sig_list(Sig,Mod):
    if not Sig:
        return [Sig]
    if (type(Sig)is str):
        if Sig in Mod.nets:
            Dir,HsLs = Mod.nets[Sig]
            if (HsLs==0):
                return [Sig]
            elif (HsLs[0]=='double'):
                H,L = total_width(Mod,HsLs)
                res=[]
                for II in range(H,-1,-1):
                    res.append(['subbit',Sig,II])
                return res
            else:
                return make_sig_list(['subbus',Sig,HsLs[0],HsLs[1]],Mod)
        if Sig[0]=='\\':
                return make_sig_list(Sig[1:],Mod)
        if Sig=='$unconnected':
            return [Sig]
        log_error('sig for flatten %s not found in %s'%(Sig,Mod.Module),True)
        return [Sig]
    if (type(Sig)is list)and(Sig[0]=='bin'):
        return make_sig_list(['const',Sig[1],'b%s'%Sig[2]],Mod)
    if (type(Sig)is list)and(Sig[0]=='hex'):
        return make_sig_list(['const',Sig[1],'h%s'%Sig[2]],Mod)

    if (type(Sig)is list)and(Sig[0]=='const'):
        Wid = Mod.compute_int(Sig[1])
        if (Wid==1):
            return [ ['const',Sig[1],Sig[2]] ] 

        Base = Sig[2][0]
        Data = Sig[2][1:]
        if (Base=='b'):
            Val = int(Data,2)
        elif (Base=='h'):
            Val = int(Data,16)
        elif (Base=='d'):
            Val = int(Data,10)
        else:
            Val=0
            log_error('bad base for const %s"%s'%(Sig[1],Sig[2]))
        res=[]    
        for i in range(Wid):
            V = (Val>>i)&1
            res.append(['const',1,'b%d'%V])
        res.reverse()
        return res
            



    if (type(Sig)is list)and(Sig[0]=='subbit'):
        Bus = Sig[1]
        _,Wid = Mod.nets[Bus]
        if (type(Wid)is tuple)and(len(Wid)==3)and(Wid[0]=='double'):
            H1 = Mod.compute_int(Wid[1][0])
            L1 = Mod.compute_int(Wid[1][1])
            H2 = Mod.compute_int(Wid[2][0])
            L2 = Mod.compute_int(Wid[2][1])
            Pos = Mod.compute_int(Sig[2])
            Mul = (H2-L2+1)
            res=[]
            for i in range(H1,L1-1,-1):
                res.append(['subbit',Bus,str(i+Mul*Pos)])
            return res
            
        return [Sig]

    if (type(Sig)is list)and(Sig[0]=='subbus'):
        Bus = Sig[1]
        _,Wid = Mod.nets[Bus]
        if len(Sig)==3:
            H = int(Sig[2][0])
            L = int(Sig[2][1])
        elif len(Sig)==4:
            H = compute1(Sig[2],Mod)
            L = compute1(Sig[3],Mod)
        else:
            log_error('bus indexing failed %s  "%s" '%(Bus,Sig))
            H=1
            L=0
        if (type(Wid)is tuple)and(len(Wid)==3)and(Wid[0]=='double'):
            H1 = Mod.compute_int(Wid[1][0])
            L1 = Mod.compute_int(Wid[1][1])
            H2 = Mod.compute_int(Wid[2][0])
            L2 = Mod.compute_int(Wid[2][1])
            res=[]
            Mul = (H2-L2+1)
            for JJ in range(H,L-1,-1):
                for II in range(H1,L1-1,-1):
                    res.append(['subbit',Bus,str(II+Mul*JJ)])
            return res
            
        else:    
            res=[]
            for i in range(H,L-1,-1):
                res += [ ['subbit',Bus,str(i)]]
            return res
    if (type(Sig)is list)and(Sig[0]=='curly'):
        res=[]
        for Item in Sig[1:]:
            res += make_sig_list(Item,Mod)
        return res

    log_error('make_sig_list failed on %s'%(str(Sig)))
    return [Sig]


NCCON=0
def flatten_trans(Inst,Sig,Translate,SonMod):
    global NCCON
    X=flatten_trans2(Inst,Sig,Translate,SonMod)
    if (X==''):
        X = 'nc_con%d'%(NCCON)
        NCCON+=1
        
    return X

def relax_inst(Inst):
    Soninst=Inst
    if (Inst[0]=='\\'):
        Soninst = Inst[1:]
    if (Inst[-1]==' '):
        Soninst = Inst[:-1]
    Soninst = Soninst.replace('[','_')
    Soninst = Soninst.replace(']','_')
    Soninst = Soninst.replace('\\','')
    Soninst = Soninst.replace(' ','')
#    Soninst = Soninst.replace('.','_')
    return Soninst


def flatten_trans2(Inst,Sig,Translate,SonMod):
    if (Sig=='$unconnected'):
        return '$unconnected'
    if (Sig==False):
        return False
    if (Sig==None):
        return None
    if (type(Sig)is str)and("'" in Sig):
        return Sig
    if (type(Sig)is str)and(Sig in Translate):
        return Translate[Sig]
    if (type(Sig)is str)and(Sig not in Translate):
        if (Sig==''):
            return ''
        if (Sig in SonMod.nets):
            Dir,Wid = SonMod.nets[Sig]
            if type(Wid)is tuple:
                if len(Wid)==2:
                    H = SonMod.compute_int(Wid[0])
                    L = SonMod.compute_int(Wid[1])
                    return flatten_trans(Inst,['subbus',Sig,H,L],Translate,SonMod)
                elif (len(Wid)==3)and(Wid[0]=='double'):
                    H,L = total_width(SonMod,Wid)
                    return flatten_trans(Inst,['subbus',Sig,H,L],Translate,SonMod)
                    

        if (Sig[0]=='\\'):
            Sig = Sig[1:]
        Inst1 = relax_inst(Inst)
        if (Sig[0]=='\\'):
            Sig = relax_inst(Sig)
        return '%s_%s'%(Inst1,Sig)
    if (type(Sig)is list)and(Sig[0]=='const'):
        return Sig
    if (type(Sig)is list)and(Sig[0] in ['bin','hex']):
        Lii = make_sig_list(Sig,SonMod)
        if len(Lii)==1:
            return Lii[0]
        return ['curly']+Lii
    if (type(Sig)is tuple):
        return Sig

    if (type(Sig)is list)and(Sig[0]=='repeat'):
        Many = SonMod.compute_int(Sig[1])
        LL = make_sig_list(Sig[2],SonMod)
        return ['curly']+LL * Many
    if (type(Sig)is list)and(Sig[0]=='subbit'):
        Bus=Sig[1]
        if (Bus[0]=='\\'):
            Bus = relax_inst(Bus)
        Ind=Sig[2]
        Bsig = '%s[%s]'%(Bus,Ind)
        if (Bsig in Translate):
            return Translate[Bsig]
        return ['subbit',Inst+'_'+Bus,Ind]

    if (type(Sig)is list)and(Sig[0]=='subbus'):
        Bus=Sig[1]
        if (Bus[0]=='\\'):
            Bus = relax_inst(Bus)
        if len(Sig)==3:
            H = SonMod.compute_int(Sig[2][0])
            L = SonMod.compute_int(Sig[2][1])
        elif len(Sig)==4:
            H = SonMod.compute_int(Sig[2])
            L = SonMod.compute_int(Sig[3])
        else:
            log_error('bus indexing failed %s  "%s" '%(Bus,Sig))
            H=1
            L=0
        res=[]
        for i in range(H,L-1,-1):
            res += [flatten_trans(Inst,['subbit',Bus,str(i)],Translate,SonMod)]
        return ['curly']+res

    if (type(Sig)is list)and(Sig[0]=='curly'):
        res = ['curly']
        for X in Sig[1:]:
            Y = flatten_trans(Inst,X,Translate,SonMod)
            res += [Y]
        return res
    if (type(Sig)is list)and(Sig[0]=='question'):
        res = ['question']
        for X in Sig[1:]:
            Y = flatten_trans(Inst,X,Translate,SonMod)
            res += [Y]
        return res
    if (type(Sig)is list)and(Sig[0] in MathOpts):
        res = [Sig[0]]
        for X in Sig[1:]:
            Y = flatten_trans(Inst,X,Translate,SonMod)
            res += [Y]
        return res


    log_error('flatten_trans inst=%s for %s failed'%(Inst,Sig),True)
    return '%s_%s'%(Inst,Sig)

    
