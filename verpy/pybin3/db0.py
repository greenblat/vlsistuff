
import os,sys,string,pickle,types
import logs
import traceback
import module_class as mcl
# from module_class import pr_stmt
# from module_class import module_class
import matches
import pprint
MathOps = ('** ~| ~& ~^ !^ + - * / ^ % & | && || ! ~ < > << >> >>> == <= >= != !== ~& === !==').split()
if os.path.exists('packages_save.py'):
    sys.path.append('.')
    import packages_save
else:
    packages_save = False
def main():
    load_parsed('.')
    dump_all_verilog('all.v')
    dump_all_all()
    if PackFile: 
        PackFile.write('endmodule\n')
        PackFile.close()
        Pack2File.close()

Modules = {}

def dumpDataBase():
    Keys = list(DataBase.keys())
    Keys.sort()
    Fout = open('database.dump','w')
    for Key in Keys:
        Fout.write('db %s %s\n'%(Key,DataBase[Key]))

def dump_all_verilog(Fname):
    Fout = open(Fname,'w')
    for Mod in Modules:
        logs.log_info('dumping %s'%Mod)
        Modules[Mod].dump_verilog(Fout)
    Fout.close()

def dump_all_all():
    for Mod in Modules:
        logs.log_info('dumping %s'%Mod)
        Modules[Mod].dump()


def load_parsed(Rundir):
    global Global,Modules
    Modules={}
    Global = mcl.module_class('global_module')
    logs.setCurrentModule('load_parsed db0')
    try:
        load_db0('%s/db0.pickle'%Rundir)
        Key = 'Main',1
        dumpDataBase()
        scan1(Key)
        return Modules
    except:
        load_db0('db0.pickle')
        Key = 'Main',1
        scan1(Key)
        logs.log_fatal('reading file probably failed on syntax')
        return {}

     
            
def load_db0(Fname):
    global DataBase
    File = open(Fname,'rb')
    DataBase = pickle.load(File) 
    File.close()


def scan1(Key):
    global Stack,State,Current,Modules,ModuleStuffs
    Stack=[]            
    State='idle'
    Current=0
    ModuleStuffs=[]
    if Key not in DataBase: return
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
            else:
                scan1(Item)
        else:
            logs.log_err('exxx %s %s'%(Key,Item))
                
PackFile = False
def add_package(Key):
    global PackFile,Pack2File
    List = DataBase[Key]
    Vars = matches.matches(List,'package ? ; !Parameters endpackage')
    if Vars:
        Pack = Vars[0][0]
        Pack2File = open('%s_save.py'%Pack,'w')
        Pack2File.write('# PARAMETERS,TYPEDEFS = {},{} \n')
        List = get_list(Vars[1])
        for Item in List:
            if Item[0]=='parameter':
                Pack2File.write('PARAMETERS["%s"] = '%(Item[1]))
                pprint.pprint(Item[2],Pack2File)
            elif Item[0]=='typedef':
                Pack2File.write('TYPEDEFS["%s"] = '%(Item[1]))
                pprint.pprint(Item[2:],Pack2File)
                if (Item[2][0]=='enum'):
                    LL = Item[3]
                    if LL[0][0]=='parameter':
                        for Prm in LL:
                            Pack2File.write('PARAMETERS["%s"] = '%(Prm[1]))
                            pprint.pprint(Prm[2],Pack2File)
            else:
                logs.log_error('package got item=%s'%str(Item))
        return
    logs.log_error('package got list=%s'%str(List))


def pr_typedef(List):
    if List[0]!='typedef':
        logs.log_error('typedef print got "%s" as header, not typedef'%(str(List[0])))
        return '// err typedef'

    Name = List[1]
    Str = 'typedef '
    Vars = matches.matches(List[2],['?','?',['?','?']])
    if Vars:
        Str += '%s %s [%s:%s] {\n  '%(Vars[0],Vars[1],Vars[2],Vars[3])
    else:
        logs.log_error('typedef of %s got for list2 "%s"'%(Name,List[2]))
    LL = []
    for Item in List[3]:
        Vars = matches.matches(Item,'parameter ? ?')
        if Vars:
            X = '%s = %s\n'%(Vars[0],mcl.pr_expr(Vars[1]))
            LL.append(X) 
    Lstr = '  ,'.join(LL)
    Str += Lstr
    Str += '\n} %s;'%(Name)
    return Str


def add_module(Key):
    global Current,ModuleStuffs
    List = DataBase[Key]
    Module = List[1][0]
    Current = mcl.module_class(Module)
    Modules[Module]=Current
    logs.log_info('addmodule %s (%s)'%(Module,Modules.keys()))
    if len(List)==5:
        Lhead = DataBase[List[2]]
        Lbody = DataBase[List[3]]
        Lparams=[]
    elif len(List)==6:
        Lparams = DataBase[List[2]]
        Lhead = DataBase[List[3]]
        Lbody = DataBase[List[4]]
    elif len(List)==3:
        if (List[0][1]=='define'):
            Var = List[1][0]
            Expr = get_expr(List[2])
            add_module_define(Var,Expr)
    else:
       logs.log_err('dont know to deal with %d %s'%(len(List),List))
       return
    if (len(Lparams)>0):
         add_module_params(Lparams)
    if (len(Lhead)>1):
         add_module_header(Lhead)
    if (len(Lbody)>0):
        ModuleStuffs = [Lbody]
        while (ModuleStuffs!=[]):
            add_module_stuff()

def add_module_define(Var,Expr):
    Current.add_define(Var,Expr)

def add_generate_item(List):
    Vars = matches.matches(List,'if ( !Expr ) !GenStatement else !GenStatement')
    if Vars:
        Cond = get_expr(Vars[0])
        Yes = get_statements(Vars[1])
        No = get_statements(Vars[2])
        Current.add_generate([['ifelse',Cond,['list']+Yes,['list']+No]])
        return
    Vars = matches.matches(List,'if ( !Expr ) !GenStatement')
    if Vars:
        Cond = get_expr(Vars[0])
        Yes = get_statements(Vars[1])
        Current.add_generate([['if',Cond,['list']+Yes]])
        return

    if len(List)==3:
        Statement = get_statements(List[1])
        if (len(Statement)==1)and(type(Statement) is list):
            Statement = Statement[0]

        Current.add_generate(Statement)
    else:
        logs.log_err('dont know to deal with generate len=%d %s'%(len(List),str(List)))
        

def add_define_item(List):
    Tok = List[0][1]
    if Tok=='backtick_include':
        Expr = get_expr(List[1])
        if Current:
            Current.add_include(Expr)
        else:
            logs.log_err('dont know to deal with %d %s'%(len(List),List))
        return
    elif Tok=='backtick_undef':
        return
    elif Tok=='define':
        if List[0][0]=='`include':
            Expr = get_expr(List[1])
            Current.add_include(Expr)
            return
    logs.log_err('dont know to deal with %d add_define_item %s'%(len(List),List))

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
                Vars = matches.matches(LL,'parameter ? ? = ?')
                if Vars:
                    Who = Vars[1][0]
                    Expr = get_expr(Vars[2])
                    Current.add_parameter(Who,Expr)
                elif (len(LL)==4)and(LL[0][0]=='parameter'):
                    Who = LL[1][0]
                    Expr = get_expr(LL[3])
                    Current.add_parameter(Who,Expr)
                elif (len(LL)==4)and(LL[0][0]=='localparam'):
                    Who = LL[1][0]
                    Expr = get_expr(LL[3])
                    Current.add_parameter(Who,Expr)
                elif (len(LL)==3)and(LL[1][0]=='='):
                    Who = LL[0][0]
                    Expr = get_expr(LL[2])
                    Current.add_parameter(Who,Expr)
                else:
                    logs.log_err('add_module_param got %d %s'%(len(LL),LL))
                


def add_module_header(List0):
    Dir = False
    Vars = matches.matches(List0,'( !Header_list ) ;')
    if Vars:
        List = get_list(DataBase[Vars[0]])
        for Item in List:
            if type(Item) is tuple:
                Vars2 = matches.matches(Item,'extdir ? ? ?')
                if Vars2:
                    Dir = Vars2[0]
                    Net = Vars2[1]
                    if notUsualDir(Dir):
                        Usual,Type = notUsualDir(Dir)
                        Wid = getTypeDefWid(Type)
                        Current.add_sig(Net,Usual,Wid) 
                        record_original_typedef(Net,Type)
                    else:
                        Wid = Vars2[2]
                        Current.add_sig(Net,Dir,Wid) 
                else:
                    logs.log_error('add_module_header got %s'%str(Item))
            elif type(Item) is str:
                if Dir: Current.add_sig(Item,Dir,Wid) 
            else:                    
                logs.log_error('add_module_header got(1) %s'%str(Item))
        return
    logs.log_error('add_module_header got(1) %s'%str(List0))
    return

OriginalTypeDefs={}
def record_original_typedef(Net,Type):
    OriginalTypeDefs[(Net,Current.Module)] = Type
    

def getStructFields(Kind):
    if not packages_save: return 0,{}
    if Kind in packages_save.TYPEDEFS:
        Struct = packages_save.TYPEDEFS[Kind]
        if Struct[0]=='struct':
            res = {}
            Tot = 0
            Str = Struct[1][:]
            Str.reverse()
            for Item in Str:
                Wid = getTypeDefWid(Item[0])
                Name = Item[1]
                res[Name] = (Wid+Tot-1,Tot)
                Tot += Wid
            return Tot,res
    logs.log_error('getStructFields name=%s '%(str(Kind)))
    return 0,{}

def getTypeDefWid(Kind):

    if packages_save and (Kind in packages_save.TYPEDEFS):
        Struct = packages_save.TYPEDEFS[Kind]
        if Struct[0]=='struct':
            Tot = 0
            for Item in Struct[1]:
                Wid = getTypeDefWid(Item[0])
                Tot += Wid
            return Tot 
        Vars = matches.matches(Struct[0],'enum logic ?')
        if Vars:
            H,L = Vars[0]
            return H-L+1
            
    
    if Kind=='logic': return 1
    if Kind=='integer': return 32
    if Kind=='real': return 64




    logs.log_error('getTypeDefWid name=%s '%(str(Kind)))
    traceback.print_stack(None,None,logs.Flogs[0])
    return 5


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
    if is_terminal(Item1):
        if Item1[0]=='*':
            return ['*']

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
    Vars = matches.matches(List,'assign !Soft_assigns ;')
    if Vars:
        Res = get_soft_assigns(Vars[0])
        return Res
    Vars = matches.matches(List,'assign ? = !Expr ;')
    if Vars:
        Dst = get_expr(Vars[0])
        Src = get_expr(Vars[1])
        res.append(['=',Dst,Src])
        return ('=',Dst,Src)
    for Item in List:
        if Item[0]=='Soft_assigns':
            More = get_soft_assigns(Item)
            res.extend(More)
        elif Item[0]=='Soft_assign':
            List2 = DataBase[Item]
            done=False
            Vars = matches.matches(List2,'integer ? = ?')
            if Vars:
                Dst = get_expr(Vars[0])
                Src = get_expr(Vars[1])
                res.append(['=',Dst,Src])
                Current.add_sig(Dst,'integer',0)
                done=True
            Vars = matches.matches(List2,'genvar ? = ?')
            if Vars:
                Dst = get_expr(Vars[0])
                Src = get_expr(Vars[1])
                res.append(['=',Dst,Src])
                Current.add_sig(Dst,'genvar',0)
                done=True

            Vars = matches.matches(List2,'? = ?')
            if not done and Vars:
                Dst = get_expr(Vars[0])
                Src = get_expr(Vars[1])
                res.append(['=',Dst,Src])
                done=True
            Vars = matches.matches(List2,'? plusplus')
            if not done and Vars:
                Dst = get_expr(Vars[0])
                res.append(['=',Dst,['+',Dst,1]])
                done=True
            if not done:
                logs.log_err('get_soft_assigns not done got %s'%str(List2))
        elif Item[0]=='assign':
            List2 = DataBase[Item]
        else:
            logs.log_err('get_soft_assigns got %s'%str(Item))
    return res


def get_statement(Item):
    if (type(Item) is tuple):
        List = DataBase[Item]
    else:
        List = Item

    Vars = matches.matches(List,'!AlwaysKind !Statement')
    if Vars:
        Always = get_expr(Vars[0])
        Stats = get_statement(Vars[1])
        return [Always,[],Stats]
    Vars = matches.matches(List,'!AlwaysKind !When !Statement')
    if Vars:
        Always = get_expr(Vars[0])
        When = get_when(Vars[1])
        Stats = get_statement(Vars[2])
        return [Always,When,Stats]

    Vars = matches.matches(List,'always !When !Statement')
    if Vars:
        When = get_when(Vars[0])
        Stats = get_statement(Vars[1])
        return ['always',When,Stats]

        
    Vars = matches.matches(List,'!IntDir !Tokens_list ;')
    if Vars:
        Dir = get_dir(Vars[0])
        if Dir=='logic': Dir='wire';
        List0 = get_list(Vars[1])
        res=[]
        for Net in List0:
            res.append(('declare',Dir,Net,0))
        return res 

    Vars = matches.matches(List,'!IntDir !Width !Width ? ;')
    if Vars:
        Dir = get_dir(Vars[0])
        if Dir=='logic': Dir='wire';
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        List0 = get_list(Vars[3])
        res=[]
        for Net in List0:
            res.append(('declare',Dir,Net,('packed',Wid0,Wid1)))
        return res 

    Vars = matches.matches(List,'!IntDir !Width ?  = !Expr ;')
    if Vars:
        Dir = get_dir(Vars[0])
        if Dir=='logic': Dir='wire';
        Wid = get_wid(Vars[1])
        Net = Vars[2]
        res=['list']
        res.append(('declare',Dir,Net,Wid))
        Src = get_expr(Vars[3])
        Dst = get_expr(Net)
        res.append(('assigns',['list',['=',Dst,Src]]))
        return res 
        
        
    Vars = matches.matches(List,'!IntDir !Width !Tokens_list ;')
    if Vars:
        Dir = get_dir(Vars[0])
        if Dir=='logic': Dir='wire';
        Wid0 = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        res=[]
        for Net in List0:
            res.append(('declare',Dir,Net,Wid0))
        return res 

    Vars = matches.matches(List,"for ( ? ; ? ; ? ) ?")
    if Vars:
        Assigns1 = get_soft_assigns(Vars[0])
        Cond = get_expr(Vars[1])
        Assigns2 = get_soft_assigns(Vars[2])
        Stmt = get_statement(Vars[3])
        return ['for',Assigns1,Cond,Assigns2,Stmt]
#ILIA
    Vars = matches.matches(List,"parameter  ? ;")
    if Vars:
        More = get_list(Vars[0])
        return More

    Vars = matches.matches(List,"localparam  ? ;")
    if Vars:
        More = get_list(Vars[0])
        return More

    if len(List)==1:
        if List[0][0]=='Always':
            LL = DataBase[List[0]]
            return get_statement(LL)
        if List[0][0]=='While_statement':
            List2 = DataBase[List[0]]
            Cond = get_expr(List2[2])
            Stmt = get_statement(List2[4])
            return ['while',Cond,Stmt]
        if List[0][0] in ['Instance']:
            List = DataBase[List[0]]
            return instance_statement(List)
        if List[0][0] in ['Assign']:
            List2 = DataBase[List[0]]
            Assigns = get_soft_assigns(List[0])
            return ['assigns',Assigns]
            
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
        if List[0][0]=='reg':
            Wid = get_expr(List[1])
            Src = get_expr(List[2])
            return ['reg',Wid,Src]
    if len(List)==3:
        if List[0][0]=='reg':
            Src = get_expr(List[1])
            return ['reg',0,Src]


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
        if (List[0][0] in ['CaseKind'] ):
            Switch = get_expr(List[2])
            Cases  = get_cases(List[4])
            Default  = get_default(List[5])
            Cases.append(['default',Default])
            XX = DataBase[List[0]]
            if matches.matches(XX,'unique case'):
                return ['unique_case',Switch,Cases]
            elif matches.matches(XX,'case'):
                return ['case',Switch,Cases]
            else:
                logs.log_err('CaseKind got %s'%str(List[0]))
            return [] 

        if (List[0][0] in ['case','casez','casex'] ):
            Switch = get_expr(List[2])
            Cases  = get_cases(List[4])
            Default  = get_default(List[5])
            Cases.append(['default',Default])

            return [List[0][0],Switch,Cases]

    Vars = matches.matches(List,'!CaseKind ( !Expr ) !Cases !Default endcase')
    if Vars:
        Switch = get_expr(Vars[1])
        Cases  = get_cases(Vars2[2])
        XX = DataBase[Vars[0]]
        Default  = get_default(List[5])
        Cases.append(['default',Default])
        if matches.matches(XX,'unique case'):
            return ['unique_case',Switch,Cases]
        elif matches.matches(XX,'case'):
            return ['case',Switch,Cases]
        else:
            logs.log_err('CaseKind got %s'%str(List[0]))

    Vars = matches.matches(List,'!CaseKind ( !Expr ) !Cases endcase')
    if Vars:
        Switch = get_expr(Vars[1])
        Cases  = get_cases(Vars[2])
        XX = DataBase[Vars[0]]
        if matches.matches(XX,'unique case'):
            return ['unique_case',Switch,Cases]
        elif matches.matches(XX,'case'):
            return ['case',Switch,Cases]
        else:
            logs.log_err('CaseKind got %s'%str(List[0]))

    Vars = matches.matches(List,'return ? ;')
    if Vars:
        return ['return',Vars[0]]

    if (type(List) is list)and(len(List)==1):
        return get_statement(List[0])

    Vars = matches.matches(List,'!IntDir !Tokens_list  = !Expr ;')
    if Vars:
        logs.log_warning('needs care. wire in genvar with assign')
        return
    Vars = matches.matches(List,'!pragma1 !pragma_stuffs  !pragma2')
    if Vars:
        logs.log_warning('needs care. pragma in genvar with assign')
        return
    Vars = matches.matches(List,'!IntDir !Width ? !Width ;')
    if Vars:
        logs.log_warning('needs care. sigs def in genvar ')
        return

    Vars = matches.matches(List,'!IntDir !ManyDefs ;')
    if Vars:
        logs.log_warning('needs care. sigs many def in genvar ')
        return

    Vars = matches.matches(List,'!IntDir !Width !ManyDefs ;')
    if Vars:
        logs.log_warning('needs care. sigs width many def in genvar ')
        return
    Vars = matches.matches(List,'initial  !Statement ')
    if Vars:
        logs.log_warning('needs care. initial def in genvar ')
        return
     

    logs.log_err(' db0: untreated statement len=%d list="%s"'%(len(List),List),True)
    return []

def get_default(Item):
    List = DataBase[Item]
    if List[2][0]==';':
        return ['empty_begin_end']
    return get_statement(List[2])

def get_cases(Item1):
    if Item1 not in DataBase: return []
    List = DataBase[Item1][:]
    while List[0][0]=='Cases':
        Itm = List[0]
        Part = DataBase[Itm][:]
        List = Part + List[1:]
        

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
            elif (Item[0]=='default'):
                return ['default']
            else:
                logs.log_err('bad case item "%s"'%(str(Item)))
                return []
        else:
            logs.log_err('bad case item "%s"'%(str(Item)))
            return []
    return res

def get_statements(Item1):
    List2 = flattenList(Item1)
    Vars = matches.matches(List2,'begin !GenStatements end')
    if Vars:
        more = get_statements(Vars[0])
        return more

    Vars = matches.matches(List2,'begin : ? !GenStatements end')
    if Vars:
        more = get_statements(Vars[1])
        return more


    res = []
    for Item in List2:
        if len(Item)==2:
            if (Item[0]=='Statement'):
                x = get_statement(Item)
                res.append(x)
            elif (Item[0]=='Statements'):
                more = get_statements(Item)
                res.extend(more)
            elif (Item[0]=='GenStatements'):
                more = get_statements(Item)
                res.extend(more)
            elif (Item[0]=='GenStatement'):
                x = get_statement(Item)
                res.append(x)
            elif (Item[0]=='Assign'):
                LL = DataBase[Item]
                Vars = matches.matches(LL,'assign ? = ? ;')
                if Vars:
                    Dst = get_expr(Vars[0])
                    Src = get_expr(Vars[1])
                    res.append(['assigns',('=',Dst,Src)])
                else:
                    logs.log_error('Assign %s'%str(DataBase[Item]))
            else:
                logs.log_err('fallOff #0411# %s'%str(Item))
        elif (len(Item)==3)and(Item[0][0]=='begin')and(Item[2][0]=='end'):
            x = get_statement(Item[1])
            res.append(x)
        else:
            logs.log_err('fallOff #0413#   %s "%s"'%(Item,List2))
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
        elif len(List)==3:
            if (List[0][0]=='[')and(List[2][0]==']'):
                Num  =get_expr(List[1])
                return ['-',Num,1],0
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
    if (type(Item) is list)and(len(Item)==1):
        return get_dir(Item[0])
    if tuple(Item) in DataBase:
        return get_dir(DataBase[tuple(Item)])
    if (type(Item) is tuple)and(len(Item)==4):
        return Item[0]
    Vars = matches.matches(Item,'!PureExt !IntKind',False)
    if Vars:
        AA = Vars[0][0]
        BB = Vars[1][0]
        return '%s %s'%(AA,BB)
    Vars = matches.matches(Item,'!PureExt !IntKind signed',False)
    if Vars:
        AA = Vars[0][0]
        BB = Vars[1][0]
        return '%s %s signed'%(AA,BB)

    Vars = matches.matches(Item,'!PureExt signed',False)
    if Vars:
        AA = Vars[0][0]
        return '%s signed'%(AA)
    Vars = matches.matches(Item,'wire signed',False)
    if Vars:
        return 'wire signed'
    Vars = matches.matches(Item,'reg signed',False)
    if Vars:
        return 'reg signed'
    Vars = matches.matches(Item,'input logic',False)
    if Vars:
        return 'input'
    Vars = matches.matches(Item,'output logic',False)
    if Vars:
        return 'output'

    if type(Item) is tuple:
        if Item[0] in ['wire','logic']:
            return Item[0]


    logs.log_err('get_dir %s'%str(Item))
    return 'wire'


def get_list(Item):
    if (type(Item) is list)and(len(Item)==1):
        Item =  Item[0]
    if tuple(Item) in DataBase:
        Item = DataBase[tuple(Item)]
    if (type(Item) is list)and(len(Item)==1):
        Item =  Item[0]

    if (type(Item) is tuple)and(len(Item)==4):
        return [Item[0]]

    if tuple(Item) in DataBase:
        Item = DataBase[tuple(Item)]

    Vars = matches.matches(Item,'? , !Tokens_list')
    if Vars:
        More = get_list(Vars[1])
        return [Vars[0][0]]+More

    Vars = matches.matches(Item,'!Header_list , !Header_item')
    if Vars:
        More = get_list(Vars[0])
        This = get_list(Vars[1])
        return More+This
    Vars = matches.matches(Item,'!Pairs2 , !Pair2')
    if Vars:
        More0 = DataBase[Vars[0]]
        if len(More0)==3:
            More = get_list(Vars[0])
        else:
            More = [get_pair(Vars[0])]
        This = get_pair(Vars[1])
        return More+[This]

    Vars = matches.matches(Item,'!Parameters !PackageItem')
    if Vars:
        More = get_list(Vars[0])
        This = get_list(Vars[1])
        return This+More

    Vars = matches.matches(Item,'parameter !Pairs ;')
    if Vars:
        More = get_list(Vars[0])
        return More
    Vars = matches.matches(Item,'localparam !Pairs ;')
    if Vars:
        More = get_list(Vars[0])
        return More


    Vars = matches.matches(Item,'? = !Expr')
    if Vars:
        Expr = get_expr(Vars[1])
        return [('parameter',Vars[0][0],Expr)]
    Vars = matches.matches(Item,'typedef enum logic !Width  { !Pairs } ? ;')
    if Vars:
        Wid = get_wid(Vars[0])
        Pairs = get_list(Vars[1])
        Name = get_expr(Vars[2])

        return [('typedef',Name,['enum','logic',Wid],Pairs)]

    Vars = matches.matches(Item,'!Pairs , !Pair')
    if Vars:
        Pairs = get_list(Vars[0])
        Pair  = get_list(Vars[1])
        return Pairs+Pair

    Vars = matches.matches(Item,'!ManyDefs , !OneDef')
    if Vars:
        Defs = get_list(Vars[0])
        Def  = get_list(Vars[1])
        return Defs+Def



    Vars = matches.matches(Item,'!SimpleDefs !SimpleDef')
    if Vars:
        Pairs = get_list(Vars[0])
        Pair  = get_list(Vars[1])
        return Pairs+Pair
    Vars = matches.matches(Item,'!IntDir ? ;')
    if Vars:
        Dir = get_dir(Vars[0])
        Name = get_expr(Vars[1])
        return [(Dir,Name)]

    if Item[0][0]=='ExtDir':
        return [getExtDir(Item)]

    if (type(Item) is list)and(len(Item))==1:
        return get_list(Item[0])

    logs.log_err('get_list %s'%str(Item))
    logs.pStack()
    return []


def getExtDir(Item):
    Vars = matches.matches(Item,'!ExtDir ?')
    if Vars:
        Dir = get_dir(Vars[0])
        Name = get_expr(Vars[1])
        return ('extdir',Dir,Name,0)
    Vars = matches.matches(Item,'!ExtDir !Width ?')
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        Name = get_expr(Vars[2])
        return ('extdir',Dir,Name,Wid)

    Vars = matches.matches(Item,'!ExtDir !Width !Width ?')
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        Name = get_expr(Vars[3])
        return ('extdir',Dir,Name,('packed',Wid0,Wid1))

    Vars = matches.matches(Item,'!ExtDir !Width ? !Width')
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[3])
        Name = get_expr(Vars[2])
        return ('extdir',Dir,Name,('double',Wid0,Wid1))

    logs.log_err('getExtDir got "%s"'%str(Item))
    return []

def get_pair(Item):
    if len(Item)==1: return get_pair(Item[0])
    if in_db(Item):
        return get_pair(DataBase[Item])
    Vars = matches.matches(Item,'? : ?')
    if Vars:
        Var = get_expr(Vars[0])
        Expr = get_expr(Vars[1])
        return (Var,Expr)
    logs.log_error('get_pair %s failed'%str(Item))
    return False

def add_module_stuff():
    List1 = ModuleStuffs.pop(0)
    if len(List1)==0:
        return
    for Item in List1:
        if len(Item)==2:
            if (Item[0]=='Mstuff'):
                Mstuff = DataBase[Item]
                if Mstuff[0][0] in ['if','ifelse']:
                    add_generate_item(Mstuff)
                else:
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
            add_localparam(List)
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
        elif Item[0]=='Typedef':
            add_typedef_item(List)
        elif Item[0]=='GenFor_statement':
            X = get_statement(Item)
            Current.add_generate(X)
        elif Item[0]=='Pragma':
            Item = List[1]
            List = get_list(Item)
            add_pragma(List)

        else:
            logs.log_err('untreated(0) "%s" "%s"'%(Item,List))
    elif (len(Item)==4)and(Item[1]=='pragma'):
        add_pragma(Item)
    elif (len(Item)==4)and(Item[1]=='newver'):
        add_newver(Item)
    else:
        logs.log_err('untreated(1) len=%d "%s"'%(len(Item),str(Item)))

def add_typedef_item(List):
    Vars = matches.matches(List,'typedef struct { ? } ? ;')
    if Vars:
        Name = get_expr(Vars[1])
        LL = get_list(Vars[0])
        packages_save.TYPEDEFS[Name]=('struct',LL)
        return

    logs.log_error('add_typedef_item got "%s"'%str(List))


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
    Kind = get_expr(List[0])
    if len(List)==3:
        When = get_when(List[1])
        Statement = get_statement(List[2])
        if len(When)>1:
            When = ['list']+When
        else:
            When = When[0]
        Current.add_always(Statement,When,Kind)
    elif len(List)==2:
        Statement = get_statement(List[1])
        Current.add_always(Statement)
    else:
        logs.log_err('bad always %s'%List)
def add_initial(List):
    Statement = get_statement(List[1])
    Current.add_initial(Statement)
    


def add_instance(List):
    Vars = matches.matches(List,'? ? ;')
    if Vars:
        Current.add_inst(Vars[0],Vars[1])
        return
        


    Type = List[0][0]
    if (List[1][0]=='('):
        Inst = invent_inst(Type,Current)
        Current.add_inst(Type,Inst)
        if (len(List)>=4)and(List[2][0]=='Exprs'):
            LL = get_exprs(List[2])
            for i in range(len(LL)):
                Sig = LL[i]
                Pin = 'pin%d'%i
                Current.add_conn(Inst,Pin,Sig)
            return
        else:
            logs.log_error('add_instance %d %s'%(len(List),str(List)))
    if istoken(List[1]):
        Inst = List[1][0]
        Params=[]
    elif (List[1][0]=='('):
        Inst = invent_inst('buf',Current)
        Params=[]
    else:
        Inst = List[2][0]
        Params = get_inst_params(List[1])
    Current.add_inst(Type,Inst)

    for (Prm,Val) in Params:
        Current.add_inst_param(Inst,Prm,Val)
    if List[-5][0]=='Width':
        Wid = get_wid(List[-5])
        Current.add_inst_param(Inst,'inst_width',('width',Wid))
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
    if (List[-2][0]==')')and(List[-3][0]=='('): return
    logs.log_err('add_instance len=%d list=%s'%(len(List),List))


def instance_statement(List):
    Type = List[0][0]
    Inst = '?'
    Conns = {}
    Params = {}
    if (List[1][0]=='('):
        Inst = invent_inst(Type,Current)
    elif istoken(List[1]):
        Inst = List[1][0]
        Params={}
    else:
        Inst = List[2][0]
        Params = get_inst_params(List[1])
    if List[-3][0]=='Conns_list':
        Conns = get_conns(List[-3])
    elif List[-3][0]=='Exprs':
        Conns={}
        LL = get_exprs(List[-3])
        for i in range(len(LL)):
            Sig = LL[i]
            Pin = 'pin%d'%i
            Conns[Pin]=Sig
    return ['instance',Type,Inst,Params,Conns] 


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
    Vars = matches.matches(List,'!Soft_assign',False)
    if Vars:
        Item = DataBase[Vars[0]]
        add_hard_assign(Item)
        return
        
    Vars = matches.matches(List,'!LSH = !Expr',False)
    if Vars:
        Dst = get_expr(Vars[0])
        Src = get_expr(Vars[1])
        Current.add_hard_assign(Dst,Src)
        return

    Vars = matches.matches(List,'!Soft_assigns , !Soft_assign',False)
    if Vars:
        add_hard_assign(DataBase[Vars[0]])
        add_hard_assign(DataBase[Vars[1]])
        return

    Vars = matches.matches(List,'assign !Soft_assigns ;',False)
    if Vars:
        Item = Vars[0]
        add_hard_assign(DataBase[Item])
        return



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

    Vars = matches.matches(List,'enum !WireLogic !Width { !Tokens_list } !Tokens_list ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        List1 = get_list(Vars[3])
        for Net in List1:
            Current.add_sig(Net,Dir,Wid)
        for ind,Enum in enumerate(List0):
            Current.add_localparam(Enum,ind)
            
        return

    Vars = matches.matches(List,'!ExtDir !Tokens_list ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        List0 = get_list(Vars[1])
        for Net in List0:
            Current.add_sig(Net,Dir,0)
        return
    Vars = matches.matches(List,'!ExtDir !Width !Tokens_list ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        for Net in List0:
            Current.add_sig(Net,Dir,Wid)
        return

    Vars = matches.matches(List,'!IntDir !Width !Tokens_list = !Expr ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        Expr = get_expr(Vars[3])
        for Net in List0:
            Current.add_sig(Net,Dir,Wid)
            Current.add_hard_assign(Net,Expr)
        return

    Vars = matches.matches(List,'!IntDir ?  = !Expr ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        List0 = get_list(Vars[1])
        Expr = get_expr(Vars[2])
        for Net in List0:
            Current.add_sig(Net,Dir,0)
            Current.add_hard_assign(Net,Expr)
        return

    Vars = matches.matches(List,'!IntDir !Width ?  = !Expr ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        Expr = get_expr(Vars[3])
        for Net in List0:
            Current.add_sig(Net,Dir,Wid)
            Current.add_hard_assign(Net,Expr)
        return

    Vars = matches.matches(List,'!IntDir !InstParams ?  = !Expr ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        List0 = get_list(Vars[2])
        Expr = get_expr(Vars[3])
        for Net in List0:
            Current.add_sig(Net,Dir,0)
            Current.add_hard_assign(Net,Expr)
        return



    Vars = matches.matches(List,'!IntDir !Width !Tokens_list ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        for Net in List0:
            Current.add_sig(Net,Dir,Wid)
        return
        
    Vars = matches.matches(List,'!IntDir !Tokens_list ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        List0 = get_list(Vars[1])
        if notUsualDir(Dir):
            Usual,Type = notUsualDir(Dir)
            Wid = getTypeDefWid(Type)
            
            for Net in List0:
                record_original_typedef(Net,Type)
                Current.add_sig(Net,Usual,Wid)
        else:            
            for Net in List0:
                Current.add_sig(Net,Dir,0)
        return
    Vars = matches.matches(List,'!IntDir ? !Width ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[2])
        Name = get_expr(Vars[1])
        Current.add_sig(Name,Dir,Wid0)
        return

    Vars = matches.matches(List,'!IntDir !Width !Width ? ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        Name = get_list(Vars[3])
        if type(Name) is list:
            for Net in Name:
                Current.add_sig(Net,Dir,('packed',Wid0,Wid1))
        else:
            Current.add_sig(Name,Dir,('packed',Wid0,Wid1))
        return

    Vars = matches.matches(List,'!IntDir !Width ? !Width ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[3])
        Name = get_list(Vars[2])
        Current.add_sig(Name,Dir,('packed',Wid0,Wid1))
        return

    Vars = matches.matches(List,'!IntDir !Width ? !BusBit ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Name = get_expr(Vars[2])
        Wid1 = get_wid(Vars[3])
        Current.add_sig(Name,Dir,('double',Wid0,Wid1))
        return

    Vars = matches.matches(List,'!IntDir !Width !Width ? ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        Name = get_expr(Vars[3])
        Current.add_sig(Name,Dir,('packed',Wid0,Wid1))
        return

    Vars = matches.matches(List,'!IntDir !Width !Width ? = ?  ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        Name = get_expr(Vars[3])
        Expr = get_expr(Vars[4])
        Current.add_sig(Name,Dir,('packed',Wid0,Wid1))
        Current.add_hard_assign(Name,Expr)
        return

    Vars = matches.matches(List,'!IntDir !ManyDefs ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        List0 = get_list(Vars[1])
        for Item in List0:
            if type(Item) is str:
                Current.add_sig(Item,Dir,0)
            elif (Item[0] == 'parameter'):
                Current.add_sig(Item[1],Dir,0)
                Expr = get_expr(Item[2])
                Current.add_hard_assign(Item[1],Expr)
        return

    Vars = matches.matches(List,'!IntDir !Width !ManyDefs ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        List0 = get_list(Vars[2])
        for Item in List0:
            if type(Item) is str:
                Current.add_sig(Item,Dir,Wid0)
            elif (Item[0] == 'parameter'):
                Current.add_sig(Item[1],Dir,Wid0)
                Expr = get_expr(Item[2])
                Current.add_hard_assign(Item[1],Expr)



        return

    Vars = matches.matches(List,'!IntDir !Width !Width !ManyDefs ;',False)
    if Vars:
        Dir = get_dir(Vars[0])
        Wid0 = get_wid(Vars[1])
        Wid1 = get_wid(Vars[2])
        List0 = get_list(Vars[3])
        for Item in List0:
            if type(Item) is str:
                Current.add_sig(Item,Dir,('packed',Wid0,Wid1))
            elif (Item[0] == 'parameter'):
                Current.add_sig(Item[1],Dir,('packed',Wid0,Wid1))
                Expr = get_expr(Item[2])
                Current.add_hard_assign(Item[1],Expr)
        return

    Vars = matches.matches(List,'const logic !Width !Width ? = { !Exprs } ;',False)
    if Vars:
        Wid0 = get_wid(Vars[0])
        Wid1 = get_wid(Vars[1])
        Exprs = get_expr_list(Vars[3])
        Name = Vars[2];
        Current.add_sig(Name,'wire',('packed',Wid1,Wid0))
        for ind,Val in enumerate(Exprs):
            Current.add_hard_assign(['subbit',Name,ind],Val)
        return
        


    logs.log_err('bad new definition "%s"'%str(List))


def get_expr_list(Item):
    if (type(Item) is list)and(len(Item)==1):
        return get_expr_list(Item[0])
    if in_db(Item):
        return get_expr_list(DataBase[Item])

    if is_terminal(Item):
        return [get_expr(Item)]


    Vars = matches.matches(Item,'!Exprs , !Expr')
    if Vars:
        if in_db(Vars[0]):
            More = get_expr_list(DataBase[Vars[0]])
        else:
            More = get_expr(Vars[0])
        Expr = get_expr(Vars[1])
        return More + [Expr]

    logs.log_err('get_expr_list failed on "%s"'%str(Item))
    return []

def in_db(Item):
    if type(Item) is not tuple: return False
    return Item in DataBase

def is_terminal(Item):
    if type(Item) is not tuple: return False
    return len(Item)==4
    if type(Item) is not tuple: return False
    return Item in DataBase

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

def add_localparam(List0):
    Vars = matches.matches(List0,'localparam !Pairs ;',False)
    if Vars:
        List1 = DataBase[Vars[0]]
        Pairs = get_list(Vars[0])
        for Item in Pairs:
            if len(Item)==2:
                List2 = DataBase[Item]
                Vars2 = matches.matches(List2,'?token = !Expr',False)
                if Vars2:
                    Name = Vars2[0][0]
                    Expr = get_expr(Vars2[1])
                    Current.add_localparam(Name,Expr)
            elif (len(Item)==3)and(Item[0]=='parameter'):
                Name = Item[1]
                Expr = get_expr(Item[2])
                Current.add_localparam(Name,Expr)
        return

    Vars = matches.matches(List0,'localparam !Width !Pairs ;',False)
    if Vars:
        List1 = get_list(Vars[1])
        for Item in List1:
            Vars2 = matches.matches(Item,'?token = !Expr',False)
            if Vars2:
                Name = Vars2[0][0]
                Expr = get_expr(Vars2[1])
                Current.add_localparam(Name,Expr)
        return
    Vars = matches.matches(List0,'localparam !Width !Width !Pairs ;',False)
    if Vars:
        List1 = DataBase[Vars[2]]
        for Item in List1:
            List2 = DataBase[Item]
            Vars2 = matches.matches(List2,'?token = !Expr',False)
            if Vars2:
                Name = Vars2[0][0]
                Expr = get_expr(Vars2[1])
                Current.add_localparam(Name,Expr)
        return

    logs.log_error('localparam failed in %s'%(str(List0)))
    return

def flattenList(Ptr):
    Key = Ptr[0]
    if tuple(Ptr) not in DataBase: return Ptr
    List = DataBase[Ptr]
    if (List[0][0]==Key):
        if len(List)>=3:
            while (len(List)>=3)and(List[1][0]==',')and(List[0][0]==Key):
                LL = DataBase[List[0]]
                List = LL + List[2:]
        else:
            while (len(List)>=2)and(List[0][0]==Key):
                LL = DataBase[List[0]]
                List = LL + List[1:]
    return List
        

def get_conns(Ptr):
    List=DataBase[Ptr]
    List2 = flattenList(Ptr)
    res = []
    for Item in List2:
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
                    Sig='*'
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
                    logs.log_err( 'strange get_conns %s'%str(List2))

            else:
                logs.log_err('strange get_conns %s'%str(Item))
        elif (type(Item) is tuple)and(Item[0]==','):
            pass
        else:
            logs.log_err('strange2 get_conns %s'%str(Item))
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




def checkInPackages(Item):
    if not packages_save: return
    if 'PARAMETERS' not in dir(packages_save): return
    if Item in packages_save.PARAMETERS:
        if Item not in Current.localparams:
            Current.localparams[Item]=packages_save.PARAMETERS[Item]

def findField(Item):
    wrds = Item.split('.')
    Net = wrds[0]
    Base = OriginalTypeDefs[(Net,Current.Module)]
    Field = wrds[1]
    Tot,Fields = getStructFields(Base)
    if Field in Fields:
        
        return ['subbus',Net,Fields[Field]]


    logs.log_info('findField failed on net="%s"'%str(Base))
    return 'findField'

def get_expr(Item):
    if type(Item) is int: return Item
    if type(Item) is str: return Item
    if len(Item)==4:
        if Item[1]=='token':
            if '.' in Item[0]:
                return findField(Item[1])
            checkInPackages(Item)
            return Item[0]
        if Item[1]=='number':
            return int(Item[0])
        if Item[1]=='string':
            return Item[0]
        if Item[1]=='hex':
            return ['hex',Item[0]]
    if (type(Item) is tuple):
        if Item[0]=='*':
            return '*'
    if len(Item)==2:
        if Item[0] == '~': return Item
        List = DataBase[Item]
        if Item[0]=='Crazy3':
            Vars = matches.matches(List,'? !crazy2 ? )',False)
            if Vars:
                Type = Vars[0][0]
                Expr = get_expr(Vars[2])
                return Expr


        if len(List)==1:
            if List[0][0]in ['always','always_comb','always_ff','always_latch']: return 'always'
            if List[0][0]in ['always','always_comb','always_ff']: return List[0][0]
            if List[0][0]=='Expr':
                return get_expr(List[0])
            if List[0][1]=='floating':
                return float(List[0][0])
            if List[0][1]=='exttype':
                return List[0][0]

            if List[0][1]=='number':
                return int(List[0][0])
            if List[0][1]=='define':
                return ['define',List[0][0]]
            if List[0][1]=='token':
                if '.' in List[0][0]:
                    return findField(List[0][0])
                checkInPackages(List[0][0])
                return List[0][0]
            if List[0][1]=='string':
                return List[0][0]
            if List[0][1]=='ubin':    
                X = List[0][0].split("'b")
                return ['bin',X[0],X[1]]
            if List[0][1]=='uhex':    
                X = List[0][0].split("'h")
                return ['hex',X[0],X[1]]
            if List[0][1]=='udig':    
                X = List[0][0].split("'d")
                if len(X)==2:
                    if X[0] == '':
                        return ['dig',32,X[1]]

                    return ['dig',X[0],X[1]]
                else:
                    return ['dig',32,X[0]]
            if List[0][1]=='bin':    
                if List[0][0]=="'x":
                    return ['bin',32,'x']
                X = List[0][0].replace("'b",' ')
                X = X.replace("'sb",' ')
                X1 = X.split()
                return ['bin',X1[0],X1[1]]
            if List[0][1]=='dig':    
                if "'sd" in List[0][0]:
                    X = List[0][0].replace("'sd",' ')
                else:
                    X = List[0][0].replace("'d",' ')
                X1 = X.split()
                if len(X1)==1:
                    return ['dig',0,X1]
                else:
                    return ['dig',X1[0],X1[1]]
            if List[0][1]=='hex':    
                X = List[0][0].replace("'h",' ')
                X1 = X.split()
                return ['hex',X1[0],X1[1]]
            if List[0][0]=='CurlyList':    
                return curly_list(List[0])
            if List[0][0]=='Dotted':    
                List2 = DataBase[List[0]]
                Dotted = get_dotted_items(List2)
                return ('dotted',Dotted)
            if List[0][0]=='Crazy':    
                XX  = DataBase[List[0]]
                Vars = matches.matches(XX,"crazy1 default : ? }")
                if Vars:
                    Expr = get_expr(Vars[0])
                    return Expr
                Vars = matches.matches(XX,"crazy1 !Pairs2 }")
                if Vars:
                    Pairs = get_list(Vars[0])
                    res = ['curly']
                    for A,B in Pairs:
                        res.append(B)

                    return res
                
                logs.log_error('crazy got "%s"'%(str(XX)))
                return 0

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
                X =  get_curly_items(List[1])
                return ['curly']+X

            if isexpr(List[0])and isexpr(List[2]) and is_math_op(List[1]):
                Expr0 = get_expr(List[0])
                Expr1 = get_expr(List[2])
                Op = List[1][0]
                if Op in ['==','!=','+','*','|','||','^','&&','||','<<','>>']:
                    RR = [Op]
                    if (type(Expr0) is tuple)and(Expr0[0]==Op):
                        RR.extend(list(Expr0[1:]))
                    else:
                        RR.append(Expr0)
                    if (type(Expr1) is tuple)and(Expr1[0]==Op):
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
            elif (List[0][1]=='#')and(List[1][1]=='(')and(List[3][1]==')'):
                return get_expr(List[2])
                
                
                
        elif len(List)==5:
            if List[1][0]=='?':
                try:
                    return ['question',get_expr(List[0]),get_expr(List[2]),get_expr(List[4])]
                except:
                    return ['question',get_expr(List[0]),get_expr(List[2]),List[4]]
            if (List[0][0]=='[')and(List[2][0]==':'):
                Hi = get_expr(List[1])
                Lo = get_expr(List[3])
                return ['width',Hi,Lo]
        

        logs.log_err('bad get_expr %s %s %s'%(Item,len(List),List))
        traceback.print_stack(None,None,logs.Flogs[0])
        return 0

    if len(Item)==3:
            if Item[0]=='dig':
                return ['dig',Item[1],Item[2]]
            if Item[0]=='hex':
                return ['hex',Item[1],Item[2]]
            if Item[0]=='bin':
                return ['bin',Item[1],Item[2]]
    if len(Item)==4:
        if (Item[1]=='floating'):
            return float(Item[0])
        if Item[1]=='always':
            return Item[0]
    if (len(Item)==3)and(Item[0] in ['**','<<','>>','+','-','/','*','functioncall']):
        return Item
    if (len(Item)==4)and(Item[0] in ['question']):
        return Item
    if Item[0] == 'curly':
        return Item 
    if len(Item)==3:
        if Item[0] == 'subbus':
            return Item
        if Item[0] == 'subbit':
            return Item
        if Item[0] in MathOps:
            Expr0 = get_expr(Item[1])
            Expr1 = get_expr(Item[2])
            return [Item[0],Expr0,Expr1]
    logs.log_err('DB0: very bad expr %s %s'%(len(Item),str(Item)))
    traceback.print_stack()
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
                elif(len(LL)==2):
                    X = get_expr(LL[0])
                    Y = curly_list(LL[1])
                    return ['repeat',X,Y]
                else:
                    logs.log_err('curly got %s out of %s'%(Item,LL))
                    X='error'
                if (type(X) is list)and(len(X)==1)and (type(X[0])is list):
                    res.extend(X)
                else:
                    res.append(X)
            elif (Item[0]=='CurlyItems'):
                LL = DataBase[Item]
                while (len(LL)==3)and(LL[1][0]==','):
                    A = get_curly_items(LL[2])
                    LL = DataBase[LL[0]]
                    res = A + res
                more = get_curly_items(LL[0])
                res = more + res
            elif (Item[0]=='Expr'):
                X = get_expr(Item)
                res.append(X)
            else:
                logs.log_err('curly got %s'%(str(Item)))
                return []
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
MathOps = ('** ~^ !^ ~& !&  ~| !& + - * / ^ % & | && || ! ~ < > << >> >>> == <= >= != === !==').split()


def infoOf(Key):
    List = DataBase[Key]
    for X in List:
        if len(X)==4:
            return 'line=%s pos=%s'%(X[2],X[3])
    return 'location unknown'
    
usualDirs = ('input output inout wire reg logic signed unsigned genvar integer').split()
def notUsualDir(Dir):
    if Dir in  usualDirs: return False
    ww = Dir.split()
    goods = []
    for word in ww:
        if word not in usualDirs: 
            if goods==[]: goods=['wire']
            return ' '.join(goods),word
        else:
            goods.append(word)
            
    return False


def picklize():
    Fout = open('modules.pickle','w')
    pickle.dump(Modules,Fout)
    Fout.close()

def ensure(Cond,What):
    if Cond: return
    logs.log_err('ensure failed on %s'%str(What))

if __name__=='__main__':
    main()


