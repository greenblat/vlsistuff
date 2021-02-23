import os,sys
import logs
import datetime 
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
    wrds = scanFunctions(wrds,Env,Mod)
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

    if (wrds[0]=='add_inout'):
        add_wires(Mod,'inout',wrds[1:])
        return
    if (wrds[0]=='add_input'):
        add_wires(Mod,'input',wrds[1:])
        return
    if (wrds[0]=='add_output'):
        add_wires(Mod,'output',wrds[1:])
        return


    if (wrds[0]=='copy_params'):
        From = wrds[1]
        Other = Env.Modules[From]
        for Param in  Other.parameters:
            Mod.parameters[Param] =  Other.parameters[Param]
        for Param in  Other.localparams:
            Mod.localparams[Param] =  Other.localparams[Param]
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
                Oobj =  Other.insts[Inst]
                for Pin in Oobj.conns:
                    Sig =  Oobj.conns[Pin]
                    if (type(Sig) is str) and (Sig in Other.nets):
                        _,WW = Other.nets[Sig]
                        if (type(WW) is tuple)and(len(WW)==2):
                            Sig = '%s%s'%(Sig,module_class.pr_wid(WW))
                            Sup = module_class.support_set(WW[0])
                            for Param in Sup:
                                if Param in Other.parameters:
                                    Mod.parameters[Param] =  Other.parameters[Param]
                                elif Param in Other.localparams:
                                    Mod.localparams[Param] =  Other.localparams[Param]
                    Mod.add_conn(Inst,Pin,module_class.pr_expr(Sig))
                                
                for Param in Oobj.params:
                   Mod.insts[Inst].params[Param] =  Oobj.params[Param]

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

    if (wrds[0]=='del_conn'):
        Inst = wrds[1]
        if Inst not in  Mod.insts:
            logs.log_error('instance %s is not in module'%Inst)
            return
        Obj = Mod.insts[Inst] 
        for Pin in wrds[2:]:
            if Pin in Obj.conns: 
                Obj.conns.pop(Pin)
            else:
                logs.log_error('del_conn isnt=%s pin=%s failed'%(Inst,Pin))
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
        report_connectivity(Mod,Env)
        pairsTable(Mod)
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

def add_wires(Mod,Dir,wrds):
    for Wrd in wrds:
        Wrd0 = module_class.busify_x(Wrd)
        if type(Wrd0) is str:
            Mod.nets[Wrd] = Dir,0
        elif Wrd0[0] == 'subbus':
            Mod.nets[Wrd0[1]] = Dir,(Wrd0[2],Wrd0[3])
        else:
            log.log_error('add_%s doesnt make sense "%s"'%(Dir,wrds))

def add_conns(Mod,Inst,List,Env):
    Obj = Mod.insts[Inst]
    for PinNet in List:
        if '=' in PinNet:
            Pin,Net  = PinNet.split('=')
            Mod.add_conn(Inst,Pin,Net)
            Env.donesx +=1
        else:
            logs.log_error('bad Pin=Net token %s for inst %s'%(PinNet,Inst))

def recomputeDims(Sig,Oparameters,Mparameters,Mlocals,Oobj_params):
    if type(Sig) is str: return Sig
    y = {**Mlocals, **Oobj_params}
    z = {**Oparameters, **Mparameters}
    zz = {**z, **y}
    if (type(Sig) is tuple)or(type(Sig) is list): 
        if Sig[0] == 'subbus':
            if len(Sig)==3:
                print('PREXPR',Sig[2][0],module_class.pr_expr(Sig[2][0]),zz )
                H = eval(str(module_class.pr_expr(Sig[2][0])),zz)
                L = eval(str(Sig[2][1]),zz)
            elif len(Sig)==4:
                print('PREXPR',Sig[2],module_class.pr_expr(Sig[2]),zz )
                H = eval(str(module_class.pr_expr(Sig[2])),zz)
                L = eval(str(Sig[3]),zz)
            return ['subbus',Sig[1],H,L]
    return Sig        


AHBX = 'haddrYY=hsXX_haddr[31:0] hselYY=hsXX_hsel hwriteYY=hsXX_hwrite hwdataYY=hsXX_hwdata[31:0] hrdataYY=hsXX_hrdata[31:0] htransYY=hsXX_htrans[1:0] hburstYY=hsXX_hburst[2:0] hreadyYY=bmc_hsXX_hready hreadyoutYY=hsXX_bmc_hready hsizeYY=hsXX_hsize[2:0] hprotYY=hsXX_hprot[3:0] hrespYY=hsXX_hresp[1:0]'

APBX = 'paddr=paddr psel=psXX_psel pwrite=pwrite pwdata=pwdata[31:0] prdata=psXX_prdata[31:0] penable=penable pready=psXX_pready pstrb=pstrb[3:0] pslverr=psXX_pslverr'
def scanFunctions(wrds,Env,Mod):
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
                        if (type(Wid) is tuple)and(len(Wid) == 2):
                            Sup = module_class.support_set(Wid)
                            for Param in Sup:
                                if Param in Sonobj.parameters:
                                    Mod.parameters[Param] =  Sonobj.parameters[Param]
                                elif Param in Sonobj.localparams:
                                    Mod.localparams[Param] =  Sonobj.localparams[Param]
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

PINDIRS = {}
def buildPinDirs(Mod,Env):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type not in Env.Modules:
            Env.try_and_load_module(Type,Env)
        if Type in Env.Modules:
            Son = Env.Modules[Type]
            for Pin in Son.nets:
                Dir,_ = Son.nets[Pin]
                if ' ' in Dir:
                    ww = Dir.split()
                    Dir = ww[0]
                PINDIRS[(Inst,Pin)] = Dir
        else:
            logs.log_error('missing %s being loaded'%Type)


def report_connectivity(Mod,Env):
    Mod.prepareNetTable()
    reportNetTable(Mod)
    Mod.mergeNetTableBusses()
    buildPinDirs(Mod,Env)
    Nets = list(Mod.netTable.keys())
    Num = 0
    Singles = {}
    Fines = []
    for Net in Nets:
        if Net in Mod.nets:
            Dir,WW = Mod.nets[Net]
            if not is_external_dir(Dir):
                List = Mod.netTable[Net]
                if len(List)==1:
                    Inst,Type,Pin = List[0]
                    if Inst not in Singles:
                        Singles[Inst] = [(Type,Pin,Net)]
                    else:
                        Singles[Inst].append((Type,Pin,Net))
        else:
            print('WWWWW',Net)
    for Inst in Mod.insts:
        if Inst not in Singles:
            Type = Mod.insts[Inst].Type
            Fines.append((Inst,Type))

    for Inst in Singles:
        LL = Singles[Inst]
        (Type,_,_) = LL[0]
        logs.log_info('SINGLE ____  %s   %s'%(Inst,Type))
        for Type,Pin,Net in LL:
            if Net in Mod.nets:
                Dir,Wid = Mod.nets[Net]
                if type(Wid) is tuple:
                    Net = '%s[%s:%s]'%(Net,Wid[0],Wid[1])
            Dir = '.'
            if (Inst,Pin) in PINDIRS:
               Dir = PINDIRS[(Inst,Pin)]
            logs.log_info('             #%d        %-50s    %s'%(Num,Net,Dir))
            Num += 1

    Date = datetime.date.today()
    Time = datetime.datetime.now()
    DDD = str(Date.day)+'/'+str(Date.month)+'/'+str(Date.year)+' '+str(Time.hour)+'h,%s'%(os.environ['HOST'])
    CSVDATE = 'd'+str(Date.day)+'_m'+str(Date.month)+'_'+str(Date.year)+'_'+str(Time.hour)+'h'

    Fcsv = open('missing_%s.csv'%CSVDATE,'w')

    Fcsv.write('generated on,%s\n'%DDD)
    Fcsv.write('MODULE,Instance,Type,Orphan Connect,Port Dir,Suggested Buddy\n')
    Num = 0
    for Inst in Singles:
        LL = Singles[Inst]
        (Type,_,_) = LL[0]
        Fcsv.write('cell ,%s,%s\n'%(Inst,Type))
        for Type,Pin,Net in LL:
            Dir = '.'
            if (Inst,Pin) in PINDIRS:
                Dir = PINDIRS[(Inst,Pin)]
            if Net in Mod.nets:
                _,Wid = Mod.nets[Net]
                if type(Wid) is tuple:
                    Net = '%s[%s:%s]'%(Net,Wid[0],Wid[1])
            Fcsv.write('%d,,,%s,%s,\n'%(Num,Net,Dir)) 
            Num += 1
    Fcsv.write('MODULE,Fully Covered\n')
    for Inst,Type in Fines:
        Fcsv.write('cell ,%s,%s\n'%(Inst,Type))
    Fcsv.close()


def pairsTable(Mod):
    buildPairsTable(Mod)
    reportPairsTable(Mod)

def reportPairsTable(Mod):
    Keys = list(PAIRS.keys())
    Keys.sort()
    Fcsv = open('%s_pairs.csv'%Mod.Module,'w')
    Fcsv.write('Src,Dst,#fwrd,#back\n')
    Dones = []
    for Src,Dst in Keys:
        if (Src,Dst) not in Dones:
            List = PAIRS[(Src,Dst)]
            List.sort()
            List2 = []
            if (Dst,Src) in PAIRS:
                List2 = PAIRS[(Dst,Src)]
            Fcsv.write('%s,%s,%d,%d\n'%(Src,Dst,len(List),len(List2)))
            for Net in List:
                Fcsv.write('->,,->,,%s\n'%(Net))
            for Net in List2:
                Fcsv.write('<-,,,<-,%s\n'%(Net))
            Dones.append((Dst,Src))
            
    Fcsv.close()

def buildPairsTable(Mod):
    Nets = list(Mod.netTable.keys())
    Num = 0
    for Net in Nets:
        if Net in Mod.nets:
            Dir,WW = Mod.nets[Net]
            Ext =  is_external_dir(Dir)
            List = Mod.netTable[Net]
            if len(List) == 2:
                Inst0,_,Pin0 = List[0]
                Inst1,_,Pin1 = List[1]
                if (Inst0,Pin0) in PINDIRS:
                    Dir0 = PINDIRS[(Inst0,Pin0)]
                else:
                    Dir0 = 'inout'
                if (Inst1,Pin1) in PINDIRS:
                    Dir1 = PINDIRS[(Inst1,Pin1)]
                else:
                    Dir1 = 'inout'

                if (Dir0,Dir1) == ('input','output'):
                    recordPair(Inst1,Inst0,Net)
                elif (Dir1,Dir0) == ('input','output'):
                    recordPair(Inst0,Inst1,Net)
                else:
                   logs.log_warning('DIRECTIONS %s  %s=%s %s=%s'%(Net,Inst0,Dir0,Inst1,Dir1))
                    

PAIRS = {}
                
def recordPair(Src,Dst,Net):
    Key=(Src,Dst)
    if Key not in PAIRS: PAIRS[Key] = []
    PAIRS[Key].append(Net)
                

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




