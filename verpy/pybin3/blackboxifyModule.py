
import logs
import os,sys


def help_main(Env):
    Mod = False
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        Mod.new_assigns = []
        fixStuffs(Mod)
        prepare_assigns(Mod)
#        Fout = open('%s.tmp1' % Mod.Module,'w')
#        Mod.dump_verilog(Fout)
#        Fout.close()
        do_alwayses(Mod)
        do_assigns(Mod)
#        Fout = open('%s.tmp2' % Mod.Module,'w')
#        Mod.dump_verilog(Fout)
#        Fout.close()
        wrapUps(Mod)
    if not Mod:
        logs.log_error('none module was opened')

    if not os.path.exists('gutted'): os.mkdir('gutted')
    if not Mod:
        logs.log_error('none module was opened')
        sys.exit()

    Fout = open('gutted/%s.v' % Mod.Module,'w')
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        Mod.dump_verilog(Fout)
    Fout.close()
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        do_empty(Mod)
    Fout = open('gutted/%s_invents.py' % Mod.Module,'w')        
    Fout.write('INVENTIONS = {}\n')
    for Inv in INVENTIONS:
        Fout.write('INVENTIONS["%s"] = "%s"\n' % (Inv,INVENTIONS[Inv]))
    Fout.close()

def wrapUps(Mod):
    if Marker[0] == 0: return
    Mod.nets['markerarg'] = ['output',1]
    Mod.nets['marker_agregate'] = ['wire',1]
    Or = ['|']
    for ii in range(1,1+Marker[0]):
        Sig = 'markereg%d' % ii
        Or.append(Sig)
        
    Mod.hard_assigns.append(( 'marker_agregate',Or,'',''))

    Box = Mod.add_inst_conns('blkbox','marker_blkbox',[('a','marker_agregate'),('x','markerarg')])
    Box.params['WID'] = 1


def prepare_assigns(Mod):
    New = []
    for (Dst,Src,A,B) in Mod.hard_assigns:
        Src0 = reworkExpression(Mod,Src)
        New.append((Dst,Src0,'',''))

    Mod.hard_assigns = New
    Mod.hard_assigns.extend(Mod.new_assigns)
    Mod.new_assigns = []
        
        


def fixStuffs(Mod):
    ind = 0
    Hassigns = []
    while ind < len(Mod.hard_assigns):
        (Dst,Src,A,B) = Mod.hard_assigns[ind]
        if (type(Dst) is list) and (Dst[0] == 'curly') and (type(Src) is str):
            Mod.hard_assigns.pop(ind)
            LL = Dst[1:]
            LL.reverse()
            Low = 0
            for Item in LL:
                Wid = Mod.exprWidth(Item)
                if Wid == 1:
                    Hassign = (Item,['subbit',Src,Low],'','')
                else:
                    Hassign = (Item,['subbus',Src,(Wid-1+Low,Low)],'','')
                Low += Wid
                Hassigns.append(Hassign)
        else:
            ind += 1
    Mod.hard_assigns.extend(Hassigns)         


def do_alwayses(Mod):
    for When,Body,Alw in Mod.alwayses:
        Edges = getEdged(When)
        scanAlwaysBody(Mod,Edges,Body,0)

def getEdged(When):
    if When == '*': return []
    if type(When) is list:
        if When[0] == 'list':
            Res = []
            for Item in When[1:]:
                Sig = getEdged(Item)
                Res += Sig
            return Res
        if When[0] == 'edge':
            return [When[2]]
    return []




OPS = '+ curly == != || && > < >= | & ^ ! ~ question '.split()
OPS = '+ curly == != || && > < >= | & ^ question '.split()

SIMPLEASSIGNS = {}
INVENTIONS = {}
RESETS = 'rst_n can_rst_n sys_rst_n'.split()
def makeSimpleAssign(Mod,Edges,Expr):
    if str(Expr) in SIMPLEASSIGNS: return SIMPLEASSIGNS[str(Expr)]
    if type(Expr) is str: return Expr
    if type(Expr) is int: return Expr
    Exprs = str(Expr)
    if type(Expr) is list:
        if (len(Expr) == 2) and (Expr[0] == '!') and (Expr[1] in RESETS):
            return Expr
        if Expr[0] in ['subbit','subbus','bin','hex']: return Expr
        Wid = Mod.exprWidth(Expr)
        if Expr[0] == 'question':

            Expr[1] = makeSimpleAssign(Mod,Edges,Expr[1])
            Expr[2] = makeSimpleAssign(Mod,Edges,Expr[2])
            Expr[3] = makeSimpleAssign(Mod,Edges,Expr[3])
            New = getNewWire(Mod,Wid,Expr,'quest')
            Mod.hard_assigns.append((New,Expr,'',''))
            SIMPLEASSIGNS[Exprs] = New
            INVENTIONS[New] = Mod.pr_expr(Expr)
            return New
            
        if (Expr[0] in OPS)and not isInEdges(Expr,Edges):
            New = getNewWire(Mod,Wid,Expr,'ops')
            Mod.hard_assigns.append((New,Expr,'',''))
            SIMPLEASSIGNS[Exprs] = New
            INVENTIONS[New] = Mod.pr_expr(Expr)
            return New
    return Expr

def isInEdges(Expr,Edges):
    if len(Expr) == 2:
        if Expr[0] in ['!','~']:
            if Expr[1] in Edges:
                return True
    return False



Inventive = [0]
Marker = [0]
def getNewMarker(Mod):
    Marker[0] += 1
    Reg = 'markereg%s' % Marker[0]
    Mod.nets[Reg] = 'reg',1
    return Reg

def getNewWire(Mod,Wid,Expr,From):
    Inventive[0] += 1
    Wire = 'invented_%s_' % Inventive[0]
    if Wid>1:
        Mod.nets[Wire] = 'wire',(Wid-1,0)
    else:
        Mod.nets[Wire] = 'wire',1
    logs.log_info('INV %s %s %s expr=%s from=%s' % (Mod.Module,Wire,Wid,Expr,From))
    return Wire
    
def addCatch(Body,Mod):
    if Body[0] == 'list':
        Q = getNewMarker(Mod)
        Body.append( ('<=',Q,['!',Q]) )

def scanAlwaysBody(Mod,Edges,Body,Depth):
    if Body[0] == 'ifelse':
        Body[1] = makeSimpleAssign(Mod,Edges,Body[1])
        scanAlwaysBody(Mod,Edges,Body[2],Depth+1)
        if (len(Edges)==1) or (Depth>0):
            addCatch(Body[2],Mod)
        scanAlwaysBody(Mod,Edges,Body[3],Depth+1)
        addCatch(Body[3],Mod)
    elif Body[0] == 'if':
        Body[1] = makeSimpleAssign(Mod,Edges,Body[1])
        scanAlwaysBody(Mod,Edges,Body[2],Depth+1)
        addCatch(Body[2],Mod)
    elif Body[0] == 'case':
        Cond = Body[1]
        List = Body[2]
        for ind,Item in enumerate(List):
            scanAlwaysBody(Mod,Edges,Item[1],Depth+1)
            addCatch(Item[1],Mod)
    elif Body[0] == '<=':
        Body[2] = makeSimpleAssign(Mod,Edges,Body[2])
    elif Body[0] == '=':
        Body[2] = makeSimpleAssign(Mod,Edges,Body[2])
    elif Body[0] == 'list':
        for Item in Body[1:]:
            scanAlwaysBody(Mod,Edges,Item,Depth)
    else:
        print("SCAN got %s" % Body[0])

def do_assigns(Mod):
    ind = 0
    while ind<len(Mod.hard_assigns):
        (Dst,Src,A,B) = Mod.hard_assigns[ind]
        if not isLiteral(Src):
#            Src0 = reworkExpression(Mod,Src)
            Newout = extoutput(Dst,Src,Mod)
            if Newout:
                Mod.hard_assigns[ind] = (Newout,Src,A,B)
                ind += 1
            else:
                Mod.hard_assigns.pop(ind)
        else:
            ind += 1

OPERANDS = '* curly >> << >= + - & && ^ | || question <= == < != > ! ~'.split()
DOUBLES = '<= >> * + - | || == != > < ?? << >= & && ^'

def reworkExpression(Mod,Expr):
    Exprs = str(Expr)
    if Exprs in SIMPLEASSIGNS: return SIMPLEASSIGNS[Exprs]
    if type(Expr) is str: return Expr
    if type(Expr) is int: return Expr
    if type(Expr) is list:
        if (len(Expr) == 2) and (Expr[0] == '!') and (Expr[1] in RESETS):
            return Expr
        if Expr[0] in ['subbit','subbus','bin','hex','dig']: return Expr
        Wid = Mod.exprWidth(Expr)

        Expr = flattenExpr(Expr,Mod)

#        print("EXPR",len(Expr),Expr)
        if (Expr[0] in DOUBLES) and (len(Expr) >= 3):
            Res = [Expr[0]]
            for Item in Expr[1:]:
                AA = reworkExpression(Mod,Item)
                Res.append(AA)
            return reworkFinal(Mod,Res)
        elif Expr[0] == 'question':
            A = reworkExpression(Mod,Expr[1])
            B = reworkExpression(Mod,Expr[2])
            C = reworkExpression(Mod,Expr[3])
            return reworkFinal(Mod,[Expr[0],A,B,C])
#        elif (len(Expr) == 2) and (Expr[0] in ['^','!','~','|']):
        elif (len(Expr) == 2) and (Expr[0] in ['^','|','&']):
            A = reworkExpression(Mod,Expr[1])
            return reworkFinal(Mod,[Expr[0],A])
        elif (len(Expr) == 2) and (Expr[0] in ['~','!']):
            A = reworkExpression(Mod,Expr[1])
            return [Expr[0],A]
        elif Expr[0] == 'functioncall':
            return Expr
        elif Expr[0] in ['curly']:
            return Expr
    logs.log_error('reworkExpression got "%s"' % str(Expr))
    return Expr
   
DOUBLESFLAT = '* + - | || & && ^'
def flattenExpr(Expr,Mod):
    if type(Expr) is not list: return Expr
    if Expr[0] not in DOUBLESFLAT: return Expr
    Ok = True
    while Ok:
        Len = len(Expr)
        Res = [ Expr[0] ]
        if Expr[0] in DOUBLESFLAT:
            for Item in Expr[1:]:
                if (type(Item) is list) and (Item[0] == Expr[0]):
                    Res.extend(Item[1:])
                else:
                    Res.append(Item)
        Ok = len(Res)>Len
        Expr = Res[:]
    return Res 



def reworkFinal(Mod,Expr):
    Wid = Mod.exprWidth(Expr)
    New = getNewWire(Mod,Wid,Expr,'final')
    SIMPLEASSIGNS[str(Expr)] = New
    INVENTIONS[New] = Mod.pr_expr(Expr)
    Mod.new_assigns.append((New,Expr,'',''))
    return New


def isLiteral(Src):
    if type(Src) is int: return True
    if type(Src) is list:
        if Src[0] in ['bin','hex','dec']: return True
        if Src[0] in ['subbus','subbit','functioncall']: return False
        if Src[0] in OPERANDS: return False
    if type(Src) is str: return False

    logs.log_error("isLiteral got %s" % str(Src))
    return False

def extoutput(Dst,Src,Mod):
    Bus = getBus(Dst)
    if type(Bus) is not str:
        logs.log_error('extoutput got "%s", must be string' % Mod.pr_expr(Bus))
        return 'ERROR'
    if Bus not in Mod.nets:
        Dir,Wid = 'wire',1
        logs.log_warning('net %s was not defined' % Bus)
    else:
        Dir,Wid = Mod.nets[Bus]
    if type(Src) is str:
        Box = Mod.add_inst_conns('blkbox',Bus+'_blkbox',[('a',Src),('x',Dst)])
        Bits = extractWidth(Wid,Mod)
        Box.params['WID'] = Bits
        return False
    else:        
        Bus2 = 'outx_'+Bus
        Out = outx(Dst)
        Box = Mod.add_inst_conns('blkbox',Bus+'_blkbox',[('a',Out),('x',Dst)])
        Bits = extractWidth(Wid,Mod)
        Box.params['WID'] = Bits
        Mod.nets[Bus2] = 'wire',Wid
        return Out

def extractWidth(Wid,Mod):
    if Wid == 0: return 1
    if type(Wid) is int: return Wid
    if type(Wid) is tuple:
        if Wid[1] == 0: 
            if type(Wid[0]) is int:
                return Wid[0]+1
            X = Mod.pr_expr(Wid[0])
            return "%s+1" % X
            

    logs.log_error('extractWidth got "%s"' % str(Wid))
    return 1


def newinput(Dst,Mod):
    Bus = getBus(Dst)
    Dir,Wid = Mod.nets[Bus]
    Mod.nets[Bus] = 'input',Wid

def getBus(Dst):
    if type(Dst) is str: return Dst
    if (type(Dst) is  list) or (type(Dst) is  tuple):
        return Dst[1]

    logs.log_error('getBus got %s' % str(Dst))
    return 'xxx'

def outx(Dst):
    if type(Dst) is str: return 'outx_'+Dst
    if (type(Dst) is  list) or (type(Dst) is  tuple):
        return [Dst[0],'outx_'+Dst[1],Dst[2]]

    logs.log_error('getOUTX got %s' % str(Dst))
    return 'xxx'




def do_empty(Mod):
    hard_assigns = Mod.hard_assigns
    alwayses = Mod.alwayses
    insts = Mod.insts
    localparams = Mod.localparams

    Mod.hard_assigns = []
    Mod.alwayses = []

    Mod.localparams = {}
    Mod.insts = {}

    Nets = list(Mod.nets.keys())
    for Net in Nets:
        Dir,_ = Mod.nets[Net]
        if ('input' not in Dir) and ('output' not in Dir): Mod.nets.pop(Net)
    if not os.path.exists('blackboxes'): os.mkdir('blackboxes')
    Fout = open('blackboxes/%s.blkbox' % Mod.Module,'w')
    Fout.write('(* blackbox *)\n')
    Mod.dump_verilog(Fout)
    Fout.close()
    Mod.alwayses = alwayses
    Mod.hard_assigns = hard_assigns
    Mod.insts = insts
    Mod.localparams = localparams



