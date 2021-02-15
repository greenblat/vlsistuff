import os,sys
import logs
from executes import execute_line
from module_class import is_external_dir
from dump_instance import wids
import module_class
def help_main(Env):
    Mod = Env.Current
    Env.donesx = 0
    if not '-file' in sys.argv:
        print('i need -file <COMMAND_FILE')
        return
    X = sys.argv.index('-file')
    Cmdfilename = sys.argv[X+1]
    File = open(Cmdfilename)
    Cmdlines = File.readlines()
    File.close()
    executeLines(Mod,Cmdlines,Env)
    execute_line('dump_verilog %s.modv'%Env.Current.Module,Env)
    logs.log_info('Done %d modification commands, failed %d '%(Env.donesx,logs.Errors))

def executeLines(Mod,Cmdlines,Env):
    Env.donesx = 0
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
            Mod = Env.Current

def excecuteLine(Mod,wrds,Env):
    wrds = scanFunctions(wrds,Env)
    if (wrds[0]=='source'):
        Fname = wrds[1]
        os.system(Fname)
        return
    if (wrds[0]=='new'):
        newModule = wrds[1]
        Env.Current =  module_class.module_class(newModule)
        Env.Modules[newModule] = Env.Current
        return
    if (wrds[0]=='load'):
        Fname = wrds[1]
        Env.read_verilog_file(Fname,Env.rundir,Env)
        return

    if (wrds[0]=='copy_inst'):
        From = wrds[1]
        TypeInst = wrds[2]
        if From not in Env.Modules:
            Env.try_and_load_module(From,Env)
            if From not in Env.Modules:
                logs.log_error('failed to load "%s" module'%(From))
                return
        Other = Env.Modules[From]
        for Inst in Other.insts:
            found = False
            if (Inst == TypeInst):
                Type = Other.insts[Inst].Type
                Mod.add_inst(Other.insts[Inst].Type,Inst)
                found = True
            elif (Other.insts[Inst].Type==TypeInst):
                Mod.add_inst(TypeInst,Inst)
                found = True
            if found:
                for Pin in Other.insts[Inst].conns:
                    Sig =  Other.insts[Inst].conns[Pin]
                    if (type(Sig) is str) and (Sig in Other.nets):
                        Dir,WW = Other.nets[Sig]
                        if (type(WW) is tuple)and(len(WW)==2):
                            Sig = ['subbus',Sig,WW[0],WW[1]]

                    Mod.add_conn(Inst,Pin,module_class.pr_expr(Sig))
        return


    if (wrds[0]=='unconn'):
        Inst = wrds[1]
        if Inst not in  Mod.insts:
            logs.log_error('instance %s is not in module'%Inst)
            return
        Obj = Mod.insts[Inst]
        for Pin in wrds[2:]:
            if Pin in Obj.conns:
                Obj.conns[Pin]=False
                Env.donesx +=1
            else:
                logs.log_error('instance %s has no pin %s'%(Inst,Pin))
        return

    if (wrds[0]=='add_conn'):
        Inst = wrds[1]
        if Inst not in  Mod.insts:
            logs.log_error('instance %s is not in module'%Inst)
            return
        add_conns(Mod,Inst,wrds[2:],Env)
        return
    if (wrds[0]=='del_inst'):
        for Inst in wrds[1:]:
            if Inst in Mod.insts:
                Mod.insts.pop(Inst)
                Env.donesx +=1
            else:
                logs.log_error('del instance %s is not in module'%Inst)
        return

    if (wrds[0]=='del_wire'):
        for Net in wrds[1:]:
            if Net in Mod.nets:
                 Mod.nets.pop(Net)
                 Env.donesx +=1
            else:
                logs.log_error('net %s is not in module'%Net)
        return
    if (wrds[0]=='add_inst'):
        Type = wrds[1]
        Inst = wrds[2]
        Mod.add_inst(Type,Inst)
        add_conns(Mod,Inst,wrds[3:],Env)
        return
    if (wrds[0]=='add_param'):
        Inst = wrds[1]
        for PrmVal in wrds[2:]:
            Prm,Val  = PrmVal.split('=')
            Mod.add_inst_param(Inst,Prm,Val)
        return
    if (wrds[0]=='add_wire'):
        Dir = wrds[1]
        Wid = eval(wrds[2])
        for Net in wrds[3:]:
            Mod.add_sig(Net,Dir,Wid)
        return
    if (wrds[0]=='rename_inst'):
        Old  = wrds[1]
        New  = wrds[2]
        if Old not in Mod.insts:
            logs.log_error('inst %s is not in module'%(Old))
            return
        Obj = Mod.insts.pop(Old)
        Obj.Name = New
        Mod.insts[New] = Obj
        return

    if (wrds[0]=='retype_inst'):
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
        Env.donesx +=1
        return
    if (wrds[0]=='report_connectivity'):
        report_connectivity(Mod)
        return
    if (wrds[0]=='remove_unused_wires'):
        removeUnused(Mod)
        return
    if (wrds[0]=='elaborateSimpleAssigns'):
        elaborateSimpleAssigns(Mod)
        return
    if (wrds[0]=='assign'):
        treatAssigns(Env,Mod,wrds[1],wrds[2])
        return

    if (wrds[0]=='save'):
        Fname = wrds[1]
        execute_line('dump_verilog %s'%Fname,Env)
        return
    if wrds[0].startswith('remove_gen'):
        Mod.generates=[]
        return
    logs.log_error('bad command line %s'%' '.join(wrds))

def add_conns(Mod,Inst,List,Env):
    Obj = Mod.insts[Inst]
    for PinNet in List:
        if '=' in PinNet:
            Pin,Net  = PinNet.split('=')
            Mod.add_conn(Inst,Pin,Net)
            Env.donesx +=1
        else:
            logs.log_error('bad Pin=Net token %s for inst %s'%(PinNet,Inst))



AHBX = 'haddrYY=hsXX_haddr[31:0] hselYY=hsXX_hsel hwriteYY=hsXX_hwrite hwdataYY=hsXX_hwdata[31:0] hrdataYY=hsXX_hrdata[31:0] htransYY=hsXX_htrans[1:0] hburstYY=hsXX_hburst[2:0] hreadyYY=bmc_hsXX_hready hreadyoutYY=hsXX_bmc_hready hsizeYY=hsXX_hsize[2:0] hprotYY=hsXX_hprot[3:0]'

APBX = 'paddr=paddr32 psel=psXX_psel pwrite=pwrite pwdata=pwdata[31:0] prdata=psXX_prdata[31:0] penable=penable pready=psXX_pready pstrb=pstrb[3:0]'
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
            print('remove %s'%Net)
            Mod.nets.pop(Net)

def report_connectivity(Mod):
    Mod.prepareNetTable()
    reportNetTable(Mod)
    Mod.mergeNetTableBusses()
    Nets = list(Mod.netTable.keys())
    Num = 0
    Singles = {}
    for Net in Nets:
        if Net in Mod.nets:
            Dir,_ = Mod.nets[Net]
            if not is_external_dir(Dir):
                List = Mod.netTable[Net]
                if len(List)==1:
                    Inst,Type,Pin = List[0]
                    if Inst not in Singles:
                        Singles[Inst] = [(Type,Pin,Net)]
                    else:
                        Singles[Inst].append((Type,Pin,Net))

    for Inst in Singles:
        LL = Singles[Inst]
        (Type,_,_) = LL[0]
        logs.log_info('SINGLE ____  %s   %s'%(Inst,Type))
        for Type,Pin,Net in LL:
            logs.log_info('             #%d        %s'%(Num,Net))
            Num += 1

reported = True
def reportNetTable(Mod):
    global reported
    if reported: return
    for Key in Mod.netTable.keys():
        List = Mod.netTable[Key]
        logs.log_info('NETABLE %s %s'%(Key,List),2)
    reported = True

def treatAssigns(Env,Mod,Dst,Src):
    Mod.prepareNetTable()
#    reportNetTable(Mod)
    More,Ldst = [],[]
    if Dst in Mod.nets:
        _,Wid = Mod.nets[Dst]
        if (type(Wid) is tuple)and(len(Wid)==2):
            Alt = '%s[%s:%s]'%(Dst,Wid[0],Wid[1])
            if (Alt in Mod.netTable): 
                More = Mod.netTable[Alt]
    if (str(Dst) in Mod.netTable):
        Ldst = Mod.netTable[Dst]
    Lboth = Ldst + More
    if Lboth == []:
        logs.log_error('cannot treat assign %s <-- %s'%(Dst,Src))
        return
    for (Inst,Type,Pin) in Lboth:
        if (Inst != 'switchbox'):
            Mod.insts[Inst].conns[Pin]=Src
            Env.donesx += 1
        else:
            Mod.insts[Inst].conns.pop(Pin)


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




