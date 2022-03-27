#! /usr/bin/env python3
import os,sys



def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fout = open('myproc.py','w')
    lines = File.readlines()
    File.close()
    for line in lines:
        Fout.write(line)
    LL = getLines(lines)
    LL.append('        self.Done = True')
    LL.append("        yield 'NotOk'")

    for line in LL:
        if line[-1] == '\n':
            line = line[:-1]
        if len(line)>1:
            Fout.write(line+'\n')
    Fout.close()


def getLines(lines):
    state = 'idle'
    LL = []
    for line in lines:
        wrds = line.split()
        if wrds==[]:
            pass
        elif (state=='idle') and line.startswith('    def code_source'):
            state = 'getting'
            LL = [line.replace('code_source','code')]
        elif (state=='getting'):
            if line.startswith('    def '):
                state = 'work'
            else:
                LL.append(line)
        elif (state=='work'):
            Res = work(LL)
            return Res

    Res = work(LL)
    return Res

def work(Lines):
    Res = [Lines[0]]
    for line in Lines[1:]:
        if ('axi_read' in line):
            Res.extend(axi_read(line))
        elif ('axi_write' in line):
            Res.extend(axi_write(line))
        elif '        posedge(' in line:
            Res.extend(posedge(line))
        elif '        negedge(' in line:
            Res.extend(negedge(line))
        else:
            Res.append(line)
    return Res

def axi_write(line):
    pos = line.replace('(',' ')
    pos = pos.replace(')',' ')
    pos = pos.replace(',',' ')
    wrds = pos.split()
    Addr = cleanit(wrds[-2])
    Data = cleanit(wrds[-1])
    codex = AXI_WRITE.replace('VAR',Addr)
    codex = codex.replace('DATA',Data)
    return adjustIndent(line,codex)

def cleanit(Txt):
    Txt = Txt.replace('"','')
    Txt = Txt.replace("'",'')
    return Txt
def axi_read(line):
    pos = line[line.index('axi_read')+9:]
    pos = pos[:pos.index(')')]
    pos = cleanit(pos)
    codex = AXI_READ.replace('VAR1',pos)
    for Chr in '+-*':
        pos = pos.replace(Chr,'_')
    codex = codex.replace('VAR2',pos)
    return adjustIndent(line,codex)
    


def posedge(line):
    Expr = line[line.index('(')+1:]
    Expr = Expr[:Expr.index(')')]
    Expr = Expr.replace('"','')
    Expr = Expr.replace("'",'')
    Pos = POS.replace('EXPR',Expr)
    return adjustIndent(line,Pos)

def negedge(line):
    Expr = line[line.index('(')+1:]
    Expr = Expr[:Expr.index(')')]
    Expr = Expr.replace('"','')
    Expr = Expr.replace("'",'')
    Pos = NEG.replace('EXPR',Expr)
    return adjustIndent(line,Pos)

def adjustIndent(line,LLs):
    LL =  LLs.split('\n')
    Indent = indentation(line)
    res = []
    for Line in LL:
        res.append(Indent+Line)
    return res        

def indentation(line):
    wrds = line.split()
    X = wrds[0][0]
    res = line[:line.index(X)]
    return res



POS = '''
while not self.valid("EXPR"):
    self.waitExpr = self.Path+'EXPR'
    yield 'Ok'
'''
NEG = '''
while self.valid("EXPR"):
    self.waitExpr = self.Path+'EXPR'
    yield 'Ok'
'''

AXI_READ = '''
self.issue('%s read 1 1 XL+VAR1 2' % self.Axi)
self.armCallback = True
yield 'Ok'
self.VAR2 = self.Data
'''

AXI_WRITE = '''
self.issue('%s write 1 1 XL+VAR 2 DATA' % self.Axi)
self.waiting = 1
'''

if __name__ == '__main__': main()
