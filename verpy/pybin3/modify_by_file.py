import sys
import logs
from executes import execute_line
from module_class import is_external_dir
from dump_instance import wids
def help_main(Env):
    Mod = Env.Current
    if not '-file' in sys.argv:
        print('i need -file <COMMAND_FILE')
        return
    X = sys.argv.index('-file')
    Cmdfilename = sys.argv[X+1]
    File = open(Cmdfilename)
    Cmdlines = File.readlines()
    File.close()
    executeLines(Mod,Cmdlines,Env)
    execute_line('dump_verilog %s.modv'%Mod.Module,Env)
    logs.log_info('Done %d modification commands, failed %d '%(Mod.donesx,logs.Errors))

def executeLines(Mod,Cmdlines,Env):
    Mod.donesx = 0
    while Cmdlines != []:
        Cmdline = Cmdlines.pop(0)
        if '//' in Cmdline: Cmdline = Cmdline[:Cmdline.index('//')]
        if '#' in Cmdline: Cmdline = Cmdline[:Cmdline.index('#')]
        wrds = Cmdline.split()
        if wrds==[]:
            pass
        elif (wrds[0]=='include'):
            Fil = open(wrds[1])
            LL = Fil.readlines()
            Fil.close()
            Cmdlines = LL + Cmdlines

        else:
            excecuteLine(Mod,wrds,Env)

def excecuteLine(Mod,wrds,Env):
    wrds = scanFunctions(wrds,Env)
    if (wrds[0]=='unconn'):
        Inst = wrds[1]
        if Inst not in  Mod.insts:
            logs.log_error('instance %s is not in module'%Inst)
            return
        Obj = Mod.insts[Inst]
        for Pin in wrds[2:]:
            if Pin in Obj.conns:
                Obj.conns[Pin]=False
                Mod.donesx +=1 
            else:
                logs.log_error('instance %s has no pin %s'%(Inst,Pin))

    elif (wrds[0]=='add_conn'):
        Inst = wrds[1]
        if Inst not in  Mod.insts:
            logs.log_error('instance %s is not in module'%Inst)
            return
        add_conns(Mod,Inst,wrds[2:])
    elif (wrds[0]=='del_inst'):
        for Inst in wrds[1:]:
            if Inst in Mod.insts:
                Mod.insts.pop(Inst)
                Mod.donesx +=1 
            else:
                logs.log_error('del instance %s is not in module'%Inst)
                
    elif (wrds[0]=='del_wire'):
        for Net in wrds[1:]:
            if Net in Mod.nets:
                 Mod.nets.pop(Net)
                 Mod.donesx +=1 
            else:
                logs.log_error('net %s is not in module'%Net)
    elif (wrds[0]=='add_inst'):
        Type = wrds[1]
        Inst = wrds[2]
        Mod.add_inst(Type,Inst)
        add_conns(Mod,Inst,wrds[3:])
    elif (wrds[0]=='add_param'):
        Inst = wrds[1]
        for PrmVal in wrds[2:]:
            Prm,Val  = PrmVal.split('=')
            Mod.add_inst_param(Inst,Prm,Val)
    elif (wrds[0]=='add_wire'):
        Dir = wrds[1]
        Wid = eval(wrds[2])
        for Net in wrds[3:]:
            Mod.add_sig(Net,Dir,Wid)
    elif (wrds[0]=='retype_inst'):
        Old  = wrds[1]
        Type = wrds[2]
        if len(wrds)>=4:
            New = wrds[3]
        else:
            New = Old
        if Old not in Mod.insts:
            logs.log_error('inst %s / %s  is not in module'%(Type,Old))
            return
            
        Obj = Mod.insts[Old]
        Obj.Type = Type
        Obj.Name = New
        if Old!=New:
            Mod.insts.pop(Old)
            Mod.insts[New] = Obj
        Mod.donesx +=1 
    elif (wrds[0]=='remove_unused_wires'):
        removeUnused(Mod)
    elif (wrds[0]=='elaborateSimpleAssigns'):
        elaborateSimpleAssigns(Mod)
    elif (wrds[0]=='save'):
        Fname = wrds[1]
        execute_line('dump_verilog %s'%Fname,Env)
    elif wrds[0].startswith('remove_gen'):
        Mod.generates=[]
    else:
        logs.log_error('bad command line %s'%' '.join(wrds))

def add_conns(Mod,Inst,List):
    Obj = Mod.insts[Inst]
    for PinNet in List:
        if '=' in PinNet:
            Pin,Net  = PinNet.split('=')
            Mod.add_conn(Inst,Pin,Net)
            Mod.donesx +=1
        else:
            logs.log_error('bad Pin=Net token %s for inst %s'%(PinNet,Inst))
AHBX = 'haddrYY=hsXX_haddr hselYY=hsXX_hsel hwriteYY=hsXX_hwrite hwdataYY=hsXX_hwdata hrdataYY=hsXX_hrdata htransYY=hsXX_htrans hburstYY=hsXX_hburst hreadyYY=hsXX_hready hreadyoutYY=hsXX_hreadyout hsizeYY=hsXX_hsize'

APBX = 'paddr=paddrXX psel=pselXX pwrite=pwriteX pwdata=pwdataXX prdata=prdataXX penable=penableXX pready=preadyXX pstrb=pstrbXX'
def scanFunctions(wrds,Env):
    Res = []
    for Word in wrds:
        if Word.startswith('ahbconn('):
            Job = Word[8:-1]
            if ',' in Job: 
                wx = Job.split(',')
                SL = wx[0]
                PI = wx[1]
            else:
                SL = Job
                PI = ''
            Str = AHBX.replace('YY',PI)                    
            Str = Str.replace('XX',SL)                    
            Res.extend(Str.split())

        elif Word.startswith('apbconn('):
            Job = Word[8:-1]
            Str = APBX.replace('XX',Job)
            Res.extend(Str.split())
        elif Word.startswith('conns('):
            Son = Word[6:-1]
            Env.try_and_load_module(Son,Env)
            if Son in Env.Modules:
                Sonobj = Env.Modules[Son]
                for Net in Sonobj.nets:
                    Dir,Wid = Sonobj.nets[Net]
                    if is_external_dir(Dir):
                        Str = '%s=%s%s'%(Net,Net,wids(Wid))
                        Res.append(Str)
            else:
                logs.log_error('module %s could not be loaded'%Son)

                
    
        else:
            Res.append(Word)
    return Res

def removeUnused(Mod):
    Mod.prepareNetTable()
    Nets = list(Mod.nets.keys())
    for Net in Nets:
        if Net not in Mod.netTable:
            Mod.nets.pop(Net)
            
def elaborateSimpleAssigns(Mod):
    Mod.prepareNetTable()
    Ind = 0
    dones = 0
    failed = 0
    while Ind < len(Mod.hard_assigns):
        done = False
        Dst,Src,_,_  = Mod.hard_assigns[Ind]
        if (str(Dst) in Mod.netTable):             #and (str(Src) in Mod.netTable):
            if (str(Dst) in Mod.nets)and((str(Src) in Mod.nets)or(Src[0] in ['subbus','subbit'])):
                Ldst = Mod.netTable[Dst]
                for (Inst,Type,Pin) in Ldst:
#                Lsrc = Mod.netTable[Src]
#                if (len(Ldst)==1)and(len(Lsrc)==1):
#                    (Inst,Type,Pin) = Ldst[0]
                    Mod.insts[Inst].conns[Pin]=Src
                    Mod.hard_assigns.pop(Ind)
                    done = True
                    dones += 1
        if not done: 
            Ind += 1 
            failed += 1
    logs.log_info('elaborateSimpleAssigns did %d replacements and skipped %d'%(dones,failed))

