
import types
import logs
from extract_expr_nets import extract_sigs
import traceback




def scan_statements(Current,Root,functiontorun,Params,Stack):
    if type(Root)is list:
        if Root[0]=='list':
            for Item in Root[1:]:
                scan_statement(Current,functiontorun,Item,Params,Stack)
        else:
            scan_statement(Current,functiontorun,Root,Params,Stack)
    else:
        logs.log_err('scan_statements not list %s %s %s'%(type(Root),Root,Stack))
        print(traceback.print_stack())





def scan_statement(Current,functiontorun,Item,Params,Stack):
    if Item[0] == 'ifelse':
        scan_statements(Current,Item[2],functiontorun,Params,Stack+[('if',Item[1])])
        scan_statements(Current,Item[3],functiontorun,Params,Stack+[('else',Item[1])])
    elif Item[0] == 'if':
        functiontorun(Current,Item,Params,Stack)
        scan_statements(Current,Item[2],functiontorun,Params,Stack+[('if',Item[1])])
    elif Item[0] == 'named_begin':
        scan_statement(Current,functiontorun,Item[2],Params,Stack)
    elif Item[0] == 'list':
        for X in Item[1:]:
            scan_statements(Current,X,functiontorun,Params,Stack)
    elif Item[0] == 'while':
        functiontorun(Current,Item,Params,Stack)
        scan_statements(Current,Item[2],functiontorun,Params,Stack+[('while',Item[1])])
        functiontorun(Current,False,Params,Stack)
    elif Item[0] == 'for':
        functiontorun(Current,Item,Params,Stack)
        scan_statements(Current,Item[4],functiontorun,Params,Stack+[('for',Item[1])])
        functiontorun(Current,False,Params,Stack)
    elif Item[0] in ['case','casez','casex']:
        for NX in Item[2]:
            Case=NX[0]
            Stmnt=NX[1]
            scan_statements(Current,Stmnt,functiontorun,Params,Stack+[('case',Item[1]),('item',Case)])
    elif Item[0] in ['wait','when','#','$finish','force','release','disable']:
        functiontorun(Current,Item,Params,Stack)
    elif Item[0] == 'functioncall':
        functiontorun(Current,Item,Params,Stack)
    elif Item[0] in ['<=','=','emit']:
        functiontorun(Current,Item,Params,Stack)
    elif Item[0] == 'taskcall':
        Task = Item[1]
        if Task in Current.tasks:
            logs.log_info('going into task %s'%Task)
            Code = Current.tasks[Task]
            scan_statements(Current,Code[0],functiontorun,Params,Stack)
        else:
            logs.log_err('scan_statement: task %s not in tasks %s %s'%(Task,Params,Stack))
    elif Item[0] == 'empty_begin_end':
        pass
    else:
        logs.log_err('scan_statement: %s %s stack=%s'%(Item,Params,Stack))
  


def is_edged_timing(List):
    if not List:
        return False
    if type(List)is str:
        return False
    if type(List)is tuple:
        if List[0]=='*':
            return False
        if List[1]=='token':
            return False
    if List=='*':
        return False
    if List[0]=='edge':
        return True
    if List[0]=='list':
        edges=0
        nonedges=0
        for Item in List[1:]:
            if Item[1] in ['posedge','negedge']:
                edges +=1 
            else:
                nonedges +=1
        if (edges>0)and(nonedges>0):
            logs.log_error('scan_rtl: is_edged_timing got edges and nonedges  %s'%str(List))

        return (edges>0)
    logs.log_error('scan_rtl: is_edged_timing got %s'%str(List))
    return False

def get_sensitivity_list(Current,Item):
    global SenseAlwaysList
    SenseAlwaysList={}
    scan_statement(Current,get_senses,Item,[[]],[])
    return SenseAlwaysList.keys()

def get_senses(Current,Item,Params,Stack):
    if Item[0] in ['=','<=']:
        Srcs= extract_sigs(Item[2])
        for X in Srcs:
            SenseAlwaysList[X]=1
    elif Item[0] in ['if','ifelse']:
        Srcs= extract_sigs(Item[1])
        for X in Srcs:
            SenseAlwaysList[X]=1
    else: 
        logs.log_error('get_senses got %s'%str(Item))


def compute1(Item,Mod):
    if type(Item)is int:
        return Item
    if type(Item)is str:
        if Item in Mod.parameters:
            return compute1(Mod.parameters[Item],Mod)
        if Item in Mod.localparams:
            return compute1(Mod.localparams[Item],Mod)

        if Item=='': return 1
        try:
            return int(Item)
        except:
            logs.log_warning('compute1 %s failed string'%(str(Item)))
            return 0
    if type(Item)is list:
        if Item[0] in ['-','+','*','/']:
            A = compute1(Item[1],Mod)
            B = compute1(Item[2],Mod)
            Str = '%s%s%s'%(A,Item[0],B)
            try:
                return eval(Str)
            except:
                logs.log_warning('compute1 %s failed list'%(str(Item)))
                traceback.print_stack()
                return 0
    return 0

