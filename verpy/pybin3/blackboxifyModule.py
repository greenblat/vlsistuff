
import logs


def help_main(Env):
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        do_assigns(Mod)
    Fout = open('gutted/%s.v' % Mod.Module,'w')
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        Mod.dump_verilog(Fout)
    Fout.close()
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        do_empty(Mod)

def do_assigns(Mod):
    for ind,(Dst,Src,A,B) in enumerate(Mod.hard_assigns):
        if not isLiteral(Src):
            Newout = extoutput(Dst,Mod)
            Mod.hard_assigns[ind] = (Newout,Src,A,B)
OPERANDS = '* curly >> << >= + - & && ^ | || question == < != > ! ~'.split()

def isLiteral(Src):
    if type(Src) is int: return True
    if type(Src) is list:
        if Src[0] in ['bin','hex','dec']: return True
        if Src[0] in ['subbus','subbit']: return False
        if Src[0] in OPERANDS: return False
    if type(Src) is str: return False

    logs.log_error("isLiteral got %s" % str(Src))
    return False

def extoutput(Dst,Mod):
    Bus = getBus(Dst)
    Dir,Wid = Mod.nets[Bus]
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
    Fout = open('blackboxes/%s.blkbox' % Mod.Module,'w')
    Fout.write('(* blackbox *)\n')
    Mod.dump_verilog(Fout)
    Fout.close()
    Mod.alwayses = alwayses
    Mod.hard_assigns = hard_assigns
    Mod.insts = insts
    Mod.localparams = localparams



