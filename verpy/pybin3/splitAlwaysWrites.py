
'''
 scan all <= edged alwayses and assign to each destination
   full list of condtiions it is written.
'''

import logs
import module_class
Assigns = {}
def help_main(Env):
    Mod = Env.Current
    Lnum = 1000
    for When,Body,_ in Mod.alwayses:
        if When != '*':
            analyzeBody(Body,[Lnum])
            Lnum += 1
    

    Fout = open('twos.vh','w')
    Fio = open('twos.io','w')
    for Key in Assigns:
#        logs.log_info('\n\nKEY %s:' % Key)
        Oks = []
        for Item in Assigns[Key]:
            Expr = module_class.pr_expr(Item)
            if Expr == 'rst_n':
                pass
            elif '!rst_n' in Expr:
                pass
            else:
                Oks.append(Expr)
        if len(Oks)>1:
            for ind,Ex0 in enumerate(Oks[:-1]):
                for Ex1 in Oks[ind+1:]:
                    Fout.write('assign check%d_%s = (%s) && (%s);\n' % (ind,Key,Ex0,Ex1))
                    Fio.write(' ,output check%d_%s\n' % (ind,Key))

    Fio.close()
    Fout.close()
    report9()

def analyzeBody(Body,Cond):
    if Body == []: return
    if Body[0] == 'list':
        for Item in Body[1:]:
            analyzeBody(Item,Cond)
    elif Body[0] == 'ifelse':
        Cond0 = Body[1]
        analyzeBody(Body[2],Cond+[Cond0])
        analyzeBody(Body[3],Cond+[('!',Cond0)])
    elif Body[0] == 'if':
        Cond0 = Body[1]
        analyzeBody(Body[2],Cond+[Cond0])
    elif Body[0] == 'empty_begin_end':
        return
    elif Body[0] == 'case':
        Key = Body[1]
        for (A,B) in Body[2]:
            analyzeBody(B,('==',Key,A))
    elif Body[0] == '<=':
        addAssign(Body[1],Cond)
    elif Body[0] == '=':
        logs.log_error('analyzeBody found "=" %s' % str(Body))
    else:
        logs.log_error('analyzeBody failed on "%s" ' % str(Body[0]))

def addAssign(Dst,Cond):
    Dst = simplify(Dst)
    Dst = module_class.hashit(Dst)
    if Dst not in Assigns:
        Assigns[Dst] = []
    Cond = simplify(Cond)
    if (type(Cond) == list):
        if(len(Cond)==2) and (Cond[0] == '!'):
            pass
        elif(len(Cond)>=2):
            Cond = ['&&']+Cond
    Assigns[Dst].append(Cond)



def report9():
    for Dst in Assigns:
        List = Assigns[Dst]
        List = cleanList(List)
        for Cond in List:
            Expr =  module_class.pr_expr(Cond)
            if type(Cond) is list:
                logs.log_info("<= %s %d  %s" % (Dst,len(Cond),Cond),'len')
            else:
                logs.log_info("<= %s %d  %s" % (Dst,len(Cond),Cond),'len')


def cleanList(List):
    Res = []
    for Cond in List:
        if type(Cond) is list:
            while '&&' in Cond:
                Cond.remove('&&')
        Res.append(Cond)
    Res = removeHead(Res)

    return Res

def removeHead(List):
    Cond0 = List[0]
    if Cond0 == []: return List
    if type(Cond0) is list:
        Head = Cond0[0]
    else:
        Head = Cond0
    Ok = True
    for Cond in List:
        if inverted(Head,Cond):
            pass
        elif Head not in Cond: Ok = False
        elif (Cond.index(Head) != 0): Ok =False
    if Ok:
        for ind,Cond in enumerate(List):
            if type(Cond) is list: 
                Cond.pop(0)
            else:
                Cond = []
            List[ind] = Cond
        List = removeHead(List)
    return List
        
def isgood(AA):
    if type(AA) is tuple: return True
    if type(AA) is list: return True

def inverted(AA,BB):
    if type(BB) is list: BB = BB[0]
    if isgood(AA)and(AA[0] in ['!','~']) and (len(AA) == 2): AA = AA[1]
    if isgood(BB)and(BB[0] in ['!','~']) and (len(BB) == 2): BB = BB[1]
    return AA==BB




def simplify(Expr):
    if type(Expr) is str: return Expr
    if type(Expr) is int: return Expr
    if type(Expr) is list:
        if len(Expr) == 1:
            return simplify(Expr[0])
        if len(Expr) == 0:
            return 0
        if Expr[0] == 'subbus':
            return Expr[1]
        if Expr[0] == 'subbit':
            return Expr[1]
        for ind,Item in enumerate(Expr):
            Expr[ind] = simplify(Item)
            
    if (type(Expr) is tuple)and(len(Expr)==2) and (Expr[0] == '!'):
        if type(Expr[1]) is list:
            if Expr[1][0] == '!':
                return simplify(Expr[1][1])

    return Expr


        
