import os,sys,string
import veri

New = os.path.expanduser('~/verification_libs3')
sys.path.append(New)
import logs


BASE = 'tb'
CLK = BASE + '.clock'

def peekbin(Sig):
    X = veri.peek(Sig)
    return X

def peek(Sig):
    return logs.intx(peekbin(Sig))

def valid(Sig):
    X = peekbin(Sig)
    return X=='1'









class coverClass:
    def __init__(self):
        self.DEFINES = {}
        self.PATHS = {}
        self.COVERS = {}

        self.history = {}
        self.VALUES = {}
        self.RECORDS = {}
        self.Clock = 'tb.clk'


    def peekbin(self,Sig):
        X = veri.peek(Sig)
        return X

    def peek(self,Sig):
        return logs.intx(self.peekbin(Sig))

    def valid(self,Sig):
        X = self.peekbin(Sig)
        return X=='1'

    def eq(self,Str,Val):
        Sig = self.PATHS[Str]
        X = self.peek(Sig)
        return X == eval(str(Val),self.DEFINES)

    def posedge(self,Str):
        Sig = self.PATHS[Str]
        X = self.peek(Sig)
        if X<0: return
        if Str not in self.history: self.history[Str] = 'x'
        if self.valid(Sig) and self.history[Str]==0:
            self.history[Str] = X
            return True

        self.history[Str] = X
        return False

    def values(self,Str):
        Sig = self.PATHS[Str]
        X = self.peek(Sig)
        if X<0: return
        if Str not in self.VALUES: self.VALUES[Str] = []
        if X not in self.VALUES[Str]: self.VALUES[Str].append(X)
        self.record(Str,'values',X)



    def togglebits(self,Str):
        Sig = self.PATHS[Str]
        X = self.peekbin(Sig)
        for ind,Bit in enumerate(X):
            NN = '%s[%s]'%(Str,ind)
            if NN not in self.VALUES: self.VALUES[NN] = []
            if NN not in self.history: self.history[NN] = 'x'
            if (Bit=='1')and (self.history[NN]=='0'):
                if Bit not in self.VALUES[NN]:
                    self.VALUES[NN].append(Bit)
            elif (Bit=='0')and (self.history[NN]=='1'):
                if Bit not in self.VALUES[NN]:
                    self.VALUES[NN].append(Bit)
            self.history[NN] = Bit 

    def run(self):
        for Cover in self.COVERS.keys():
            Cond,Code = self.COVERS[Cover]
            if self.compute(Cond): self.execute(Cover,Code)

    def compute(self,Cond):
        if Cond == 'True' : return True
        if type(Cond) is str:
            if Cond in self.PATHS:
                Sig = self.PATHS[Cond]
                Val = self.peek(Sig)
                return Val
            if Cond[0] in '0123456789':
                return eval(Cond)

        if Cond[1] == '==':
            return self.eq(Cond[0],Cond[2])
        if Cond[1] == '!=':
            return not self.eq(Cond[0],Cond[2])
        if Cond[1] == 'and':
            A = self.compute(Cond[0])
            B = self.compute(Cond[2])
            return A and B
        if Cond[1] == 'or':
            A = self.compute(Cond[0])
            B = self.compute(Cond[2])
            return A or B
        if Cond[1] == '&':
            A = self.compute(Cond[0])
            B = self.compute(Cond[2])
            return A&B
            
        logs.log_error('compute failed on "%s"'%str(Cond))
        return False

    def execute(self,Cover,Code):
        if Code[0] == 'posedge':
            if self.posedge(Code[1][0]):
                self.record(Cover,'happened')
            return
        if Code[0] == 'togglebits':
            self.togglebits(Code[1][0])
            return
        if Code[0] == 'values':
            self.values(Code[1][0])
            return

        logs.log_error('code failed on "%s"'%str(Code))
        return False

    def record(self,Name,Division,Val=0):
        Key = (Name,Division)
        if (Name,Division) not in self.RECORDS:
            self.RECORDS[Key] = 0
            if Division=='values':
                self.RECORDS[Key] = []
        
        if Division=='happened':
            self.RECORDS[Key] +=1
            return
        if Division=='values':
            if Val not in self.RECORDS[Key]:
                self.RECORDS[Key].append(Val)
                self.RECORDS[Key].sort()
            return

        logs.log_error('name=%s division=%s'%(Name,Division))

    def conclusions(self):
        for Str in self.VALUES:
            logs.log_info('values %s %s'%(Str,self.VALUES[Str]))
        for Str in self.RECORDS:
            logs.log_info('records %s %s'%(Str,self.RECORDS[Str]),2)


cvr = coverClass()
def negedge():
    cvr.run()

def conclusions():
    cvr.conclusions()



def readCoverFile(Fname):
    lines = open(Fname).readlines()
    for line in lines:
        wrds = line.split()
        if len(wrds)==0:
            pass
        elif (wrds[0]=='clock'):
            cvr.Clock = wrds[1]
        elif (wrds[0]=='alias'):
            cvr.PATHS[wrds[1]] = wrds[2]
        elif (len(wrds)==3) and (wrds[1]=='='):
            cvr.DEFINES[wrds[0]] = eval(wrds[2],cvr.DEFINES)
        elif (wrds[0]=='cover'):
            Name = wrds[1]
            for AA in ['==',')','(','and',]:
                line = line.replace(AA,' %s '%AA)
            wrds = line.split()
            lwrds = logs.bracketize(wrds[2:])
            if len(lwrds)<2:
                logs.log_error('BAD COVER %s   %s'%(len(lwrds),lwrds))
            else:
                cvr.COVERS[Name] = (lwrds[0],lwrds[1:])
               

readCoverFile('covergroups0')


veri.sensitive(cvr.Clock,'0','negedge()')

