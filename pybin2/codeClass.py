
import string

class codeClass:
    def __init__(self):
        self.Globals = []
        self.Functions = {}
        self.Current = []
        self.Function = ''
        self.cmp = False
#        self.Fout = open('code.preasm','w')

    def dump(self,Fname):
        self.Fout = open(Fname,'w')
        for Line in self.Globals:
            self.Fout.write('%s\n'%Line)
        for Func in self.Functions:
            self.Fout.write('label %s\n'%Func)
            for Line in self.Functions[Func]:
                self.Fout.write('%s\n'%Line)
            self.Fout.write('\n')
        

    def optimizes(self):
        self.optimizeConstants(self.Globals)
        for Func in self.Functions:
            List = self.Functions[Func]
            self.optimizeBranches(List)
            self.optimizeBranches2(List)
            self.optimizeBranches3(List)
            self.optimizeIfThenElse(List)
            self.optmizeSexts(List)
            self.optimizeConstants(List)
        
    def assignRegs(self):
        for Func in self.Functions:
            List = self.Functions[Func]
            for ind,Line in enumerate(List):
                print('ILIA',Line)





    def defineConstant(self,Vars):
        if Vars[1]=='i32':
            self.Globals.append('int %s = %s'%(Vars[0][1:],Vars[2]))
        elif Vars[1]=='float':
            self.Globals.append('float %s = %s'%(Vars[0][1:],Vars[2]))
        else:            
            self.Globals.append('CONSTANT '+str(Vars))

    def defineGlobal(self,Vars):
        if Vars[1]=='i32':
            self.Globals.append('int %s = %s'%(Vars[0][1:],Vars[2]))
        elif Vars[1]=='float':
            self.Globals.append('float %s = %s'%(Vars[0][1:],Vars[2]))
        else:
            self.Globals.append(str(Vars))

    def defineCommonGlobal(self,Vars):
        self.defineGlobal(Vars)

    def defineCode(self,Code):
        self.Current.append(Code)

    def defineArray(self,Vars):
        self.Globals.append('%s %s[%s]'%(Vars[2],Vars[0][1:],Vars[1]))

    def defineOpenFunction(self,Vars):
        self.Function = Vars[1][1:]
        self.Current = []

    def defineCloseFunction(self):
        self.Functions[self.Function] = self.Current[:]

    def defineCall1Assign(self,Vars):
        if Vars[2]=='@setup':
            if Vars[1]=='i32':
                self.Current.append('    XV%s = setup( %s )'%(Vars[0][1:],Vars[4]))
            else:
                print('ERROR defineCall1Assign ',Vars)
                
        elif Vars[2]=='@xFloat':
                self.Current.append('    FV%s = float( XV%s )'%(Vars[0][1:],Vars[4][1:]))
        else:
            print('ERROR defineCall1Assign ',Vars)
    def defineCall2(self,Vars):
        if Vars[1]=='@wr_setup':
            Src = Vars[5]
            if Src[0]=='%':
                self.Current.append('    setup( %s ) = XV%s'%(Vars[3],Vars[5][1:]))
            else:
                self.Current.append('    setup( %s ) = XV%s'%(Vars[3],Vars[5]))
        else:
            print('ERROR Call2 %s'%str(Vars))

    def defineStore(self,Vars):
        if Vars[0]=='float':
            self.Current.append('    %s = %s'%(mem(Vars[3]),varf(Vars[1])))
        elif Vars[0]=='i32':
            self.Current.append('    %s = %s'%(mem(Vars[3]),varx(Vars[1])))
        else:
            print('ERROR defineStore ',Vars)
    def defineLoad(self,Vars):
        if Vars[1]=='float':
            self.Current.append('    FV%s = %s'%(Vars[0][1:],mem(Vars[3])))
        elif Vars[1]=='i32':
            self.Current.append('    XV%s = %s'%(Vars[0][1:],mem(Vars[3])))
        else:
            print('ERROR defineLoad ',Vars)
    def defineBiop(self,Op,Vars):
        self.Current.append('// %s %s'%(Op,Vars))
        if Op in ['fmul','fsub','fadd','fdiv']:
            self.Current.append('    FV%s = FV%s %s %s'%(Vars[0][1:],Vars[2][1:],opsx(Op),varf(Vars[3])))
        elif Op in ['add','and','sub']:
            if (len(Vars)==5):
                self.Current.append('    XV%s = XV%s %s  %s'%(Vars[0][1:],Vars[3][1:],opsx(Op),Vars[4]))
            else:
                self.Current.append('    XV%s = XV%s %s  %s'%(Vars[0][1:],Vars[2][1:],opsx(Op),varx(Vars[3])))
        elif Op in ['sext']:
            self.Current.append('    XV%s = XV%s'%(Vars[0][1:],Vars[2][1:]))
        else:
            print('ERROR defineBiop ',Op,Vars)
    def defineIcmp(self,Vars):
        self.cmp = Vars
    def defineFcmp(self,Vars):
        self.cmp = Vars
    def defineBranchCond(self,Vars):
        if self.cmp[2]=='i32':
            Str = '    if ( XV%s %s %s ) goto label%s else label%s'%(self.cmp[3][1:],self.cmp[1],varx(self.cmp[4]),Vars[1][1:],Vars[2][1:])
            self.Current.append(Str)
        elif (self.cmp[2]=='float'):
            self.Current.append('    if ( FV%s %s %s ) goto label%s else label%s'%(self.cmp[3][1:],self.cmp[1],varf(self.cmp[4]),Vars[1][1:],Vars[2][1:]))

        self.cmp = False
    def defineFetch(self,Vars):
        if Vars[2]=='float':
            self.Current.append('    XV%s = @%s + XV%s'%(Vars[0][1:],Vars[5][1:],Vars[9][1:]))
        else:
            self.Current.append('    XV%s = @%s + XV%s'%(Vars[0][1:],Vars[5][1:],Vars[9][1:]))
    def declares(self,Vars):
        return

    def optimizeConstants(self,List):
        Ind = 0
        while Ind < len(List):
            This = List[Ind]
            wrds = string.split(This)
            dones = False
            for xx,wrd in enumerate(wrds):
                wrdx = replaceConstant(wrd,wrds[0])
                if (wrds[xx] != wrdx): dones = True
                wrds[xx] = wrdx
            if (dones):
                List[Ind] = '    '+string.join(wrds,' ')
            Ind += 1

    def optmizeSexts(self,List):
        Ind = 0
        while Ind < len(List):
            This = List[Ind]
            if '//' in This:
                This = This[:This.index('//')]
            wrds = string.split(This)
            if wrds==[]: 
                List.pop(Ind)
            else:
                Ind += 1

        Ind = 0
        while Ind < (len(List)-1):
            This = List[Ind]
            Next = List[Ind+1]
            wrdsT = string.split(This)
            wrdsN = string.split(Next)
            if (wrdsT[0] == wrdsN[-1])and(wrdsT[1]=='=')and(wrdsN[1]=='=')and(len(wrdsN)==3)and('XV' in wrdsN[0])and('XV' in wrdsT[0]):
                List.pop(Ind+1)
                wrdsT[0]=wrdsN[0]
                List[Ind]= '    '+string.join(wrdsT,' ')
            else:
                Ind += 1


    def optimizeBranches(self,List):
        Ind = 0
        while Ind < (len(List)-1):
            This = List[Ind]
            Next = List[Ind+1]
            wrdsT = string.split(This)
            wrdsN = string.split(Next)
            if (wrdsT[0] == 'branch')and(wrdsN[0] == 'label')and(wrdsT[1]==wrdsN[1]):
                List.pop(Ind)
            elif ('sleep()' in This)and('branch ' in Next):
                List.pop(Ind+1)
            else:
                Ind += 1
            
    def optimizeBranches2(self,List):
        Ind = 0
        Sleeps = []
        while Ind < (len(List)-1):
            This = List[Ind]
            Next = List[Ind+1]
            wrdsT = string.split(This)
            wrdsN = string.split(Next)
            if (wrdsT[0]=='label')and(wrdsN[0]=='sleep()'):
                Sleeps.append(wrdsT[1])
            Ind += 1

        Ind = 0
        while Ind < len(List):
            This = List[Ind]
            wrdsT = string.split(This)
            if (wrdsT[0]=='branch')and(wrdsT[1] in Sleeps):
                List[Ind]='    sleep()'
            Ind += 1


    def optimizeBranches3(self,List):
        Defined = []
        Used = []
        for Line in List:
            wrds = string.split(Line)
            if wrds[0]=='label': Defined.append(wrds[1])
            else:
                for wrd in wrds:
                    if ('label' in wrd)and(wrd.index('label')==0)and(wrd not in Used):
                        Used.append(wrd)

        Defs = set(Defined)            
        Useds = set(Used)            
        Notused = Defs-Useds
#        print('not used',Notused)
        
        ind = 0
        while ind<len(List):
            Line  = List[ind]
            wrds = string.split(Line)
            if (wrds[0]=='label')and(wrds[1] in Notused):
                List.pop(ind)
            else:
                ind += 1

    def optimizeIfThenElse(self,List):
        Ind = 0
        while Ind < (len(List)-1):
            This = List[Ind]
            Next = List[Ind+1]
            wrdsT = string.split(This)
            wrdsN = string.split(Next)
            if (wrdsT[0]=='if')and(wrdsN[0]=='label'):
                Gind = wrdsT.index('goto')
                Goto = wrdsT[Gind+1]
                if wrdsN[1]==Goto:
                    List.pop(Ind+1)
                    LL = wrdsT[:3]+[inverted(wrdsT[3])]+wrdsT[4:7]+[wrdsT[9]]
                    List[Ind]='    '+string.join(LL,' ')
            Ind += 1           




def inverted(Txt):
    if Txt == 'eq': return '!='
    if Txt == 'ogt': return '>'
    if Txt == 'olt': return '<'
    if Txt == 'slt': return '<'
    if Txt == 'sgt': return '>'
    if Txt == 'ne': return '=='
    return '!'+Txt


def varx(Txt):
    if Txt[0] in '0123456789': return Txt
    return 'XV'+Txt[1:]
def varf(Txt):
    if Txt[0] in '0123456789': return Txt
    return 'FV'+Txt[1:]

def mem(Txt):
    if Txt[0] == '%':
        return 'mem[ XV%s ]'%Txt[1:]
    if Txt[0] == '@':
        return Txt[1:]
    print('ERROR mem %s'%Txt)
    return Txt

def opsx(Op):
    if Op == 'fmul': return '*'
    if Op == 'fsub': return '-'
    if Op == 'fadd': return '+'
    if Op == 'fdiv': return '/'
    if Op == 'add': return '+'
    if Op == 'and': return '&'
    if Op == 'sub': return '-'
    if Op == 'mul': return '*'
    if Op == 'div': return '/'
    return 'ERROR'+Op

def replaceConstant(Txt,First):
    if (Txt=='0.000000e+00'): return '0.0'
    if '00000e+00' in Txt: return string.replace(Txt,'00000e+00','')
    if (len(Txt) == 18)and(Txt[:2]=='0x')and(First=='float'):
        X = eval(Txt)
        return '%f'%binary2float(X)
    return Txt



def binary2float(Float):
    if Float<0: return 0
    if Float==0: return 0
    Bin = bin(Float)[2:]
    if len(Bin)<64:
        Bin = (64-len(Bin))*'0'+Bin
    Sign = int(Bin[0],2)
    Exps = Bin[1:12]
    Exp0  = int(Exps,2)
    Exp  = Exp0-1023
    Mant = 1.0*int('1'+Bin[12:],2)
    Shift  = Exp-52

    if Shift>0:
        Int = Mant* (1<<Shift)
    else:
        Int = Mant/(1<< -Shift)
    if Sign:
        Int = -Int
    return Int



