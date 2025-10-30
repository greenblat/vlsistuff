
import logs

def help_main(Env):
    Mod = Env.Current
    Mod.nets_wires = {}
    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        Mod.hard_assigns[ind] = (Dst,Src,'',[('ADLY','ADLY')])

    Mod.localparams['ADLY'] = 1
    Gens = []
    for ind,(Kind,Body,Alw)  in enumerate(Mod.alwayses):
        if not edged(Kind):
#            Body2 = scanBody2(Body)
            if Body[0] == 'list':
                Body.insert(1,['#','ADLY'])
            else:
                print("BODY",Body)
            print("XBX",Body)
            Mod.alwayses[ind] = ('*',Body,Alw)
        elif edged(Kind):
            Body2 = scanBody0(Body)
            if Body2[0] == 'list':
                Body2.insert(1,['#','ADLY'])
            else:
                Body2 = ['list',['#','ADLY'],Body2]

            LL = ['list']
            Body3 = ['list']
            while Pairs != []:
                A,B = Pairs.pop(0)
                addDefines(A,B,Mod)
                LL.append(['<=',A,B])
                Body3.append(['=',B,A])
            if (Body3!=[]) and (Body2[0] == 'list'):
                Body2 = ['list'] + Body3[1:] + Body2[1:]
            else:
                Body2 = ['list',Body3,Body2]
            Mod.alwayses[ind] = ('*',Body2,'always')
    
            Gens.append((removeRst(Kind),LL,'always')) 

    Mod.alwayses.extend(Gens)
    for Net in Mod.nets_wires:
        Mod.nets[Net] = Mod.nets_wires[Net]
    Initials = ['list']
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'reg' in Dir:
            Initials.append(['=',Net,0])
    if len(Initials)>1:
        Mod.initials = [Initials]           


    Fout = open('%s.dlyv' % Mod.Module,'w')
    Fout.write(' `timescale 1ns / 1ps\n')
    Mod.dump_verilog(Fout)
    Fout.close()
        
def scanBody2(Body):
    if type(Body) is list:
        if Body[0] == '=':
            Body2 = ['=',Body[1],Body[2],['#','ADLY']]
            return Body2

        if Body[0] == 'list':
            Res = ['list']
            for Item in Body[1:]:
                Item2 = scanBody2(Item)
                Res.append(Item2)
            return Res

        if Body[0] == 'if':
            B2 = scanBody2(Body[2])
            return [Body[0],Body[1],B2]

        if Body[0] == 'ifelse':
            B2 = scanBody2(Body[2])
            B3 = scanBody2(Body[3])
            return [Body[0],Body[1],B2,B3]

        logs.log_error("BAD2 LIST %s " %(str(Body)))
        return Body

    logs.log_error("MISSING2 %s" % (str(Body)))
    return Body


def addDefines(Reg,Sig,Mod):
    if type(Reg) is str:
        Dir,Wid = Mod.nets[Reg]
        Mod.nets_wires[Sig] = 'reg',Wid
        return
    
    if type(Reg) is list:
        if Reg[0] in ['subbit','subbus']:
            Bus = Reg[1]
            Dir,Wid = Mod.nets[Bus]
            Mod.nets_wires[Sig[1]] = 'reg',Wid
            return
        if Reg[0] == 'curly':
            return

    logs.log_error('in %s ADD DEFINES %s %s' % (Mod.Module,Reg,Sig))

def scanBody(Body):
    if type(Body) is tuple:
        if Body[0] == '<=':
            Body2 = [Body[0],Body[1],Body[2],['#', 'ADLY']]
            return Body2
            
    if type(Body) is list:
        if Body[0] == '<=':
            Body2 = [Body[0],Body[1],Body[2],['#', 'ADLY']]
            return Body2

        if Body[0] == 'list':
            Res = ['list']
            for Item in Body[1:]:
                Item2 = scanBody(Item)
                Res.append(Item2)
            return Res

        if Body[0] == 'if':
            B2 = scanBody(Body[2])
            return [Body[0],Body[1],B2]

        if Body[0] == 'ifelse':
            B2 = scanBody(Body[2])
            B3 = scanBody(Body[3])
            return [Body[0],Body[1],B2,B3]

        if Body[0] == 'case':
            Res = Body[:2]
            Work = []
            Cases = Body[2]
            for Case in Cases:
                Cond = Case[0]
                Do = Case[1]
                Do2 = scanBody(Do)
                Work.append([Cond,Do2])

            Res = [ Body[0],Body[1],Work]
            return Res

        logs.log_error("BAD LIST %s" % str(Body))
        return Body

    logs.log_error("MISSING %s" % str(Body))
    return Body

def wirify(Dst):
    if type(Dst) is str: return 'wire_%s' % Dst
    if type(Dst) is list:
        Dstres = Dst[:]
        if Dst[0] == 'subbit': 
            Dstres[1] = 'wire_%s' % Dst[1]
            return Dstres
        if Dst[0] == 'subbus': 
            Dstres[1] = 'wire_%s' % Dst[1]
            return Dstres
        if Dst[0] == 'curly': 
            Res = ['curly']
            for Item in Dst[1:]:
                Item2 = wirify(Item)
                Res.append(Item2)
            return Res
    logs.log_error('wirify failed on %s' % str(Dst))


Pairs = []
Useds = []
def scanBody0(Body):
    if type(Body) is list:
        if Body[0] == '<=':
            Wired = wirify(Body[1])
            Body2 = ['=',Wired,Body[2]]
            if str(Body[1]) not in Useds:
                Pairs.append((Body[1],Wired))
                Useds.append(str(Body[1]))
            return Body2

        if Body[0] == 'list':
            Res = ['list']
            for Item in Body[1:]:
                Item2 = scanBody0(Item)
                Res.append(Item2)
            return Res

        if Body[0] == 'if':
            B2 = scanBody0(Body[2])
            return [Body[0],Body[1],B2]

        if Body[0] == 'ifelse':
            B2 = scanBody0(Body[2])
            B3 = scanBody0(Body[3])
            return [Body[0],Body[1],B2,B3]

        if Body[0] == 'case':
            Res = Body[:2]
            Work = []
            Cases = Body[2]
            for Case in Cases:
                Cond = Case[0]
                Do = Case[1]
                Do2 = scanBody0(Do)
                Work.append([Cond,Do2])

            Res = [ Body[0],Body[1],Work]
            return Res
        if Body[0] == 'empty_begin_end':
            return Body

        logs.log_error("BAD LIST %s " %(str(Body)))
        return Body

    logs.log_error("MISSING %s" % (str(Body)))
    return Body

def removeRst(Kind):
    if Kind[0] == 'list':
        return Kind[1]
    return Kind

def edged(Kind):
    if Kind[0] == 'list':
        return edged(Kind[1])
    if Kind[0] == '*': return False
    if Kind[0] == 'edge': return True
    logs.log_error("EDGE %s" % (str(Kind)))
    return False


