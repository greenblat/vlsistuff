

'''
 look for wire[7:0] ABC = PREV+1;
 and make module that turns number of state into string.
'''


def help_main(Env):
    Mod = Env.Current
    List0 = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if (Dir == 'wire') and( Wid == (7,0)) and allCapital(Net):
            List0.append(Net)
    Dic0 = {}
    for (Dst,Src,_,_)  in Mod.hard_assigns:
        if Dst in List0:
            if type(Src) is int:
                Dic0[Dst] = Src
            elif type(Src) is str:
                Dic0[Dst] = Src,0
            elif (type(Src) is list) and (Src[0] == '+'):
                if Src[1] in List0:
                    Dic0[Dst] = Src[1],Src[2]
    rounds(Dic0)
    Wides = {}
    for Dst in Dic0:
        Base,Ind = splitBaseIndex(Dst)
        if Ind>=0:
            if Base not in Wides: Wides[Base] = []
            Wides[Base].append(Ind)
            Wides[Base].sort()
            Wides[Base].reverse()
    for Base in Wides:
        LL = Wides[Base]
        Start = Dic0[Base+str(LL[0])]
        if type(Start) is not int:
            print('ERROR bases=%s ll=%s start=%s' % (Base,LL,Start))
        for X in range(LL[0],LL[-1]-1,-1):
            New = Base+str(X)
            if (New in Dic0):
                if Dic0[New] != Start:
                    print('ERROR %s %s %s' % (New,Dic0[New],Start))
            Dic0[New] = Start
            Start += 1
    Fout = open('%s_states.v' % Mod.Module,'w')
    Fout.write('module %s_states ( input [7:0] State);\nreg [127:0] Str;\n' % Mod.Module)
    Fout.write('always @* begin\n    Str = 0;\n')
    List2 = []
    for Dst in Dic0:
        List2.append((Dic0[Dst],Dst))
    List2.sort()
    Else = ''
    for Val,Dst in List2:
        Fout.write('    %s if (State == %s) Str = "%s";\n' % (Else,Val,Dst))
        Else = 'else'
    Fout.write('end\nendmodule\n')
    Fout.close()


def splitBaseIndex(Dst):
    if Dst[-1] in string.digits:
        for X in range(len(Dst)):
            if Dst[X] in string.digits:
                Base = Dst[:X]
                Ind = int(Dst[X:])
                return Base,Ind
    else:
        return Dst,-1



def round(Dic0):
    dones = 0
    for Dst in Dic0:
        if type(Dic0[Dst]) is tuple:
            Var,Add = Dic0[Dst]
            if type(Dic0[Var]) is  int:
                Dic0[Dst] = Dic0[Var]+Add
                dones += 1
    return dones

def rounds(Dic0):
    Dones = 1
    while Dones>0:
        Dones = round(Dic0)
            
        



import string
def allCapital(Net):
    if Net[0] not in string.ascii_uppercase: return False
    for Chr in Net[1:]:
        if Chr not in (string.ascii_uppercase+string.digits): return False
    return True
            
