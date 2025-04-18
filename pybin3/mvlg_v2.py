#! /usr/bin/python
import os,sys,string

try:
    import genver
except:
    genver = False

try:
    import regfile3
except:
    regfile3 = False

try:
    import regfile2
except:
    regfile2 = False




def main():
    if len(sys.argv)==1:
        print("new mvlg:   mvlg.py [input.mvlg] [optional: output.file]")
        return

    Fname = sys.argv[1]
    List = workClass(Fname).run()
    List = removeDoubles(List)
    for line in List:
        if not os.path.exists(line):
            print('file %s is not found'%line)
    if len(sys.argv)==3:
        Fout = open(sys.argv[2],'w')
        for line in List:
            if os.path.exists(line):
                Keys = buildKeys(line)
                Fout.write('%s         // %s \n'%(line,Keys))
        Fout.close()
        return
    for line in List:
        print(line)

def buildKeys(line):
    File = open(line)
    Chars = File.read()
    K0 = len(Chars)
    K1 = len(Chars.split())
    K2 = 0
    for Chr in Chars:
        X = ord(Chr)
        K2 += X
    return '%s %s %s'%(K0,K1,K2)

def removeDoubles(List):
    Keep = []
    Doubles = {}
    for Line in List:
        Path,Module = justPath(Line)
        Keep.append(Module)
    Keep.sort()
    for ind,Module in enumerate(Keep[:-1]):
        if Module==Keep[ind+1]:
            Doubles[Module]=True
    Seen = [] 
    Result = []
#    print('dubles',Doubles)
    for Line in List:
        Path,Module = justPath(Line)
        if Module in Doubles:
            if Module not in Seen:
                Seen.append(Module)
                Result.append(Line)
#            else:
#                print('removed %s'%Line)
        else: 
            Result.append(Line)

    return Result



class workClass:
    def __init__(self,Fname):
        File = open(Fname)
        lines = File.readlines()
        File.close()
        self.curpath = os.path.dirname(os.path.abspath(Fname))
        self.lines=[]
        self.absorbLines(lines)

    def run(self):
        return self.lines

    def absorbLines(self,lines):
        for line in lines:
            if '//' in lines:
                line = line[:line.index('//')]
            line = replace_setenvs(line)
            wrds = string.split(line)
            if (len(wrds)>0)and(wrds[0][0]=='#'):
                pass
            elif len(wrds)>0:
                if wrds[0] in ['-f','-F']:
                    There = self.addpath(wrds[1])
                    More = workClass(There).run()
                    self.lines.extend(More)
                elif (len(wrds)==1)and(endsWith(wrds[0],'.v') or endsWith(wrds[0],'.sv')):
                    Abs = self.addpath(wrds[0])
                    self.lines.append(Abs)
                elif (len(wrds)==1)and(endsWith(wrds[0],'.vvv')):
                    if genver:
                        There = self.addpath(wrds[0])
                        Final = string.replace(There,'.vvv','.v')
                        genver.run(There,Final,[])
                        print('>>>>>>>>',Final)
                        self.lines.append(Final)
                    else:
                        print('no genver.py script found')
                elif (len(wrds)==1)and(endsWith(wrds[0],'.regfile')):
                    There = self.addpath(wrds[0])
                    Mode = determineWhichRegfileIsCorrect(There) 
                    if regfile3 and (Mode=='ram'):
                        Module = regfile3.run(There)
                        Path,_ = justPath(There)
                        os.system('/bin/mv %s.v %s'%(Module,Path))
                        Final = '%s/%s.v'%(Path,Module)
                        self.lines.append(Final)
                    elif regfile2 and (Mode=='apb'):
                        Module = regfile2.run(There)
                        Path,_ = justPath(There)
                        os.system('/bin/mv %s.v %s'%(Module,Path))
                        Final = '%s/%s.v'%(Path,Module)
                        self.lines.append(Final)
                    else:
                        print('no correct regfile*.py script found for interface mode=%s'%Mode)

                elif (len(wrds)==1)and(endsWith(wrds[0],'.rdl')):
                    There = self.addpath(wrds[0])
                    os.system('bluez %s'%There)
                    There = string.replace(There,'.rdl','.v')
                    self.lines.append(There)
                else:
                    print('ilia: %s'%str(wrds))

    def addpath(self,fname):
        Path = os.path.join(self.curpath, os.path.expandvars(os.path.expanduser(fname)))
        if '..' in Path:
            ww = string.split(Path,'/')
            while '..' in ww:
                ind = ww.index('..')
                ww.pop(ind-1)
                ww.pop(ind-1)
            Path = string.join(ww,'/')
        return Path

def replace_setenvs(line):
    if '$' not in line:
        return line
    Keys = os.environ.keys()
    for Key in Keys:
        if '$%s'%Key in line:
            line = string.replace(line,'$%s'%Key,os.environ[Key])
            line = string.replace(line,'//','/')
    return line


def endsWith(Txt,Ending):
    if Ending not in Txt: return False
    Lend = len(Ending)
    return Ending == Txt[-Lend:]


def justPath(Path):
    ww = string.split(Path,'/')
    if len(ww)==1: return '.',ww[0]
    Base = string.join(ww[:-1],'/')
    return Base,ww[-1]

def determineWhichRegfileIsCorrect(There):
    File = open(There)
    while 1:
        line = File.readline()
        if line=='': return 'apb'
        wrds = string.split(line)
        if (len(wrds)>0)and(wrds[0]=='chip'):
            if 'apb' in wrds: return 'apb'
            if 'ram' in wrds: return 'ram'
            print('no specific interface given. assume apb')
            return 'apb'

if __name__ == '__main__': main()
