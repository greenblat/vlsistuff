#! /usr/bin/env python3
import os,sys,string

class moduleClass:
    def __init__(self,Module):
        self.Module = Module
        self.Instance = []
        self.statemachines = {}

    def dump(self,Fout):
        for sm in self.statemachines:
            stm = self.statemachines[sm]
            Fout.write('class %s_%s_Class:\n' % (self.Module,sm))
            Fout.write('    def __init__(self,Path):\n')
            LS = stm[1]
            LLS = []
            for (Name,Val) in LS:
                LLS.append('"%s":%d' % (Name,Val))
            States = '{'+','.join(LLS)+'}'
            Fout.write('        self.Path = Path\n')
            Fout.write('        self.States = %s\n' % States)
            Fout.write('        self.Bus = "%s"\n' % (stm[0]))
            Fout.write('        self.actPairs = {}\n')
            Fout.write('        self.was = ""\n')
            Fout.write('        self.expPairs = []\n')
            for A,B in stm[2]:
                if A[0] in '0123456789': A = int(A)
                if B[0] in '0123456789': B = int(B)
                if type(A) is str: A = '"%s"' % A
                if type(B) is str: B = '"%s"' % B
                Fout.write('        self.expPairs.append((%s,%s))\n' % (A,B))

            Fout.write('    def run(self):\n')
            Fout.write('        now = rawpeek("%s.%s" % (self.Path,self.Bus))\n')
            Fout.write('        if now in self.States:\n')
            Fout.write('            state = self.States[now]\n')
            Fout.write('        else:\n')
            Fout.write('            state = str(now)\n')
            Fout.write('        if self.was=="":\n')
            Fout.write('            self.was=state\n')
            Fout.write('        else:\n')
            Fout.write('            if (self.was!= state) and (self.was,state) not in self.actPairs:\n')
            Fout.write('                self.actPairs[(self.was,state)] = 0\n')
            Fout.write('            if (self.was!= state):\n')
            Fout.write('                self.actPairs[(self.was,state)] += 1\n')
            Fout.write('                self.was=state\n')

            Fout.write('    def report(self,Fout):\n')
            Fout.write('        reportx(Fout,self.actPairs,self.expPairs,self.States,"%s %s")\n' % (self.Module,sm))
#            Fout.write('        for Pair in self.actPairs:\n')
#            Fout.write('            Fout.write("%s %s %%s %%s %%d\\n" %% (revdir(Pair[0],self.States),revdir(Pair[1],self.States),self.actPairs[Pair]))\n' % (self.Module,sm))


Modules = {}

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Big = File.read()
    Big = Big.replace('(',' ( ')
    Big = Big.replace(')',' ) ')
    wrds = Big.split()
    Stack = [[]]
    listify(wrds,Stack)
    List = Stack[0]
    for Item in List:
        useItem(Item)
    Foutname = sys.argv[2]
    Fout = open(Foutname+'.py','w')
    Fout.write(STRING0)
    for Mod in Modules:
        Modules[Mod].dump(Fout)
    Fout.write('class %sClass:\n' % Foutname)
    Fout.write('    def __init__(self,Path):\n')
    Fout.write('        self.Mods = []\n')
    for Mod in Modules:
        sms = Modules[Mod].statemachines.keys()
        for sm in sms:
            Fout.write('        self.Mods.append(%s_%s_Class(Path))\n' % (Mod,sm)) 
    Fout.write('    def run(self):\n')
    Fout.write('        for Mod in self.Mods: Mod.run()\n') 
    Fout.write('    def conclusions(self):\n')
    Fout.write('        Fout = open("conclusions","w")\n')
    Fout.write('        for Mod in self.Mods: Mod.report(Fout)\n') 
    Fout.write('        Fout.close()\n')
    Path = sys.argv[3]
    Fout.write('aaa = %sClass("%s")\n' % (Foutname,Path))
    Fout.close()
        




def useItem(Item):
    global Module
    if Item[0] != 'module': 
        print('error exp module = %s' % Item[0])
        return

    Module = Item[1]
    Modules[Module] = moduleClass(Module)
    for More in Item[2:]:
        if More[0] == 'instance':
            Modules[Module].Instance.append(More[1])
        elif More[0] == 'statemachine':
            Hold = ['bus',[],[]]
            Modules[Module].statemachines[More[1]] = Hold
            for Down in More[2:]:
                if Down[0] == 'bus':
                    Hold[0] = Down[1]
                elif (Down[0] == 'states'):
                    for (Name,Code) in Down[1:]:
                        Hold[1].append((Name,eval(Code)))
                elif (Down[0] == 'flows'):
                    for (From,To) in Down[1:]:
                        Hold[2].append((From,To))
                else:
                    print('error in statemachine %s' % Down[0])
        else:
            print('not yet %s' % More[0])



def listify(wrds,Stack):
    for wrd in wrds:
        if wrd == '(':
            Stack.append([])
        elif wrd == ')':
           New = Stack.pop(-1)
           Stack[-1].append(New)
        else:
            Stack[-1].append(wrd)
            
STRING0 = '''
import os,sys
import veri

New = os.path.expanduser('~/vlsistuff/verification_libs3')
sys.path.append(New)
import logs

    

def revdir(Int,Dir):
    for Key in Dir:
        if int(Int) == Dir[Key]: return Key

    return Int

def conclusions():
    aaa.conclusions()
    logs.closeLogs()

BASE = 'tb'
CLK = BASE + '.clk'

def peekbin(Sig,Base=BASE):
    X = veri.peek('%s.%s'%(Base,Sig))
    return X

def peek(Sig,Base=BASE):
    return logs.intx(peekbin(Sig,Base))

def rawpeek(Sig):
    return logs.intx(veri.peek(Sig))

def valid(Sig,Base=BASE):
    X = peekbin(Sig,Base)
    return X=='1'

def reportx(Fout,actPairs,expPairs,States,Str):
    for (A,B) in actPairs:
        Fout.write("%s %s %s %d\\n" % (Str,revdir(A,States),revdir(B,States),actPairs[(A,B)]))
    for (A,B) in expPairs:
        Ax = strdir(A,States)
        Bx = strdir(B,States)
#        print("AAAAAAA",Ax,Bx,(Ax,Bx) in actPairs,actPairs)
        if (Ax,Bx) not in actPairs:
            Fout.write("%s %s %s 0\\n" % (Str,A,B))

def strdir(AA,States):
    if AA in States: return str(States[AA])
    return str(AA)

def negedge():
    aaa.run()

veri.sensitive(CLK,'0','negedge()','0')

'''




if __name__ == '__main__': main()
