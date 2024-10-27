
import os,sys
import logs
import importlib
import module_class
INPS = []
OUTS = []

MENTIONED = []
DRIVEN = []
LOOKED = []

def help_main(Env):
    Mod = Env.Current
    computeParams(Mod)
    gatherIoBits(Mod)
    gatherParams(Mod)
    gatherInstMentioned(Mod)
    gatherAssignMentioned(Mod)
    gatherAlwaysMentioned(Mod)
    unusedPins(Mod)
    drivenReport(Mod)
    mentionedReport(Mod)

def computeParams(Mod):
    Mod.params = {}
    for Prm in Mod.parameters:
        Mod.params[Prm] = initialX(Mod.parameters[Prm])
    for Prm in Mod.localparams:
        Mod.params[Prm] = initialX(Mod.localparams[Prm])

    Keys = list(Mod.params.keys())
    for Prm in Keys:
        Val = Mod.params[Prm]
        if type(Val) is not int:
            Vals = module_class.pr_expr(Val)
            try:
                X = eval(Vals,Mod.params)
                Mod.params[Prm] = X
            except:
                pass
    if "__builtins__" in Mod.params.keys():
        Mod.params.pop("__builtins__")
    
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if ((type(Wid) is list) or (type(Wid) is tuple)) and (len(Wid) == 2):
            Hi_s = module_class.pr_expr(Wid[0])
            Hi = eval(Hi_s,Mod.params)

            Lo_s = module_class.pr_expr(Wid[1])
            Lo = eval(Lo_s,Mod.params)
            Mod.nets[Net] = Dir,(Hi,Lo)



def initialX(Val):
    if type(Val) is int: return Val
    if type(Val) is str:
        try:
            return eval(Val)
        except:
            return Val
    return Val


def gatherParams(Mod):
    for Prm in Mod.localparams:
        DRIVEN.append(Prm)
    for Prm in Mod.parameters:
        DRIVEN.append(Prm)

def drivenReport(Mod):
    for Sig in LOOKED+OUTS:
        if Sig not in DRIVEN+INPS:
            logs.log_error('%s: not driven %s' % (Mod.Module,Sig))
            logs.keep_error('%s: not driven %s' % (Mod.Module,Sig))




def mentionedReport(Mod):
    for Bit in MENTIONED:
        if Bit in INPS: INPS.remove(Bit)
        if Bit in OUTS: OUTS.remove(Bit)
    if len(INPS)==0: 
        logs.log_info('%s: mentioned CORRECT' % Mod.Module)
    else:
        logs.log_error('%s: LEFTOVERS %s %s' % (Mod.Module,len(INPS),INPS))
        logs.keep_error('%s: LEFTOVERS %s %s' % (Mod.Module,len(INPS),INPS))

def gatherAlwaysMentioned(Mod):
    for Cond,Alw,_ in Mod.alwayses:
        Sig1 = actuals(Cond)
        Used = gatherAlways(Alw,Mod)
        for Item in Used+Sig1:
            Bits = clean0(Mod.explodeBus(Item,'xxx'))
            for Bit in Bits:
                if (Bit not in MENTIONED):
                    MENTIONED.append(Bit)


def gatherAlways(Alw,Mod):
        if type(Alw) is list:
            if Alw[0] in ['=','<=']:
                Sig1 = actuals(Alw[1])
                addToDriven(Sig1,Mod)
                Sig2 = actuals(Alw[2])
                addToLooked(Sig1,Mod)
                return Sig1+Sig2
            elif Alw[0] == 'list':
                Res = []
                for Item in Alw[1:]:
                    More = gatherAlways(Item,Mod)
                    Res.extend(More)
                return Res
            elif Alw[0] in ['if','ifelse']:
                Res = actuals(Alw[1])
                addToLooked(Res,Mod)
                for Item in Alw[2:]:
                    More = gatherAlways(Item,Mod)
                    Res.extend(More)
                return Res
            elif Alw[0] == 'case':
                Res = actuals(Alw[1])
                addToLooked(Res,Mod)
                for _,Item in Alw[2]:
                    More = gatherAlways(Item,Mod)
                    Res.extend(More)
                return Res
            elif Alw[0] == 'empty_begin_end':
                return []
            elif Alw[0] == 'functioncall':
                if (Alw[1] == '$display'): 
                    return []
                else:
                    logs.log_error('functioncall got %s' % (str(Alws)))
                
        if type(Alw) is str:
            addToLooked([Alw],Mod)
            return [Alw]
                
        logs.log_error('gatherAlways got "%s"' % str(Alw))
        return []
                
def addToLooked(List,Mod):
    for Item in List:
        Bits = clean0(Mod.explodeBus(Item,'xxx'))
        for Bit in Bits:
            if (Bit not in LOOKED):
                LOOKED.append(Bit)

def addToDriven(List,Mod):
    for Item in List:
        Bits = clean0(Mod.explodeBus(Item,'xxx'))
        for Bit in Bits:
            if (Bit not in DRIVEN):
                DRIVEN.append(Bit)

def gatherAssignMentioned(Mod):
    for Dst,Src,_,_ in Mod.hard_assigns:
        Sig1 = actuals(Dst)
        Sig2 = actuals(Src)
        for Item in Sig1:
            Bits = clean0(Mod.explodeBus(Item,'xxx'))
            for Bit in Bits:
                if (Bit not in MENTIONED):
                    MENTIONED.append(Bit)
                if (Bit not in DRIVEN):
                    DRIVEN.append(Bit)

        for Item in Sig2:
            Bits = clean0(Mod.explodeBus(Item,'xxx'))
            for Bit in Bits:
                if (Bit not in MENTIONED):
                    MENTIONED.append(Bit)
                if (Bit not in LOOKED):
                    LOOKED.append(Bit)
        

HOLDS = {}
sys.path.append('arcs')
def is_input(Pin,Module):
    if Module in HOLDS:
        return Pin in HOLDS[Module].INPUTS
    elif os.path.exists('arcs/%s.py' % Module):
        X = importlib.import_module(Module)
        HOLDS[Module] = X.hld
        return is_input(Pin,Module)
    else:
        logs.log_error('missing arcs file for %s' % Module)
        return False

def is_output(Pin,Module):
    if Module in HOLDS:
        return Pin in HOLDS[Module].OUTPUTS
    elif os.path.exists('arcs/%s.py' % Module):
        X = importlib.import_module(Module)
        HOLDS[Module] = X.hld
        return is_output(Pin,Module)
    else:
        logs.log_error('missing arcs file for %s' % Module)
        return False




def unusedPins(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Pins = list(Obj.conns.keys())
        for In in HOLDS[Obj.Type].INPUTS:
            if In in Pins:
                Pins.remove(In)
            else:
                logs.log_error('INPUT PIN %s of %s is not connected in %s %s' % (In,Obj.Type,Inst,Mod.Module))

        for Ou in HOLDS[Obj.Type].OUTPUTS:
            if Ou in Pins:
                Pins.remove(Ou)
            else:
                logs.log_error('OUTPUT PIN %s of %s is not connected in %s %s' % (Ou,Obj.Type,Inst,Mod.Module))

        if Pins!=[]:
            logs.log_error('EXTRA %s %s %s CONNS %s' % (Inst,Obj.Type,Mod.Module,Pins))






def gatherInstMentioned(Mod):
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig1 = actuals(Sig)
            for Item in Sig1:
                Bits = clean0(Mod.explodeBus(Item,Pin))
                for Bit in Bits:
                    if (Bit not in MENTIONED):
                        MENTIONED.append(Bit)
                    if is_input(Pin,Obj.Type):
                        if Bit not in LOOKED: LOOKED.append(Bit)
                    if is_output(Pin,Obj.Type):
                        if Bit not in DRIVEN: DRIVEN.append(Bit)

def actuals(Sig):
    if type(Sig) is str: return [Sig]
    if type(Sig) is int: return []
    if not Sig: return []
    if type(Sig) is list:
        if (Sig==[]): return []
        if (Sig[0] == 'edge'): return [Sig[2]]
        if (Sig[0] == 'functioncall'):
            Res = []
            for Item in Sig[2]:
                More = actuals(Item)
                Res.extend(More)
            return Res
            
        if (Sig[0] == 'list'):
            Res = []
            for Item in Sig[1:]:
                More = actuals(Item)
                Res.extend(More)
            return Res
        if (Sig[0] == 'bin'): return []
        if (Sig[0] == 'dig'): return []
        if (Sig[0] == 'hex'): return []
        if (Sig[0] in ['subbit','subbus']): return [Sig]
        if Sig[0] in ['<<','>>','~&','~^','^','~','/','*','+','-','>=','<=','>','!','question','<','|','&','==','!=','||','&&']:
            Res = []
            for Item in Sig[1:]:
                More = actuals(Item)
                Res.extend(More)
            return Res
        if Sig[0] == 'curly':
            Res = []
            for Item in Sig[1:]:
                if (Item != 'repeat'):
                    More = actuals(Item)
                    Res.extend(More)
            return Res
            
    logs.log_error("ACTUALS got %s %s" % (Sig,type(Sig)))
    return []
        


def gatherIoBits(Mod):
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'input' in Dir:
            Bits = clean0(Mod.explodeBus(Net,'xxx'))
            INPS.extend(Bits)
        elif 'output' in Dir:
            Bits = clean0(Mod.explodeBus(Net,'xxx'))
            OUTS.extend(Bits)


def clean0(LL):
    res = []
    for (Bit,_) in LL: res.append(Bit)
    return res
