#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    parseCode(Fname)

DEFINES = {}
PAIRS = {}
VARS = {}
def parseCode(Fname,Foutname=''):
    File = open(Fname)
    Lines = File.readlines()
    Lines = expandIncludes(Lines)
    Lines = useDefines(Lines)
    for ind,line in enumerate(Lines):
        Lines[ind] = line[:-1]

    for ind,line in enumerate(Lines):
        wrds = line.split()
        if (len(wrds)>=2) and (wrds[0] == 'def'):
            DEFINES[wrds[1]] = ind
        
    Stack = [] 
    for ind,line in enumerate(Lines):
        wrds = line.split()
        if '{' in line: Stack.append(ind)
        if '}' in line: 
            Start = Stack.pop(-1)
            PAIRS[Start] = ind
            PAIRS[ind] = Start
        if (len(wrds)>=3) and (wrds[1] == '='):
            if (Stack == []):
                VARS[wrds[0]] = wrds[2]
        
        


#    print(DEFS)
#    print(PAIRS)
#    for ind,line in enumerate(Lines):
#        print('%s %s' % (ind,line))
    if Foutname == '':
        Foutname = 'prog_'+Fname + '.py'
    dump(Foutname,Lines)

def dump(Fname,Lines):
    Fout = open(Fname,'w')
    Fout.write('DEFINES = {}\n')
    Fout.write('PAIRS = {}\n')
    Fout.write('LINES = {}\n')
    Fout.write('VARS = {}\n')
    for Def in list(DEFINES.keys()):
        print("CCCCCC",Def)
        if not Def.startswith('__'):
            Val = DEFINES[Def]
            if (type(Val) is str):
                try:
                    Val = eval(Val,DEFINES)
                except:
                    Val = '"%s"' % Val
            Fout.write('DEFINES["%s"] = %s\n' % (Def,Val))
    for Var in VARS:
        Fout.write('VARS["%s"] = %s\n' % (Var,VARS[Var]))
    for Pair in PAIRS:
        Fout.write('PAIRS[%s] = %s\n' % (Pair,PAIRS[Pair]))
    for ind,line in enumerate(Lines):
        Fout.write('LINES[%d] = \'%s\'\n' % (ind,line))
    Fout.close()
        

def useDefines(Lines):
    Res = []
    for line in Lines:
        wrds = line.split()
        if (len(wrds)>=3) and (wrds[0] == 'define'):
            DEFINES[wrds[1]] = ''.join(wrds[2:])
        else:
            Res.append(line)
    return Res

def expandIncludes(Lines):
    Res = []
    dones = 0
    for line in Lines:
        wrds = line.split()
        if (len(wrds)==2) and (wrds[0] == 'include'):
           Fname = wrds[1]
           File = open(Fname)
           More = File.readlines()
           File.close()
           Res.extend(More)
           dones += 1
        else:
            Res.append(line)
    if dones==0: return Res
    return expandIncludes(Res)



if __name__ == '__main__': main()
