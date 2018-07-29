#! /usr/bin/python

import os,sys,string,pickle,types
import logs
import traceback
from module_class import module_class

def main():
    load_parsed('.')
    dump_all_verilog('all.v')

Modules = {}

def dump_all_verilog(Fname):
    Fout = open(Fname,'w')
    for Mod in Modules:
        print 'dumping %s'%Mod
        Modules[Mod].dump_verilog(Fout)
    Fout.close()

def load_parsed(Rundir):
    global Global,Modules
    Modules={}
    Global = module_class('global_module')
    try:
        load_db0('%s/db0.pickle'%Rundir)
        Key = 'Main',1
        scan1(Key)
        for Mod in Modules:
            Modules[Mod].check_interfaces()
        return Modules
    except:
        load_db0('db0.pickle')
        Key = 'Main',1
        scan1(Key)
        logs.log_fatal('reading file probably failed on syntax')
        return {}

     
            
def load_db0(Fname):
    global DataBase
    File = open(Fname)
    DataBase = pickle.load(File) 
    File.close()


def scan1(Key):
    global Stack,State,Current,Modules,ModuleStuffs
    Stack=[]            
    State='idle'
    Current=0
    ModuleStuffs=[]
    List = DataBase[Key]
    if (List==[]):
        return
    for Item in List:
        if len(Item)==2:
            if Item[0]=='Define':
                add_define(Item)
            elif Item[0]=='Module':
                add_module(Item)
            elif Item[0]=='Package':
                add_package(Item)
            elif Item[0]=='Interface':
                add_interface(Item)
            else:
                scan1(Item)
        else:
            logs.log_err('exxx %s %s'%(Key,Item))
                
def add_interface(Key):
    global Current
    List = DataBase[Key]
    if len(List)==6:
        Name = List[1][0]
        Current = module_class(Name,'interface')
        Modules[Name]=Current
        XX = DataBase[List[2]]
        if XX[0][0]!=';':
            add_module_header(DataBase[List[2]])
        List2=DataBase[List[3]]
        add_interface_stuffs(List2)
        return

    logs.log_err('add_interface %s %d %s'%(Key,len(List),List))

def add_package(Key):
    global Current
    List = DataBase[Key]
    if len(List)==7:
        Name = List[1][0]
        Current = module_class(Name,'package')
        Modules[Name]=Current
        Stuffs = DataBase[List[3]]
        add_package_item(DataBase[Stuffs[0]])
        add_package_items(DataBase[Stuffs[1]])
    else:
        logs.log_err('add_package %s %d %s'%(Key,len(List),List))

def add_package_item(List):
    if (len(List)==1):
        Key = List[0]
        List2 = DataBase[Key]
        if List2[0][0]=='parameter':
            add_parameter(List2[1])
        elif List2[0][0]=='typedef':
            add_typedef(List2)
#        print 'add_package_item',Key,List2

def add_interface_stuffs(Stuffs):
    if len(Stuffs)==0:
        return
    elif len(Stuffs)==2:
        add_interface_stuff(DataBase[Stuffs[0]])
        add_interface_stuffs(DataBase[Stuffs[1]])
    elif len(Stuffs)==1:
        add_interface_stuff(DataBase[Stuffs[0]])
    else:
        logs.log_err('add_interface_stuffs %d %s'%(len(Stuffs),Stuffs))


def add_interface_stuff(List):
    if List[0][0]=='Import':
        return
    if (len(List)==1)and(List[0][0]=='Parameter'):
        List2 = DataBase[List[0]]
        add_parameter(List2[-2])
        return
    if (len(List)==4)and(List[0][0]=='logic'):
        Wid= get_wid(List[1])
        Name = List[2][0]
        Current.add_sig(Name,'logic',Wid)
        return
    if (len(List)==3)and(List[0][0]=='logic'):
        Name = List[1][0]
        Current.add_sig(Name,'logic',0)
        return
    if (len(List)==6)and(List[0][0]=='modport'):
        Name = List[1][0]
        More = gather_module_items(DataBase[List[3]])
        print 'modport',Name,More
        Current.add_modport(Name,More)
        return

    logs.log_err('add_interface_stuff %d %s'%(len(List),List))



def gather_module_items(Stuffs):
    if len(Stuffs)==3:
        More = gather_module_items(DataBase[Stuffs[0]])
        Item = gather_module_item(DataBase[Stuffs[2]])
        return More+[Item]
    elif len(Stuffs)==1:
        Item = gather_module_item(DataBase[Stuffs[0]])
        return [Item]
    else:
        logs.log_err('gather_module_items %d %s'%(len(Stuffs),Stuffs))
        return []

def gather_module_item(List):
    if (len(List)==2)and(List[0][0]=='ExtDir'):
        Name = List[1][0]
        Dir = get_dir(List[0])
        return (Dir,Name)
        
    if len(List)==1:
        return List[0][0]
    print 'gather_module_item',List
    return []


def add_package_items(Stuffs):
    if len(Stuffs)==2:
        add_package_item(DataBase[Stuffs[0]])
        add_package_items(DataBase[Stuffs[1]])
    elif len(Stuffs)==1:
        add_package_item(DataBase[Stuffs[0]])
    else:
        logs.log_err('add_package_items %d %s'%(len(Stuffs),Stuffs))

def add_typedef(List):
    if len(List)==9:
        if (List[1][0]=='enum')and(List[2][0]=='logic'):
            Name = List[-2][0]
            Wid = get_wid(List[3])
            Singles = get_singles(DataBase[List[5]])
            Current.add_enum(Name,('width_singles',Wid,Singles))
            return
    if len(List)==8:
        Name = List[-2][0]
        if List[1][0]=='struct':
            Key = List[4]
            List2 = DataBase[Key]
            Things = add_typedef_items(List2)
            Current.add_typedef(Name,Things)
            return
        if (List[1][0]=='enum')and(List[2][0]=='logic'):
            Name = List[-2][0]
            Singles = get_singles(DataBase[List[4]])
            Current.add_enum(Name,('singles',Singles))
            return
    if len(List)==7:
        if List[1][0]=='enum':
            Name = List[-2][0]
            Pairs = get_pairs(DataBase[List[3]])
            Current.add_enum(Name,Pairs)
            return
            
    logs.log_err('add_typedef %d %s'%(len(List),List))

def get_singles(List):
    if len(List)==3:
        if len(List[0])==2:
            More = get_singles(DataBase[List[0]])
            Single = List[2][0]
            return More+[Single]
        if len(List[2])==2:
            More = get_singles(DataBase[List[2]])
            Single = List[0][0]
            return [Single]+More

    if len(List)==1:
        return [List[0][0]]
    logs.log_err('get_single %d %s'%(len(List),List))
    return []

def get_single(List):
    return List[0]

def get_pairs(List):
    if len(List)==3:
        More = get_pairs(DataBase[List[0]])
        Pair = get_pair(DataBase[List[2]])
        return More+[Pair]
    if len(List)==1:
        Pair = get_pair(DataBase[List[0]])
        return [Pair]
    logs.log_err('get_pairs %d %s'%(len(List),List))
    return []

def get_pair(List):
    if len(List)==3:
        Name = List[0][0]
        Expr = get_expr(List[2])
        return (Name,Expr)
    logs.log_err('get_pair %d %s'%(len(List),List))
    return []


def add_typedef_items(Stuffs):
    if len(Stuffs)==2:
        Item = add_typedef_item(DataBase[Stuffs[1]])
        More = add_typedef_items(DataBase[Stuffs[0]])
        return More+[Item]
    elif len(Stuffs)==1:
        Item = add_typedef_item(DataBase[Stuffs[0]])
        return [Item]
    else:
        logs.log_err('add_typedef_items %d %s'%(len(Stuffs),Stuffs))
        return []

def add_typedef_item(List):
    if len(List)==3:
        if List[0][0]=='logic':
            return ('logic',List[1][0])
        if List[0][1]=='token':
            return (List[0][0],List[1][0])

    elif len(List)==4:
        if List[0][0]=='logic':
            Wid = get_wid(List[1])
            return ('logic',Wid,List[2][0])
    elif len(List)==5:
        if List[0][0]=='logic':
            Wid1 = get_wid(List[1])
            Wid2 = get_wid(List[2])
            return ('logic',Wid1,Wid2,List[3][0])

    logs.log_err('add_typedef_item %d %s'%(len(List),List))
    return False

def add_module(Key):
    global Current,ModuleStuffs
    List = DataBase[Key]
    Module = List[1][0]
    Current = module_class(Module,'module')
    Modules[Module]=Current
    print 'addmodule %s (%s)'%(Module,Modules.keys()),List[-2]
    if List[-1][0]=='Ending':
        List = List[:-1]
    if len(List)==5:
        Lhead = DataBase[List[2]]
        Lbody = DataBase[List[3]]
        Lparams=[]
    elif len(List)==6:
        Lparams = DataBase[List[2]]
        Lhead = DataBase[List[3]]
        Lbody = DataBase[List[4]]
    else:
       logs.log_err('dont know to deal with %s'%List)
       return
    if (len(Lparams)>0):
         add_module_params(Lparams)
    if (len(Lhead)>1):
         add_module_header(Lhead)
    if (len(Lbody)>0):
        ModuleStuffs = [Lbody]
        while (ModuleStuffs!=[]):
            add_module_stuff()

def add_generate_item(List):
    if len(List)==3:
        Statement = get_statements(List[1])
        Current.add_generate(Statement)
        

def add_define_item(List):
    Tok = List[0][1]
    if Tok=='backtick_include':
        Expr = get_expr(List[1])
        if Current:
            Current.add_include(Expr)
        else:
            logs.log_err('dont know to deal with %s'%List)
        return
    elif Tok=='backtick_undef':
        return
    logs.log_err('dont know to deal with %s'%List)

def add_define(Key):
    List = DataBase[Key]
    Tok = List[1][0]
    if len(List)>2:
        Expr = get_expr(List[2])
    else:
        Expr = 1
    if Current:
        Current.add_define(Tok,Expr)
    else:
        Global.add_define(Tok,Expr)

def add_module_params(List1):
    for Item in List1:
        if len(Item)==2:
            if (Item[0]=='head_params'):
                add_module_params(DataBase[Item])
            elif (Item[0]=='head_param'):
                LL = DataBase[Item]
                if (len(LL)==4)and(LL[0][0]=='parameter'):
                    Who = LL[1][0]
                    Expr = get_expr(LL[3])
                    Current.add_parameter(Who,Expr)
                elif (len(LL)==3)and(LL[1][0]=='='):
                    Who = LL[0][0]
                    Expr = get_expr(LL[2])
                    Current.add_parameter(Who,Expr)
                else:
                    logs.log_err('add_module_paran got %d %s'%(len(LL),LL))
                


def add_module_header(List1):
    if len(List1)==1:
        add_header_item(DataBase[List1[0]])
        return
    if len(List1)==3:
        if (List1[0][0]=='(')and(List1[1][0]==')'):
            return
        add_module_header(DataBase[List1[0]])
        add_header_item(DataBase[List1[2]])
        return        
    if (len(List1)==4)and(List1[1][0]=='Header_list'):
        add_module_header(DataBase[List1[1]])
        return        
    logs.log_err('add_module_header got-b %d %s'%(len(List1),List1))
                

LastWidDir=False
def add_header_item(List1):
    global LastWidDir
    if (len(List1)==1):
        Name = List1[0][0]        
        if LastWidDir:
            Current.add_sig(Name,LastWidDir[0],LastWidDir[1])
        return

    if (len(List1)==2)and(List1[0][1]=='token')and(List1[1][1]=='token'):
# we look at interface
        Current.add_interface(List1[0][0],List1[1][0],'ext')
        return

    Name = List1[-1][0]
    Dir = get_dir(List1[0])
    if (len(List1)==3):
        Wid = get_wid(List1[1])
    elif (len(List1)==2):
        Wid = 0
    elif (len(List1)==4):
        Wid0 = get_wid(List1[1])
        Wid1 = get_wid(List1[3])
        Wid = ('double',Wid0,Wid1)
        Name = List1[2][0]
    else:
        logs.log_err('get_dd_header %s'%str(List1))
    if Dir in ['input','output','inout','output reg']:
        LastWidDir=(Dir,Wid)
    Current.add_sig(Name,Dir,Wid)

def get_when(Item):
    List = DataBase[Item]
    if len(List)==4:
        return get_when_items(List[2])
    elif (len(List)==2)and(List[0][0]=='@'):
        Ok = List[1]
        if len(Ok)==1:
            return [Ok]
        if (len(Ok)==4)and(Ok[1]=='token'):
            return [Ok[0]]
        if (len(Ok)==4)and(Ok[0]=='*'):
            return [Ok[0]]
        if (len(Ok)==4)and(Ok[0]=='(*)'):
            return ['*']
        logs.log_err('get_when got0 %s'%str(List))
        return []
    else:
        logs.log_err('get_when got1 %s'%str(List))
        return []
        
#    ensure(len(List)==4,(List,Item))

def get_when_items(Item1):
    List = DataBase[Item1]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='When_item'):
                LL = DataBase[Item]
                if len(LL)==2:
                    Edge = LL[0][0]
                    Expr = get_expr(LL[1])
                    res.append(['edge',Edge,Expr])
                elif len(LL)==1:
                    Expr = get_expr(LL[0])
                    res.append(Expr)
                else:
                    logs.log_err('get_when_items %s'%(LL))
            elif (Item[0]=='When_items'):
                more = get_when_items(Item)
                res.extend(more)
    return res
def get_exprs(Item1):
    List = DataBase[Item1]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='Exprs'):
                more = get_exprs(Item)
                res.extend(more)
            elif (Item[0]=='Expr'):
                more = get_expr(Item)
                res.append(more)
    return res

def get_soft_assigns(Item1):
    List = DataBase[Item1]
    res=['list']
    for Item in List:
        if Item[0]=='Soft_assigns':
            More = get_soft_assigns(Item)
            res.extend(More)
        elif Item[0]=='Soft_assign':
            List2 = DataBase[Item]
            if (len(List2)==3)and(List2[1][0]=='='):
                Dst = get_expr(List2[0])
                Src = get_expr(List2[2])
                res.append(['=',Dst,Src])
    return res


def get_statement(Item):
    List = DataBase[Item]
    if List[-1][0]=='Ending':
        List = List[:-1]
    if len(List)==1:
        if List[0][0]=='While_statement':
            List2 = DataBase[List[0]]
            Cond = get_expr(List2[2])
            Stmt = get_statement(List2[4])
            return ['while',Cond,Stmt]
        if List[0][0]=='For_statement':
            List2 = DataBase[List[0]]
            Assigns1 = get_soft_assigns(List2[2])
            Cond = get_expr(List2[4])
            Assigns2 = get_soft_assigns(List2[6])
            Stmt = get_statement(List2[8])
            return ['for',Assigns1,Cond,Assigns2,Stmt]
    if len(List)==2:
        if List[0][0]=='Dotted':
            Dotted = get_dotted_items(DataBase[List[0]])
            return ['dotted',Dotted]
        if List[0][0]=='When':
            When = get_when(List[0])
            if len(When)==1:
                When = When[0]
            return ['when',When]
        if List[0][0]=='$finish':
            return ['$finish']
        if List[0][1]=='token':
            return ['taskcall',List[0][0]]
        if (List[0][0]=='begin')and(List[1][0]=='end'):
            return ['empty_begin_end']
        


    if len(List)==3:
        if List[0][0]=='integer':
            return ['integer',List[1][0]]
        if List[0][0]=='genvar':
            return ['genvar',List[1][0]]
        if List[0][0]=='begin':
            LL =  get_statements(List[1])
            return ['list']+LL
        if List[0][0]=='fork':
            LL =  get_statements(List[1])
            return ['fork']+LL
        if List[0][0]=='#':
            Dly = get_expr(List[1])
            return ['#',Dly]
        if List[0][0]=='wait':
            Dly = get_expr(List[1])
            return ['wait',Dly]
        if List[0][1]=='emit':
            Eve = get_expr(List[1])
            return ['emit',Eve]
        if List[0][1]=='disable':
            Eve = get_expr(List[1])
            return ['disable',Eve]
        if List[0][1]=='release':
            Eve = get_expr(List[1])
            return ['release',Eve]
    if len(List)==4:
        if List[1][0]=='<=':
            Dst = get_expr(List[0])
            Src = get_expr(List[2])
            return ['<=',Dst,Src]
        if List[1][0]=='=':
            Dst = get_expr(List[0])
            Src = get_expr(List[2])
            return ['=',Dst,Src]
    if len(List)==5:
        if (List[0][0]=='force'):
             Dst = get_expr(List[1])
             Src = get_expr(List[3])
             return   ['force',Dst,Src]
        if (List[0][0]=='assign'):
             Dst = get_expr(List[1])
             Src = get_expr(List[3])
             return   ['assign',Dst,Src]

        if List[1][0]=='<=':
            Dst = get_expr(List[0])
            Dly = get_expr(List[2])
            Src = get_expr(List[3])
            return ['<=',Dst,Src,Dly]
        if List[0][0]=='begin':
            return ['named_begin',List[2][0],['list']+get_statements(List[3])]
        if (List[1][0]=='(')and(List[0][1]=='token'):
            exprs = get_exprs(List[2])
            return ['functioncall',List[0][0],exprs]
        if (List[0][0]=='if'):
            Cond = get_expr(List[2])
            Yes = get_statement(List[4])
            return ['if',Cond,Yes]
    if len(List)==6:
        if (List[0][0] in ['case','casez','casex']):
            Switch = get_expr(List[2])
            LLL = DataBase[List[4]]
            Cases  = get_cases(List[4])
            return [List[0][0],Switch,Cases]
    if len(List)==7:
        if (List[0][0]=='if')and(List[5][0]=='else'):
            Cond = get_expr(List[2])
            Yes = get_statement(List[4])
            No = get_statement(List[6])
            return ['ifelse',Cond,Yes,No]
        if (List[0][0] in ['case','casez','casex'] ):
            Switch = get_expr(List[2])
            Cases  = get_cases(List[4])
            Default  = get_default(List[5])
            Cases.append(['default',Default])

            return [List[0][0],Switch,Cases]

    logs.log_err(' db0: untreated statement %s %d "%s"'%(Item,len(List),List),True)
    return []

def get_default(Item):
    List = DataBase[Item]
    if List[2][0]==';':
        return ['empty_begin_end']
    return get_statement(List[2])

def get_cases(Item1):
    List = DataBase[Item1]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='Case'):
                List2 = DataBase[Item]
                if len(List2)==3:
                    Cond = get_exprs(List2[0])
                    if List2[2][0]!=';':
                        Statement = get_statement(List2[2])
                        res.append([Cond,Statement])
                else:
                    logs.log_err('case %s %s'%(Item,List2))
            elif (Item[0]=='Cases'):
                more = get_cases(Item)
                res.extend(more)
    return res

def get_statements(Item1):
    List = DataBase[Item1]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='Statement'):
                x = get_statement(Item)
                res.append(x)
            elif (Item[0]=='Statements'):
                more = get_statements(Item)
                res.extend(more)
    return res

def get_wid(Item):
    if len(Item)==2:
        List = DataBase[Item]
        if (len(List)==5):
            if List[2][0]==':':
                High = get_expr(List[1])
                Low = get_expr(List[3])
                return High,Low
            if List[2][1]=='plus_range':
                High = get_expr(List[1])
                Low = get_expr(List[3])
                return ['-',['+',High,Low],1],High
            if List[2][1]=='minus_range':
                High = get_expr(List[1])
                Low = get_expr(List[3])
                return High,['+',['-',High,Low],1]
        elif (len(List)==1):
            if List[0][0]=='integer':
                return 31,0
            if List[0][0]=='Width':
                return get_wid(List[0])
        elif len(List)==4:
            if (List[0][0]=='#')and(List[2][0]=='Prms_list'):
                LL = get_conns(List[2])
                return LL
        logs.log_err('get_wid got %s %s'%(len(List),List))
    elif len(Item)==1:
        if Item[0][0]=='integer':
            return 31,0
            
    logs.log_err('get_wid %s'%str(Item))
    return 0,0

def get_busbit(Item):
    if len(Item)==2:
        List = DataBase[Item]
        if (len(List)==3):
            Ind = get_expr(List[1])
            return Ind
    logs.log_err('get_busbit %s %s'%(Item,List))

def get_dir(Item):
    if len(Item)==2:
        List = DataBase[Item]
        res = []
        for Thing in List:
            res.append(Thing[0])
        res.sort()
        return string.join(res)
    if (type(Item)==types.TupleType) and (len(Item)==4):
        return Item[0]
        
    logs.log_err('get_dir %s'%str(Item))
    return Item

def add_module_stuff():
    List1 = ModuleStuffs.pop(0)
    if len(List1)==0:
        return
    for Item in List1:
        if len(Item)==2:
            if (Item[0]=='Mstuff'):
                add_module_item(DataBase[Item][0])
            elif (Item[0]=='Module_stuffs'):
                ModuleStuffs.append(DataBase[Item])

def add_module_item(Item):
    if len(Item)==2:
        List = DataBase[Item]
        if Item[0]=='Definition':
            add_definition(List)
        elif Item[0]=='Parameter':
            add_parameter(List[-2])
        elif Item[0]=='Localparam':
            add_localparam(List[1])
        elif Item[0]=='Assign':
            add_hard_assign(List)
        elif Item[0]=='Instance':
            add_instance(List)
        elif Item[0]=='Always':
            add_always(List)
        elif Item[0]=='Initial':
            add_initial(List)
        elif Item[0]=='Function':
            add_function(List)
        elif Item[0]=='Task':
            add_task(List)
        elif Item[0]=='Define':
            add_define_item(List)
        elif Item[0]=='Generate':
            add_generate_item(List)
        elif Item[0]=='Import':
            pass
        elif Item[0]=='Typedef':
            add_typedef(List)
        else:
            logs.log_err('untreated(0) "%s" "%s"'%(Item,List))
    elif (len(Item)==4)and(Item[1]=='pragma'):
        add_pragma(Item)
    elif (len(Item)==4)and(Item[1]=='newver'):
        add_newver(Item)
    else:
        logs.log_err('untreated(1) len=%d "%s"'%(len(Item),str(Item)))


def add_pragma(Item):
    Current.pragmas.append(Item)

def add_newver(Item):
    Current.newvers.append(Item)

def add_function(List):
    if istoken(List[1]):
        Func = List[1][0]
        Wid=0
        Next = 2
    elif iswidth(List[1]):
        Func = List[2][0]
        Wid = get_wid(List[1])
        Next = 3
    else:
        logs.log_err('untreated add_func %s'%(str(List)))
        return

    if List[Next][0]=='(':
        Header = get_header_list(List[Next+1])
        Next += 4
    else:
        Header=[]
        
    if List[Next][0]=='Mem_defs':
        Memdefs = get_mem_defs(List[Next])
    else:
        Memdefs = []
    Statement = get_statement(List[-2])
    Header.extend(Memdefs)
    Current.add_function(Func,Wid,Header,Statement)

def get_mem_defs(Ptr):
    List=DataBase[Ptr]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='Mem_defs'):
                more = get_mem_defs(Item)
                res.extend(more)
            if (Item[0]=='Mem_def'):
                List2 = DataBase[Item]
                Dir,Wid,Names = get_definition(List2)
                for Name in Names:
                    res.append([Name,Wid,Dir])
    return res        

def add_task(List):
    Task = List[1][0]
    if len(List)==5:
        Statement = get_statement(List[3])
        Current.add_task(Task,Statement)
        return
    if len(List)==6:
        Statement = get_statement(List[4])
        Defs = get_mem_defs(List[3])
        Current.add_task(Task,Statement,Defs)
        return
    if len(List)==9:
        Statement = get_statement(List[7])
        Defs = get_mem_defs(List[6])
        Header = get_header_list(List[3])
        Header.extend(Defs)
        Current.add_task(Task,Statement,Header)
        return
        
    logs.log_err('task not treated %s %s %s'%(Task,len(List),List))


def get_header_list(Item1):
    List = DataBase[Item1]
    res=[]
    for Item in List:
        if Item[0]=='Header_list':
            X = get_header_list(Item)
            res.extend(X)
        elif Item[0]=='Header_item':
            List2 = DataBase[Item]
            if (len(List2)==3)and(List2[0][0]=='ExtDir'):
                Dir = get_dir(List2[0])
                Wid = get_wid(List2[1])
                Name = List2[2][0]
                res.append([Name,Wid,Dir])
        elif Item[0][0]==',':
            pass
        else:
            logs.log_err('get_header_list %s'%List)
    return res


def add_always(List):
    if len(List)==3:
        When = get_when(List[1])
        Statement = get_statement(List[2])
        if len(When)>1:
            When = ['list']+When
        else:
            When = When[0]
        Current.add_always(Statement,When,List[0][0])
    elif len(List)==2:
        Statement = get_statement(List[1])
        Current.add_always(Statement,False,List[0][0])
    else:
        logs.log_err('bad always %s'%List)
def add_initial(List):
    Statement = get_statement(List[1])
    Current.add_initial(Statement)
    


def add_instance(List):
    Type = List[0][0]
    if (List[1][0]=='('):
        Inst = invent_inst(Type,Current)
        Current.add_inst(Type,Inst)
        if (len(List)==4)and(List[2][0]=='Exprs'):
            LL = get_exprs(List[2])
            for i in range(len(LL)):
                Sig = LL[i]
                Pin = 'pin%d'%i
                Current.add_conn(Inst,Pin,Sig)
            return
    if istoken(List[1]):
        Inst = List[1][0]
        Params=[]
    else:
        Inst = List[2][0]
        Params = get_inst_params(List[1])
    Current.add_inst(Type,Inst)
    for (Prm,Val) in Params:
        Current.add_inst_param(Inst,Prm,Val)
    if List[-3][0]=='Conns_list':
        Conns = get_conns(List[-3])
        for Pin,Sig in Conns:
            Current.add_conn(Inst,Pin,Sig)
        return
    if List[-3][0]=='Exprs':
        LL = get_exprs(List[-3])
        for i in range(len(LL)):
            Sig = LL[i]
            Pin = 'pin%d'%i
            Current.add_conn(Inst,Pin,Sig)
        return
    if (len(List)==3)and(List[1][0]=='Tokens_list'):
        Type = List[0][0]
        Singles = get_singles(DataBase[List[1]])
        for Inst in Singles:
            Current.add_inst(Type,Inst)
        return
    if (len(List)==4)and(List[2][0]=='Width'):
        Type = List[0][0]
        Inst = List[1][0]
        Wid = get_wid(List[2])
        Current.add_inst(Type,Inst)
        Current.add_inst_param(Inst,'width',['width']+list(Wid))

        return
    
    logs.log_err('add_instance len=%d list=%s'%(len(List),List))

Invents={}
def invent_inst(Base,Current):
    while 1:
        if Base not in Invents:
            Invents[Base]=0
        Indx = Invents[Base]
        Invents[Base] += 1
        Inst = '%s_%d'%(Base,Indx)
        if Inst not in Current.insts:
            return Inst
    

def add_hard_assign(List):
    if (len(List)==5):
        Dst = get_expr(List[1])
        Src = get_expr(List[3])
        Current.add_hard_assign(Dst,Src)
    elif (len(List)==6):
        Dst = get_expr(List[2])
        Src = get_expr(List[4])
        if List[1][0]=='AssignParams':
            Params = get_inst_params(List[1])
            Current.add_hard_assign(Dst,Src,'',Params)
        elif List[1][0]=='StrengthDef':
            Strength = get_strength(List[1])
            Current.add_hard_assign(Dst,Src,Strength,'')
        else:
            Current.add_hard_assign(Dst,Src)
            logs.log_err('add_hard_assign %d %s'%(len(List),List))
    elif (len(List)==7):
        Dst = get_expr(List[3])
        Src = get_expr(List[5])
        if List[1][0]=='AssignParams':
            Params = get_inst_params(List[1])
        elif List[2][0]=='AssignParams':
            Params = get_inst_params(List[2])
        else:
            Params=''

        if List[1][0]=='StrengthDef':
            Strength = get_strength(List[1])
        elif List[2][0]=='StrengthDef':
            Strength = get_strength(List[2])
        else:
            Strength=''
        Current.add_hard_assign(Dst,Src,Strength,Params)
    else:
        logs.log_err('add_hard_assign %d %s'%(len(List),List))

def get_strength(Item):
    List = DataBase[Item]
    if (len(List)==5)and(Item[0]=='StrengthDef'):
        One = get_strength(List[1])
        Two = get_strength(List[3])
        return One,Two
    if (len(List)==1)and(Item[0]=='Strength'):
        return List[0][0]

    logs.log_err('get_strength %s %s'%(Item,List))
    return []

def get_inst_params(Item):
    List = DataBase[Item]
    if (len(List)==2)and(List[0][0]=='#'):
        Dly = get_expr(List[1])
        return [['delay',Dly]]
    if (len(List)==4)and(List[2][0]=='Exprs'):
        LL = get_exprs(List[2])
        res=[]
        for i in range(len(LL)):
            res.append([i,LL[i]])
        return res
    if (len(List)==4)and(List[2][0]=='Prms_list'):
        LL = get_conns(List[2])
        return LL
    if Item[0]=='Tokens_list':
        return []

    logs.log_err('get_inst_params %d %s %s'%(len(List),Item,List))
    return []

def get_definition(List):
    if List[1][1]=='domino':
        return 'wire',0,List[3][0]
    Dir = get_dir(List[0])
    if len(List)>4:
        if List[-3][0]=='=':
            List1 = List[:-3]+[(';',';',0,0)]
            What = get_definition(List1)
            return What


    if len(List)==5:
        Wid = get_wid(List[1])
        Name = get_names(List[2])
        Wid2 = get_wid(List[3])
        return Dir,Wid,Name,Wid2
    if len(List)==4:
        Wid = get_wid(List[1])
        Names = get_names(List[2])
        return Dir,Wid,Names
    if len(List)==3:
        Wid=0
        Names = get_names(List[1])
        return Dir,Wid,Names
    logs.log_err('bad definition %d %s'%(len(List),List))
    return 0


def add_definition(List):
    Tuple = get_definition(List)
    if len(Tuple)==3:
        Dir,Wid,Names = Tuple
        for Name in Names:
            Current.add_sig(Name,Dir,Wid)
        if List[-3][0]=='=':
            Expr = get_expr(List[-2])
            Current.add_hard_assign(Names[0],Expr)
    elif len(Tuple)==4:
        Dir,Wid,Name,Wid2 = Tuple
        if Dir in ['wire','reg']:
            Current.add_mem(Name,Dir,Wid,Wid2)
        elif (type(Name)==types.ListType):
            for NN in Name:
                Current.add_sig(NN,Dir,('double',Wid,Wid2))
        else:
            Current.add_sig(Name,Dir,('double',Wid,Wid2))

def add_parameter(Ptr):
    List2 = DataBase[Ptr]
    for Item in List2:
        if len(Item)==2:    
            if (Item[0]=='Pair'):
                List = DataBase[Item]
                Name=List[0][0]
                Expr = get_expr(List[2])
                Current.add_parameter(Name,Expr)
            else:
                add_parameter(Item)
        else:
            logs.log_err('add_parameter ptr=%s item=%s'%(Ptr,Item))

def add_localparam(Ptr):
    List2 = DataBase[Ptr]
    for Item in List2:
        if len(Item)==2:    
            if (Item[0]=='Pair'):
                List = DataBase[Item]
                Name=List[0][0]
                Expr = get_expr(List[2])
                Current.add_localparam(Name,Expr)
            else:
                add_localparam(Item)


def get_conns(Ptr):
    List=DataBase[Ptr]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='Conns_list'):
                more = get_conns(Item)
                res.extend(more)
            elif (Item[0]=='Prms_list'):
                more = get_conns(Item)
                res.extend(more)
            elif (Item[0]=='Connection'):
                List2 = DataBase[Item]
                Pin = List2[1][0]
                if Pin=='*':
                    Sig=''
                elif List2[3][0]==')':
                    Sig=False    
                else:
                    Sig = get_expr(List2[3])
                res.append([Pin,Sig])
            elif (Item[0]=='PrmAssign'):
                List2 = DataBase[Item]
                if (len(List2)==5)and(List2[0][0]=='.'):
                    Param = List2[1][0]
                    Sig = get_expr(List2[3])
                    res.append((Param,Sig))
                else:
                    print 'strange get_conns %s'%str(List2)

            else:
                print 'strange get_conns %s'%str(Item)
        elif (type(Item)==types.TupleType)and(Item[0]==','):
            pass
        else:
            print 'strange2 get_conns %s'%str(Item)
    return res        

def get_names(Ptr):
    if (len(Ptr)==4)and(Ptr[1]=='token'):
        return Ptr[0]
    List = DataBase[Ptr]
    res = []
    More=[]
    while List!=[]:
        for Item in List:
            if len(Item)==2:
                if (Item[0]=='Tokens_list'):
                    More.extend(DataBase[Item])
    #                more = get_names(Item)
    #                res.extend(more)
            elif len(Item)==4:
                if Item[0]!=',':
                    res.append(Item[0])
        List=More[:]
        More=[]



    return res        


def get_expr(Item):
    if len(Item)==4:
        if Item[1]=='token':
            return Item[0]
        if Item[1]=='number':
            return int(Item[0])
        if Item[1]=='string':
            return Item[0]
    if (type(Item)==types.TupleType):
        if Item[0]=='*':
            return '*'
    if len(Item)==2:
        List = DataBase[Item]
        if len(List)==1:
            if List[0][1]=='floating':
                return float(List[0][0])

            if List[0][1]=='number':
                return int(List[0][0])
            if List[0][1]=='define':
                return ['define',List[0][0]]
            if List[0][1]=='token':
                return List[0][0]
            if List[0][1]=='string':
                return List[0][0]
            if List[0][1]=='ubin':    
                X = string.split(List[0][0],"'b")
                return ['bin',X[0],X[1]]
            if List[0][1]=='uhex':    
                X = string.split(List[0][0],"'h")
                return ['hex',X[0],X[1]]
            if List[0][1]=='udig':    
                X = string.split(List[0][0],"'d")
                return ['dig',X[0],X[1]]
            if List[0][1]=='bin':    
                X = string.replace(List[0][0],"'b",' ')
                X1 = string.split(X)
                return ['bin',X1[0],X1[1]]
            if List[0][1]=='dig':    
                X = string.replace(List[0][0],"'d",' ')
                X1 = string.split(X)
                return ['dig',X1[0],X1[1]]
            if List[0][1]=='hex':    
                X = string.replace(List[0][0],"'h",' ')
                X1 = string.split(X)
                return ['hex',X1[0],X1[1]]
            if List[0][0]=='CurlyList':    
                return curly_list(List[0])
            if List[0][0]=='Dotted':    
                List2 = DataBase[List[0]]
                Dotted = get_dotted_items(List2)
                return ('dotted',Dotted)

        elif len(List)==2:
            if List[0][0]=='#':
                Dly = get_expr(List[1])
                return ['#',Dly]
            if istoken(List[0])and(iswidth(List[1])):
                return ['subbus',List[0][0],get_wid(List[1])]
            if istoken(List[0])and(isbusbit(List[1])):
                return ['subbit',List[0][0],get_busbit(List[1])]
            if is_math_op(List[0])and isexpr(List[1]):
                return [List[0][0],get_expr(List[1])]
                
        elif len(List)==3:
            if List[1][0]=='CurlyItems':
                return get_curly_items(List[1])
                

            if isexpr(List[0])and isexpr(List[2]) and is_math_op(List[1]):
                Expr0 = get_expr(List[0])
                Expr1 = get_expr(List[2])
                Op = List[1][0]
                if Op in ['+','*','|','||','^','&&','||']:
                    RR = [Op]
                    if (type(Expr0)==types.TupleType)and(Expr0[0]==Op):
                        RR.extend(list(Expr0[1:]))
                    else:
                        RR.append(Expr0)
                    if (type(Expr1)==types.TupleType)and(Expr1[0]==Op):
                        RR.extend(list(Expr1[1:]))
                    else:
                        RR.append(Expr1)
                    return RR
                return [Op,Expr0,Expr1]
            if (List[0][0]=='(')and(List[2][0]==')'):
                return get_expr(List[1])
            if (List[0][1]=='token')and(List[1][0]=='BusBit')and(List[2][0]=='Width'):
                BB = get_busbit(List[1])
                BW = get_wid(List[2])
                return ['sub_slice',List[0][0],BB,BW]
            if (List[0][1]=='token')and(List[1][0]=='BusBit')and(List[2][0]=='BusBit'):
                BB = get_busbit(List[1])
                BW = get_busbit(List[2])
                return ['sub_slicebit',List[0][0],BB,BW]

        elif len(List)==4:
            if (List[1][0]=='(') and istoken(List[0]):
                exprs = get_exprs(List[2])
                return ['functioncall',List[0][0],exprs]
            elif (List[0][1]=='define'):
                Def = List[0][0]
                expr = get_expr(List[2])
                return ['define',Def,expr]
                
                
        elif len(List)==5:
            if List[1][0]=='?':
                return ['question',get_expr(List[0]),get_expr(List[2]),get_expr(List[4])]


        logs.log_err('bad get_expr %s %s %s'%(Item,len(List),List))
        return 0
    if len(Item)==4:
        if (Item[1]=='floating'):
            return float(Item[0])

    logs.log_err('very bad expr %s %d'%(str(Item),len(Item)))
    return 0

def get_dotted_items(List):
    if len(List)==3:
        if istoken(List[0]) and istoken(List[2]):
            return [List[0][0],List[2][0]]
        More = get_dotted_items(DataBase[List[2]])
        return [List[0]]+More
    elif len(List)==4:
        LL = [List[0][0]]
        if isbusbit(List[3]):
            LL.append(('subbit',List[2][0],get_busbit(List[3])))
            return LL
        if List[3][0]=='Width':
            Wid = get_wid(List[3])
            LL.append(('subbus',List[2][0],Wid))
            return LL

    elif len(List)==6:
        if istoken(List[0]) and istoken(List[2])and(isexpr(List[4])):
            return [List[0][0],('functioncall',List[2][0],get_expr(List[4]))]
        
            
    logs.log_err('dotted ilia! len=%d %s'%(len(List),List))

    return []

def curly_list(Item):
    List = DataBase[Item]
    Item1 = List[1]
    return ['curly']+get_curly_items(Item1)

def get_curly_items(Item1):
    List = DataBase[Item1]
    res = []
    for Item in List:
        if len(Item)==2:
            if (Item[0]=='CurlyItem'):
                LL = DataBase[Item]
                if len(LL)==4:
                    Rep = get_expr(LL[0])
                    What = get_expr(LL[2])
                    X=['repeat',Rep,What]
                elif(len(LL)==1):
                    X = get_expr(LL[0])
                elif len(LL)==2:
                    Rep = get_expr(LL[0])
                    What = get_expr(LL[1])
                    X=['repeat',Rep,What]
                else:
                    logs.log_err('curly got %s out of %s'%(Item,LL))
                    X='error'
                res.append(X)
            elif (Item[0]=='CurlyItems'):
                more = get_curly_items(Item)
                res.extend(more)
    return res


def istoken(X):
    return  (len(X)==4)and(X[1]=='token')
def isbusbit(X):
    return (len(X)==2)and(X[0]=='BusBit')
def iswidth(X):
    if (len(X)==2):
        if (X[0]=='Width'): return True
        if (X[0]=='WidthInt'): return True

    return False
def isexpr(X):
    return (len(X)==2)and(X[0]=='Expr')
def is_math_op(X):
    return (len(X)==4)and(X[0] in MathOps)
MathOps = string.split('~^ !^ ~& !&  ~| !& + - * / ^ % & | && || ! ~ < > << >> == <= >= !=')


def infoOf(Key):
    List = DataBase[Key]
    for X in List:
        if len(X)==4:
            return 'line=%s pos=%s'%(X[2],X[3])
    return 'location unknown'
    

    
def picklize():
    Fout = open('modules.pickle','w')
    pickle.dump(Modules,Fout)
    Fout.close()

def ensure(Cond,What):
    if Cond: return
    logs.log_err('ensure failed on %s'%str(What))

if __name__=='__main__':
    main()


