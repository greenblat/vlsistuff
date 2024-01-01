

import sys,os,logs,string
import module_class
DIR = 'tmptmp'
if not os.path.exists(DIR): os.mkdir(DIR)

HARDS = 'PLLTS16FFCLAINTB TS1N16FFCLLMBLVTC4096X32M8SWB TS1N16FFCLLSBLVTD1024X72M4SWB'.split()

def help_main(Env):
    Mod = Env.Current
    if not Mod: return
    if (Mod.Module in HARDS) or ('-hard' in sys.argv):
        New = createHardWrapped(Mod)
        ending(New,True)
        return

    if '-wrap' in sys.argv:
        New = createReverseWrap(Mod)
        ending(New,True)
        return
    if '-noname' not in sys.argv:    
        addNames(Mod)


    cleanConns(Mod)
    cleanPrimitives(Mod)
    SingleOuts = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Wid in [0,1]:
            Mod.nets[Net] = Dir,(31,0)
            if 'output' in Dir:
                SingleOuts.append(Net)
        elif type(Wid) is tuple:
            Wid2 = ('packed',Wid,(31,0))
            Mod.nets[Net] = Dir,Wid2

    SingleOuts = []
    Alwayses = []
    Initials = []
    ind = 0
    while ind < len(Mod.hard_assigns):
        (Dst,Src,X0,X1) = Mod.hard_assigns[ind];
        if type(Src) is str: 
            ind += 1
        elif type(Src) is int: 
            Mod.hard_assigns[ind] = (Dst,2 | Src,X0,X1)
            ind += 1
        elif (type(Src) is list) and (Src[0] == 'bin'):
            if Src[1] in ['1',1]:
                if Src[2] in ['1',1]:
                    Mod.hard_assigns[ind] = (Dst,2 | 1,X0,X1)
                elif Src[2] in ['0',0]:
                    Mod.hard_assigns[ind] = (Dst,2 | 0,X0,X1)
                else:
                    logs.log_error('HARD ASSIGNS in %s : %s <= %s ' % (Mod.Module,Dst,Src))
                ind += 1
        elif (type(Src) is list) and (len(Src) == 2)and(type(Src[1]) is str):
            if (Src[0] in ['!','~']) and (type(Src[1]) is str):
               Res = (Dst,('curly',('subbus',Src[1],31,1),('!',('subbit',Src[1],0))),X0,X1) 
               Mod.hard_assigns[ind] = Res
            else:
                logs.log_error('ILIA %s %s' % (Dst,Src))
            ind += 1
        else:
            Mod.hard_assigns.pop(ind)
            Alwayses.append(('*',('=',('subbit',Dst,0),remodelSrc(Src)),'always'))                
            if (type(Dst) is tuple)or(type(Dst) is list):
                Bus = Dst[1]
                Dir,Wid = Mod.nets[Bus]
            else:
                Dir,Wid = Mod.nets[Dst]
                Bus = Dst
            if Dir == 'output':
                Mod.nets[Bus] = 'output reg',Wid
            Vars = getVars(Src)
            for Var in Vars: 
                Alwayses.append( (('subbit',Var,0),('=',('subbus',Dst,31,1),('subbus',Var,31,1)),'always'))                
            Initials.append(('=',('subbus',Dst,31,1),0))
    Flops = False
    for ind,(When,Body,Kind)  in enumerate(Mod.alwayses):
        When2 = remodelSrc(When)
        Body2 = remodelBody(Body)
        Mod.alwayses[ind] = (When2,Body2,Kind)
        Flops = True
        print("WHEN",When,Body)
    Mod.alwayses.extend(Alwayses)
    Mod.initials.extend(Initials)
    if '-noname' not in sys.argv:
        for Net in SingleOuts:
            Mod.nets['name_'+Net] = 'wire',(255,0)
            Mod.hard_assigns.append(('name_'+Net,('subbit','tb.flops',('subbus',Net,31,1)),'',''))

    ending(Mod,Flops)

NAMES = []
def addNames(Mod):
    Names = [] 
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sup = module_class.support_set(Sig,False)
            for Net in Sup:
                Dir,Wid = Mod.nets[Net]
                if type(Wid) is tuple:
                    NN = '%s[0]' % (Net)
                else:
                    NN = Net
                if NN not in Names: Names.append(NN)
    
    for Name in Names:
        if not Name.startswith('\\'):
            Bus = Name
            if '[' in Bus: Bus = Bus[:Bus.index('[')]
            if Bus.startswith('\\'): Bus = Bus[1:]
            if Name[0] == '\\': Name = Name+' '
            Str = 'wire [255:0] name_%s  = {tb.flops[%s[31:1]],8\'d61,(8\'d48+%s[0])};\n' % (Bus,Name,Name)
            NAMES.append(Str)


def ending(Mod,Flops):
    global FLOPNAME
    if Flops:
        Mod.nets['flopname'] = 'reg',(30,0)
    Fout = open('%s/%s.v' % (DIR,Mod.Module),'w')
    Mod.dump_verilog(Fout,{'endmodule':False})
    for Nstr in NAMES:
        Fout.write(Nstr)
    if Flops:
        if QQ!=[]:
            Str = ''
            for Q0 in QQ:
                Str += '    %s[31:1] = flopname;\n' % Q0
            FLOPNAME = FLOPNAME.replace('end',Str+'\nend\n')
        Fout.write(FLOPNAME)
        Fout.write('endmodule\n')
    else:
        Fout.write('endmodule\n')
    Fout.close()

FLOPNAME = '''
wire [255:0] name = tb.flops[flopname];
reg [255:0] Instance;
initial begin
    #1;
    flopname = tb.flopname;
    tb.flopname = tb.flopname + 1;
    $sformat(Instance,"%m");
    tb.flops[flopname] = Instance;
end

'''

QQ = []
def remodelBody(Body):
    if Body[0] == 'ifelse':
        Cond = remodelSrc(Body[1])
        Yes = remodelBody(Body[2])
        No = remodelBody(Body[3])
        return ['ifelse',Cond,Yes,No]
    elif Body[0] in ['=','<=']:
        Dst = remodelSrc(Body[1])
        Src = remodelSrc(Body[2])
        Body2 = ['list',[Body[0],Dst,Src],['<=',('subbus',Body[1],31,1),'flopname']]
        if Body[1] not in QQ: QQ.append(Body[1])
        return Body2 

    logs.log_error('BODY %s' %str(Body)) 
    return Body

def getVars(Src):
    if Src == '*': return []
    if type(Src) is int:
        return []
    if type(Src) is str:
        if Src[0] in string.ascii_letters: return [Src]
        return []
    Res = []
    for X in Src:
        LL = getVars(X)
        for L0 in LL:
            if L0 not in Res:
                Res.append(L0)
    return Res

def remodelSrc(Src):
    if Src == '*': return '*'
    if  type(Src) is str: return ('subbit',Src,0)
    if type(Src) is int: return Src
    if (type(Src) is tuple)or(type(Src) is list) and (Src[0] == 'subbit'):
        return Src
    if (type(Src) is tuple)or(type(Src) is list) and (Src[0] == 'hex'):
        return expandHex(Src)

    if Src[0] in ['!','~']:
        Sec = remodelSrc(Src[1])
        return ('~',Sec)
    if Src[0] in ['&&','||','^','|','&']:
        LL = [Src[0]]
        for XL in Src[1:]:
            XL2 = remodelSrc(XL)
            LL.append(XL2)
        return LL
    if Src == '*':
        return Src
    if Src[0] in ['edge']:
        Src[2] = ('subbit',Src[2],0)
        return Src
    if Src[0] in ['list']:
        LL = ['list']
        for XL in Src[1:]:
            X0 = remodelSrc(XL)
            LL.append(X0)
        return LL 
    if Src[0] in ['question']:
        Cond = remodelSrc(Src[1])
        Yes = remodelSrc(Src[2])
        No = remodelSrc(Src[3])
        return ['question',Cond,Yes,No]
    if Src[0] in ['curly']:
        Res = ['curly']
        for X in Src[1:]:
            Y = remodelSrc(X)
            Res.append(Y)
        return Res
        
    logs.log_error('REMODEL %s' % str(Src))
    return Src

def expandHex(Sig):
    Wid = int(Sig[1])
    Bin = (32*'0') + bin(int(Sig[2],16))[2:]
    Bin = Bin[-Wid:]
    Bin  = Bin.replace('1','OOOOOOON')
    Bin  = Bin.replace('0','OOOOOOOO')
    Bin  = Bin.replace('O','0')
    Bin  = Bin.replace('N','1')
    return ('hex',32*Wid,Bin)


def expandSig(Sig,Mod):
    if (type(Sig) is list) or (type(Sig) is tuple):
        if (Sig[0] == '!'):
            X = expandSig(Sig[1],Mod)
            return ('^',X,1)
        if (Sig[0] == 'subbit') and Sig[2] in [0,'0', (0,0)]:
            Dir,Wid = Mod.nets[Sig[1]]
            if Wid in [0,1,(0,0)]:
                return Sig[1]
            return Sig
        elif (Sig[0] == 'bin'):
            if Sig[1] in ['1',1]:
                return ('bin',32,Sig[2])
            else:
                Wid = int(Sig[1])
                Bin = (32*'0') + Sig[2]
                Bin = Bin[-Wid:]
                Bin  = Bin.replace('1','OOOOOOON')
                Bin  = Bin.replace('0','OOOOOOOO')
                Bin  = Bin.replace('O','0')
                Bin  = Bin.replace('N','1')
                return ('hex',32*Wid,Bin)
        elif (Sig[0] == 'hex'):
            return expandHex(Sig)
        elif (Sig[0] == 'curly'):
            for ind,X in enumerate(Sig):
                if (ind==0):
                    pass
                elif (type(X) is str):
                    pass
                else: 
                    New = expandSig(X,Mod)
                    if not New:
                        logs.log_error('expandSig failed on "%s" %s ' % (X,Mod))
                    Sig[ind] = New
            return Sig
        elif (Sig[0] == 'subbit'):
            return Sig
        else:
            logs.log_error('SIGSIG %s' % str(Sig))
            return Sig
    else:
        return Sig

def cleanConns(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sigx = expandSig(Sig,Mod)
            Obj.conns[Pin] = Sigx
            logs.log_info("CONN %s %s %s %s" % (Inst,Pin, Sig,Sigx),"ssd")
        if Obj.Type in HARDS:
            Obj.Type = 'TRACED_' + Obj.Type
        if len(Obj.Type)>250:
            Obj.Type = Obj.Type[:250]
    if len(Mod.Module)>250:
        Mod.Module = Mod.Module[:250]
        print("SHORTS")

def createHardWrapped(Mod):
    NewName = 'TRACED_'+Mod.Module
    New = module_class.module_class(NewName)
    New.insts[Mod.Module] =  module_class.instance_class(Mod.Module,Mod.Module)
    Modobj = New.insts[Mod.Module]
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Wid in [0,1]:
            New.nets[Net] = Dir,(31,0)
        elif type(Wid) is tuple:
            Wid2 = ('packed',Wid,(31,0))
            New.nets[Net] = Dir,Wid2
        if ('input' in Dir)or('output' in Dir):
            Modobj.conns[Net] = 'xx_'+Net
            New.nets['xx_'+Net] = 'wire',Wid
        else:
            Modobj.conns[Net] = Net
            New.nets[Net] = Dir,Wid
        if ('input' in Dir):
            if Wid in [0,1]:
                New.hard_assigns.append(('xx_'+Net,('subbit',Net,0),'',''))
            elif (type(Wid) is tuple) or (type(Wid) is list):
                Hi,Lo = Wid
                for Ind in range(Lo,Hi+1):
                    New.hard_assigns.append((('subbit','xx_'+Net,Ind),'%s[%s][0]' % (Net,Ind),'',''))
        if ('output' in Dir):
            if Wid in [0,1]:
                New.hard_assigns.append((Net,('curly','flopname','xx_'+Net),'',''))
            elif (type(Wid) is tuple) or (type(Wid) is list):
                Hi,Lo = Wid
                for Ind in range(Lo,Hi+1):
                    New.hard_assigns.append(( ('subbit',Net,Ind),('curly','flopname',('subbit','xx_'+Net,Ind)),'',''))
    return New


def createReverseWrap(Mod):
    NewName = 'WRAP_'+Mod.Module
    New = module_class.module_class(NewName)
    New.insts[Mod.Module] =  module_class.instance_class(Mod.Module,Mod.Module)
    Modobj = New.insts[Mod.Module]
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if externalNet(Dir):
            New.nets[Net] = Dir,Wid

            if Wid in [0,1]:
                New.nets['xx_'+Net] = 'wire',(31,0)
            elif type(Wid) is tuple:
                Wid2 = ('packed',Wid,(31,0))
                New.nets['xx_'+Net] = 'wire',Wid2
            Modobj.conns[Net] = 'xx_'+Net

        if ('output' in Dir):
            if Wid in [0,1]:
                New.hard_assigns.append((Net,('subbit','xx_'+Net,0),'',''))
            elif (type(Wid) is tuple) or (type(Wid) is list):
                Hi,Lo = Wid
                for Ind in range(Lo,Hi+1):
                    New.hard_assigns.append((('subbit',Net,Ind),'xx_%s[%s][0]' % (Net,Ind),'',''))
        if ('input' in Dir):
            if Wid in [0,1]:
                New.hard_assigns.append(('xx_'+Net,('curly','flopname',Net),'',''))
            elif (type(Wid) is tuple) or (type(Wid) is list):
                Hi,Lo = Wid
                for Ind in range(Lo,Hi+1):
                    New.hard_assigns.append(( ('subbit','xx_'+Net,Ind),('curly','flopname',('subbit',Net,Ind)),'',''))
        if ('inout' in Dir):
            if Wid in [0,1]:
                New.hard_assigns.append(('xx_'+Net,('curly','flopname',Net),('pull0','pull1'),''))
            elif (type(Wid) is tuple) or (type(Wid) is list):
                Hi,Lo = Wid
                for Ind in range(Lo,Hi+1):
                    New.hard_assigns.append(( ('subbit','xx_'+Net,Ind),('curly','flopname',('subbit',Net,Ind)),('pull0','pull1'),''))

    return New


def externalNet(Dir):
    if 'output' in Dir: return True
    if 'input' in Dir: return True
    if 'inout' in Dir: return True
    return False



def cleanPrimitives(Mod):
    Insts = list(Mod.insts.keys())
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type in ['xor','and','or']:
            Out = Obj.conns['pin0']         
            Op = OPS[Type]
            Ins = [Op]
            for Pin in Obj.conns:
                if (Pin!='pin0'):
                    Ins.append(Obj.conns[Pin])
            Mod.insts.pop(Inst)
            Mod.hard_assigns.append( (Out,Ins,'',''))

OPS = {'xor':'^','and':'&&','or':'||'}




