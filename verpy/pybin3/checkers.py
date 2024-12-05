#! /usr/bin/python

import os,sys,string
import types
import logs
import traceback

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1
from extract_expr_nets import extract_sigs
from rtl_width import get_width,get_width2
from module_class import pexpr,support_set
from executes import try_and_load_module


Inits=[]
Codes=[]
def help_main(Env):
    if Env.Current==None:
        logs.log_err('no module to work on')
        return
    load_sons(Env)
    Env.Current.buildNetTable()
    create_drive_table(Env.Current)
    
    for Net in Env.Current.netTable:
        if '[' in Net: Net = Net[:Net.index('[')]
        List = Env.Current.netTable[Net]
        if (Net not in ['gnd','vcc']) and (len(List) ==1):
            Bus = Net
#            logs.log_info('%s >>>0 %s' % ((Bus,Net),list(TableDrives.keys())))
#            logs.log_info('>>>1 %s' % list(InvTableDrives.keys()))
#            logs.log_info('>>>2 %s' % list(Env.Current.netTable.keys()))
            if (Bus not in TableDrives)and (Bus not in InvTableDrives):
                if (Bus not in EdgeTableDrives)and (Bus not in InvEdgeTableDrives):
                    logs.log_errx(101,'Net %s / %s has 1 connectivity : %s' % (Net,Bus,List))
        
    checkZeroMinusOneBug(Env.Current)            

    check_integrity(Env,Env.Current)
    check_instance_connections(Env,Env.Current)
    look_for_loops(Env.Current)
    look_for_short_loops(Env.Current)
    look_for_pass_throughs(Env.Current)
    check_cases(Env.Current)
    logs.report_errx(Env.Current.Module)

def load_sons(Env):
    Current = Env.Current
    Types=[]
    for Inst in Current.insts:
        Type = Current.insts[Inst].Type
        if Type not in Types:
            Types.append(Type)
    for Type in Types:
        try_and_load_module(Type,Env)

TableDrives={}
InvTableDrives={}
def add_drives(Dst,Src):
    if Dst not in TableDrives:
        TableDrives[Dst]=[]
    if type(Src)is list:
        for X in Src:
            add_drives(Dst,X)
        return
    if Src not in TableDrives[Dst]:
        TableDrives[Dst].append(Src)
    if Src in InvTableDrives:
        InvTableDrives[Src].append(Dst)
    else:
        InvTableDrives[Src] = [Dst]

EdgeTableDrives={}
InvEdgeTableDrives={}
def add_edged_drives(Dst,Src):
    if Dst not in EdgeTableDrives:
        EdgeTableDrives[Dst]=[]
    if type(Src)is list:
        for X in Src:
            add_edged_drives(Dst,X)
        return
    if Src not in EdgeTableDrives[Dst]:
        EdgeTableDrives[Dst].append(Src)
    if Src in InvEdgeTableDrives:
        InvEdgeTableDrives[Src].append(Dst)
    else:
        InvEdgeTableDrives[Src] = [Dst]

def compatible_width(Dst,Src,Current):
    Wsrc1,Wsrc0 = get_width2(Src,Current)
    Wdst1,Wdst0 = get_width2(Dst,Current)
    if Wdst0>Wsrc1:
        return False
    if Wdst1<Wsrc0:
        return False
    return True

def create_drive_table(Current):
    for HAS in Current.hard_assigns:
        Dst1 = HAS[0]
        Src1 = HAS[1]
        Dsts = extract_sigs(Dst1)
        Srcs = extract_sigs(Src1)
        if not compatible_width(Dst1,Src1,Current):
            logs.log_errx(1,'diff width hard_assign (%d) != (%d)  %s <= %s ;'%(get_width(Dst1,Current),get_width(Src1,Current),pexpr(Dst1),pexpr(Src1)))
        for Dst in Dsts:
            for Src in Srcs:
                 add_drives(Dst,Src)
    create_always_drive_tables(Current)

def create_always_drive_tables(Current):
    for Always in Current.alwayses:
        if len(Always) in [2,3]:
            if not is_edged_timing(Always[0]):
                scan_statements(Current,Always[1],drive_assist1,[[]],[])
            else:
                Clks = support_set(Always[0])
                scan_statements(Current,Always[1],drive_assist2,[[]],Clks)
        else:
            logs.log_err('unrecognized always %d'%(len(Always)))

def drive_assist1(Current,Item,Params,Stack):
    Sofar = Params[0]
    if not Item:
        return
    if Item[0] == '=':
        Dsts = extract_sigs(Item[1])
        Srcs = extract_sigs(Item[2])
        Stcks = support_set(Stack)
        for Dst in Dsts:
            for Src in Srcs+Stcks:
                 add_drives(Dst,Src)
    if Item[0] == '<=':
        logs.log_errx(113,'"<=" assign in combi always %s' % str(Item))
        


def drive_assist2(Current,Item,Params,Stack):
    Sofar = Params[0]
    if not Item:
        return
    if Item[0] == '<=':
        Dsts = extract_sigs(Item[1])
        Srcs = extract_sigs(Item[2])
        for Dst in Dsts:
            Stcks = support_set(Stack)
            for Src in Srcs+Stcks:
                add_edged_drives(Dst,Src)



    if Item[0] == '=':
        logs.log_errx(112,'"=" assign in edged always %s' % str(Item))
        



Transitionals=[]
Loops=[]

def run_transitional(Sig,Sofar,Path):
    if Sig not in TableDrives:
        Transitionals.append(Path)
        return
            
    Now = TableDrives[Sig]
    for X in Now:
        if X in Path:
            Loops.append(Path+[X])
        else:
            run_transitional(X,Sofar,Path+[X])
    

def look_for_short_loops(Current):
    for Dst in EdgeTableDrives:
        Srcs = EdgeTableDrives[Dst]
        for Src in Srcs:
            if Src in TableDrives:
                List = TableDrives[Src]
                if Dst in List:
                    logs.log_errx(100,'SHORT LOOP %s %s (through edged always)'%(Dst,Src))
                    

def look_for_pass_throughs(Mod):
    for List in Transitionals:
        LOUT = []
        In,Out = False,False
        for Sig in List:
            if Mod.is_input(Sig): 
                In = True
                LOUT.append((Sig,'i'))
            elif Mod.is_output(Sig): 
                Out = True
                LOUT.append((Sig,'o'))
            else:
                LOUT.append((Sig,'x'))
        if In and Out:
            logs.log_errx(500,'PASS THROUGH %s' % str(LOUT))


def look_for_loops(Current):
    List = list(TableDrives.keys())
    List.sort()
    for Dst in List:
        run_transitional(Dst,[Dst],[Dst])
    LoopDir={}        
    for Loop in Loops:
        Loop1 = get_just_loop(Loop)
        Loop2 = reorder_loop(Loop1)
        Str = str(Loop2)
        if Str not in LoopDir:
            LoopDir[Str]=Loop2
    for Str in LoopDir:
        logs.log_errx(101,'LOOP %s'%str(Str))


def get_just_loop(Loop):
    for ind,Sig in enumerate(Loop):
        if Sig == Loop[-1]:
            return Loop[ind:]
    return Loop

def reorder_loop(Loop):
    Tmp =Loop[1:]
    Tmp2 = Tmp[:]
    Tmp.sort()
    Low = Tmp[0]
    ind = Loop.index(Low)
    Loop1 = Tmp2[ind:]+Tmp2[:ind]
    Loop1 = Loop1 + [Loop1[0]]
    return Loop1

def check_integrity(Env,Current):
    logs.setCurrentModule(Current.Module)
    always_assigns(Current)
    always_assigns_reset(Current)
    register_hard_assigns_usage(Current)
    register_instances_usage(Env,Current)
    check_usage_driven(Current)

def register_instances_usage(Env,Current):
    for Inst in Current.insts:
        Obj = Current.insts[Inst]
        Type = Obj.Type
        if Type not in Env.Modules:
            SonNets = []    
        else:
            Son = Env.Modules[Type]
            SonNets = Son.nets
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Nets = extract_sigs(Sig)
            for Net in Nets:
                if Pin in SonNets:
                    (Dir,W)=SonNets[Pin]
                    if 'input' in Dir:
                        Used[Net]=1
                    else:
                        incr_driven(Net,(Pin,Type))
                else:
                    print("NNN",Net,Sig)
                    Mentioned[Net]=1
    for Param in Current.parameters:
        Mentioned[Param]=1




def register_hard_assigns_usage(Current):
    for HAS in Current.hard_assigns:
        Dst = HAS[0]
        Src = HAS[1]
        check_src_expr(Current,Src)
        check_dst_expr(Current,Dst,False)

def check_usage_driven(Current):
    for Net in Current.nets:
        (Dir,WW) = Current.nets[Net]
        if Net in Driven:
            DD = Driven[Net]
        else:
            DD = []
        if 'input' in Dir:
            DD.append('input')

        if Net in Used:
            UU = Used[Net]
        else:
            UU = 0
        if 'output' in Dir:
            UU += 1

        if (len(DD)>1):
           logs.log_errx(2,'net %s (%s) is overdriven %s '%(Net,Dir,DD))
        if (len(DD)>0)and(UU==0)and(Net not in Mentioned)and(not Net.startswith('panic')):
           logs.log_errx(3,'net %s (%s) is driven, but not used '%(Net,Dir))
        if (DD==[])and(UU>0)and(Net not in Mentioned):
           logs.log_errx(102,'net %s (%s) is not driven, but used '%(Net,Dir))
        if (DD==[])and(UU==0):
           logs.log_errx(4,'net %s (%s) is neither driven, nor used '%(Net,Dir))
        if (Net in Mentioned)and(DD==[])and(UU==0):
           logs.log_errx(5,'net %s (%s) dangles from instance '%(Net,Dir))



def always_assigns_reset(Current):
    for Always in Current.alwayses:
        if len(Always) in [2,3]:
            if is_edged_timing(Always[0]):
                Ifelse = Always[1]
                if (Ifelse[0] == 'list') and (len(Ifelse) == 2):
                    Ifelse = Ifelse[1]
                    if Ifelse[0] == 'ifelse':
                        Rsts = getDsts(Ifelse[2])
                        Alws = getDsts(Ifelse[3])
                        for Alw in Alws:
                            if Alw not in Rsts:
                                logs.log_error("always_assigns_reset missing %s" % Alw)
                        for Rst in Rsts:
                            if Rst not in Alws:
                                logs.log_error("always_assigns_reset spare %s" % Rst)
                    

def getDsts(Expr):
    if type(Expr) == list:
        if (len(Expr) == 3) and (Expr[0] in ['<=','=']):
            Set = support_set(Expr[1],False)
            return Set
        if Expr[0] == 'list':
            Res = []
            for Item in Expr[1:]:
                More = getDsts(Item)
                Res += More
            return Res                
        if Expr[0] == 'if':
            return getDsts(Expr[2])                
        if Expr[0] == 'ifelse':
            return getDsts(Expr[2])+getDsts(Expr[3])

        logs.log_error("getDsts %s " % Expr[0])
        return []
    logs.log_error("getDsts0 %s " % Expr)
    return []

def always_assigns(Current):
    Alw = 1
    for Always in Current.alwayses:
        if len(Always) in [2,3]:
            check_src_expr(Current,Always[0])
            check_src_expr(Current,Always[1])

            if is_edged_timing(Always[0]):
                Time = Always[0]
                if (Time[0] == 'list') and (len(Time) == 3):
                    if Time[1][1] in ['posedge','negedge']:
                        if Time[2][1] in ['posedge','negedge']:
                            if (type(Always[1]) is list):
                                if len(Always[1])>2:
                                    logs.log_errx(114,'unrecognized edged always %s'%(str(Time)))
                                elif (Always[1][0] == 'list'):
                                    if (Always[1][1][0] != 'ifelse'):
                                        logs.log_errx(115,'double edged always %s has no ifelse(x) top (%s)'%(Always[1][1],Time))
                                elif (Always[1][0] != 'ifelse'):
                                    logs.log_errx(115,'double edged always %s has no ifelse top (%s)'%(Time,Always[1][0]))
                            else:
                                logs.log_errx(116,'unrecognized edged always %s'%(str(Type)))



                scan_statements(Current,Always[1],checker1,('<=','=',Alw),[])
            else:
                scan_statements(Current,Always[1],checker1,('=','<=',Alw),[])
            Alw += 1
        else:
            logs.log_errx(117,'unrecognized always %d'%(len(Always)))

def checker1(Current,Item,Params,Stack):
    if not Item:
        return
    if Item[0] == 'ifelse':
        check_src_expr(Current,Item[1])
    elif Item[0] == 'if':
        check_src_expr(Current,Item[1])
    elif Item[0] == 'case':
        check_src_expr(Current,Item[1])
        for NX in Item[2]:
            Case=NX[0]
            Stmnt=NX[1]
            check_src_expr(Current,Case)
    elif Item[0] == Params[1]:
        check_double_dst(Current,Item[1],Params[2])
        check_dst_expr(Current,Item[1])
        check_src_expr(Current,Item[2])
        logs.log_errx(8,'wrong assign %s prms=%s item=%s'%(Item,Params,Item))
    elif Item[0] == Params[0]:
        Dst=Item[1]
        Src=Item[2]
        check_double_dst(Current,Dst,Params)
        check_dst_expr(Current,Dst)
        check_src_expr(Current,Src)
        if not compatible_width(Dst,Src,Current):
            logs.log_errx(7,'diff width soft_assign (%s!=%s) %s   <= %s;'%(get_width(Dst,Current),get_width(Src,Current),pexpr(Dst),pexpr(Src)))
#        if (Item[0]=='<='):
#            make_sure_simple_src(Current,Item)
        
def make_sure_simple_src(Current,Item):
    Src = Item[2]
    if type(Src)is str:
        return
    if type(Src)is list:
        if Src[0] in ['subbus','subbit','bin','hex','dig']:
            return
        if Src[0]=='curly':
            LL = map(simple_curly,Src[1:])
            if not (False in LL):
                return
    logs.log_errx(10,'<= assign is not simple %s'%(Item))

def simple_curly(Item):
    if type(Item)is list:
        if Item[0] in ['bin','dig','hex']:
            return True
        if Item[0]=='curly':
            LL = map(simple_curly,Src[1:])
            if not (False in LL):
                return True
        if Item[0]=='repeat':
            return simple_curly(Item[2])
    return False
            
    

AlwaysAssign={}
def check_double_dst(Current,Dst,AlwInd):
        Dsts = extract_sigs(Dst)
        for Sig in Dsts:
            if Sig in AlwaysAssign:
                if AlwInd!=AlwaysAssign[Sig]:
                    logs.log_errx(103,'var %s assigned in two alwayses'%Sig)
            else:
                AlwaysAssign[Sig]=AlwInd

def incr_driven(Item,Whom):
    if Item in Driven:
        if Whom not in Driven[Item]:
            Driven[Item].append(Whom)
    else:
        Driven[Item] = [Whom]

def check_dst_expr(Current,Item,MustBeReg=True):
    if type(Item) is str:
        if Item in Current.nets:
            Data = Current.nets[Item]
            incr_driven(Item,'rtl')
            if MustBeReg and (Data[0] not in ['reg','integer','output reg','output wire']):
                logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Item,Data[0]))
            if not MustBeReg and (Data[0] not in ['wire','output','output wire','wire signed','output signed','input signed']):
                logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Item,Data[0]))
        else:
            logs.log_errx(11,'check dst failed on net %s'%(Item))
        return
    if type(Item) is list:
        if Item[0]=='curly':
            if Item[1]=='repeat':
                for It in Item[2:]:
                    check_dst_expr(Current,It,MustBeReg)
                return 
            for It in Item[1:]:
                check_dst_expr(Current,It,MustBeReg)
            return
        if Item[0]=='subbus':
            Bus = Item[1]
            incr_driven(Bus,'subbus')
            Wid = Item[2]
            if Bus not in Current.nets:
                logs.log_errx(11,'check dst failed on  bus %s'%(Bus))
            Data = Current.nets[Bus]
            check_bus_usage(Current,Bus,Wid)
            if MustBeReg and (Data[0] not in ['reg','integer','output reg','output wire']):
                logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Bus,Data[0]))
            if not MustBeReg and (Data[0] not in ['wire','output','output wire']):
                logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Bus,Data[0]))
            return
        if Item[0]=='subbit':
            Bus = Item[1]
            incr_driven(Bus,'subbit')
            Wid = Item[2]
            if (Bus in Current.nets):
                Data = Current.nets[Bus]
                check_bus_usage(Current,Bus,(Wid,Wid))
                if MustBeReg and (Data[0] not in ['reg','integer','output reg','output wire']):
                    logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Bus,Data[0]))
                if not MustBeReg and (Data[0] not in ['wire','output','output wire']):
                    logs.log_errx(104,'check dst of %s failed on bad kind %s'%(Bus,Data[0]))
                return
            if (Bus in Current.mems):
                return
            logs.log_errx(11,'check dst failed on  bus "%s"'%(Bus))
            return

    logs.log_err('check dst untreated %s'%(str(Item)))


Used={}
Driven={}
Mentioned={}
def check_src_expr(Current,Item):
    if type(Item)is tuple:
        if Item[0]=='*': return
        if Item[0]=='dotted': return
    if type(Item)is list:
        if (len(Item)==1):
            check_src_expr(Current,Item[0])
            return
        if (Item[0] in ['bin','dig','hex']):
            return
        if ((len(Item)==3) and (Item[0] == '=')):
            check_src_expr(Current,Item[2])
            return
        if (Item[0]=='for'):
            check_src_expr(Current,Item[1])
            check_src_expr(Current,Item[2])
            return
        if (Item[0]=='if'):
            check_src_expr(Current,Item[1])
            check_src_expr(Current,Item[2])
            return
        if (Item[0]=='ifelse'):
            check_src_expr(Current,Item[1])
            check_src_expr(Current,Item[2])
            check_src_expr(Current,Item[3])
            return
        if (Item[0]=='list'):
            for X in Item[1:]:
                check_src_expr(Current,X)
            return
        if Item[0] in ['edge']:
            check_src_expr(Current,Item[2])
            return
        if Item[0] in ['bin','hex','dig']:
            return
        if Item[0]=='subbus':
            Bus = Item[1]
            Wid = Item[2]
            check_bus_usage(Current,Bus,Wid,372)
            if (type(Wid) is tuple) and (len(Wid) ==2) and (type(Wid[0]) is int):
                pass
            else:
                check_src_expr(Current,Wid[0])
                check_src_expr(Current,Wid[1])
            Used[Bus]=1
            return
        if Item[0]=='subbit':
            Bus = Item[1]
            Wid = Item[2]
            check_bus_usage(Current,Bus,(Wid,Wid),378)
            check_src_expr(Current,Wid)
            Used[Bus]=1
            return
        if Item[0]=='curly':
            if Item[1]=='repeat':
                for X in Item[2:]:
                    check_src_expr(Current,X)
            else:
                for X in Item[1:]:
                    check_src_expr(Current,X)
            return 
        if Item[0]=='functioncall':
            LL = Item[2]
            for X in LL:
                check_src_expr(Current,X)
            return 

        if Item[0] in ['>>>','~&','~|','/','>','<','!','~','&&','||','&','|','^','+','-','*','>=','>>','<<','<=','curly','==','!=','question','repeat']:
            for X in Item[1:]:
                check_src_expr(Current,X)
            return 
    elif (type(Item)is str):
        if Item in ['*','default']:
            return
        if Item[0] in ['"']:
            return
        if (Item not in Current.nets)and(Item not in Current.parameters)and(Item not in Current.localparams):
            logs.log_errx(20,'item %s not defined'%(str(Item)))
        Used[Item]=1
        return
    elif (type(Item)is int):
        return
    if (type(Item) is list)and(Item[0] == 'case'):
        check_src_expr(Current,Item[1])
        for _,Code in Item[2]:
            check_src_expr(Current,Code)
        return            
    if (type(Item) is str) and (Item[0] == '#'):
        return            
        

    logs.log_err('check src expr %s %s'%(str(Item),type(Item)))
#    traceback.print_stack(None,None,logs.Flogs[0])

def check_bus_usage(Current,Bus,Wid,Where=0):
    if Bus in Current.mems:
        return
    if Bus not in Current.nets:
        logs.log_errx(106,'check_bus_usage failed on %s not defined (line=%d)'%(Bus,Where))
        return

    Data = Current.nets[Bus]
    Wid1 = Data[1]
    (H,L)=Wid
    if type(Wid1)is not tuple:
        logs.log_errx(107,'check_bus_usage failed on %s[%s:%s]'%(Bus,Wid[0],Wid[1]))
    else:
        if Wid1[0]=='double':
            (H1,L1)=Wid1[1]
        elif Wid1[0]=='packed':
            H1 = (compute1(Wid1[1][0],Current)+1)*(compute1(Wid1[2][0],Current)+1)
            L1 = 0
        else:
            (H1,L1)=Wid1

    HH = compute1(H,Current)
    LL = compute1(L,Current)
    HH1 = compute1(H1,Current)
    LL1 = compute1(L1,Current)
    if (type(HH1) is int)and(type(HH)is int)and(HH>HH1):
        logs.log_errx(108,'check_bus_usage.0 failed on %s[%s:%s]'%(Bus,Wid[0],Wid[1]))
    if (type(HH1) is int)and(type(LL)is int)and(LL>HH1):
        logs.log_errx(109,'check_bus_usage.1 failed on %s[%s:%s]'%(Bus,Wid[0],Wid[1]))

    if (type(LL1) is int)and(type(LL)is int)and(LL<LL1):
        logs.log_errx(110,'check_bus_usage.2 failed on %s[%s:%s]'%(Bus,Wid[0],Wid[1]))
    if (type(LL1) is int)and(type(HH)is int)and(HH<LL1):
        logs.log_errx(111,'check_bus_usage.3 failed on %s[%s:%s]'%(Bus,Wid[0],Wid[1]))


def check_cases(Current):
    for Always in Current.alwayses:
        scan_statements(Current,Always[1],case_assist1,[[]],[])

def case_assist1(Current,Item,Params,Stack):
    Sofar = Params[0]
    if not Item:
        return
    if Item[0] == 'case':
        print('case',Item)


def check_instance_connections(Env,Current):
    for Inst in Current.insts:
        Obj = Current.insts[Inst]
        Type = Obj.Type
        if Type in Env.Modules:
            Son = Env.Modules[Type]
            Exts=[]
            for Net in Son.nets:
                (Dir,_)=Son.nets[Net]
                if external_dir(Dir):
                    Exts.append(Net)
            Exts.sort()
            Ins = list(Obj.conns.keys())
            Ins.sort()
            for Ext in Exts:
                if Ext not in Ins:
                    logs.log_errx(21,'pin %s of %s %s is not connected in %s'%(Ext,Inst,Type,Current.Module))

            for In in Ins:
                if In not in Exts:
                    logs.log_errx(113,'connection to pin=%s of %s %s is not signal in  module=%s'%(In,Inst,Type,Current.Module))


def checkZeroMinusOneBug(Mod):
    for _,Body,_ in Mod.alwayses:
        scanZeroMinusOne(Body)
    for _,Src,_,_ in Mod.hard_assigns:
        scanZeroMinusOne(Src)
        

def scanZeroMinusOne(Body):
    if type(Body) is list:
        if Body[0] == 'list':
            for Item in Body[1:]:
                scanZeroMinusOne(Item)
            return
        if Body[0] == 'ifelse':
            scanZeroMinusOne(Body[1])
            scanZeroMinusOne(Body[2])
            scanZeroMinusOne(Body[3])
            return
        if Body[0] == 'if':
            scanZeroMinusOne(Body[1])
            scanZeroMinusOne(Body[2])
            return
        if Body[0] == '!':
            scanZeroMinusOne(Body[1])
            return
        if Body[0] == '<=':
            scanZeroMinusOne(Body[1])
            scanZeroMinusOne(Body[2])
            return
        if Body[0] == 'for':
            return
        if Body[0] == 'case':
            for Item in Body[2]:
                scanZeroMinusOne(Item[1])
            return


        if Body[0] == 'question':
            scanZeroMinusOne(Body[1])
            scanZeroMinusOne(Body[2])
            scanZeroMinusOne(Body[3])
            return
        if Body[0] in ['=']:
            scanZeroMinusOne(Body[2])
            return

        if Body[0] in ['==','!=']:
            if (type(Body[1]) is list) and (Body[1][0] in ['-','+']):
                if (type(Body[1][1]) is int)or (type(Body[1][2]) is int):
                    logs.log_errx(700,"dangerous comparison %s" % str(Body))


            if (type(Body[2]) is list) and (Body[2][0] in ['-','+']):
                if (type(Body[2][1]) is int)or (type(Body[2][2]) is int):
                    logs.log_errx(700,"dangerous comparison %s" % str(Body))
                
            scanZeroMinusOne(Body[1])
            scanZeroMinusOne(Body[2])
            return
        if Body[0] in ['-','+']:
            scanZeroMinusOne(Body[1])
            if len(Body)>2:
                scanZeroMinusOne(Body[2])
            return
        if Body[0] in ['&&','||','|','&','^','>','<','>=','~','>>','<<','*','~&']:
            scanZeroMinusOne(Body[1])
            if len(Body)>2:
                scanZeroMinusOne(Body[2])
            return
            

        if Body[0] in ['subbit','subbus','curly','bin','hex','dig','functioncall','empty_begin_end']:
            return

    if type(Body) is str:
        return
    if type(Body) is int:
        return
    logs.log_errx(700,("not covered scanZeroMinusOne %s" % str(Body)))

def external_dir(Dir):
    if 'input' in Dir: return True
    if 'output' in Dir: return True
    if 'inout' in Dir: return True
    if Dir in ['logic','wire','reg','integer','signed']:
        return False
    logs.log_err('external dir got "%s"'%(Dir))
    return False


