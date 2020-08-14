import os,string,sys
from logs import *
import traceback
import types
import module_class

import new_flattens
import fixingModule
import interactive
import logs

def select_current(Env):
    if (Env.Current==None):
        Keys = Env.Modules.keys()
        Keys.sort()
        if (len(Keys)==1):
            TT = Keys[0]
            Env.Current=Env.Modules[TT]
        elif (len(Keys)>0):
            TT = Keys[0]
            Env.Current=Env.Modules[TT]
            log_warning('since no -top given, %s selected randomly'%(TT))

def execute_line(Line,Env):
    RegisteredList = Registered.split()
    wrds = Line.split()
    print('execute_line "%s"'%(wrds))
    if (len(wrds)==0):
        return
    if (wrds[0][0]=='#'):
        return
    if (len(wrds[0])>=2)and(wrds[0][:2]=='//'):
        return
    i = 0
    for word in wrds:
        if '${' in word:
            word = word.replace('$','')
            St = word.find('{')
            En = word.find('}')
            Key1 = '-'+word[St+1:En]
            Key2 = word[St+1:En]
            if Key1 in params:
                Replace = params[Key1]
            elif Key2 in params:
                Replace = params[Key2]
            else:
                Replace = ''
                log_error('param replacement failed, param %s not found'%(Key2))
            word = word[:St]+Replace+word[En+1:]
            wrds[i] =word
        i += 1

    if (wrds[0]=='interactive'):
        interactive.runInteractive(Env)
        return
    if (wrds[0]=='skeleton'):
        print(Skeleton)
        return
    if (wrds[0]=='clean'):
        os.system('/bin/rm yacc.log lex.out db0.pickle database.dump')
        return
    if (wrds[0]=='set'):
        params[wrds[1]]=wrds[2]
        print('add param %s=%s'%(wrds[1],wrds[2]))
        return

    if (wrds[0]=='quit')or(wrds[0]=='exit'):
        sys.exit()
    if (wrds[0]=='libdir')or(wrds[0]=='dir'):
        Env.SearchDirs.extend(wrds[1:])
        return
    if (wrds[0]=='pre_dir'):
        Env.SearchDirs = wrds[1:]+Env.SearchDirs
        return
    if (wrds[0]=='dont_flatten_from_file'):
        Fix = open(wrds[1])
        ok=True
        while ok:
            line = Fix.readline()
            if (line==''):
                return
            else:
                ww= line.split()
                Env.DontFlattens.extend(ww)
    if (wrds[0]=='dont_flatten'):
        Env.DontFlattens.extend(wrds[1:])
        return
    if (wrds[0]=='load_module'):
        try_and_load_module(wrds[1],Env)
        return
    if (wrds[0]=='load')or(wrds[0]=='load_verilog')or(wrds[0]=='load_verilog_file'):
        Fname = wrds[1]
        Env.read_verilog_file(Fname,Env.rundir,Env)
        log_info('read verilog file %s'%(Fname))
        return
    if (wrds[0]=='help_main'):
        exec('from __main__ import help_main')
        help_main(Env)
        return

    if (wrds[0]=='import'):
        Fname = wrds[1]
        importing(Fname,Env)
        return

    if wrds[0]=='remove_notused_signals':
        select_current(Env)
        remove_notused_signals(Env.Current)
        return
        
    if wrds[0]=='check':
        select_current(Env)
        Env.Current.check_verilog()
        return
    if wrds[0]=='dump':
        select_current(Env)
        Env.Current.dump()
        return
    if wrds[0] in ['write_verilog','dump_verilog']:
        select_current(Env)
#        Root = get_param(wrds,'root')    
        Root = Env.Current.Module
        if len(wrds)>1:
            Fname = wrds[-1]
        else:
            Fname = '%s.dumpv'%Root
        check_directory_exists(Fname)
        Fout = open(Fname,'w')
        Env.Current.dump_verilog(Fout,True)
        Fout.close()
        return

    if wrds[0]=='write_all_verilog':
        Fname = wrds[1]
        Fout = open(Fname,'w')
        for Module in Env.Modules:
            Env.Modules[Module].dump_verilog(Fout)
        Fout.close()
        return



    if (wrds[0]=='top')or(wrds[0]=='root'):
        Env.Top = wrds[1]
        if (Env.Top in Env.Modules):
            Env.Current = Env.Modules[Env.Top]
        elif (string.lower(Env.Top) in Env.Modules):
            Env.Current = Env.Modules[string.lower(Env.Top)]
        elif (string.upper(Env.Top) in Env.Modules):
            Env.Current = Env.Modules[string.upper(Env.Top)]
        else:
            log_err('module %s not loaded, cannot become top'%(Env.Top))
            log_err('loads: %s'%str(Env.Modules.keys()))
            sys.exit(3)
        return
    if (wrds[0]=='retype')or(wrds[0]=='retype_instance'):
        select_current(Env)
        From=wrds[1]
        To=wrds[2]
        if From in Env.Current.insts:
            Env.Current.retype(From,To)
        else:
            donesx = 0
            Insts = Env.Current.insts.keys()
            for II in Insts:
               Iobj = Env.Current.insts[II]
               if Iobj.Type==From:
                   Env.Current.retype(II,To)
                   donesx+=1
            if (donesx==0):
                log_error('retype failed on %s, none found in %s'%(From,Env.Current.Module))
        return    
    if wrds[0]=='rename':
        select_current(Env)
        From=wrds[1]
        To=wrds[2]
        Env.Current.rename(From,To)
        return    
    if wrds[0]=='rename_module':
        select_current(Env)
        New = wrds[1]
        Env.Current.Module=New
        Env.Modules[New]=Env.Current
        return
    if wrds[0]=='assign':
        select_current(Env)
        for wrd in wrds[1:]:
            if '=' in wrd:
                ww = wrd.split('=')
                Env.Current.add_hard(ww[0],ww[1])
        return
    if (wrds[0]=='add_con')or(wrds[0]=='addcon'):
        select_current(Env)
        Inst=wrds[1]
        for PinSig in wrds[2:]:
            ps = PinSig.split('=')
            if (len(ps)!=2):
                log_err('in add_con the params should be in form Pin=Sig, you gave me %s'%(PinSig))
            else:
                Pin = ps[0]
                Sig=ps[1]
                if (Sig=='gnd'):
                    Sig = "1'b0"
                elif (Sig=='vcc'):
                    Sig = "1'b1"
                Env.Current.add_conn(Inst,Pin,Sig)
        return    

    if (wrds[0]=='rep_con')or(wrds[0]=='repcon'):
        select_current(Env)
        Inst=wrds[1]
        for PinSig in wrds[2:]:
            ps = PinSig.split('=')
            if (len(ps)!=2):
                log_err('in rep_con the params should be in form Pin=Sig, you gave me %s'%(PinSig))
            else:
                Pin = ps[0]
                Sig=ps[1]
                Env.Current.add_conn(Inst,Pin,Sig)
        return 

    if wrds[0] in ['del_con','delcon']:
        select_current(Env)
        Inst=wrds[1]
        if Inst not in Env.Current.insts:
            log_err('del_con of %s %s failed on no instance'%(Inst,wrds[2:]))
            return
        Obj = Env.Current.insts[Inst]
        for Pin in wrds[2:]:
            if Pin in Obj.conns:
                Env.Current.del_conn(Inst,Pin)
            else:
                worked=False
                Pins = Obj.conns.keys()
                for P in Pins:
                    if Pin==Obj.conns[P]:
                        worked=True
                        Env.Current.del_conn(Inst,P)
                if not worked:
                    log_err('del_con (sig) of %s %s failed pin/sig not found'%(Inst,Pin))

                        
        return 

    if wrds[0]=='del_wire':
        select_current(Env)
        for wrd in wrds[1:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            if Bus in Env.Current.nets:
                Env.Current.nets.pop(Bus)
            else:
                log_err('del_wire of %s in %s failed'%(wrd,Env.Current.Module))
        return
    if wrds[0]=='add_wire':
        select_current(Env)
        for wrd in wrds[1:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            Env.Current.add_net('wire',Bus,Hi,Lo)
        return

    if wrds[0]=='add_signal':
        select_current(Env)
        Dir = wrds[1]
        for wrd in wrds[2:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            Env.Current.add_net(Dir,Bus,Hi,Lo)
        return

    if wrds[0]=='add_input':
        select_current(Env)
        for wrd in wrds[1:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            Env.Current.add_net('input',Bus,Hi,Lo)
        return
    if wrds[0]=='add_output':
        select_current(Env)
        for wrd in wrds[1:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            Env.Current.add_net('output',Bus,Hi,Lo)
        return
    if wrds[0]=='add_inout':
        select_current(Env)
        for wrd in wrds[1:]:
            (Bus,Hi,Lo)=parse_net(wrd)
            Env.Current.add_net('inout',Bus,Hi,Lo)
        return
    
    if (wrds[0]=='add_inst')or(wrds[0]=='add_object'):
        select_current(Env)
        Type=wrds[1]
        Inst = wrds[2]
        Env.Current.add_inst(Type,Inst)
        if (wrds[3]=='*'):
            try_and_load_module(Type,Env)
            for Net in Env.Modules[Type].nets:
                XX=Env.Modules[Type].nets[Net]
                if (XX[0] in ['input','output','inout','output reg']):
                    if (XX[1]==-1):
                        Env.Current.add_conn(Inst,Net,Net)
                    else:    
                        Env.Current.add_conn(Inst,Net,['subbus',Net,XX[1],XX[2]])
                elif (XX[0] not in  ['wire','reg']):
                    log_error('ilia! direction of a wire is %s (%s)'%(XX[0],XX))
            return 
        for PinSig in wrds[3:]:
            ps = PinSig.split('=')
            if (len(ps)!=2):
                log_err('in add_con the params should be in form Pin=Sig, you gave me %s'%(PinSig))
            else:
                Pin = ps[0]
                Sig=ps[1]
                if (Sig=='gnd'):
                    Sig = "1'b0"
                elif (Sig=='vcc'):
                    Sig = "1'b1"
                Env.Current.add_conn(Inst,Pin,Sig)
        return
    if wrds[0] in ['delete_object','del_inst']:
        select_current(Env)
        for Inst in wrds[1:]:
            if Inst in Env.Current.insts:
                Env.Current.del_inst(Inst)
            else:
               Insts = Env.Current.insts.keys()
               donex=False
               for II in Insts:
                  Iobj = Env.Current.insts[II]
                  if Iobj.Type==Inst:
                      Env.Current.del_inst(II)
                      donex=True
               if not donex:
                   log_err('delete instance not found %s in %s'%(Inst,Env.Current.Module))
        return


    if wrds[0]=='del_module':
        Whome = wrds[1]
        if (Whome not in Env.Modules):
            log_err('delete module failed, because not found %s '%(Whome))
            return
        Env.Modules.pop(Whome)
        return
    
    if (wrds[0]=='constant_inputs'):
        select_current(Env)
        new_flattens.constant_inputs(Env.Current,Env)
        return
    if (wrds[0]=='remove_buffers'):
        select_current(Env)
        new_flattens.remove_buffers(Env.Current,Env)
        return

    if (wrds[0]=='fixing'):
        select_current(Env)
        fixingModule.fixingModule(Env.Current,Env)
        return

    if (wrds[0]=='flatten'):
        select_current(Env)
        if len(wrds)>1:
            Whome = wrds[1:]
            if len(Whome)==1:
                Whome=Whome[0]
        else:
            Whome = '*'
        new_flattens.flatten(Env.Current,Whome,Env,try_and_load_module)
        return
    
    if (wrds[0]=='flatten_deep'):
        select_current(Env)
        if len(wrds)>1:
            Whome = wrds[1]
        else:
            Whome = '*'
        new_flattens.flatten_deep(Env.Current,Whome,Env,try_and_load_module)
        return
    
    
    if (wrds[0]=='list_instances'):
        select_current(Env)
        DDD = {}
        log_print('list_instances %s'%Env.Current.Module)
        Max=0
        for Inst in Env.Current.insts:
            Type = Env.Current.insts[Inst].Type

            Max = max(Max,len(Type))
            if Type not in DDD:
                DDD[Type]=[Inst]
            else:
                DDD[Type].append(Inst)
        res=[]
        for Type in DDD:
            res.append((len(DDD[Type]),Type))
        res.sort()
        res.reverse()
        Pattern = '%5d  %WWWs    %s'.replace('WWW',str(Max+3))
        Tot=0
        for Len,Type in res:
            log_print(Pattern%(Len,Type,DDD[Type][0]))
            Tot += Len
        log_print('total %d instances'%Tot)
        return
            

    if (wrds[0]=='undefinedWires'):
        select_current(Env)
        undefinedWires(Env.Current)
        return

    if (wrds[0]=='expand'):
        select_current(Env)
        expandStarConnections(Env.Current,Env)
        return

    
    if (wrds[0]=='build_mvlg'):
        select_current(Env)
        All  = get_types_deep(Env.Current.Module,Env)    
        Fout = open('%s.sons'%(Env.Current.Module),'w')
        Fout.write('%s\n'%(where_comes_from(Env.Current.Module)))
        for Son in All:
            Fout.write('%s\n'%(where_comes_from(Son)))
        Fout.close()
        return
    

    if (wrds[0]=='help'):
        log_screen('registered options are:')
        for word in RegisteredList:
            log_screen('-do %s'%(word))
        

    if (wrds[0] in RegisteredList):
        select_current(Env)
        String = '%s(Env.Current,Env.Modules,wrds)'%(wrds[0])
        exec(String)
        return
    print('got here') 
    if len(wrds)==1:
       Done = importing(wrds[0],Env,False)
       print('done %s'%Done)
       if Done: return 


    log_screen('error! execute line unknows: %s'%(Line))
    log_screen('knowns: %s'%' '.join(RegisteredList))




def importing(Fname,Env,Original=True):
    Env.try_and_load_module = try_and_load_module
    sys.path += ['.']
    Orig = Fname
    if (len(Fname)>2)and(Fname[-3:]=='.py'):
        Fname = Fname[:-3]
    if ('/' in Fname):
        wrds2 = Fname.split('/')
        Fname = wrds2[-1]
        Path = '/'.join(wrds2[:-1])
        Path = os.path.abspath(Path)
        sys.path += [Path]

    what = 'from %s import help_main'%(Fname)
    print('importing "%s"'%what)
    try:
        exec(what)
    except:
        traceback.print_exc()
        if Original:
            log_fatal('failed to import "help_main" from %s or -do %s does not exist'%(Fname,Fname))
        else:
            return False
    if (Env.Current==None):
        Keys = Env.Modules.keys()
        Keys.sort()
        if (len(Keys)==1):
            TT = Keys[0]
            Env.Current=Env.Modules[TT]
        elif (len(Keys)>0):
            TT = Keys[0]
            Env.Current=Env.Modules[TT]
            log_warning('since no -top given, %s selected randomly'%(TT))
    try:
        help_main(Env)
    except:
        traceback.print_exc()
        log_error('import help_main of %s failed'%(Fname),True)
    return True



comes_from ={}
def set_comes_from(Module,Fname):
    global comes_from
    comes_from[Module]=Fname

def where_comes_from(Module):
    if Module in comes_from:
        return comes_from[Module]
    else:
        return '// not found %s.v'%(Module)



def try_and_load_module(Cell,Env):
    if Cell in Env.Modules:
        return
    for Ext in Env.VerilogExtensions:
        for Dir in Env.SearchDirs:
            Fname = '%s/%s.%s'%(Dir,Cell,Ext)
            if os.path.exists(Fname):
                set_comes_from(Cell,Fname)
                log_info('read verilog file %s'%(Fname))
                if Env.GateLevelRead:
                    Env.read_gate_level_verilog_file(Fname,Env.rundir)
                else:
                    Env.read_verilog_file(Fname,Env.rundir,Env)
                if Cell in Env.Modules:
                    Env.Modules[Cell].cleanZeroNets()
                return
    log_err('cell %s was not loaded, was not found in dirs: %s (try adding -y param)'%(Cell,Env.SearchDirs))



deep_sons_keeper={}
def get_types_deep(Module,Env):
    global deep_sons_keeper
    if (Module in deep_sons_keeper):
        return deep_sons_keeper[Module]
    Types = get_all_types(Module,Env,)
    res = {} 
    for Type in Types:
        res[Type]=1
        Part = get_types_deep(Type,Env)
        for Son in Part:
            res[Son]=1
    Keys = res.keys()
    Keys.sort()
    deep_sons_keeper[Module]=Keys
    return Keys 

sons_keeper={}
def get_all_types(Module,Env):
    global sons_keeper
    if (Module in sons_keeper):
        return sons_keeper[Module]
    if (Module in ['and','or','xor','not','nand','nor','buf']):
        return [Module]
    try_and_load_module(Module,Env)
    if (Module not in Env.Modules):
        return []
    This = Env.Modules[Module]
    res={}  
    for Inst in This.insts:
        Son = This.insts[Inst]
        if Son.Type not in res: 
            res[Son.Type]=1
    Types = res.keys()
    Types.sort()
    sons_keeper[Module]=Types
    Env.Modules.pop(Module)
    return Types

def scan_used(Inst,Pin,Sig,Used):
    if not Sig:
        return
    if type(Sig)==types.StringType:
        if Sig not in Used:
            Used[Sig]=1
        else:
            Used[Sig] +=1 
    elif type(Sig)==types.ListType:
        if Sig[0] in ['const','hex','bin']:
            return
        elif Sig[0] in ['subbus','subbit']:
            Bus=Sig[1]
            if Bus not in Used:
                Used[Bus]=1
            else:
                Used[Bus] +=1 
        elif Sig[0] in ['curly']:
            for Si in Sig[1:]:
                scan_used(Inst,Pin,Si,Used)
        else:
            log_err('strange inst=%s pin=%s sig=%s %s'%(Inst,Pin,str(Sig),type(Sig)))
    else:
         log_err('strange inst=%s pin=%s sig=%s %s'%(Inst,Pin,str(Sig),type(Sig)))

def remove_notused_signals(Mod):
    Used = {}
    for Net in Mod.nets:
        Used[Net]=0
        if external_sig(Mod,Net):
            Used[Net]=1

    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            scan_used(Inst,Pin,Sig,Used)

    for Sig in Used:
        if Used[Sig]==0:
            for Ind,(Dst,_,_,_) in enumerate(Mod.hard_assigns):
                if new_flattens.same_expr(Dst,Sig,Mod):
                    Mod.hard_assigns.pop(Ind)
            if Sig in Mod.nets:
                print('remove_notused_signals: remove %s'%Sig )
                Mod.nets.pop(Sig)
            
        elif Used[Sig]==1:
            print('remove_notused_signals: single sig %s'%Sig)




def external_sig(Mod,Sig):
    if type(Sig)==types.StringType:
        (Dir,Wid)=Mod.nets[Sig]
        if 'input' in Dir: return True
        if 'output' in Dir: return True
        if 'inout' in Dir: return True
    return False
    if type(Sig)==types.StringType:
        if Sig in Mod.nets:
            (Dir,Wid)=Mod.nets[Sig]
            return Dir not in ['wire','reg']
        if '[' in Sig:
            Bus = Sig[:Sig.index('[')]
            (Dir,Wid)=Mod.nets[Bus]
            return Dir not in ['wire','reg']

    if type(Sig)==types.ListType:
        if Sig[0] in ['subbit','subbus']:
            return external_sig(Mod,Sig[1])

    return False

def expandStarConnections(Mod,Env):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        try_and_load_module(Obj.Type,Env)
        Pins = Obj.conns.keys()
        for Pin in Pins:
            Conn = Obj.conns[Pin]
            if Pin=='*':
                if Obj.Type in Env.Modules:
                    Obj.conns.pop('*')
                    Son = Env.Modules[Obj.Type]
                    for Net in Son.nets:
                        if external_sig(Son,Net):
                            Dir,WW = Son.nets[Net]
                            if Net not in Obj.conns:
                                Obj.conns[Net] = Net
                                Mod.add_sig(Net,'wire',WW)
                            
            elif type(Conn) is str:
                if Obj.Type in Env.Modules:
                    Son = Env.Modules[Obj.Type]
                    if (Pin in Son.nets)and(Conn in Mod.nets):
                        if external_sig(Son,Pin):
                            _,WWs = Son.nets[Pin]
                            _,WWf = Mod.nets[Conn]
                            if WWs!=WWf:
                                logs.log_warning('mod=%s inst=%s pin=%s conn=%s wws=%s wwf=%s'%(Mod.Module,Inst,Pin,Conn,WWs,WWf))
                        
                




def undefinedWires(Mod):
    Sets=[]
    Founds = {}
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Conn = Obj.conns[Pin]
            Set = module_class.support_set(Conn)
            Sets.extend(Set)
    for Dst,Src,_,_ in Mod.hard_assigns:
        Set0 = module_class.support_set(Dst)
        Set1 = module_class.support_set(Src)
        Sets.extend(Set0)
        Sets.extend(Set1)
    
    for Item in Sets:
        if type(Item)==types.StringType:
            if '[' in Item:
                x = Item.index('[')
                Bus = Item[:x]
                AA = Item[x+1:]
                if ':' in AA:
                    x = AA.index(':')
                    Ind = int(AA[:x])
                else:
                    Ind = int(AA[:-1])
                if Bus not in Mod.nets:
                    Founds[Item]=max(Ind,Founds[Item])




            elif Item not in Mod.nets:
                Founds[Item]=0
        else:
            print('strange %s'%str(Item))
    for Bus in Founds:
        print(Bus,Founds[Bus])


def runInteractive(Env):
    print(Env.Current.Module,'interactive')
    return


Skeleton = """
import random,os,sys,string
import types

def help_main(Env):
    Removes={}
    Counts={}
    for Inst in Env.Current.insts:
        Obj=Env.Current.insts[Inst]
        for Pin in Obj.conns:
            Con = Obj.conns[Pin]
            Con = str(Con)
            if Con in Counts:
                Counts[Con] += 1 
            else:
                Counts[Con] = 1  
    for Con in Counts.keys():
        if (Counts[Con]>2):
            print(Con,Counts[Con])
    for Inst in Env.Current.insts:
        Obj=Env.Current.insts[Inst]
        Type =Obj.Type
        if (Type in Patterns):
            Dst,Src = work_pattern(Obj,Patterns[Type])
            Env.Current.add_hard(Dst,Src,rnddly(Inst))
            Removes[Inst]=1

    for Inst in Removes.keys():
        Env.Current.del_inst(Inst)
    dump(Current)

def rnddly(Inst):
    Dly = random.randint(1,10)
    return Dly

def dump(Current):
    Fname = '%s.vrnd'%(Current.Module)
    Fout = open(Fname,'w')
    Current.dump_verilog(Fout)
    Fout.close()


#invoke:   pyver.py -import llbin/rework.py vgate/halfreg.v -do 'top halfreg'

"""
Registered = '''
add_con add_object add_output 
add_inst add_instances  add_input  add_inout
add_signal add_wire addcon assign
build_mvlg check clean constant_puts del_con
del_inst del_module del_wire delcon delete_object
dir dont_flatten dont_flatten_from_file dump dump_verilog
exit expand fixg flatten flatten_deep
help help_ma import libdir list_instances
load load_module load_verilog load_verilog_file quit
remove_buffers remove_notused_signals rename rename_module rep_con
repcon retype retype_stance root set
skeleton top undefedWires write_all_verilog write_verilog
interactive
'''
