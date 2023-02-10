

# remove stupid code artifacts
import module_class
import fubarize
import logs

def help_main(Env):
    Mod = Env.Current
    stupidExpressions(Mod)
    stupidAssigns(Mod)
    removeUnused(Mod)
    Fout = open('%s.vcleaned' % Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()


def removeUnused(Mod):
    Used = []
    for Dst,Src,_,_ in Mod.hard_assigns:
        Sup = module_class.support_set(Src,False)
        for Net in Sup:
            if Net not in Used: Used.append(Net)
    for Head,Body,Alw in Mod.alwayses:
        Sup1 = module_class.support_set(Head,False)
        Sup2 = module_class.support_set(Body,False)
        for Net in Sup1+Sup2:
            if Net not in Used: Used.append(Net)
    for Body in Mod.generates:
        Sup = module_class.support_set(Body,False)
        for Net in Sup:
            if Net not in Used: Used.append(Net)
    Nets = list(Mod.nets.keys())
    for Net in Nets:
        if (Net not in Used)and not isExternal(Net,Mod):
            Mod.nets.pop(Net)
            logs.log_info('remove unused %s' % Net)


def stupidAssigns(Mod):
    fub = fubarize.fubarizeClass(Mod,False)
    fub.Translation = {}
    for Dst,Src,_,_ in Mod.hard_assigns:
        if simpleEnough(Dst,Mod) and simpleEnough(Src,Mod) and isOutput(Dst,Mod):
            fub.Translation[Src] = Dst
            logs.log_info('stupidAssign %s <= %s' % (Dst,Src))
    fub.renameDeep(True)
    ind = 0
    while ind < len(Mod.hard_assigns):
        Dst,Src,A,B = Mod.hard_assigns[ind]
        if Dst==Src:
            Mod.hard_assigns.pop(ind)
        else:
            ind += 1


def simpleEnough(Net,Mod):
    if (type(Net) is tuple) or (type(Net) is list):
        return False
    return True

def isOutput(Dst,Mod):
    if (type(Dst) is tuple) or (type(Dst) is list):
        if Dst[0] in ['subbus','subbit']:
            return isOutput(Dst[0],Mod)
        return False
    if Dst in Mod.nets:
        Dir,_ = Mod.nets[Dst]
        return 'output' in Dir
    return False
    
def isReg(Dst,Mod):
    if (type(Dst) is tuple) or (type(Dst) is list):
        if Dst[0] in ['subbus','subbit']:
            return isOutput(Dst[0],Mod)
        return False
    if Dst in Mod.nets:
        Dir,_ = Mod.nets[Dst]
        return 'reg' in Dir
    return False
    

def isExternal(Dst,Mod):
    if (type(Dst) is tuple) or (type(Dst) is list):
        if Dst[0] in ['subbus','subbit']:
            return isExternal(Dst[0],Mod)
        return False
    if Dst in Mod.nets:
        Dir,_ = Mod.nets[Dst]
        return ('output' in Dir)or('input' in Dir)or('inout' in Dir)
    return False

def do_always(Always):
    (Head,Body,Alw) = Always
    Head1 = cleanHead(Head)
    Body1 = cleanBody(Head1,Body)
    if (Head1 != '*')and(len(Head1)==3)and(Body1[0] == 'list')and(Body1[1][0] == 'ifelse'):
        Cond = Body1[1][1]
        if (Cond[0] == '!'):
            Rst = Cond[1]
            if (Head1[1][2] == Rst)and(Head1[1][1] == 'posedge'):
                Head1[1][1] = 'negedge'
            if (Head1[2][2] == Rst)and(Head1[2][1] == 'posedge'):
                Head1[2][1] = 'negedge'
    elif (Head1 != '*')and(len(Head1)==2)and(Body1[0] == 'list')and(Body1[1][0] == 'ifelse'):
        Cond = Body1[1][1]
        if (Cond[0] == '!'):
            Rst = Cond[1]
            if (Head1[0][2] == Rst)and(Head1[0][1] == 'posedge'):
                Head1[0][1] = 'negedge'
            if (Head1[1][2] == Rst)and(Head1[1][1] == 'posedge'):
                Head1[1][1] = 'negedge'

    return (Head1,Body1,Alw)

def stupidExpressions(Mod):
    for ind,(Dst,Src,A,B) in enumerate(Mod.hard_assigns):
        Src1 = cleanExpr(Src)
        Mod.hard_assigns[ind] = (Dst,Src1,A,B)

    for ind,(Head,Body,Alw) in enumerate(Mod.alwayses):
        Head1 = cleanHead(Head)
        Body1 = cleanBody(Head1,Body)
        if (Head1 != '*')and(len(Head1)==3)and(Body1[0] == 'list')and(Body1[1][0] == 'ifelse'):
            Cond = Body1[1][1]
            if (Cond[0] == '!'):
                Rst = Cond[1]
                if (Head1[1][2] == Rst)and(Head1[1][1] == 'posedge'):
                    Head[1][1] = 'negedge'
                if (Head1[2][2] == Rst)and(Head1[2][1] == 'posedge'):
                    Head[2][1] = 'negedge'

        Mod.alwayses[ind] = (Head1,Body1,Alw)

    for ind,Body in enumerate(Mod.generates):
        Body1 = cleanBody('*',Body)
        Mod.generates[ind] = Body1




        

def cleanBody(Kind,Body):
    if type(Body) is list:
        if (Body[0] == 'assigns'):
            Body1 = cleanBody(Kind,Body[1])
            return [Body[0],Body1]
        if (Body[0] == 'list'):
            Res = ['list']
            for Bd in Body[1:]:
                Res.append(cleanBody(Kind,Bd))
            return Res
        if (Body[0] == '<='):
            Src = cleanExpr(Body[2])
            if Kind == '*': 
                return ['=',Body[1],Src]
            else:
                return ['<=',Body[1],Src]

        if (Body[0] == '='):
            Src = cleanExpr(Body[2])
            if Kind == '*': 
                return ['=',Body[1],Src]
            else:
                return ['<=',Body[1],Src]
        if Body[0] == 'ifelse':            
            Cond = cleanExpr(Body[1])
            Yes = cleanBody(Kind,Body[2])
            No = cleanBody(Kind,Body[3])
            return ['ifelse',Cond,Yes,No]
        if Body[0] == 'if':            
            Cond = cleanExpr(Body[1])
            Yes = cleanBody(Kind,Body[2])
            return ['if',Cond,Yes]
        if Body[0] == 'case':            
            Cond = cleanExpr(Body[1])
            Res = []
            for Case in Body[2]:
                Key = Case[0]
                Bd = cleanBody(Kind,Case[1])
                Res.append([Key,Bd])
            return ['case',Cond,Res]
        if Body[0] == 'empty_begin_end':            
            return Body
        if Body[0] == 'for':            
            Body4 = cleanBody(Kind,Body[4])
            return [Body[0],Body[1],Body[2],Body[3],Body4]
        if Body[0] == 'instance':            
            return Body
        if Body[0] == 'always':            

            Body1 = do_always([Body[1],Body[2],'always'])
            Ret = ['always',Body1[0],Body1[1]]
            return  Ret


    logs.log_error('BODY %s' % str(Body))
    return Body

def cleanHead(Head):
    if (type(Head) is  list)and(Head[0] == 'list'):
        for Item in Head[1:]:
            if (type(Item) is list) and (Item[0] == 'edge'): return Head
    if (type(Head) is  list)and(Head[0][0] in ['edge']):
        return Head
    return '*'





def cleanExpr(Src):
    if (type(Src) is tuple) or (type(Src) is list):
        if Src[0] in ['subbit','subbus']:
            return Src
        if Src[0] == 'question':            
            if (Src[2] == ['bin','1','1'])and (Src[3] == ['bin','1','0']):
                return cleanExpr(Src[1])
            if (Src[2] == ['bin','1','0'])and (Src[3] == ['bin','1','1']):
                return ['!',cleanExpr(Src[1])]
            Cond = cleanExpr(Src[1])
            Yes = cleanExpr(Src[2])
            No = cleanExpr(Src[3])
            return ['question',Cond,Yes,No]

        if Src[0] == '==':            
            if (Src[2] == ['bin','1','1']):
                return Src[1]
            if (Src[2] == ['bin','1','0']):
                return ('!',Src[1])
        if Src[0] in ['bin','hex']:            
            return Src

        if Src[0] in ['&&','||','|','&','+','%','*','>','<','>=','<=','==','!=']:
            A = cleanExpr(Src[1])
            if len(Src) == 3:
                B = cleanExpr(Src[2])
                return [Src[0],A,B]
            else:
                return [Src[0],A]
        if Src[0] in ['!','~']:
            A = cleanExpr(Src[1])
            return [Src[0],A]
        if Src[0] == '-':
            A = cleanExpr(Src[1])
            if len(Src) == 3:
                B = cleanExpr(Src[2])
                return [Src[0],A,B]
            else:
                return [Src[0],A]
            
        if (Src[0] == 'curly')and(Src[1] == 'repeat'):            
            if (Src[3][0] == 'curly')and(Src[3][1][0]) == 'bin':
                return Src[3][1][2]
        if Src[0] == 'curly':
            return Src


        logs.log_error('cleanExpr treat %s %s' % (module_class.pr_expr(Src),Src))
        return Src
    else:
        return Src






