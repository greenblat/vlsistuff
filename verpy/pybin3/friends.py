
import sys,os
import logs
import module_class

import rtl_width
Msgs = {}
def help_main(Env):
    Mod = Env.Current
    Lines = readDefFile(Mod.Module)
    Friend = module_class.module_class('%s_friend' % Mod.Module)
    if not os.path.exists('holder'):
        os.mkdir('holder')
    Flist = open('holder/%s.list' % Mod.Module,'w')
    Dones = []
    for wrds in Lines:
        if '->' in wrds:
            for wrd in wrds:
                if wrd[0] in '!~':
                    wrd = wrd[1:]
                if wrd in Mod.nets:
                    Dir,Wid = Mod.nets[wrd]
                    Friend.nets[wrd] = 'input',Wid
                    if wrd not in Dones:
                        Flist.write('%s\n' % wrd)
                        Dones.append(wrd)
        else:
            logs.log_error('wrds %s' % str(wrds))
    Clock = 'clk'
    for wrds in Lines:
        if '->' in wrds:
            Ind = wrds.index('->')
            Expr0 = wrds[:Ind]
            Action = wrds[Ind+1]
            if Action in ['clock','reset']: 
                if Action == 'clock':
                    Clock = buildExpr(Expr0,Friend,Clock)
                    Obj = Friend.add_inst('clock_mon','')
                    Obj.conns['din'] = Clock
                    Obj.params['WHO'] = '"'+Clock+'"'

            else:
                Expr = buildExpr(Expr0,Friend,Clock)
                Obj = Friend.add_inst(Action,'')
                Obj.conns['din'] = Expr
                Wid = computeWidth(Expr,Mod,Friend)
                Obj.conns['clk'] = Clock
                More = wrds[Ind+2:]
                who = '"'+''.join(Expr0)+'"'
                who = getPair(More,'who',who)
                if who[0] != '"': who = '"'+who+'"'
                Obj.params['WHO'] =  who
                if Wid>1: Obj.params['WID'] =  Wid

    for Net in Mod.nets:
        if Net.startswith('panic'):
            buildPanic(Net,Clock,Mod,Friend,Mod.nets[Net][1],Flist)
        

    Fout = open('holder/%s_friend.v' % Mod.Module,'w')
    Friend.dump_verilog(Fout)
    Fout.close()
    Flist.close()

def buildPanic(Net,Clock,Mod,Friend,Widx,Flist):
    Obj = Friend.add_inst('panic_button','')
    Obj.conns['din'] = Net
    Obj.conns['clk'] = Clock
    Obj.params['WHO'] = '"'+Net+'"'
    Wid = computeWidth(Net,Mod)
    if (Wid>1):
        Obj.params['WID'] = Wid
    
    Friend.nets[Net] = 'input',Widx
    Flist.write('%s\n' % Net)
def getPair(wrds,Key,Def):
    for wrd in wrds:
        if wrd.startswith(Key+'='):
            ind = wrd.index('=')
            val = wrd[ind+1:]
            return val
    return Def

def buildExpr(Expr0,Mod,Clock):
    for Ind,Wrd in enumerate(Expr0):
        if (Wrd[0] == '$')and(Expr0[Ind+1] == '('):
            Tail = Expr0[Ind:]
            Func = Tail[: Tail.index(')')+1]
            Funcx = buildFunction(Func,Mod,Clock)
            if Ind == 0:
                Head = []
            else:
                Head = Expr0[:Ind]
            Expr1 = Head + [Funcx] + Expr0[Ind+len(Func):]
            return buildExpr(Expr1,Mod,Clock)
    return ' '.join(Expr0)

def buildFunction(Func,Mod,Clock):
    if Func[0] == '$bus_range':
        if len(Func)<6:
            logs.log_error('FUNC %s should have four params' % (str(Func)))
            Name = 'error_'+inventNet(Mod)
            return Name
        Till = Func[-2]
        From = Func[-4]
        Expr0 = Func[2:-5]
        Expr = buildExpr(Expr0,Mod,Clock)
        Obj = Mod.add_inst(Func[0][1:],'')
        Obj.conns['clk'] = Clock
        Obj.conns['din'] = Expr
        Obj.conns['from'] = From
        Obj.conns['till'] = Till
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        Wid = computeWidth(Expr0,Mod)
        if Wid>1:
            Obj.params['WID'] = Wid
        return Name
    if Func[0] == '$clocks':
        From = my_eval(Func[2])
        Till = my_eval(Func[4])
        Obj = Mod.add_inst('clocks_range','')
        Obj.conns['clk'] = Clock
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        return Name
    if Func[0] == '$time':
        From = my_eval(Func[2])
        Till = my_eval(Func[4])
        Obj = Mod.add_inst('time_range','')
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        return Name

    if Func[0] in ['$rising','$falling']:
        Expr0 = Func[2:-1]
        Expr = buildExpr(Expr0,Mod,Clock)
        Obj = Mod.add_inst(Func[0][1:],'')
        Obj.conns['clk'] = Clock
        Obj.conns['din'] = Expr
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        return Name
        
    if Func[0] in ['$constant','$duration']:
        if len(Func)<6:
            logs.log_error('FUNC %s should have four params' % (str(Func)))
            Name = 'error_'+inventNet(Mod)
            return Name
        Till = Func[-2]
        From = Func[-4]
        Expr0 = Func[2:-5]
        Expr = buildExpr(Expr0,Mod,Clock)
        Obj = Mod.add_inst(Func[0][1:],'')
        Obj.conns['clk'] = Clock
        Obj.conns['din'] = Expr
        Obj.conns['from'] = From
        Obj.conns['till'] = Till
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        Wid = computeWidth(Expr0,Mod)
        if Wid>1:
            Obj.params['WID'] = Wid
        return Name
    if Func[0] in ['$unknown']:
        Expr0 = Func[2:-1]
        Expr = buildExpr(Expr0,Mod,Clock)
        Obj = Mod.add_inst(Func[0][1:],'')
        Obj.conns['clk'] = Clock
        Obj.conns['din'] = Expr
        Name = inventNet(Mod)
        Obj.conns['dout'] = Name
        Wid = computeWidth(Expr0,Mod)
        if Wid>1:
            Obj.params['WID'] = Wid
        return Name

    if Func[0] in ['$condition']:
       ind = Func.index(',')
       Cond = Func[2:ind]
       What = Func[ind+1:-1]
        
       Expr = buildExpr(Cond,Mod,Clock)
       Expr2 = buildExpr(What,Mod,Clock)
       Wid = computeWidth(Expr2,Mod)
       Obj = Mod.add_inst('condition','')
       Obj.conns['clk'] = Clock
       Obj.conns['en'] = Expr
       Obj.conns['din'] = Expr2
       Name = inventNet(Mod)
       Obj.conns['dout'] = Name
       Mod.nets[Name] = 'wire',(Wid-1,0)
       Obj.params['WID'] = Wid
       return Name

    if Func[0] in ['$becoming_x']:
        List = Func[2:-1]+[',']
        Names = []
        while ',' in List:
            Ind = List.index(',')
            Head = List[: Ind]
            List = List[Ind+1:]
            Expr = buildExpr(Head,Mod,Clock)
            Obj = Mod.add_inst('becoming_x','')
            Obj.conns['clk'] = Clock
            Obj.conns['din'] = Expr
            Wid = computeWidth(Head,Mod)
            Name = inventNet(Mod)
            Obj.conns['dout'] = Name
            if Wid>1:
                Obj.params['WID'] = Wid
            Names.append(Name)
            Msgs[Obj.Name] = ''.join(Func)

        Name = inventNet(Mod)
        if len(Names):
            Mod.hard_assigns.append((Name,Names[0],'',''))
        else:
            Mod.hard_assigns.append((Name,['||']+Names,'',''))
        return Name

    logs.log_error("Unknown function %s" % str(Func))
    return 'aaa'

def computeWidth(Head,Mod,Mod2=False):
    if (type(Head) is list) and (len(Head)==1):
        return computeWidth(Head[0],Mod)
    if (type(Head) is str) and (Head in Mod.nets):
        _,Wid = Mod.nets[Head]
        if type(Wid) is int: return Wid
        if type(Wid) is str: return eval(Wid)
        if type(Wid) is tuple:
            if type(Wid[0]) is int:
                Wid = my_eval(Wid[0]) - my_eval(Wid[1]) + 1
                return Wid

    if (type(Head) is str) and (Head in Mod2.nets):
        return computeWidth(Head,Mod2)
    if type(Head) is list:
        Expr = makeExpression(Head)
        if Expr[0] in ['==','!=','<','>','||','&&']: return 1
        return computeWidth(Expr,Mod)

    logs.log_error('failed wid on %s ' % str(Head))
    return 1

def makeExpression(Head):
    if type(Head) is str: return Head
    if len(Head)==1: return makeExpression(Head[0])
    if len(Head)>=3:
        if Head[1] in ['==','!=','<','>','||','&&','|','&','+','-']: 
            Bef = makeExpression(Head[0])
            Aft = makeExpression(Head[1])
            return ((Head[1],Bef,Aft))
    logs.log_error('makeExpression got "%s"' % ' '.join(Head))
    return Head


def my_eval(Txt):
    if type(Txt) is int: return Txt
    return eval(Txt)

def inventNet(Mod):
    Name = 'net_%d'%Mod.inventedNets
    Mod.inventedNets += 1
    Mod.nets[Name] = 'wire',0
    return Name



def readDefFile(Module):
    Fname = 'friends.txt'
    result = []
    Params = sys.argv
    if '-friend' in Params:
        Ind = Params.index('-friend')
        Fname = Params[Ind+1]
    if not os.path.exists(Fname):
        logs.log_error('FATAL %s file cannot be opened. check or add -friend <FILENAME>' % Fname)
        sys.exit()

    File = open(Fname)
    Lines = File.readlines()
    state = 'idle'
    for line in Lines:
        for Chr in '[]():;,':
            line = line.replace(Chr,' %s ' % Chr)
        wrds = line.split()
        if wrds==[]:
            pass
        elif state=='idle':
            if wrds[0] == Module: state = 'work'
        elif state=='work':
            if (len(wrds)==2) and (wrds[1] == ':'): return result
            result.append(wrds)
    return result
