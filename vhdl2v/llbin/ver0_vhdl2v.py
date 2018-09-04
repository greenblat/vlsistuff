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

def main():
    if len(sys.argv)>1:
        Fname = sys.argv[1]
        os.system('vhdllexer.py %s'%Fname)
        os.system('pybin/reworkMyLex.py lex.out lex2.out')
        os.system('pybin/vyaccer2.py lex2.out')

    File = open('db0.pickle')
    Adb = pickle.load(File)
#    reportAdb(Adb,'zzz')
    cleanComas(Adb)
    rounds0(Adb)
    rounds1(Adb)
#    removes0(Adb)

#    mergeLists(Adb)
    dones = 1
    while dones>0:
        dones = removeUnused(Adb)
#    special0(Adb)
#    return
    scanStuff_new(Adb)
    makeVerilog()
    mod.dumpVerilog()

    reportAdb(Adb,'fff')
#    reportLinks(Adb)

def special0(Adb):
    Found={}
    for Key in Adb:
        List = Adb[Key]
        if len(List[0])==4:
            First = List[0][0]
            if First not in Found:
                info('first %s'%str(List))
                Found[First]=True


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
        Vars = matches(List,'ARCHITECTURE ? OF ? IS !architecture_declarative_part BEGIN_ !architecture_statement_part END ARCHITECTURE')
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

        Vars = matches(List,'ENTITY ? IS !.port_clause. END')
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


def getList_new(Item,Adb):
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
        return AA+[BB]

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
        return [('assign',Vars[0][0],Expr)]

    Vars = matches(Item,'? <= !..waveform__WHEN__condition__ELSE.. ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Expr = getExpr(Adb[Vars[1]],Adb)
        Else = getExpr(Vars[2],Adb)
        Expr = ['question',Expr[1],Expr[2],Else]
        return [('assign',Dst,Expr)]


    Vars = matches(Item,'? => ?')
    if Vars:
        Expr = getExpr(Vars[1],Adb)
        return [('=>',Vars[0][0],Expr)]

    Vars = matches(Item,'? <= ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Src = getExpr(Vars[1],Adb)
        return [('assign',Dst,Src)]

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

    Vars = matches(Item,'SIGNAL ? Colon !subtype_indication')
    if Vars:
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        return [('signal',Vars[0][0],Subtype)]
    Vars = matches(Item,'SIGNAL ? Colon ?')
    if Vars:
        return [('signal',Vars[0][0],Vars[1][0])]


    Vars = matches(Item,'Constant ? Colon ? !.VarAsgn__expression.')
    if Vars:
        return [('constant',Vars[0][0],Vars[1][0],getVarAsgn(Adb[Vars[2]],Adb))]

    Vars = matches(Item,'!a_label ? !.generic_map_aspect. !.port_map_aspect.')
    if Vars:
        print 'vars',Vars
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
        return [('port_map_aspect',Label,Vars[1][0],LL)]

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

    Vars = matches(Item,'WAIT !.condition_clause.')
    if Vars:
        LL = getExpr(Adb[Vars[0]],Adb)
        return [('wait',LL)]

    Vars = matches(Item,'CASE !expression IS !case_statement_alternative  !..case_statement_alternative.. END CASE')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('case',Cond,LL0,LL1)]

    Vars = matches(Item,'CASE ? IS !case_statement_alternative  !..case_statement_alternative.. END CASE')
    if Vars:
        Cond = Vars[0]
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('case',Cond,LL0,LL1)]


    Vars = matches(Item,'IF !condition')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        return [('if',Cond)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL = getList_new(Adb[Vars[1]],Adb)
        return [('if',Cond,LL)]

    Vars = matches(Item,'ELSIF !condition THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts..')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('elsif',Cond,LL0,LL1)]

    Vars = matches(Item,'ELSIF !condition THEN !sequence_of_statements')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        return [('elsif',Cond,LL0)]

    Vars = matches(Item,'WHEN OTHERS =>')
    if Vars:
        return [('case','default')]

    Vars = matches(Item,'WHEN ? => !sequence_of_statements')
    if Vars:
        Cond = getExpr(Vars[0],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        return [('case',Cond,LL0)]
    Vars = matches(Item,'? := ?')
    if Vars:
        Dst = getExpr(Vars[0],Adb)
        Src = getExpr(Vars[1],Adb)
        return [(':=',Dst,Src)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts.. !.ELSE__seq_of_stmts. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        LL2 = getList_new(Adb[Vars[3]],Adb)
        return [('ifelse',Cond,LL0,LL1,LL2)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !..ELSIF__THEN__seq_of_stmts.. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('ifelse',Cond,LL0,LL1)]

    Vars = matches(Item,'IF !condition THEN !sequence_of_statements !.ELSE__seq_of_stmts. END IF')
    if Vars:
        Cond = getExpr(Adb[Vars[0]],Adb)
        LL0 = getList_new(Adb[Vars[1]],Adb)
        LL1 = getList_new(Adb[Vars[2]],Adb)
        return [('ifelse',Cond,LL0,LL1)]

    Vars = matches(Item,'ELSE !sequence_of_statements')
    if Vars:
        LL0 = getList_new(Adb[Vars[0]],Adb)
        return [('else',LL0)]

    Vars = matches(Item,'VARIABLE ? Colon !subtype_indication')
    if Vars:
        Subtype = getSubtype(Adb[Vars[1]],Adb)
        return [('variable',Vars[0][0],Subtype)]

    Vars = matches(Item,'COMPONENT ? !.PORT__local_port_list.  END COMPONENT')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        return [('port_map',Vars[0][0],LL)]

    Vars = matches(Item,'PROCESS !.sensitivity_list. BEGIN_ !sequence_of_statements END PROCESS')
    if Vars:
        Sense = getList_new(Adb[Vars[0]],Adb)
        Stats = getList_new(Adb[Vars[1]],Adb)
        return [('process',[],Sense,Stats)]

    Vars = matches(Item,'PROCESS !process_declarative_part BEGIN_ !sequence_of_statements END PROCESS')
    if Vars:
        Declares = getList_new(Adb[Vars[0]],Adb)
        Stats = getList_new(Adb[Vars[1]],Adb)
        return [('process',Declares,[],Stats)]

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
        LL = getList_new(Adb[Vars[1]],Adb)
        return ['list',Vars[0][0]]+LL

    Vars = matches(Item,'? !...association_element..')
    if Vars:
        LL = getList_new(Adb[Vars[1]],Adb)
        return ['assoc',Vars[0][0]]+LL

    Vars = matches(Item,'!...name.. ?')
    if Vars:
        LL = getList_new(Adb[Vars[0]],Adb)
        return ['list']+LL+[Vars[0][0]]

    Vars = matches(Item,'? Colon ?')
    if Vars:
        return [('definition',Vars[0][0],Vars[1][0])]
    Vars = matches(Item,'? ?')
    if Vars:
        return ['list',Vars[0][0],Vars[1][0]]

#    justify(Item,'PROCESS !.sensitivity_list. BEGIN_ !sequence_of_statements END PROCESS')

    logs.log_error('getList_new failed on "%s"'%str(Item))
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
        Vars2 =  matches(Range,'? TO !simple_expression')
        if Vars2:
            Expr = getExpr(Adb[Vars2[1]],Adb)
            return ('range',Vars2[0][0],Expr)

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

    logs.log_error('architecture_new kind=%d'%Kind)



def scanStuff(Adb):
    for (What,Num) in Adb.keys():
        if What in ['library_unit','design_unit','..design_unit..']:
            L0 = Adb[(What,Num)]
            travelArch(L0,Adb,'scanstuff')


def architecture(Vars,Adb):
    Mod = Vars['?module']
    mod.addModule(Mod)
    L1 = Adb[Vars['?Key1']]
    L2 = Adb[Vars['?Key2']]

    if L1!=[]:
        if len(L1[0])==4:
            activate(L1,Adb,'ports')
        else: 
            for Item in L1:
                L1x = Adb[Item]
                travelArch(L1x,Adb,'ports')
    if L2!=[]:
        if len(L2[0])==4:
            activate(L2,Adb,'architecture')
        elif (L2[0][0]=='target')and(L2[0] in Adb): 
            concurrent_statement(L2,Adb,False)
        else: 
            for Item in L2:
                L2x = Adb[Item]
                info('l2x arch %s'%str(L2x))
                travelArch(L2x,Adb,'architecture')

def travelArch(List,Adb,Action,Verbose=False):
    if (type(List)==types.TupleType)and (List not in Adb):
        dealTuple(List,Adb,Action,Verbose)
        return
    if (type(List)==types.TupleType)and (List in Adb):
        Item = Adb[List]
        travelArch(Item,Adb,Action,Verbose) 
        return

    if type(List) == types.ListType:
        if  len(List[0])==4:
            if Verbose: info('travelArch1 %s %s'%(Action,str(List)))
            activate(List,Adb,Action)
            return
        if  (len(List)>1)and (len(List[1])==4):
            if Verbose: info('travelArch2 %s %s'%(Action,str(List)))
            activate(List,Adb,Action)
            return

    if Verbose: info('godown %s'%str(List))
    for Item in List:
        dealTuple(Item,Adb,Action,Verbose)
    

def dealTuple(Item,Adb,Action,Verbose=False):
    if (type(Item)==types.TupleType)and(Item in Adb):
        if lastOne('formal_port_element',Item,Adb):
            formal_port_element(Adb[Item],Adb)
        elif lastOne('concurrent_statement',Item,Adb):
            concurrent_statement(Adb[Item],Adb,False)
        elif lastOne('block_declarative_item',Item,Adb):
            block_declarative_item(Adb[Item],Adb)
        elif lastOne('sequential_statement',Item,Adb):
            sequential_statement(Adb[Item],Adb)
        else:
            if Verbose: info('travelArch3 enter down %s %s'%(Action,str(Item)))
            travelArch(Item,Adb,Action,Verbose) 
    else:
        if Verbose: info('travelArch4 %s %s'%(Action,str(Item)))
        activate(Item,Adb,Action)



FLAGGED = string.split('formal_port_element ...formal_port_element.. ..formal_port_element.. concurrent_statement ..concurrent_statement.. ..block_declarative_item.. block_declarative_item sequential_statement  ..sequential_statement.. ...local_port_element.. local_port_element')

def lastOne(What,Item,Adb):
    if Item[0]==What: return True
    LL = Adb[Item]
    if (Item[0]=='..%s..'%What)and (len(LL)!=2): return True
    if ((Item[0]=='..%s..'%What)and (LL[0][0] not in FLAGGED)): return True
    if ((Item[0]=='...%s..'%What)and (LL[0][0] not in FLAGGED)): return True
    return False



def activate(List,Adb,Action):
    if hasAssigner(List):
        concurrent_statement(List,Adb,False)
        return
    return matchit(Action,List,Adb,'activate')




def entity0(Vars,Adb):
    Mod = Vars['?module']
    mod.addModule(Mod)
    if '?Key2' in Vars:
        Key1 = Vars['?Key1']
        Key2 = Vars['?Key2']
        matchit('generic',Adb[Key1],Adb,'entity0')
        matchit('externals',Adb[Key2],Adb,'entity1')
    else:
        Key1 = Vars['?Key1']
        matchit('externals',Adb[Key1],Adb,'entity1')

def externals(Vars,Adb):
    Key = Vars['?Key1']
    List = Adb[Key]
    travelArch(List,Adb,'externals0')

def ports(Vars,Adb):
    Key = Vars['?Key1']
    List = Adb[Key]
    travelArch(List,Adb,'ports')
        

def external_wire(Vars,Adb):
    mod.addWire(Vars['?name'],Vars['?dir'])

def external_bus1(Vars,Adb):
    Bus = Vars['?name']
    Dir = Vars['?dir']
    Key = Vars['?Key1']
    From,To = matchit(3,Adb[Key],Adb,'external_bus')
    mod.addWire(Vars['?name'],Vars['?dir'],From,To)

def external_bus0(Vars,Adb):
    Bus = Vars['?name']
    Dir = Vars['?dir']
    Key = Vars['?Key1']
    LL = Adb[Vars['?Key1']]
    From,To = matchit(4,LL,Adb,'constraint0')
    mod.addWire(Bus,Dir,From,To)

def range0(Vars,Adb):
    From = Vars['?from']
    To = Vars['?to']
    return From,To

def constraint0(Vars,Adb):
    if '?Key1' in Vars:
        LL = Adb[Vars['?Key1']]
        return matchit(4,LL,Adb,'constraint0')
    if '?from' in Vars:
        return  (Vars['?from'],Vars['?to'])

def constraint1(Vars,Adb):
    return (Vars['?from'],Vars['?to'])
    
def constant0(Vars,Adb):
    if '?Key0' in Vars:
        Name = Vars['?name']
        Val = Vars['?const']
        Expr = getExpr(Vars['?Key0'],Adb)
        mod.addWire(Name,'wire',Expr)
        mod.addHardAssign(Name,Val)
        return
        
    if '?Key1' in Vars:
        Expr = getExpr(Vars['?Key1'],Adb)
        Name = Vars['?name']
        Kind = Vars['?kind']
        mod.addWire(Name,'wire',Kind)
        mod.addHardAssign(Name,Expr)


def signal0(Vars,Adb):
    Name = Vars['?name']
    if (type(Name)==types.TupleType)and(Name in Adb):
        L0 = Adb[Name]
        for Item in L0:
            VV = {}
            for Key in Vars:
                VV[Key]=Vars[Key]
            VV['?name']=Item
            signal0(VV,Adb)
        return

    if '?Key3' in Vars:
        List = getList(Vars['?Key3'],Adb)
        return

    if (type(Name)==types.TupleType)and(len(Name)==4):
        Name = Name[0]



    if '?Key0' in Vars:
        Expr = getExpr(Vars['?Key0'],Adb)
        if type(Expr)==types.ListType:
            if Expr[0]==':':
                mod.addWire(Name,'wire',Expr[1],Expr[2])
            else:
                logs.log_error('signa0: got %s %s'%(Name,Expr))
            return
        mod.addWire(Name,'wire')
        return
    if '?Key2' in Vars:
        Expr = getExpr(Vars['?Key2'],Adb)
        info('expr %s vars=%s key=%s'%(Expr,Vars['?Key2'],Adb[Vars['?Key2']]))
        mod.addWire(Name,'wire',Expr)
        return



def type0(Vars,Adb):
    info('type0 %s'%(str(Vars)))

def component0(Vars,Adb):
    Expr = Adb[Vars['?Key2']]
    Name = Vars['?name']
    scanCompPins(Expr,Name,Adb)

def scanCompPins(Expr,Name,Adb):
    if (len(Expr)==2)and(type(Expr)==types.ListType):
        scanCompPins(Expr[0],Name,Adb)
        scanCompPins(Expr[1],Name,Adb)
        return
    if (len(Expr)==2)and(type(Expr)==types.TupleType)and(Expr in Adb):
        scanCompPins(Adb[Expr],Name,Adb)
        return
    Res =  matchit('component0',Expr,Adb,'component_pins')
    if Res:
        Kind,Vars = Res
        Dir = Vars['?dir']
        Pin = Vars['?name']
        if Kind=='wire':
            addPinDef(Name,Pin,Dir,0)
        elif Kind=='bus1':
            Key = Vars['?Key1']
            From,To = matchit(3,Adb[Key],Adb,'external_bus')
            addPinDef(Name,Pin,Dir,(From,To))
        elif Kind=='bus0':
            Key = Vars['?Key1']
            From,To = matchit(3,Adb[Key],Adb,'external_bus')
            addPinDef(Name,Pin,Dir,(From,To))

        return
    logs.log_error('scanCompPins got %s %s'%(Expr,Name))

def component_wire(Vars,Adb):
    return 'wire',Vars
def component_bus0(Vars,Adb):
    return 'bus0',Vars
def component_bus1(Vars,Adb):
    return 'bus1',Vars

PINDEFS = {}
def addPinDef(Type,Pin,Dir,Wid):
    Pin = string.lower(Pin)
    if Type not in PINDEFS:
        PINDEFS[Type] = [(Pin,Dir,Wid)]
    else:
        PINDEFS[Type].append((Pin,Dir,Wid))
    
    



def genericmap0(Vars,Adb):
    info('genericmap0 %s'%(str(Vars)))

def generic0(Vars,Adb):
    Key = Vars['?Key1']
    L0 = Adb[Key]
    travelArch(L0,Adb,'generic0')

def generic00(Vars,Adb):
    Name = Vars['?name']
    Expr = getExpr(Vars['?Key1'],Adb)
    mod.addModuleParam(Name,Expr)




def assign0(Vars,Adb):
    info('assign0 %s'%(str(Vars)))
def assigner1(Vars,Adb):
    info('assigner1 %s'%(str(Vars)))
def expression0(Vars,Adb):
    if '?Key8' in Vars:
        Yes = getExpr(Vars['?Key3'],Adb)
        No = getExpr([Vars['?Key5'],Vars['?Key7'],Vars['?Key8']],Adb)
        Cond = getExpr(Vars['?Key4'],Adb)
        return ['question',Cond,Yes,No]
    if '?Key0' in Vars:
        Net = Vars['?dst']
        Ind = getExpr(Vars['?Key0'],Adb)
        if Net=='std_logic_vector': 
            return Ind
        return ['subbit',Net,Ind]
    if '?Key1' in Vars:
        Fr = getExpr(Vars['?Key1'],Adb)
        To = getExpr(Vars['?Key2'],Adb)
        return ['range',Fr,To]
    if '?Key3' in Vars:
        Yes = getExpr(Vars['?Key3'],Adb)
        No = getExpr(Vars['?Key5'],Adb)
        Cond = getExpr(Vars['?Key4'],Adb)
        return ['question',Cond,Yes,No]
    if '?Key6' in Vars:
        Others = getExpr(Vars['?Key6'],Adb)
        return Others
        
    info('expression0 %s'%(str(Vars)))
    return 'err'

def assigner0(Vars,Adb):
    LLS = explicit0('?Modsrc',Vars,Adb)
    LLD = explicit0('?Moddst',Vars,Adb)
    dst = string.lower(Vars['?dst'])
    src = string.lower(Vars['?src'])
    if LLD=='':
        Dst = dst
    else:
        Fr,To = matchit(3,LLD,Adb,'signal0')
        Dst = ['subbus',dst,(Fr,To)]

    if LLS=='':
        Src = src
    else:
        Fr,To = matchit(3,LLS,Adb,'signal0')
        Src = ['subbus',src,(Fr,To)]
    mod.addHardAssign(Dst,Src)

def explicit0(Key,Vars,Adb):
    if Key in Vars:
        return explicit(Vars[Key],Adb)
    return ''


def explicit(Key,Adb):
    if (type(Key)==types.TupleType)and (Key in Adb):
        List = Adb[Key]
        Res = []
        for Item in List:
            X = explicit(Item,Adb)
            Res.extend(X)
        return Res
    else:
        return [Key]



def concurrent_statement(List,Adb,Soft=True):
    List2 = level1up(List,Adb)
    Has = hasAssigner(List)
    if (Has):
        Has = hasAssigner(List2)
        Dst0 = List2[:Has]
        Src0 = List2[Has+1:]
        Dst1 = getExpr(Dst0,Adb)
        Src1 = getExpr(Src0,Adb)
        if Soft:
            mod.addSoftAssign(Dst1,Src1)
        else:
            mod.addHardAssign(Dst1,Src1)
    else:
        matchit('concurrent_statement',List2,Adb,'concurrent_statement')

def getList(Root,Adb):
    if (type(Root)==types.ListType)and(len(Root)==1):
        return getExpr(Root[0],Adb)
    if (len(Root)==4)and(Root[1]=='literal'): return [Root[0]]
    if (len(Root)==4)and(Root[1]=='Identifier'): return [Root[0]]
    if (len(Root)==4)and(Root[1]=='DecimalInt'): return [int(Root[0])]
    if (len(Root)==3)and(Root[0][0] == 'LeftParen')and(Root[2][0] == 'RightParen'):
        return getList(Root[1],Adb)

    info('getList %s'%str(Root))
    Vars = matches(Root,"VARIABLE ? Colon ?")
    if Vars:
        Var = Vars[0]
        Expr = getExpr(Vars[1],Adb)
        info("VARIABLE %s %s"%(Var,Expr))
        return Var

    if (len(Root)==2)and(type(Root)==types.TupleType)and(Root in Adb):
        return getList(Adb[Root],Adb)

    if (type(Root)==types.ListType):
        LL = []
        for Item in Root:
            A = getList(Item,Adb)
            LL.extend(A)
        return LL
    

    logs.log_error('getList got %s'%(str(Root)))
    return Root



BIOPS = string.split("<= GTSym LTSym SRL XOR | - + * Star AND OR DOWNTO GESym EQSym NESym /= ")
VBIOPS = string.split('<= > < << ^ | - + * * & | : >= == != !=')
def getExpr(Root,Adb):
    if (type(Root)==types.ListType)and(len(Root)==1):
        return getExpr(Root[0],Adb)
    if type(Root)==types.IntType: return Root
    if (len(Root)==4)and(Root[1]=='literal'): return Root[0][1:-1]
    if (len(Root)==4)and(Root[1]=='Identifier'): return string.lower(Root[0])
    if (len(Root)==4)and(Root[1]=='DecimalInt'): return int(Root[0])
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
            return ['subbus',XX[1],XX[2][1],XX[2][2]]
        return XX
    if (len(Root)==3)and(Root[1][0] == "'"):
        return ['funccall',Root[2][0],Root[0][0]]

    if (len(Root)==2)and(type(Root)==types.ListType)and(Root[0] in Adb)and(Root[1] in Adb):
        Expr = getExpr(Root[0],Adb)
        XX =  getExpr([DUMMY+Adb[Root[1]]],Adb)
        XX[1] = Expr
        return XX

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

    Vars = matches(Root,'? WHEN !expression ELSE')
    if Vars:
        Cond = getExpr(Adb[Vars[1]],Adb)
        Yes = getExpr(Vars[0],Adb)
        return ('?',Cond,Yes)



    Res =  matchit('expression',Root,Adb,'expression')
    if Res: return Res


    logs.log_error('getExpr got %s'%(str(Root)))
    return Root

DUMMY = [['RRRFFF','Identifier','9999','9999']]


def hasAssigner(List):
    for ind,Item in enumerate(List):
        if Item[0]=='<=': return ind
    return False

def sequential_statement(List,Adb):
    if hasAssigner(List):
        concurrent_statement(List,Adb,True)
    else:
        info('sequential_statement %s'%str(List))


def formal_port_element(List,Adb):
    if (len(List)>=4)and(List[1][0]=='Colon'):
        Net = List[0][0]
        Dir = List[2][0]
        Expr = getExpr(List[3:],Adb)
        mod.addWire(Net,Dir,Expr)

        

def block_declarative_item(List,Adb):
    List2 = level1up(List,Adb)
#    info('block_declarative_item %s'%str(List))
    matchit('block',List2,Adb,'block')

def instance0(Vars,Adb):
    Inst = Vars['?inst']
    Type = Vars['?type']
    mod.addIstance(Inst,Type)
    K0 = explicit0('?Key0',Vars,Adb)
    K1 = cleanit0(explicit0('?Key1',Vars,Adb))
    if type(K0)==types.ListType:
        while K0!=[]:
            Pin,DX,Sig = K0[:3]
            K0 = K0[3:]
            mod.add_instance_param(Inst,Pin[0],Sig[0])
    if '=>' in K1:
        explicitConns(Inst,K1)
    elif Type in PINDEFS:
        for ind,Net in enumerate(K1):
            Pin,_,_ = PINDEFS[Type][ind]
            Net = string.lower(Net)
            mod.add_conn(Inst,Pin,Net)

def explicitConns(Inst,K1):
    while K1!=[]:
        Pin,DX,Sig = K1[:3]
        Pin = string.lower(Pin)
        if DX!='=>':
            logs.log_error('wtf %s  %s %s %s'%(str(K1),Pin,DX,Sig))
        Sig = string.lower(Sig)
        K1 = K1[3:]
        if (len(K1)>2)and(K1[1]!='=>')and(K1[0]=='LeftParen'):
            Ind = K1.index('RightParen')
            Sub = K1[:Ind+1]
            if len(Sub)==3:
                Sig = ['subbit',Sig,Sub[1]]
            else:
                logs.log_error('subwire got "%s"   "%s"'%(Sub,K1))
            K1 = K1[Ind+1:]
        mod.add_conn(Inst,Pin,Sig)


def cleanit0(List):
    Res=[]
    for X in List:
        Res.append(X[0])
    return Res
Label = ''
def label0(Vars,Adb):
    global Label
    Label = Vars['?label']
    

def generate0(Vars,Adb):
    info('generate0 %s'%(str(Vars)))
def process0(Vars,Adb):
    global Label
    Sense = getList(Adb[Vars['?Key1']],Adb)
    Sense=lowerize(Sense)
    Statements = Adb[Vars['?Key2']]

    Body = travelProcess(Statements,Adb)
    info('body %s'%str(Body))
    if Label=='':
        Always = [['list']+Sense,Body,'always']
    else:
        Always = [['list']+Sense,['named_begin',Label,Body],'always']
    
    mod.addAlways(Always)
    Label=''


def travelProcess(Statements,Adb):
    if (type(Statements)==types.TupleType)and(len(Statements)==4):
        return Statements[0]
    if type(Statements)==types.ListType:
        if (len(Statements)==2)and(Statements[0][0]=='a_label'):
            return travelProcess(Adb[Statements[1]],Adb)
        if (len(Statements)==2)and(Statements[0][0]=='sequential_statement'):
            AA = travelProcess(Adb[Statements[0]],Adb)
            BB = travelProcess(Adb[Statements[1]],Adb)
            if BB[0]=='list': BB.pop(0)
            if AA[0]!='list': return ['list']+AA+BB
            return  AA+BB
        if (len(Statements)==2)and(Statements[0][0]=='..case_statement_alternative..'):
            AA = travelProcess(Adb[Statements[0]],Adb)
            BB = travelProcess(Adb[Statements[1]],Adb)
            if BB[0]=='list': BB.pop(0)
            if AA[0]!='list': return ['list']+AA+BB
            return AA+BB

        Vars =  matches(Statements,"? LOOP ? END LOOP")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Body =  travelProcess(Adb[Vars[1]],Adb)
            info('LOOOP %s %s'%(Cond,Body))
            return ['loop']

        Vars =  matches(Statements,"? LOOP ? END LOOP ?")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Body =  travelProcess(Adb[Vars[1]],Adb)
            info('LOOOP %s %s'%(Cond,Body))
            return ['loop']



        Vars =  matches(Statements,"IF ? THEN ? ? ? END IF")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            AA = travelProcess(Adb[Vars[1]],Adb)
            BB = travelProcess(Adb[Vars[2]],Adb)
            CC = travelProcess(Adb[Vars[3]],Adb)
            IF = reworkIf(['if',Cond,AA,BB,CC])
            return [IF]
        Vars =  matches(Statements,"ELSE ? ")
        if Vars:
            Seq = travelProcess(Adb[Vars[0]],Adb)
            return ['else',Seq]
        Vars =  matches(Statements,"ELSIF ? THEN ? ")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Seq = travelProcess(Adb[Vars[1]],Adb)
            return ['elsif',Cond,Seq]

        Vars =  matches(Statements,"ELSIF ? THEN ? ? ")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Seq = travelProcess(Adb[Vars[1]],Adb)
            Seq2 = travelProcess(Adb[Vars[2]],Adb)
            return [['elsif',Cond,Seq],Seq2]

        Vars =  matches(Statements,"IF ? THEN ? ? END IF")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Seq = travelProcess(Adb[Vars[1]],Adb)
            Else = travelProcess(Adb[Vars[2]],Adb)
            IF = reworkIf(['if',Cond,Seq,Else])
            return [IF]
        Vars =  matches(Statements,"IF ? THEN ? END IF")
        if Vars:
            Cond = getExpr(Adb[Vars[0]],Adb)
            Seq = travelProcess(Adb[Vars[1]],Adb)
            IF = reworkIf(['if',Cond,Seq])
            return [IF]
        Vars =  matches(Statements,"? <= ?")
        if Vars:
            Dst = getExpr(Vars[0],Adb)
            Src = getExpr(Vars[1],Adb)
            return [['<=',Dst,Src]]
        Vars =  matches(Statements,"? := ?")
        if Vars:
            Dst = getExpr(Vars[0],Adb)
            Src = getExpr(Vars[1],Adb)
            return [['<=',Dst,Src]]
        Vars =  matches(Statements,"CASE ? IS ? ? END CASE")
        if Vars:
            Cond = getExpr(Vars[0],Adb)
            Seq1 = travelProcess(Adb[Vars[1]],Adb)
            Seq2 = travelProcess(Adb[Vars[2]],Adb)
            if Seq2[0]=='list': Seq2.pop(0)
            return [['case',Cond,Seq1+Seq2]]
        Vars =  matches(Statements,"WHEN OTHERS => ? ")
        if Vars:
            Seq = travelProcess(Adb[Vars[0]],Adb)
            return [['default',Seq]]
        Vars =  matches(Statements,"WHEN OTHERS => ")
        if Vars:
            return [['default','null']]

        Vars =  matches(Statements,"EXIT ? ")
        if Vars:
            Cond = getExpr(Vars[0],Adb)
            info('EXITTTT %s'%str(Cond))
            return ['exit']
            
        Vars =  matches(Statements,"WHEN ? => ? ")
        if Vars:
            Cond = getExpr(Vars[0],Adb)
            if Cond[0]=='|': Cond=[Cond[1],Cond[2]]
            Seq = travelProcess(Adb[Vars[1]],Adb)
            return [[Cond,Seq]]

        Vars =  matches(Statements,"WAIT ?")
        if Vars:
            Cond = getExpr(Vars[0],Adb)
            return [['wait',Cond]]
                
            
    logs.log_error('travelProcess %s'%str(Statements))
    traceback.print_stack()
    return [['err']]


def reworkIf(IF):
    if len(IF)==3: return IF
    info('len=%d IF=%s'%(len(IF),IF))
    if len(IF)==5:
        IFF = ['ifelse',IF[1],IF[2]]
        AA = flattenIFELSE(IF[3])
        BB = IF[4]
        ALL = AA+[BB]
        info('ALL %s'%(str(ALL)))
        Ok=True
        while (len(ALL)>1)and Ok:
            Last= ALL[-1]
            Bef = ALL[-2]
            if (Last[0]=='else')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last[1]]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='ifelse')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            else:
                info('bad last0=%s bef0=%s ALL=%s last=%s bef=%s'%(Last[0],Bef[0],str(ALL),Last,Bef))
                Ok=False
            
        info('new ALL %s'%str(ALL))
        IFF.append(ALL)
        return IFF


    if len(IF)==4:
        IFF = ['ifelse',IF[1],IF[2]]
        AA = flattenIFELSE(IF[3])
        ALL = AA
        if ALL[0]=='elsif':
            ALL[0]='if'
            return ALL
        if ALL[0]=='else':
            return ALL[1]
        info('ALL4 %s'%(str(ALL)))
        Ok=True
        while (len(ALL)>1)and Ok:
            Last= ALL[-1]
            Bef = ALL[-2]
            if (Last[0]=='else')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last[1]]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='ifelse')and(Bef[0]=='elsif'):
                New = ['ifelse',Bef[1],Bef[2],Last]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
                info('newll %s'%str(ALL))
            elif (Last[0]=='elsif')and(Bef[0]=='elsif'):
                NewLast = ['if',Last[1],Last[2]]
                New = ['ifelse',Bef[1],Bef[2],NewLast]
                info('new %s'%str(New))
                ALL.pop(-1)
                ALL.pop(-1)
                ALL.append(New)
            else:
                info('bad4 %s %s %s %s %s'%(Last[0],Bef[0],str(ALL),Last,Bef))
                Ok=False
            
        info('new ALL4 %s'%str(ALL))
        IFF.append(ALL)
        return IFF


    logs.log_error('reworkIf got strange %d "%s"'%(len(IF),IF))
    return IF

def flattenIFELSE(LL):
    if LL[0]=='elsif': return [LL]
    if LL[0]=='else': return LL
    if (len(LL)==2)and(LL[0][0]=='elsif'):
        Seq = LL[1]
        if len(Seq)==2:
            Fseq = flattenIFELSE(Seq)
            return [LL[0]]+Fseq
        elif Seq[0]=='elsif':
            return LL
    logs.log_error('flattenIFELSE got "%s"'%(LL))
    return LL
        
    
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

def matches(List,Seq):
    Lseq = string.split(Seq)
    if len(List)!=len(Lseq): return False
    Vars=[]
    for ind,Iseq in enumerate(Lseq):
        if Iseq == '?':
            Vars.append(List[ind])
        elif Iseq[0] == '!':
            Look = Iseq[1:]
            if (Look != List[ind][0]): return False
            Vars.append(List[ind])
        elif (Iseq!=List[ind][0]):
            return False
    if Vars==[]: return True
    return Vars
        


def lowerize(List):
    if type(List)==types.StringType: return string.lower(List)
    if type(List)==types.IntType: return List

    if type(List) in [types.TupleType,types.ListType]:
        res = []
        for Item in List:
            New = lowerize(Item)
            res.append(New)
        return res
    logs.log_error('lowerize got %s %s'%(type(List),List))
    return List
            


def definition_type0(Vars,Adb):
    info('definition_type0 %s'%(str(Vars)))


def level1up(List,Adb):
    Res = []
    for Item in List:
        if (type(Item)==types.TupleType)and(Item in Adb):
            LL = Adb[Item]
            Res.extend(LL)
        else:
            Res.append(Item)
    return Res

def devnull(List,Adb): return

def case_statement(Vars,Adb):
    info('case_statement %s'%str(Vars))




def if_statement(Vars,Adb):
    info('if_statetment %s'%str(Vars))
    if '?Key7' in Vars:
        Yes  = Vars['?Key7']
        mod.addSeq(('else'))
        mod.pushIt()
        travelArch(Yes,Adb,'process_statements',True)
        mod.popIt()
        return

    if '?Key5' in Vars:
        Cond = getExpr(Vars['?Key5'],Adb)
        Yes  = Vars['?Key6']
        mod.addSeq(('elsif',Cond))
        travelArch(Yes,Adb,'process_statements',True)
        mod.popIt()
        return

    if '?Key3' in Vars:
        Cond = getExpr(Vars['?Key3'],Adb)
        Yes  = Vars['?Key4']
        mod.addSeq(('if',Cond))
        mod.pushIt()
        info('key3 %s'%str(Adb[Yes]))
        travelArch(Yes,Adb,'process_statements',True)
        mod.popIt()
        return

    Cond = getExpr(Vars['?Key0'],Adb)
    Yes  = Vars['?Key1']
    No   = Vars['?Key2']
    mod.addSeq(('if',Cond))
    mod.pushIt()
    travelArch(Yes,Adb,'process_statements',True)
    mod.popIt()
    mod.addSeq(('else'))
    mod.pushIt()
    travelArch(No,Adb,'process_statements',True)
    mod.popIt()

PATTERNS = {}
PATTERNS['scanstuff','LIBRARY ?aa']='devnull'
PATTERNS['scanstuff','USE ?aa']='devnull'
PATTERNS['scanstuff','ARCHITECTURE ? OF ?module IS ?Key1 BEGIN_  ?Key2 END ?']='architecture'
PATTERNS['scanstuff','ARCHITECTURE ? OF ?module IS BEGIN_  ?Key2 END ?']='architecture'
PATTERNS['scanstuff','ENTITY ?module IS ?Key1 END ?']='entity0'
PATTERNS['scanstuff','ENTITY ?module IS ?Key1 ?Key2 END ?']='entity0'
PATTERNS['externals','PORT LeftParen ?Key1 RightParen']='externals'
PATTERNS['generic','GENERIC LeftParen ?Key1 RightParen']='generic0'
PATTERNS['generic0','?name Colon ?Key1']='generic00'

PATTERNS['externals0','?name Colon ?dir  std_logic']='external_wire'
PATTERNS['externals0','?name Colon ?dir  std_logic_vector LeftParen ?Key1 RightParen']='external_bus0'
PATTERNS['externals0','?name Colon ?dir  std_logic_vector ?Key1']='external_bus1'

PATTERNS['component0','?name Colon ?dir  std_logic']='component_wire'
PATTERNS['component0','?name Colon ?dir  std_logic_vector LeftParen ?Key1 RightParen']='component_bus0'
PATTERNS['component0','?name Colon ?dir  std_logic_vector ?Key1']='component_bus1'

PATTERNS[3,'LeftParen ?Key1 RightParen']='constraint0'
PATTERNS[3,'LeftParen ?from ?dir ?to RightParen']='constraint0'
PATTERNS[3,'RANGE  ?from TO ?to']='range0'
PATTERNS[4,'?from ?downto ?to']='constraint1'

PATTERNS['block','Constant ?name Colon ?kind ?Key0 := ?const']='constant0'
PATTERNS['block','Constant ?name Colon ?kind  := ?Key1']='constant0'
PATTERNS['block','SIGNAL ?name Colon ?Key0']='signal0'
PATTERNS['block','SIGNAL ?name Colon ?Key1 ?Key2']='signal0'
PATTERNS['block','SIGNAL ?name ?Key3 Colon ?Key1 ?Key2']='signal0'
PATTERNS['block','SIGNAL ?name ?Key3 Colon ?Key1']='signal0'
PATTERNS['ports','SIGNAL ?name Colon ?Key0']='signal0'
PATTERNS['ports','SIGNAL ?name Colon ?Key1 ?Key2']='signal0'

PATTERNS['block','TYPE ?name IS ARRAY ?Key1 OF ?Key2']='type0'
PATTERNS['block','TYPE ?name IS LeftParen ?kind ?Key0 RightParen']='type0'
PATTERNS['ports','COMPONENT ?name ?Key0 ?Key1 END COMPONENT ']='definition_type0'
PATTERNS['block','COMPONENT ?name GENERIC LeftParen ?Key1 RightParen PORT LeftParen  ?Key2 RightParen END COMPONENT']='component0'
PATTERNS['block','COMPONENT ?name PORT LeftParen  ?Key2 RightParen END COMPONENT']='component0'
PATTERNS['architecture','PROCESS ?Key1 BEGIN_ ?Key2  END PROCESS']='process0'
PATTERNS['architecture','GENERIC MAP LeftParen ?Key1 RightParen']='genericmap0'
PATTERNS['architecture','?label Colon']='label0'

PATTERNS['concurrent_statement','?inst Colon ?type  GENERIC MAP LeftParen ?Key0 RightParen PORT MAP LeftParen ?Key1 RightParen'] = 'instance0'
PATTERNS['concurrent_statement','?inst Colon ?type  PORT MAP LeftParen ?Key1 RightParen'] = 'instance0'
PATTERNS['concurrent_statement','?gene Colon ?what  GENERATE ?Key1 END GENERATE ?'] = 'generate0'
PATTERNS['concurrent_statement','?name Colon PROCESS ?Key1 ?Key3 BEGIN_ ?Key2 END PROCESS'] = 'process0'
PATTERNS['concurrent_statement','?name Colon PROCESS ?Key1 ?Key3 BEGIN_ ?Key2 END PROCESS ?'] = 'process0'
PATTERNS['concurrent_statement','?name Colon PROCESS ?Key1 BEGIN_ ?Key2 END PROCESS'] = 'process0'
PATTERNS['concurrent_statement','?name Colon PROCESS ?Key1 BEGIN_ ?Key2 END PROCESS ?'] = 'process0'


PATTERNS['expression','?dst  LeftParen ?Key0 RightParen'] = 'expression0'
PATTERNS['expression','RANGE  ?Key1 TO ?Key2'] = 'expression0'
PATTERNS["expression","?Key3 WHEN ?Key4 ELSE ?Key5"] = "expression0"
PATTERNS["expression","OTHERS => ?Key6"] = "expression0"
PATTERNS["expression","?Key3 WHEN ?Key4 ELSE ?Key5 ?Key7 ?Key8"] = "expression0"




PATTERNS["process_statements","IF ?Key0 THEN ?Key1 ?Key2 END IF"] = "if_statement"
PATTERNS["process_statements","IF ?Key3 THEN ?Key4 END IF"] = "if_statement"
PATTERNS["process_statements","ELSIF ?Key5 THEN ?Key6"] = "if_statement"
PATTERNS["process_statements","ELSE ?Key7"] = "if_statement"
PATTERNS["process_statements","CASE ?Key0 IS  ?Key1 ?Key2 END CASE"] = "case_statement"



def matchit(Exp,L0,Adb,Where='nc'):
    for Act,Pattern in PATTERNS.keys():
        if Act==Exp:
            Wrds = string.split(Pattern)
            Vars = try_match(Wrds,L0,[])
            if Vars: 
                Proc = PATTERNS[Exp,Pattern]
#                info('matched %s to %s %s'%(Proc,Act,L0))
                try:
                    Func = globals()[Proc]
                    return Func(Vars,Adb)
                except:
                    traceback.print_exc()
                    traceback.print_stack()
                    logs.log_error('function %s failed at %s'%(Proc,Where))
                    return 'err','err'
    logs.log_error('matchit failed in exp=%s l0=%s at %s'%(Exp,L0,Where))
    traceback.print_stack()
    tryMakeProto(Exp,L0)
    return 'err','err'

def tryMakeProto(Exp,L0):
#    info('tryMakeProto %s'%str(L0))
    Res = []
    kk=0 
    jj=0 
    for Item in L0:
        if len(Item)==4:
            if Item[1] in ['identifier', 'literal']:
                Res.append('?tok%d'%kk)
            elif (Item[0]==Item[1])or(Item[0][0] not in string.letters):
                Res.append(Item[0])
            else:
                Res.append('?tok%d'%kk)
            kk += 1
        elif len(Item)==2:
            Res.append('?Key%d'%jj)
            jj += 1
    Str = string.join(Res,' ')
    info('PATTERNS["%s","%s"] = "aaaaa"'%(Exp,Str))

def try_match(Wrds,List,Vars):
    if (Wrds==[])and(List==[]): return listToDir(Vars)
    if (List==[])or(Wrds==[]): 
#        info('>><< false list=%s wrds=%s'%(List,Wrds))
        return False
    if Wrds[0]==List[0][0]:
        return try_match(Wrds[1:],List[1:],Vars)
    if Wrds[0]=='?':
        return try_match(Wrds[1:],List[1:],Vars)
    if Wrds[0][0]=='?':
        L0 = List[0]
        if (Wrds[0][1] in string.uppercase)or(len(L0)==2):
            return try_match(Wrds[1:],List[1:],Vars+[(Wrds[0],List[0])])
        else:
            
            return try_match(Wrds[1:],List[1:],Vars+[(Wrds[0],List[0][0])])
#    info('>><< false nothing list=%s wrds=%s'%(List,Wrds))
    return False



def listToDir(Vars):
    Res={}
    for A,B in Vars:
        Res[A] = B
    return Res







def mergeLists(Adb):
    Mrg0 = {}
    Mrg1 = {}
    for Key in Adb:
        List = Adb[Key]
        if (len(List)==2)and(List[0] in Adb)and(List[1] in Adb):
            if (Key[0]==List[0][0]):
                List0 = getList0(List[0],List[0][0],Adb)
                Mrg0[Key] = List0
            elif (Key[0]==List[1][0]):
                List1 = getList1(List[1],List[1][0],Adb)
                Mrg1[Key] = List1

#    for Key in Mrg0:
#        info('mrg0 key=%s val=%s'%(Key,Mrg0[Key]))
#    for Key in Mrg1:
#        info('mrg1 key=%s val=%s'%(Key,Mrg1[Key]))

    for Key in Adb:
        if (Key not in Mrg0)and(Key not in Mrg1):
            List = Adb[Key]
            dones=0
            Res = []
            for Item in List:
                if Item in Mrg0:
                    Res.extend(Mrg0[Item])
                    dones += 1
                elif Item in Mrg1:
                    Res.extend(Mrg1[Item])
                    dones += 1
                else:
                    Res.append(Item)
            if dones:
                Adb[Key]=Res

#    for Key in Mrg0:
#        Adb.pop(Key)
#    for Key in Mrg1:
#        Adb.pop(Key)


def getList0(Key,Who,Adb):
    L0 = Adb[Key]
    if (L0[0][0] == Who)and(L0[0] in Adb):
        More = getList0(L0[0],Who,Adb)
        if len(L0)==2:
            return [L0[1]]+More
        else:
            return More
    return [Key]
        
def getList1(Key,Who,Adb):
    L0 = Adb[Key]
    if (len(L0)==2)and(L0[1][0] == Who)and(L0[1] in Adb):
        More = getList1(L0[1],Who,Adb)
        return More+[L0[1]]
    return [Key]
        

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
        


def removes0(Adb):
    for Key in Adb:
        List = Adb[Key]
        if (len(List[-1])==4):
            if List[-1][0]=='Semicolon':
                Adb[Key] = List[:-1]

def rounds0(Adb):
    while True:
        Bef = len(Adb.keys())
        oneRound0(Adb)
        Aft = len(Adb.keys())
#        info('bef=%d aft=%d'%(Bef,Aft))
        if Aft==Bef: return

    
def oneRound0(Adb):
    F0,F4 = findEnds(Adb)
#    info('f0 %d   f4 %d all %d'%(len(F0),len(F4.keys()),len(Adb.keys())))
    useF0_F4(Adb,F0,F4)
#    info('f0 %d   f4 %d all %d'%(len(F0),len(F4.keys()),len(Adb.keys())))
    return Adb

    return

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
#                info('key=%s bef=%s val=%s'%(Key,Bef,Val))
    for Bef in Del:
        Adb.pop(Bef)
        


def reportLinks(Adb):
    Root = ('design_file',1)
    scanDeep(Root,Adb,[])

def scanDeep(Root,Adb,Bef):
    if Root in Adb:
        List = Adb[Root]
        for Item in List:
            if (len(Item)==2)and(Item in Adb):
                scanDeep(Item,Adb,Bef+[Item])
            elif (len(Item)==4)and(Item[0] not in Adb):
                logs.log_info('>>>>> %s   %s'%(str(Bef),Item))
                

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


def makeVerilog():
    makeVerilogEntities()
    makeVerilogArchs()


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

def makeVerilogArchs():
    for Module in ARCHITECTURES:
        L1,L2 = ARCHITECTURES[Module]
        treatSignals(L1,Module)
        treatBody(L2,Module)

def treatBody(L2,Module):
    for Item in L2:
        if len(Item)==1: Item=Item[0]

        if Item[0]=='assign':
            mod.addHardAssign(Item[1],Item[2])
        elif Item[0]=='instance':
            Inst = Item[1]
            Type = Item[2]
            Gens = Item[3]
            Ports = Item[4]
            if len(Gens)==1: Gens=Gens[0]
            if len(Ports)==1: Ports=Ports[0]
            if Gens[0]=='generic_map': Gens = Gens[1]
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



        else:
            logs.log_error('treatBody failed on "%s"'%(str(Item)))



def treatSignals(L1,Module):
    for Item in L1:
        if len(Item)==1: Item=Item[0]
        if Item[0]=='signal':
            Net = string.lower(Item[1])
            Wid = Item[2]
            if (Wid[0]=='std_logic')or(Wid=='std_logic'):
                mod.addWire(Net,'wire',0)
            elif Wid[0]=='integer':
                mod.addWire(Net,'wire',(31,0))
            elif Wid[0]=='std_logic_vector':
                mod.addWire(Net,'wire',Wid[1])
            else:
                logs.log_error('adding signal failed %s %s '%(Net,Wid))
        else:
            logs.log_error('adding signal failed "%s" '%(str(Item)))



main()

