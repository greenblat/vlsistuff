#! /usr/bin/env python3

import os,sys
import importlib
def main():
    Fname = sys.argv[1]
    os.system('v2py %s -o tmp.py' % Fname)
    sys.path.append('.')
    That = importlib.import_module('tmp')
    RawModules = That.modules

    for Module in RawModules:
        checkAlways(RawModules[Module])
        checkAssigns(RawModules[Module])

def checkAssigns(Mod):
    Asss = Mod['assigns']
    for Ass in Asss:
        checkOneAss(Ass,Mod)

def checkOneAss(Ass,Mod):
    Dst =Ass[0] 
    Src =Ass[1] 
    Line = Ass[2]['line']
    WidS = exprWid(Dst,Mod,Line)
    WidD = exprWid(Src,Mod,Line)
    if WidS!=WidD:
        print('DIFF @%d:  WID (%d) <> (%d)' % (Line,WidD,WidS))

def exprWid(Expr,Mod,Line):
    if type(Expr) is int:
        X = bin(Expr)[2:]
        return len(X)
    if type(Expr) is str:
        if Expr in Mod['nets']:
            X = Mod['nets'][Expr]
            return X['width']
        else:
            print('error! @%d:  expr %s is not in nets' % (Line,Expr))
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
            return Aw+Bw
        if Expr[0] in ['+','-','&','|']:
            if len(Expr) == 3:
                Aw = exprWid(Expr[1],Mod,Line)
                Bw = exprWid(Expr[2],Mod,Line)
                return max(Aw,Bw)
            if (len(Expr) == 2):
                return 1
        if Expr[0] == 'repl':
            Times = xeval(Expr[1],Mod)
            What = Expr[2]
            Aw = exprWid(What,Mod,Line)
            Wid = Aw * Times
            return Wid
        if Expr[0] == 'bitsel':
            return 1
        if Expr[0] == 'partsel':
            Wid = xeval(Expr[2],Mod)-xeval(Expr[3],Mod)+1
            return Wid
        if Expr[0] == '?:':
            Aw = exprWid(Expr[1],Mod,Line)
            Bw = exprWid(Expr[2],Mod,Line)
            return max(Aw,Bw)
            
    print('exprWid @%d: error %s' % (Line,Expr))
    return 0

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
            print('error! line=%d alw not recognised %s' % (Line,Assign[0]))
#            print(Assign)
    return Dsts

def getBus(Dst):
    if type(Dst) is str: return Dst
    if type(Dst) is tuple:
        if Dst[0] == 'bitsel': return Dst[1]

    print('unrec error! %s fro getBus' % str(Dst))
    return 'False'

main()
