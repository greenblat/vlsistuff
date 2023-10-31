


import logs

def help_main(Env):
    Mod = Env.Current
    for Dst,Src,_,_ in Mod.hard_assigns:
        if (type(Dst) is list) and (Dst[0] == 'curly'):
            printout(Dst,Src,'dst',Mod)
        if (type(Src) is list) and (Src[0] == 'curly'):
            printout(Src,Dst,'src',Mod)

    for When,Body,_ in Mod.alwayses:
        scanBody(Body,Mod)

def scanBody(Body,Mod):
    if Body[0] in ['<=','=']:
        Dst = Body[1] 
        Src = Body[2] 
        if (type(Dst) is list) and (Dst[0] == 'curly'):
            printout(Dst,Src,'dst',Mod)
        if (type(Src) is list) and (Src[0] == 'curly'):
            printout(Src,Dst,'src',Mod)
    elif Body[0] == 'list':
        for Item in Body[1:]:
            scanBody(Item,Mod)
    elif Body[0] == 'ifelse':
        scanBody(Body[2],Mod)
        scanBody(Body[3],Mod)
    elif Body[0] == 'if':
        scanBody(Body[2],Mod)
    elif Body[0] == 'case':
        LL = Body[2]
        for Lx in LL:
            scanBody(Lx[1],Mod)
    else: 
        logs.log_error("scanBody %s" % Body[0])



def printout(Expr,Other,Which,Mod):
    Pos = 0
    LL = Expr[1:]
    LL.reverse()
    Res = []
    for Item in LL:
        Wid = Mod.exprWidth(Item)
        Pitem = Mod.pr_expr(Item)
        Res.append((Pitem,Wid,Pos+Wid-1,Pos))
        Pos += Wid
    logs.log_info("%s:  %s = " % (Which,Other))
    for X in Res:
        logs.log_info("           %s "%(str(X)))
        

