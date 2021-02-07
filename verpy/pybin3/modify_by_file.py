import sys
import logs
from executes import execute_line
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
    executeLines(Mod,Cmdlines)
    execute_line('dump_verilog %s.modv'%Mod.Module,Env)
    logs.log_info('Done %d modification commands, failed %d '%(Mod.donesx,logs.Errors))

def executeLines(Mod,Cmdlines):
    Mod.donesx = 0
    for Cmdline in Cmdlines:
        if '//' in Cmdline: Cmdline = Cmdline[:Cmdline.index('//')]
        if '#' in Cmdline: Cmdline = Cmdline[:Cmdline.index('#')]
        wrds = Cmdline.split()
        if wrds==[]:
            pass
        else:
            excecuteLine(Mod,wrds)

def excecuteLine(Mod,wrds):
    wrds = scanFunctions(wrds)
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

def scanFunctions(wrds):
    Res = []
    for Word in wrds:
        if Word.startswith('ahbconn('):
            Job = Word[7:-1]
            if ',' in Job: 
                wx = Job.split(',')
                SL = wx[0]
                PI = wx[1]
            else:
                SL = Job
                PI = ''[1]
        if Words.startswith('conns(')


