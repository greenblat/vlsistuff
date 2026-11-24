#! /usr/bin/env python3

import os,sys
import importlib
import traceback
WorkingOn = '?'
def main():
    global WorkingOn
    Fname = sys.argv[1]
    os.system('v2py %s -o tmp.py' % Fname)
    sys.path.append('.')
    That = importlib.import_module('tmp')
    RawModules = That.modules

    for Module in RawModules:
        WorkingOn = Module
        checkAlways(RawModules[Module])
        checkAssigns(RawModules[Module])
        checkNotUsed(RawModules[Module])

def checkNotUsed(Mod):
    Inputs,Prmused = getAllInputs(Mod)
    Params = list(Mod['parameters'].keys())+list(Mod['localparams'].keys())
    Inputs += Params
    Outputs = getAllOutputs(Mod)
    Asss = Mod['assigns']
    Used = Prmused
    Driven = []
    for Ass in Asss:
        Used += getSupportSet(Ass[1],Mod)
        Driven += getSupportSet(Ass[0],Mod)

    for Alw in Mod['always']:
        When = Alw['when']
        Code = Alw['code']
        Driven1,Used1 = scanAlwaysSupport(Code,Mod)
        Used2 = getSupportSet(When,Mod)
        Used += Used1 + Used2
        Driven += Driven1
    Conns = []
    for Inst in Mod['instances']:
        Son = Mod['instances'][Inst]
        Connsx = Son['conns']
        for Pin in Connsx:
            Sig = getSupportSet(Connsx[Pin],Mod)
            Conns.extend(Sig)
    for Inp in Inputs:
        if (Inp not in Used)and(Inp not in Conns):
            print('ERROR %s: %s input not in used' % (WorkingOn,Inp))
    for Out in Outputs:
        if (Out not in Driven) and (Out not in Conns):
            print('ERROR %s: %s output not in driven' % (WorkingOn,Out))
    for Net in Used:
        if (Net not in Driven) and (Net not in Inputs)and(Net not in Conns):
            print('ERROR %s: %s used but not in driven' % (WorkingOn,Net))
    for Net in Driven:
        if (Net not in Outputs) and (Net not in Used)and(Net not in Conns):
            print('ERROR %s: %s driven but not in used' % (WorkingOn,Net))

def scanAlwaysSupport(Code,Mod):
    if type(Code) is str: return [Code],[Code]
    if type(Code) is int: return [],[]
#    if Code==[]: return [],[]
    if type(Code) is list:
        if len(Code) == 0:
            return [],[]
        if len(Code) == 1:
            return scanAlwaysSupport(Code[0],Mod)
        D,U = [],[]
        for Item in Code:
            D0,U0 = scanAlwaysSupport(Item,Mod)
            D += D0
            U += U0
        return D,U
    if type(Code) is tuple:
        if Code[0] == 'if':
            U0 = getSupportSet(Code[1],Mod)
            D1,U1 = scanAlwaysSupport(Code[2],Mod)
            if len(Code[3])>0: 
                D2,U2 = scanAlwaysSupport(Code[3],Mod)
                D1 += D2
                U1 += U2
            return D1,U0+U1
        if Code[0] in ['=','<=']:
            D0 = getSupportSet(Code[1],Mod)
            U0 = getSupportSet(Code[2],Mod)
#            traceback.print_stack()
            return D0,U0
        if Code[0] == 'for':
            Dx0 = getSupportSet(Code[1],Mod)
            Dx1 = getSupportSet(Code[2],Mod)
            Dx2 = getSupportSet(Code[3],Mod)
            D0,U0 = scanAlwaysSupport(Code[4],Mod)
            return D0+Dx0+Dx1+Dx2,U0
        if Code[0] == 'case':
            U0 = getSupportSet(Code[2],Mod)
            D0 = []
            for _,CC in Code[3]:
                Dx,Ux = scanAlwaysSupport(CC,Mod)
                D0 += Dx
                U0 += Ux
            return D0,U0
        print("ERROR! scanAlwaysSupport %s" % str(Code))
        return [],[]
    print("ERROR! scanAlwaysSupport %s" % str(Code))
    return [],[]





def getSupportSet(Expr,Mod):
    if Expr == None:
        return []
        
    if Expr == '*': return []        
    if type(Expr) is int: return []
    if type(Expr) is str: return [Expr]
    if type(Expr) is list:
        LL = []
        for Item in Expr:
            L0 = getSupportSet(Item,Mod)
            LL += L0
        return LL
    if type(Expr) is tuple:
        if Expr[0] == '=': 
            A0 = getSupportSet(Expr[1],Mod)
            A1 = getSupportSet(Expr[2],Mod)
            return A1
        if Expr[0] == 'fill': return []
        if Expr[0] in ['posedge','negedge']:
            return [Expr[1]]
        if Expr[0] == 'const': return []
        if (Expr[0] in ['%','!==','<<','>>','!=','>=','<=','!','~','+','-','==','<','>','|','||','&','&&','^']):
            Sup = []
            for Item in Expr[1:]:
                Sup += getSupportSet(Item,Mod)
            return Sup
        if (Expr[0] == 'partsel'): return [Expr[1]]
        if (Expr[0] == 'bitsel'): return [Expr[1]]
        if (Expr[0] == 'repl'): 
            return getSupportSet(Expr[2],Mod)
        if (Expr[0] == 'concat'): 
            LL = []
            for Item in Expr[1:]:
                LL += getSupportSet(Item,Mod)
            return LL
                
        if (Expr[0] == '*'): 
            A = getSupportSet(Expr[1],Mod)
            B = getSupportSet(Expr[2],Mod)
            return A+B

        if (Expr[0] == '?:'): 
            A = getSupportSet(Expr[1],Mod)
            B = getSupportSet(Expr[2],Mod)
            C = getSupportSet(Expr[3],Mod)
            return A+B+C
        if (Expr[0] == 'member'): 
            return [Expr[1]]

        print("ERROR0! EXPR '%s'" % str(Expr))
    print("ERROR! EXPR '%s'" % str(Expr))
    return []

def getAllInputs(Mod):
    Res = []
    Used = []
    for Net in Mod['nets']:
        if 'packed' in Mod['nets'][Net]:
            Packed = Mod['nets'][Net]['packed']
            if len(Packed) == 1:
                Hi,Lo = Packed[0]
                Set = getSupportSet(Hi,Mod)
                Used.extend(Set)

        Dir = Mod['nets'][Net]['dir']
        if Dir == 'input':
            Res.append(Net)

    return Res,Used

def getAllOutputs(Mod):
    Res = []
    for Net in Mod['nets']:
        Dir = Mod['nets'][Net]['dir']
        if Dir == 'output':
            Res.append(Net)
    return Res

def checkAssigns(Mod):
    Asss = Mod['assigns']
    for Ass in Asss:
        checkOneAss(Ass,Mod)

def checkOneAss(Ass,Mod):
    Dst =Ass[0] 
    Src =Ass[1] 
    Line = Ass[2]['line']
    WidD = exprWid(Dst,Mod,Line)
    WidS = exprWid(Src,Mod,Line)
    if WidS!=WidD:
        if type(WidS) is str:
            if WidS.startswith('INT'):
                X = int(WidS[3:])
                if X>WidD:
                    print('ERROR 0  DIFF @%d:  WID dst=(%d) <> src=(%s)' % (Line,WidD,WidS))
        elif (WidD<WidS):
            print('ERROR BAD DIFF %s@%d:  WID dst=(%d) <> src=(%d)' % (WorkingOn,Line,WidD,WidS))
        else:
            print('ERROR DIFF @%d:  WID dst=(%d) <> src=(%d)' % (Line,WidD,WidS))

def exprWid(Expr,Mod,Line):
    if type(Expr) is int:
        X = bin(Expr)[2:]
        return 'INT%d' % len(X)
    if type(Expr) is str:
        if Expr in Mod['nets']:
            X = Mod['nets'][Expr]
            return X['width']
        elif Expr in Mod['localparams']:
            return 32
        elif Expr in Mod['parameters']:
            return 32
        else:
            print('ERROR! @%d:  expr %s is not in nets' % (Line,Expr))
            return 1
    if type(Expr) is tuple:
        if Expr[0] == 'const':
            if Expr[1] != None:
                return Expr[1]
            return exprWid(Expr[4],Mod,Line)
        if Expr[0] == 'concat':
            res = 0
            for Item in Expr[1:]:
                Now = exprWid(Item,Mod,Line)
                res += Now
            return res
        if Expr[0] in ['<<', '>>']:
            Aw = exprWid(Expr[1],Mod,Line)
            return Aw
        if Expr[0] in ['==','!=','!','&&','||','>','<','<=','>=','!==']:
            return 1
        if Expr[0] in ['~']:
            Aw = exprWid(Expr[1],Mod,Line)
            return Aw
        if Expr[0] in ['*']:
            Aw = exprWid(Expr[1],Mod,Line)
            Bw = exprWid(Expr[2],Mod,Line)
            return resolveInt(Aw)+resolveInt(Bw)
        if Expr[0] in ['+','-','&','|']:
            if len(Expr) == 3:
                Aw = exprWid(Expr[1],Mod,Line)
                Bw = exprWid(Expr[2],Mod,Line)
                return strmax(Aw,Bw,Line)
            if (len(Expr) == 2):
                return 1
        if Expr[0] == 'repl':
            Times = xeval(Expr[1],Mod)
            What = Expr[2]
            Aw = exprWid(What,Mod,Line)
            Wid = Aw * Times
            return Wid
        if Expr[0] == 'bitsel':
            Net = Expr[1]
            LL = Mod['nets'][Net]
            if 'packed' in LL:
                Pack = LL['packed']
                if len(Pack) == 2:
                    Wid = Pack[1][0]-Pack[1][1]+1
                    return Wid
            return 1
        if Expr[0] == 'partsel':
            Wid = xeval(Expr[2],Mod)-xeval(Expr[3],Mod)+1
            return Wid
        if Expr[0] == '?:':
            Aw = exprWid(Expr[2],Mod,Line)
            Bw = exprWid(Expr[3],Mod,Line)
            return strmax(Aw,Bw,Line)
            
    print('exprWid %s@%d: ERROR %s' % (WorkingOn,Line,Expr))
    return 0
def resolveInt(Aw):
    if type(Aw) is int: return Aw
    if (type(Aw) is str) and Aw.startswith('INT'):
        Aw = int(Aw[3:])
    return Aw
def strmax(Aw,Bw,Line):
    if (type(Aw) is int) and (type(Bw) is int):
        return max(Aw,Bw)
    if (type(Aw) is str) and (type(Bw) is str):
        Aw = resolveInt(Aw)
        Bw = resolveInt(Bw)
        Max =  max(Aw,Bw)
        return "INT%d" % Max
    if (type(Aw) is str) and Aw.startswith('INT'):
        Aw = int(Aw[3:])
        if Aw>Bw:
            print('STRMAX ERROR %s@%d  bw=%d aw=%d' % (WorkingOn,Line,Bw,Aw))
        return max(Aw,Bw)
    if (type(Bw) is str) and Bw.startswith('INT'):
        Bw = int(Bw[3:])
        if Bw>Aw:
            print('STRMAX ERRORb %s@%d bw=%d aw=%d' % (WorkingOn,Line,Bw,Aw))
    return max(Aw,Bw)


def xeval(Expr,Mod):
    if type(Expr) is int: return Expr
    if Expr in Mod['parameters']:
        Exp = Mod['parameters'][Expr]
        if 'eval' in Exp: return Exp['eval']
        Val = computeVal(Mod,Mod['parameters'][Expr])
        return xeval(Val,Mod)
    if Expr in Mod['localparams']:
        if 'eval' in Expr: return Expr['eval']
        Val = computeVal(Mod,Mod['localparams'][Expr])
        return xeval(Val,Mod)
    if type(Expr) is tuple:
        if Expr[0] == '-':
            A = xeval(Expr[1],Mod)
            B = xeval(Expr[2],Mod)
            return A-B
        if Expr[0] == '+':
            A = xeval(Expr[1],Mod)
            B = xeval(Expr[2],Mod)
            return A+B
    print("ERROR! xeval of %s" % str(Expr))
    return 0

def computeVal(Mod,Expr):
    if 'eval' in Expr:
        return Expr['value'][1]
    print('computeVal',Expr)
    return 1
    
def checkAlways(Mod):
    Alws = Mod['always']
    for Alw in Alws:
        checkOneAlw(Alw)

def checkOneAlw(Alw):
    when = Alw['when']
    if len(when) == 2:
        Code = Alw['code']
        Line = Alw['line']
        checkAlwCode(Line,Code)

def checkAlwCode(Line,Code):
    Top = Code[0]
    if Top[0] != 'if': 
        print('line %s: TOP ALW is not if',Line)
        return
    Rsts = getDsts(Line,Top[2])
    Driven = getDsts(Line,Top[3])
    Driven = list(set(Driven))
    checkMissings(Line,Rsts,Driven)

def checkMissings(Line,Rsts,Driven):
    for Rst in Rsts:
        if Rst not in Driven:
            print('ERROR! @%d: rst=%s not in driven %s' % (Line,Rst,Driven))
    for Drv in Driven:
        if Drv not in Rsts:
            print('ERROR! @%d: dst=%s not in resets=%s' % (Line,Drv,Rsts))


def getDsts(Line,Code):
    Dsts = []
    for Assign in Code:
        if Assign[0] == '<=':
            Dst = getBus(Assign[1])
            Dsts.append(Dst)
        elif Assign[0] == 'if':
            More0 = getDsts(Line,Assign[2])
            Dsts.extend(More0)
            if len(Assign) == 4:
                More1 = getDsts(Line,Assign[3])
                Dsts.extend(More1)
        elif Assign[0] == 'for':
                More1 = getDsts(Line,Assign[4])
                Dsts.extend(More1)
        elif Assign[0] == 'case':
            for (_,Cd) in Assign[3]:
                More = getDsts(Line,Cd)
                Dsts.extend(More)
        else:
            print('ERROR! line=%d alw not recognised %s' % (Line,Assign[0]))
#            print(Assign)
    return Dsts

def getBus(Dst):
    if type(Dst) is str: return Dst
    if type(Dst) is tuple:
        if Dst[0] == 'bitsel': return Dst[1]

    print('unrec ERROR! %s fro getBus' % str(Dst))
    return 'False'

main()
