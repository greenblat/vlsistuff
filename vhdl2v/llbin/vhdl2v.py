#! /usr/bin/python

import os,sys,string,types
import pickle
import traceback
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)

import logs 
import moduleBuilder as mod

info = logs.log_info

ENTITIES={}
ARCHITECTURES={}
TYPES = {}

DUMMY = [['RRRFFF','Identifier','9999','9999']]

def main():
    if len(sys.argv)>1:
        Fname = sys.argv[1]
        os.system('llbin/cleanVhdl.py %s'%Fname)
        os.system('vhdllexer.py cleaned.vhd')
        os.system('pybin/reworkMyLex.py lex.out lex2.out')
        os.system('pybin/vyaccer2.py lex2.out')

    File = open('db0.pickle')
    Adb = pickle.load(File)
    cleanComas(Adb)
    rounds0(Adb)
    rounds1(Adb)

    dones = 1
    while dones>0:
        dones = removeUnused(Adb)
    scanStuff_new(Adb)
    makeVerilog(Adb)
    mod.dumpVerilog()
    reportAdb(Adb,'fff')


def cleanComas(Adb):
    for Key in Adb:
        List = Adb[Key]
        Res = []
        for Item in List:
            if (len(Item)==4)and(Item[0] in ['Comma','Semicolon']):
                pass
            else:
                Res.append(Item)
        Adb[Key]=Res


def rounds0(Adb):
    while True:
        Bef = len(Adb.keys())
        oneRound0(Adb)
        Aft = len(Adb.keys())
        if Aft==Bef: return


def oneRound0(Adb):
    F0,F4 = findEnds(Adb)
    useF0_F4(Adb,F0,F4)
    return Adb
def useF0_F4(Adb,F0,F4):
    for Key in F0:
        Adb.pop(Key)
    for Key in F4:
        Adb.pop(Key)

    for Key in Adb:
        Old = Adb[Key]
        New = simplify0(Old,F0,F4)
        if New!=Old:
            Adb[Key]=New


def simplify0(Old,F0,F4):
    New = Old[:]
    for Key in F0:
        if Key in New:
            Ind = New.index(Key)
            New.pop(Ind)
    for Key in F4:
        if Key in New:
            Ind = New.index(Key)
            New[Ind]=F4[Key]
    return New

def removeUnused(Adb):
    Defined=[]
    Used=[]
    dones = 0
    for Key in Adb.keys():
        Defined.append(Key)
        List = Adb[Key]
        for Item in List:
            if len(Item)==2:
                Used.append(Item)
    for Key in Defined:
        if Key not in Used:
            if Key[0] !='design_file':
                Adb.pop(Key)
                dones += 1
    info('removeUnused %d'%dones)
    return dones



def findEnds(Adb):
    F4 = {}
    F0 = []
    for Key in Adb.keys():
        Val = Adb[Key]
        if (len(Val)==1)and(len(Val[0])==4):
            F4[Key] = Val[0]
        if (Val==[]):
            F0.append(Key)
    return F0,F4

def rounds1(Adb):
    while True:
        Bef = len(Adb.keys())
        doTwos(Adb)
        Aft = len(Adb.keys())
        info('rounds1 bef=%d aft=%d'%(Bef,Aft))
        if Aft==Bef: return

def findOnes(Adb):
    F2 = {}
    for Key in Adb.keys():
        Val = Adb[Key]
        if (len(Val)==1)and(len(Val[0])==2):
            F2[Val[0]] = Key
    return F2

def doTwos(Adb):
    F2 = findOnes(Adb)
    Del = []
    for Key in Adb.keys():
        if Key in F2:
            Val = Adb[Key]
            if (len(Val)>1):
                Bef = F2[Key]
                Adb[Bef]=Val
                Del.append(Key)
    for Bef in Del:
        Adb.pop(Bef)




def scanStuff_new(Adb):
    RootKey =  ('design_file', 1)
    if RootKey not in Adb:
        logs.log_error('no design file found')
        return
    Root = Adb[ ('design_file', 1)]
    scanStuff_deep(Root,Adb)

def scanStuff_deep(Root,Adb):
    if (type(Root)==types.TupleType) and (Root in Adb):
        workOnItem(Root,Adb)
    else:
        for Item in Root:
            scanStuff_deep(Item,Adb)


def workOnItem(Item,Adb):
    if type(Item)==types.ListType:
        List = Item
    else:
        List = Adb[Item]
    if matches(List,"!design_unit !..design_unit.."):
        workOnItem(List[0],Adb)
        workOnItem(List[1],Adb)
    elif matches(List,"!..context_item.. !context_item"):
        workOnItem(List[0],Adb)
        workOnItem(List[1],Adb)
    elif matches(List,"!context_clause !library_unit"):
        workOnItem(List[0],Adb)
        workOnItem(List[1],Adb)
    elif matches(List,"LIBRARY ?"):
        pass
    elif matches(List,"USE ?"):
        pass
    else: 
        Vars = matches(List,'ARCHITECTURE ? OF ? IS BEGIN_ !architecture_statement_part END ?')
        if Vars:
            architecture_new(1,Vars,Adb)
            return
        Vars = matches(List,'ARCHITECTURE ? OF ? IS BEGIN_ !architecture_statement_part END')
        if Vars:
            architecture_new(1,Vars,Adb)
            return

        Vars = matches(List,'ARCHITECTURE ? OF ? IS !architecture_declarative_part BEGIN_ !architecture_statement_part END ARCHITECTURE')
        if Vars:
            architecture_new(0,Vars,Adb)
            return

        Vars = matches(List,'ARCHITECTURE ? OF ? IS !architecture_declarative_part BEGIN_ !architecture_statement_part END')
        if Vars:
            architecture_new(0,Vars,Adb)
            return
        Vars = matches(List,'ARCHITECTURE ? OF ? IS !architecture_declarative_part BEGIN_ !architecture_statement_part END ?')
        if Vars:
            architecture_new(0,Vars,Adb)
            return

        Vars = matches(List,'ENTITY ? IS !.generic_clause. !.port_clause. END')
        if Vars:
            entity_new(0,Vars,Adb)
            return
        Vars = matches(List,'ENTITY ? IS !.generic_clause. !.port_clause. END ?')
        if Vars:
            entity_new(0,Vars,Adb)
            return

        Vars = matches(List,'ENTITY ? IS !.port_clause. END ENTITY ?')
        if Vars:
            entity_new(1,Vars,Adb)
            return
        Vars = matches(List,'ENTITY ? IS !.port_clause. END ?')
        if Vars:
            entity_new(1,Vars,Adb)
            return

        Vars = matches(List,'PACKAGE ? IS !package_declarative_part END ?')
        if Vars:
            package_new(Vars,Adb)
            return
        Vars = matches(List,'PACKAGE BODY ? IS !package_body_declarative_part END ?')
        if Vars:
            package_new(Vars,Adb)
            return
        justify(List,'PACKAGE BODY ? IS !package_declarative_part END ?')
        logs.log_error('dont know to treat "%s"'%str(List))
    

def package_new(Vars,Adb):
    print 'package_new',Vars
def entity_new(Kind,Vars,Adb):
    if Kind==0:
        Gmatch = matches(Adb[Vars[1]],'GENERIC LeftParen !formal_generic_list RightParen')
        if Gmatch:
            Glist = getList_new(Adb[Gmatch[0]],Adb)

        Pmatch = matches(Adb[Vars[2]],'PORT LeftParen !formal_port_list RightParen')
        if Pmatch:
            Plist = getList_new(Adb[Pmatch[0]],Adb)
        ENTITIES[Vars[0][0]] = (Glist,Plist)
    elif Kind==1:
        Pmatch = matches(Adb[Vars[1]],'PORT LeftParen !formal_port_list RightParen')
        if Pmatch:
            Plist = getList_new(Adb[Pmatch[0]],Adb)
        ENTITIES[Vars[0][0]] = ([],Plist)
    else:
        log.log_error('entity kind missing %s'%Kind)
TRACE = []
def getList_new(Item,Adb):
    TRACE.append(Item)
    Res = getList_new__(Item,Adb)
    checkList(Res)
    TRACE.pop(-1)
    return Res

CHECKGOODS = string.split('signal_list else case wait input output port_map std_logic_vector integer unsigned port boolean')
def checkList(Res):
    if (type(Res)==types.TupleType):
        if len(Res)==4:
            if Res[1] in ['Identifier']:
                logs.log_error('checkList got "%s"'%str(Res),True)
                return
        if len(Res)==2:
            if (Res[0] not in CHECKGOODS)and(type(Res[0])!=types.IntType):
                logs.log_error('checkList got "%s"'%str(Res),True)
                return
    if (type(Res)==types.ListType):
        for Item in Res:
            checkList(Item)
    if (type(Res)==types.TupleType):
        for Item in Res:
            checkList(Item)


def getList_new__(Item,Adb):
    Vars = matches(Item,'!formal_generic_element !...formal_generic_element..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB
    Vars = matches(Item,'!...formal_generic_element.. !formal_generic_element')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+[BB]

    Vars = matches(Item,'!formal_port_element !...formal_port_element..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB
    Vars = matches(Item,'!...formal_port_element.. !formal_port_element')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+[BB]

    Vars = matches(Item,'!local_port_element !...local_port_element..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+[BB]

    Vars = matches(Item,'!...local_port_element.. !local_port_element')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB

    Vars = matches(Item,'!..block_declarative_item.. !block_declarative_item')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+[BB]

    Vars = matches(Item,'!concurrent_statement !..concurrent_statement..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB

    Vars = matches(Item,'!association_element !...association_element..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB
    Vars = matches(Item,'!sequential_statement !..sequential_statement..')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return [AA]+BB

    Vars = matches(Item,'!..process_declarative_item.. !process_declarative_item')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+[BB]
    Vars = matches(Item,'!..case_statement_alternative..  !case_statement_alternative')
    if Vars:
        AA = getList_new(Adb[Vars[0]],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return AA+BB

    Vars = matches(Item,'!a_label !unlabeled_process_statement')
    if Vars:
        AA = getList_new(Adb[Vars[1]],Adb) 
        Label = getLabel(Adb[Vars[0]],Adb)
        return [('process',Label,AA)]


    Vars = matches(Item,'!a_label !unlabeled_generate_statement')
    if Vars:
        AA = getList_new(Adb[Vars[1]],Adb) 
        Label = getLabel(Adb[Vars[0]],Adb)
        return [('generate',Label,AA)]

    Vars = matches(Item,'? <= !waveform')
    if Vars:
        Expr = getExpr(Adb[Vars[1]],Adb)
        Dst = getExpr(Vars[0],Adb)
        return [('<=',Dst,Expr)]



    Vars = matches(Item,'? <= !..waveform__WHEN__condition__ELSE.. ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Expr = getExpr(Adb[Vars[1]],Adb)
        Else = getExpr(Vars[2],Adb)
        Expr = ['question',Expr,Else]
        Expr = reworkWHENELSE(Expr)
        return [('<=',Dst,Expr)]


    Vars = matches(Item,'? => ?')
    if Vars:
        Expr = getExpr(Vars[1],Adb)
        return [('=>',Vars[0][0],Expr)]

    Vars = matches(Item,'? <= ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Src = getExpr(Vars[1],Adb)
        return [('<=',Dst,Src)]

    Vars = matches(Item,'!generation_scheme GENERATE !set_of_statements END GENERATE')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        Sch = getList_new(Adb[Vars[0]],Adb)
        return [('generate',Sch,LL)]

    Vars = matches(Item,'? Colon ? !.VarAsgn__expression.')
    if Vars:
        Expr = getVarAsgn(Adb[Vars[2]],Adb)
        return [('var_assign',Vars[0][0],Vars[1][0],Expr)]

    Vars = matches(Item,'? Colon IN std_logic')
    if Vars:
        return [('input',Vars[0][0],0)]
    Vars = matches(Item,'? Colon BUFFER std_logic')
    if Vars:
        return [('output',Vars[0][0],0)]

    Vars = matches(Item,'? Colon OUT std_logic')
    if Vars:
        return [('output',Vars[0][0],0)]

    Vars = matches(Item,'? Colon OUT std_logic_vector !.constraint.')
    if Vars:
        return [('output',Vars[0][0],getConstraint(Adb[Vars[1]],Adb))]

    Vars = matches(Item,'? Colon BUFFER std_logic_vector !.constraint.')
    if Vars:
        return [('output',Vars[0][0],getConstraint(Adb[Vars[1]],Adb))]


    Vars = matches(Item,'? Colon IN std_logic_vector !.constraint.')
    if Vars:
        return [('input',Vars[0][0],getConstraint(Adb[Vars[1]],Adb))]

    Vars = matches(Item,'SIGNAL ? Colon ? !.VarAsgn__expression.')
    if Vars:
        return [('signal',getExpr(Vars[0],Adb),getExpr(Vars[1],Adb),getVarAsgn(Adb[Vars[2]],Adb))]

    Vars = matches(Item,'SIGNAL ? Colon !subtype_indication')
    if Vars:
        Signal = getExpr(Vars[0],Adb)
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        return [('signal',Signal,Subtype)]
    Vars = matches(Item,'SIGNAL ? Colon ?')
    if Vars:
        return [('signal',Vars[0][0],Vars[1][0])]


    Vars = matches(Item,'Constant ? Colon ? !.VarAsgn__expression.')
    if Vars:
        return [('constant',Vars[0][0],getExpr(Vars[1],Adb),getVarAsgn(Adb[Vars[2]],Adb))]

    Vars = matches(Item,'!a_label ENTITY ? !.generic_map_aspect. !.port_map_aspect.')
    if Vars:
        Label = getLabel(Adb[Vars[0]],Adb)
        What = Vars[1][0]
        Gens = getList_new(Adb[Vars[2]],Adb)
        Ports = getList_new(Adb[Vars[3]],Adb)
        return [('instance',Label,What,Gens,Ports)]

    Vars = matches(Item,'!a_label ENTITY ? !.port_map_aspect.')
    if Vars:
        Label = getLabel(Adb[Vars[0]],Adb)
        What = Vars[1][0]
        Ports = getList_new(Adb[Vars[2]],Adb)
        return [('instance',Label,What,[],Ports)]

    Vars = matches(Item,'!a_label ? !.generic_map_aspect. !.port_map_aspect.')
    if Vars:
        Label = getLabel(Adb[Vars[0]],Adb)
        What = Vars[1][0]
        Gens = getList_new(Adb[Vars[2]],Adb)
        Ports = getList_new(Adb[Vars[3]],Adb)
        return [('instance',Label,What,Gens,Ports)]

    Vars = matches(Item,'GENERIC MAP LeftParen !association_list RightParen')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        return [('generic_map',LL)]

    Vars = matches(Item,'!a_label ? !.port_map_aspect.')
    if Vars:
        Label = getLabel(Adb[Vars[0]],Adb)
        LL = getList_new(Adb[Vars[2]],Adb)
        return [('instance',Label,Vars[1][0],[],LL)]

    Vars = matches(Item,'PORT MAP LeftParen !association_list RightParen')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        return [('port_map',LL)]

    Vars = matches(Item,'PORT LeftParen !local_port_list RightParen')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        return [('port',LL)]

    Vars = matches(Item,'LeftParen !signal_list RightParen')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        return [('signal_list',LL)]

    Vars = matches(Item,'LeftParen ? RightParen')
    if Vars:
        LL = getExpr(Vars[0],Adb)
        return [LL]

    Vars = matches(Item,'WAIT !.condition_clause.')
    if Vars:
        LL = getExpr(Adb[Vars[0]],Adb)
        return [('wait',LL)]

    Vars = matches(Item,'CASE !expression IS !case_statement_alternative  !..case_statement_alternative.. END CASE')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('case',Cond,LL0+LL1)]

    Vars = matches(Item,'CASE ? IS !case_statement_alternative  !..case_statement_alternative.. END CASE')
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('case',Cond,LL0+LL1)]


    Vars = matches(Item,'IF !condition')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        return [('if',Cond)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL = getList_new(Adb[Vars[1]],Adb)
        LL = listify(LL)
        return [('if',Cond,LL)]

    Vars = matches(Item,'ELSIF ? THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts..')
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        LL0 = listify(LL0)
        LL1 = listify(LL1)
        return [('ifelse',Cond,LL0,LL1)]

    Vars = matches(Item,'ELSIF ? THEN !sequence_of_statements')
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL0 = listify(LL0)
        return [('ifelse',Cond,LL0)]

    Vars = matches(Item,'WHEN OTHERS =>')
    if Vars:
        return [('case','default')]
    Vars = matches(Item,'WHEN OTHERS => Null')
    if Vars:
        return [('case','default')]

    Vars = matches(Item,'WHEN ? => !sequence_of_statements')
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        return [['case',Cond,['list']+LL0]]
    Vars = matches(Item,'? := ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Src = getExpr(Vars[1],Adb)
        return [(':=',Dst,Src)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts.. !.ELSE__seq_of_stmts. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = listify(getList_new(Adb[Vars[1]],Adb))
        LL1 = listify(getList_new(Adb[Vars[2]],Adb))
        LL2 = listify(getList_new(Adb[Vars[3]],Adb))
        return [('ifelse',Cond,LL0,LL1,LL2)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts.. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = listify(getList_new(Adb[Vars[1]],Adb))
        LL1 = listify(getList_new(Adb[Vars[2]],Adb))
        return [('ifelse',Cond,LL0,LL1)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !.ELSE__seq_of_stmts. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = listify(getList_new(Adb[Vars[1]],Adb))
        LL1 = listify(getList_new(Adb[Vars[2]],Adb))
        return [('ifelse',Cond,LL0,LL1)]

    Vars = matches(Item,'ELSE !sequence_of_statements')
    if Vars:
        LL0 = listify(getList_new(Adb[Vars[0]],Adb))
        return [('else',LL0)]

    Vars = matches(Item,'VARIABLE ? Colon !subtype_indication')
    if Vars:
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        return [('variable',Vars[0][0],Subtype)]

    Vars = matches(Item,'VARIABLE ? Colon !subtype_indication')
    if Vars:
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        return [('variable',Vars[0][0],Subtype)]

    Vars = matches(Item,'VARIABLE ? Colon ?')
    if Vars:
        Expr = getExpr(Vars[1],Adb)
        return [('variable',Vars[0][0],Expr)]

    Vars = matches(Item,'COMPONENT ? !.PORT__local_port_list.  END COMPONENT')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        return [('port_map',Vars[0][0],LL)]

    Vars = matches(Item,'PROCESS !.sensitivity_list. BEGIN_ !sequence_of_statements END PROCESS')
    if Vars:
        Sense = getList_new(Adb[Vars[0]],Adb)
        Stats = getList_new(Adb[Vars[1]],Adb)
        return [('process',[],Sense,['list']+Stats)]

    Vars = matches(Item,'PROCESS !.sensitivity_list. BEGIN_ !sequence_of_statements END PROCESS ?')
    if Vars:
        Sense = getList_new(Adb[Vars[0]],Adb)
        Stats = getList_new(Adb[Vars[1]],Adb)
        return [('process',[],Sense,Stats)]

    Vars = matches(Item,'PROCESS !.sensitivity_list. !process_declarative_part BEGIN_ !sequence_of_statements END PROCESS')
    if Vars:
        Sense = getList_new(Adb[Vars[0]],Adb)
        Declares = getList_new(Adb[Vars[1]],Adb)
        Stats = getList_new(Adb[Vars[2]],Adb)
        return [('process',Declares,Sense,Stats)]

    Vars = matches(Item,'PROCESS !.sensitivity_list. !process_declarative_part BEGIN_ !sequence_of_statements END PROCESS ?')
    if Vars:
        Sense = getList_new(Adb[Vars[0]],Adb)
        Declares = getList_new(Adb[Vars[1]],Adb)
        Stats = getList_new(Adb[Vars[2]],Adb)
        return [('process',Declares,Sense,Stats)]


    Vars = matches(Item,'PROCESS !process_declarative_part BEGIN_ !sequence_of_statements END PROCESS')
    if Vars:
        Declares = getList_new(Adb[Vars[0]],Adb)
        Stats = getList_new(Adb[Vars[1]],Adb)
        return [('process',Declares,[],Stats)]

    Vars = matches(Item,'ASSERT ? ? ?')
    if Vars:
        return []

    Vars = matches(Item,'ARRAY !index_constraint OF !subtype_indication')
    if Vars:
        Index = getConstraint(Adb[Vars[0]],Adb)
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        print 'subtype',Subtype
        return [('array',Index,Subtype)]

    Vars = matches(Item,'!.iteration_scheme. LOOP !sequence_of_statements END LOOP')
    if Vars:
        II = getExpr(Adb[Vars[0]],Adb)
        Seq = getList_new(Adb[Vars[1]],Adb)
        return [('loop',II,Seq)]

    Vars = matches(Item,'TYPE ? IS !type_definition')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        return [('type',Vars[0][0],LL)]

    Vars = matches(Item,'? !...name..')
    if Vars:
        Expr = getExpr(Vars[0],Adb)
        LL = getList_new(Adb[Vars[1]],Adb)
        return [Expr]+LL

    Vars = matches(Item,'? !...association_element..')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        return [['assoc',Vars[0][0]]]+LL

    Vars = matches(Item,'!...name.. ?')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        Expr = getExpr(Vars[1],Adb)
        return LL+[Expr]

    Vars = matches(Item,'? Colon ?')
    if Vars:
        return [('definition',Vars[0][0],Vars[1][0])]
    Vars = matches(Item,'? ?')
    if Vars:
        return [getExpr(Vars[0],Adb),getExpr(Vars[1],Adb)]

#    justify(Item,'PROCESS !.sensitivity_list. BEGIN_ !sequence_of_statements END PROCESS')

    logs.log_error('getList_new failed on "%s"'%str(Item))
    reportTrace(TRACE)
    return []


def getSubtype(List,Adb):
    Vars = matches(List,'unsigned !.constraint.')
    if Vars:
        LL = getConstraint(Adb[Vars[0]],Adb)
        return ('unsigned',LL)
    Vars = matches(List,'std_logic_vector !.constraint.')
    if Vars:
        LL = getConstraint(Adb[Vars[0]],Adb)
        return ('std_logic_vector',LL)
    Vars = matches(List,'integer !.constraint.')
    if Vars:
        LL = getConstraint(Adb[Vars[0]],Adb)
        return ('integer',LL)
        
    logs.log_error('getSubtype got "%s"'%(str(List)))
    return 'badLabel'

def getLabel(List,Adb):
    if matches(List,'? Colon'):
        return List[0][0]
    logs.log_error('getLabel got "%s"'%(str(List)))
    return 'badLabel'



def getVarAsgn(List,Adb):
    Vars = matches(List,':= ?')
    if Vars:
        Item = Vars[0]
        if len(Item)==2:
            LL = Adb[Item]
            Expr = getExpr(LL,Adb)
            return 0
        return Item[0]
    logs.log_error('getVarAsgn failed on "%s"'%(str(List)))
    return 0

def getConstraint(List,Adb):
    Vars = matches(List,'LeftParen !element_association RightParen')
    if Vars:
        List2 = Adb[Vars[0]]
        Vars2 = matches(List2,'? DOWNTO ?')
        if Vars2:
            return (getExpr(Vars2[0],Adb),getExpr(Vars2[1],Adb))
    Vars = matches(List,'RANGE !range')
    if Vars:
        Range = Adb[Vars[0]]
        Vars2 = matches(Range,'? TO ?')
        return [('range',Vars2[0][0],Vars2[1][0])]
        
    Vars = matches(List,'LeftParen !discrete_range RightParen')
    if Vars:
        Range = Adb[Vars[0]]
        Vars2 =  matches(Range,'? TO ?')
        if Vars2:
            From = getExpr(Vars2[0],Adb)
            To = getExpr(Vars2[1],Adb)
            return ('range',From,To)

        logs.log_error('discrete range %s'%(Range))
        return 0

    logs.log_error('getConstraint failed on %s'%(List))
    return 0


def architecture_new(Kind,Vars,Adb):
    if Kind==0:
        Module = Vars[1][0]
        Part0 = getList_new(Adb[Vars[2]],Adb)
        Part1 = getList_new(Adb[Vars[3]],Adb)
        ARCHITECTURES[Module]=(Part0,Part1)
        return
    if Kind==1:
        Module = Vars[1][0]
        Part0 = []
        Part1 = getList_new(Adb[Vars[2]],Adb)
        ARCHITECTURES[Module]=(Part0,Part1)
        return

    logs.log_error('architecture_new kind=%d'%Kind)

def makeVerilog(Adb):
    makeVerilogEntities()
    makeVerilogArchs(Adb)


def makeVerilogEntities():
    for Module in ENTITIES:
        mod.addModule(Module)
        Glist,Plist = ENTITIES[Module]
        for Item in Glist:
            mod.addModuleParam(Item[1],0)
        for Item in Plist:
            if len(Item)==1: Item = Item[0]
            try:
                Dir = Item[0]
                Net = Item[1]
                Wid = Item[2]
                try:
                    mod.addWire(Net,Dir,Wid)
                except:
                    logs.log_error('addWire failed "%s %s %s"'%(Dir,Net,Wid))
                    
            except:
                logs.log_error('item in plist is "%s"'%str(Item))

def makeVerilogArchs(Adb):
    for Module in ARCHITECTURES:
        L1,L2 = ARCHITECTURES[Module]
        treatSignals(L1,Module,Adb)
        treatBody(L2,Module)

def treatBody(L2,Module):
    for Item in L2:
        if len(Item)==1: Item=Item[0]
        if Item[0]=='assign':
            mod.addHardAssign(Item[1],Item[2])
        elif Item[0]=='<=':
            mod.addHardAssign(Item[1],Item[2])
        elif Item[0]=='instance':
            Inst = Item[1]
            Type = Item[2]
            Gens = Item[3]
            Ports = Item[4]
            if len(Gens)==1: Gens=Gens[0]
            if len(Ports)==1: Ports=Ports[0]
            if (len(Gens)>0)and(Gens[0]=='generic_map'): Gens = Gens[1]
            if Ports[0]=='port_map': Ports=Ports[1]
            mod.addInstance(Inst,Type)
            for PV in Gens:
                if len(PV)==1: PV=PV[0]
                if PV[0]=='=>':
                    mod.add_instance_param(Inst,PV[1],PV[2])
                else:
                    logs.log_error('add_param_inst failed on "%s"'%(str(PV)))

            for PV in Ports:
                if len(PV)==1: PV=PV[0]
                if PV[0]=='=>':
                    mod.add_conn(Inst,PV[1],PV[2])
                else:
                    logs.log_error('add_conn failed on "%s"'%(str(PV)))
        elif Item[0]=='process':
            Label = Item[1]
            Stop=False
            if len(Item)==4:
                Sense = getSenseList(Item[2])
                Flow = getProcessBody(Item[3])
                addAlways([],['list']+Sense,Flow)
                Stop=True
            elif len(Item)==3:
                Body0 = Item[2]
            else:
                logs.log_error('process has %d len'%len(Item))
                Stop=True

            if (not Stop):
                if len(Body0)==0:
                    logs.log_error('process "%s" has no body'%str(Label))
                    Body = []
                else:
                    Body = Body0[0]
                if len(Body)==4:
                    Newvars = getNewVars(Body[1])
                    Sense = getSenseList(Body[2])
                    Flow = getProcessBody(Body[3])
                    addAlways(Newvars,['list']+Sense,Flow)
                else:
                    logs.log_error('process "%s" body has %d len'%(Label,len(Body)))
        else:
            logs.log_error('treatBody failed on "%s"'%(str(Item)))

def addAlways(Vars,Sense,Body):  
    mod.addAlways([Sense,Body,'always'])

def getNewVars(List):
    if List==[]: return []
    res= []
    for Item in List:
        if len(Item)==1:
            Item = Item[0]
        if Item[0]=='variable':
            Name = Item[1]
            Kind = Item[2][0]
            Wid = Item[2][1]
            res.append((Name,Kind,Wid))
        else:
            logs.log_error('getNewVars got %s'%str(Item))
    return res
    logs.log_error('getNewVars %s'%str(List))
    return []

def getSenseList(List):
    LL = []
    for Item in List:
        if type(Item)==types.StringType:
            LL.append(Item)
        elif Item[0]=='signal_list':
            More = getSenseList(Item[1])
            LL.extend(More)
        else:
            logs.log_error('getSenseList got %s'%str(List))
    return LL

def getProcessBody(List):
    return List




def treatSignals(L1,Module,Adb):
    for Item in L1:
        if len(Item)==1: Item=Item[0]
        if Item[0]=='signal':
            Net = string.lower(Item[1])
            Wid = Item[2]
            addWire(Net,Wid)
        elif Item[0]=='constant':
            Net = string.lower(Item[1])
            Wid = Item[2]
            Val = Item[3]
            addWire(Net,Wid)
            mod.addHardAssign(Net,str(Val))
        elif Item[0]=='port_map':
            Type = Item[1]
            Ports = Item[2]
            if Ports[0]=='port':
                List = Ports[1]
        elif Item[0]=='type':
            Name = Item[1]
            Kind = Item[2]
            TYPES[Name]=Kind
        else:
            logs.log_error('treat signal failed "%s" '%(str(Item)))

def addWire(Net,Wid):
    if (Wid[0]=='std_logic')or(Wid=='std_logic')or(Wid=='boolean'):
        mod.addWire(Net,'wire',0)
    elif Wid[0]=='integer':
        mod.addWire(Net,'wire',(31,0))
    elif Wid[0]=='std_logic_vector':
        mod.addWire(Net,'wire',Wid[1])
    elif Wid=='integer':
        mod.addWire(Net,'wire',(31,0))
    elif Wid=='unsigned':
        mod.addWire(Net,'wire',(31,0))
    elif Wid[0]=='subbus':
        Hi = Wid[2]
        Lo = Wid[3]
        mod.addWire(Net,'wire',(Hi,Lo))
    elif Wid in TYPES:
        info('USING TYPE %s %s'%(Wid,Net))
    else:
        logs.log_error('adding signal failed net=%s wid=%s '%(Net,Wid))
        info('defined TYPES are %s'%(str(TYPES.keys())))

   
def justify(List,Seq):
    Lseq = string.split(Seq)
    logs.log_info('justify %d<>%d %s %s'%(len(List),len(Lseq),Seq,List))
    if len(List)!=len(Lseq): 
        logs.log_info('justify %d<>%d %s %s'%(len(List),len(Lseq),Seq,List))
        return 
    for ind,Iseq in enumerate(Lseq):
        if Iseq == '?': 
            pass 
        elif Iseq[0] == '!': 
            Look = Iseq[1:]
            if (Look != List[ind][0]): 
                logs.log_info('mismatch (0)  pos=%d look=%s act=%s'%(ind,Look,List[ind][0]))
                return 
        elif (Iseq!=List[ind][0]):
            logs.log_info('mismatch (1) pos=%d look=%s act=%s'%(ind,Iseq,List[ind][0]))
            return 
    logs.log_info('matching %s ok'%Seq) 
KNOWNFUNCTIONS = string.split('ext sxt resize conv_std_logic_vector conv_integer unsigned')
def matches(List,Seq):
    Lseq = string.split(Seq)
    if len(List)!=len(Lseq): return False
    Vars=[]
    for ind,Iseq in enumerate(Lseq):
        if Iseq == '?': 
            Vars.append(List[ind])
        elif Iseq == '$': 
            Who = List[ind][0]
            if Who in KNOWNFUNCTIONS:
                Vars.append(List[ind])
            else:
                return False

        elif Iseq[0] == '!': 
            Look = Iseq[1:]
            try:
                if (Look != List[ind][0]): return False
            except:
                return False
            Vars.append(List[ind])
        elif (Iseq!=List[ind][0]):
            return False
    if Vars==[]: return True 
    return Vars 
     


def getExpr(Root,Adb):
    TRACE.append(('expr',Root))
    Res = getExpr__(Root,Adb)
    TRACE.pop(-1)
    return Res


BIOPS = string.split("Ampersand <= GTSym LTSym SRL XOR | - + * Star AND OR DOWNTO GESym EQSym NESym /= ")
VBIOPS = string.split('concat <= > < << ^ | - + * * & | : >= == != !=')
    
def getExpr__(Root,Adb):
    if (type(Root)==types.ListType)and(len(Root)==1):
        return getExpr(Root[0],Adb)
    if type(Root)==types.IntType: return Root
    if (len(Root)==4)and(Root[1]=='literal'): return Root[0][1:-1]
    if (len(Root)==4)and(Root[1]=='Identifier'): return string.lower(Root[0])
    if (len(Root)==4)and(Root[1]=='DecimalInt'): return int(Root[0])
    if (len(Root)==4)and(Root[1]=='BasedInt'): 
        Str = Root[0]
        if Str[0]=='x':
            Val = int(Str[2:-1],16)
            return Val
        logs.log_error('getExpr of BasedInt got %s'%Str)
        return 0

    if (len(Root)==4)and(Root[1]=='BitStringLit'): return ['bin',len(Root[0])-2,Root[0][1:-1]]
    if (len(Root)==4)and(Root[1]=='OTHERS'): return ['others']

    if (len(Root)==2)and(Root[0][0] == 'NOT'):
        AA = getExpr(Root[1],Adb)
        return [['~',AA]]

    if (len(Root)==3)and(Root[1][0] in BIOPS):
        AA = getExpr(Root[0],Adb)
        BB = getExpr(Root[2],Adb)
        if Root[1][0]=='DOWTO': return [':',AA,BB]
        Ind = BIOPS.index(Root[1][0])
        return [VBIOPS[Ind],AA,BB]
    if (len(Root)==3)and(Root[0][0] == 'LeftParen')and(Root[2][0] == 'RightParen'):
        return getExpr(Root[1],Adb)

    if (len(Root)==2)and(type(Root)==types.TupleType)and(Root in Adb):
        return getExpr(Adb[Root],Adb)
    if (len(Root)==2)and(type(Root)==types.ListType)and(len(Root[0])==4)and(len(Root[1])==2)and(Root[1] in Adb):
        Root2 = level1up(Root,Adb)
        XX= getExpr(Root2,Adb)
        if (XX[0]=='subbit')and(type(XX[2])==types.ListType)and(XX[2][0]==':'):
            return ['subbus',string.lower(XX[1]),XX[2][1],XX[2][2]]
        return XX
    if (len(Root)==3)and(Root[1][0] == "'"):
        return ['funccall',Root[2][0],Root[0][0]]

    if (len(Root)==2)and(type(Root)==types.ListType)and(Root[0] in Adb)and(Root[1] in Adb):
        Expr = getExpr(Root[0],Adb)
        XX =  getExpr([DUMMY+Adb[Root[1]]],Adb)
        XX[1] = Expr
        return XX
    Vars =  matches(Root,"OTHERS => ?")
    if Vars:
        return getExpr(Vars[0],Adb)

    Vars =  matches(Root,"UNTIL ? AND ?")
    if Vars:
        AA = getExpr(Vars[0],Adb)
        BB = getExpr(Vars[1],Adb)
        return ['until',['&',AA,BB]]

    Vars =  matches(Root,"? ? | ?")
    if Vars:
        AA = getExpr(Vars[0],Adb)
        BB = getExpr(Vars[1],Adb)
        CC = getExpr(Vars[2],Adb)
        return [['|',AA,BB,CC]]
    Vars =  matches(Root,"| ?")
    if Vars:
        AA = getExpr(Vars[0],Adb)
        return [['|',AA]]

    Vars =  matches(Root,"? RANGE ?")
    if Vars:
        AA = getExpr(Vars[1],Adb)
        return ['range',Vars[0],AA]

    Vars =  matches(Root,"? TO ?")
    if Vars:
        AA = getExpr(Vars[0],Adb)
        BB = getExpr(Vars[1],Adb)
        return ['to',AA,BB]

    Vars =  matches(Root,"FOR ? IN ? ")
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        Range = getExpr(Vars[1],Adb)
        return ('for',Cond,Range)
    Vars =  matches(Root,"$ LeftParen ? !...element_association.. RightParen")
    if Vars:
        Y = getExpr(Vars[1],Adb)
        Z = getExpr(Vars[2],Adb)
        return ['funccall',Vars[0],[Y,Z]]

    Vars =  matches(Root,"LeftParen ? !...element_association.. RightParen")
    if Vars:
        X = Vars[0][0]
        Y = getExpr(Adb[Vars[1]],Adb)
        return ('elem',X,Y)
    Vars =  matches(Root,"!...element_association.. ?")
    if Vars:
        X = Vars[1][0]
        Y = getExpr(Adb[Vars[0]],Adb)
        return ('elem',Y,X)

    if (len(Root)==2)and(type(Root)==types.ListType):
        if (Root[0][1] in ['DecimalInt','BasedInt'])and(Root[0][1] in ['DecimalInt','BasedInt']):
            return ('tuple',Root[0][0],Root[1][0])

    Vars = matches(Root,'? WHEN ? ELSE ?')
    if Vars:
        Cond = getExpr(Vars[1],Adb)
        Yes = getExpr(Vars[0],Adb)
        No = getExpr(Vars[2],Adb)
        return ('question',Cond,Yes,No)

    Vars = matches(Root,'OTHERS ?')
    if Vars:
        return getExpr(Vars[0],Adb)

    Vars = matches(Root,'? WHEN !expression ELSE')
    if Vars:
        Cond = getExpr(Adb[Vars[1]],Adb)
        Yes = getExpr(Vars[0],Adb)
        return ('question1',Cond,Yes)


    Vars = matches(Root,'RANGE ? TO ?')
    if Vars:
        From = getExpr(Vars[0],Adb)
        To = getExpr(Vars[1],Adb)
        return ('range',From,To)

    Vars = matches(Root,'? LeftParen !element_association RightParen')
    if Vars:
        LL = getExpr(Adb[Vars[1]],Adb)
        return ('subbit',string.lower(Vars[0][0]),LL)
    Vars = matches(Root,'? LeftParen ? RightParen')
    if Vars:
        LL = getExpr(Vars[1],Adb)
        return ('subbit',string.lower(Vars[0][0]),LL)

    Vars = matches(Root,'!..waveform__WHEN__condition__ELSE.. ? WHEN ? ELSE')
    if Vars:
        AA = getExpr(Vars[0],Adb)
        Yes = getExpr(Vars[1],Adb)
        Cond = getExpr(Vars[2],Adb)
        Expr = ('question0',AA,Cond,Yes)
        return Expr
    Vars = matches(Root,'LeftParen ? !...enumeration_literal.. RightParen')
    if Vars:
        AA = getExpr(Vars[0],Adb)
        BB = getList_new(Adb[Vars[1]],Adb)
        return ['enumlit',[AA]+BB]


    logs.log_error('getExpr got %s'%(str(Root)))
    reportTrace(TRACE)
    traceback.print_stack()
    return Root

def reportTrace(Trace):
    for Item in Trace:
        info('          %s'%str(Item))
    info('\n\n\n')

def level1up(List,Adb):
    Res = [] 
    for Item in List:
        if (type(Item)==types.TupleType)and(Item in Adb):
            LL = Adb[Item]
            Res.extend(LL)
        else:
            Res.append(Item)
    return Res



def reportAdb(Adb,Which='stam'):
    Fout = open('%s.report'%Which,'w')
    for Key in Adb.keys():
        Val = str(Adb[Key])
#        if len(Val)>150: Val = Val[:150]

        Fout.write('%s report %s   %s\n'%(Which,Key,Val))
    Fout.close()

    Defined=[]
    Used=[]
    for Key in Adb.keys():
        Defined.append(Key)
        List = Adb[Key]
        for Item in List:
            if len(Item)==2:
                if Item not in Adb:
                    info('item %s is not in adb'%(str(Item)))



def listify(List):
    if type(List)==types.ListType:
        if len(List)==0: return List
        if (type(List[0])==types.ListType):
            return ['list']+List
    return List

def reworkWHENELSE(Expr):
    if Expr[0]=='question':
        Else = Expr[2]
        Body = Expr[1]
        if Body[0]=='question1':
            Cond = Body[1]
            Yes  = Body[2]
            No = Else
            return ['question',Cond,Yes,No]
        if Body[0]=='question0':
            Deep =  reworkDeep(Body,[],Else)
            while len(Deep)>=2:
                X = ['question',Deep[-2][0],Deep[-2][1],Deep[-1]]
                Deep.pop(-1)
                Deep.pop(-1)
                Deep.append(X)

            info('deep %s'%str(Deep))
            return Deep
    logs.log_error('0>>> %s'%str(Expr))
    return '0'

def reworkDeep(Body,Sofar,Else):
    if Body[0]=='question1':
        Cond = Body[1]
        Yes  = Body[2]
        All = [(Cond,Yes)]+Sofar+[Else]
        return All
    if Body[0]=='question0':
        Cond = Body[2]
        Yes  = Body[3]
        return reworkDeep(Body[1],[(Cond,Yes)]+Sofar,Else)
        
    logs.log_error('reworkDeep got body=%s'%str(Body))
    return []
        
def __reworkWHENELSE(Expr):
    info('expr %s'%str(Expr))
    return '0'

    if len(Expr)==3:
        if Expr[0]=='question1':
            Cond0 = Expr[1][1]
            Yes0  = Expr[1][2]
            No0  = Expr[2]
            Ret = ['question',Cond0,Yes0,No0]
            return Ret
        if Expr[0]=='question':
            if Expr[1][0]=='question1':
                Cond = Expr[1][1]
                Yes = Expr[1][2]
                No = Expr[2]
                return ['question',Cond,Yes,No]
        if Expr[0]=='question':
            if Expr[1][0]=='question0':
                if Expr[1][1][0]=='question1':
                    Cond0 = Expr[1][1][1]
                    Yes0  = Expr[1][1][2]
                    Cond1 = Expr[1][2]
                    Yes1  = Expr[1][3]
                    No    = Expr[2]
                    Ret = ['question',Cond0,Yes0,['question',Cond1,Yes1,No]]
                    return Ret
                elif Expr[1][1][0]=='question0':
                    New = reworkWHENELSE(Expr)
                    print 'new',New
    print 'reowrk failed',len(Expr),Expr
    return Expr



main()

