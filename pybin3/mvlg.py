#! /usr/bin/env python3

#         #define XXX
#         
#         #ifdef XXX
#         #else
#         #endif
#         
#         -f|-F file.mvlg
#         filename

# usage: mvlg [in_file.mvlg] [out_file]

import sys, string, os

# list of defined constants
STATE_NORM = 0
STATE_IF_TAKEN = 1
STATE_IF_SKIPPED = 2
STATE_ELSE_TAKEN = 3
STATE_ELSE_SKIPPED = 4





class scanClass:
    def __init__ (self, fname_in, fname_out=False,minusV=False):
        self.defined = []
        self.state = STATE_NORM
        self.skipping = False
        self.res = []
        self.inc = []
        self.pathstack = []
        self.err = []
        self.topLevel = True
        self.tops=[]
        self.scan(fname_in)
        self.weed_out_doubles()
        self.fname_out=fname_out
        self.minusV=minusV

        self.dump()

    def dump(self):
        if self.fname_out:
            self.File = open(self.fname_out,"w")
        for tupple in self.inc:
            self.logit("%s%s"%tupple)
        for line in self.res:
            if (self.minusV)and(line not in self.tops)and('tb.v' not in line)and('define' not in line)and('config' not in line):
                if canBeLibrary(line):
                    line = '-v  '+line
            self.logit(line)
        for tupple in self.inc:
            if tupple[0] in ['-v']:
                self.logit("%s %s"%tupple)
        for tupple in self.inc:
            if tupple[0] in ['-y']:
                self.logit("%s %s"%tupple)
        
        if self.fname_out:
            self.File.close()

    def logit(self,Txt):
        if self.fname_out:
            self.File.write(Txt+'\n')
        else:
            print(Txt)

    def begins(self, str, word):
        if len(str) < len(word):
            return False
        else:
            return str[:len(word)] == word

    def addpath(self,fname):
        Path = os.path.join(self.curpath, os.path.expandvars(os.path.expanduser(fname)))
        if '..' in Path:
            ww = Path.split('/')
            while '..' in ww:
                ind = ww.index('..')
                ww.pop(ind-1)
                ww.pop(ind-1)
            Path = '/'.join(ww)
        if (Path[0] == '/')and os.path.islink(Path):
            return os.path.realpath(Path)
            
        return Path

    def weed_out_doubles(self):
        used={}
        res = []
        for Fname in self.res:
            wrds = Fname.split('/')
            Name = wrds[-1]
            if ('define' in Name)or('config' in Name) or(Name not in used):
                res += [Fname]
                used[Name]=Fname
        self.res=res
        inc2 = []
        for (Action,Path) in self.inc:
            if Path[-1]=='/':
                Path = Path[:-1]
            found=False
            for (A,B) in inc2:
                if (A==Action)and(B==Path):
                    found=True
            if not found:
                inc2.append((Action,Path))
        self.inc = inc2



    def scan(self,fname_in):
        self.curpath = os.path.dirname(os.path.abspath(fname_in))

        try:
            fin = open(fname_in)
        except:
            err = "Couldn't open MVLG file: %s"%fname_in
            self.err.append(err)
            return
        
        lines = fin.readlines()

        for line in lines:
            if '//' in line:
                line = line[:line.index('//')]
            line = replace_setenvs(line)
            w = line.split()
            if len(w) > 0:
                # check if this is a comment of a directives line
                if line[0] == "#":
                    if not self.skipping and (w[0] == "#define"):
                        self.defined.append(w[1])
                    elif w[0] == "#ifdef":
                        if self.defined.count(w[1]):
                            self.state = STATE_IF_TAKEN
                            self.skipping = False
                        else:
                            self.state = STATE_IF_SKIPPED
                            self.skipping = True
                    elif w[0] == "#else":
                        if self.state == STATE_IF_TAKEN:
                            self.state = STATE_ELSE_SKIPPED
                            self.skipping = True
                        else:
                            self.state = STATE_ELSE_TAKEN
                            self.skipping = False
                    elif w[0] == "#endif":
                        self.state = STATE_NORM
                        self.skipping = False
                elif not self.skipping:
                    if '+incdir+' in w[0]:
                        Path = w[0][8:]
                        self.inc.append(('+incdir+',self.addpath(Path)))
                    elif '+define+' in w[0]:
                        self.inc.append(('+define+',w[0][8:]))
                    elif (w[0] == "-f") or (w[0] == "-F"):
                        self.pathstack.append(self.curpath)
                        Was = self.topLevel 
                        self.topLevel = False
                        self.scan(self.addpath(w[1]))
                        self.curpath = self.pathstack.pop()
                        self.topLevel = Was
                    elif (w[0] == "-v") or (w[0] == "-y"):
                        self.inc.append((w[0]+' ',self.addpath(w[1])))
                    elif (w[0][0] == "-") or (w[0][0] == "+"):
                        self.res.append(os.path.expandvars(line))
                    else:
                        fname = self.addpath(w[0])
                        if os.path.exists(fname):
                            if self.res.count(fname) == 0:
                                self.res.append(fname)
                                if self.topLevel:
                                    self.tops.append(fname)
                        else:
                            self.err.append("No such file: %s"%fname)

def replace_setenvs(line):
    if '$' not in line:
        return line
    Keys = os.environ.keys()
    Keys2 = []
    for Key in Keys:
        Keys2.append((len(Key),Key))
    Keys2.sort()
    Keys2.reverse()

    for _,Key in Keys2:
        if '$%s'%Key in line:
            line = line.replace('$%s'%Key,os.environ[Key])
            line = line.replace('//','/')
    return line


def canBeLibrary(Fname):
    wrds = Fname.split()
    if len(wrds)!=1: return False
    Fname = wrds[0]
    if not os.path.exists(Fname):
        print('%s does not exist'%Fname)
        return  False

    File = open(Fname)
    state='idle'
    while 1:
        line = File.readline()
        if line=='':  
            File.close()
            return False 
        if state=='idle':
            if 'module' in line:
                state='inmodule'
        elif state=='inmodule':
            if 'endmodule' in line:
                File.close()
                return  True
        




# --------------- MAIN -----------------------------------

def main():
    if len(sys.argv) < 2:
        print("mvlg.py [input.mvlg] <output> [-v]")
        return
    minusV = '-v' in sys.argv
    if len(sys.argv) < 3:
        s = scanClass(sys.argv[1],False,minusV)
    else:
        s = scanClass(sys.argv[1], sys.argv[2],minusV)


       # report errors
    if len(s.err) > 0:
        print("\n\n*** Errors encountered:")
        for err in s.err:
            print(err)
    
def run(Fname,outFname): 
    s = scanClass(Fname,outFname ,False)
    if len(s.err) > 0:
        print("\n\n*** Errors encountered:")
        for err in s.err:
            print(err)

if (__name__ == '__main__'):
    main()



