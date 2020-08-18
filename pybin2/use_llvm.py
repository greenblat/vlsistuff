#! /usr/bin/python
import os,sys,string

import matches


import codeClass
Db = codeClass.codeClass()

def main():
    Fname = sys.argv[1]
    W1 = string.split(Fname,'/')
    W2 = string.split(W1[-1],'.')
    Cell = W2[0]
    prepare(Fname,Cell)
    Db.dump('bef.tmp')
    Db.optimizes()
    Db.dump('%s.mid'%Cell)


def prepare(Fname,Cell):
    os.system('genver.py %s'%Fname)
    os.system('/bin/mv %s.v %s.c'%(Cell,Cell))
    os.system('clang -emit-llvm %s.c -S'%(Cell))
    File = open('%s.ll'%Cell)
    Lines = File.readlines()

    for line in Lines:
        if ';' in line:
            line = line[:line.index(';')]
        for Chr in ',:[]*()!{}':
            line = string.replace(line,Chr,' %s '%Chr)
        wrds = string.split(line)
        if wrds==[]:
            pass
        elif wrds[0] in ['source_filename','target','@chunk','!','attributes']:
            pass
        else:
            runMatches(wrds)

def runMatches(wrds):
    Vars =  matches.matches(wrds,'? = constant ? ? , align 4')
    if Vars:
        Db.defineConstant(Vars)
        return


    Vars =  matches.matches(wrds,'? = global ? ? , align 4')
    if Vars:
        Db.defineGlobal(Vars)
        return

    Vars =  matches.matches(wrds,'? = common global ? ? , align 4')
    if Vars:
        Db.defineCommonGlobal(Vars)
        return

    Vars =  matches.matches(wrds,'? :')
    if Vars:
        Db.defineCode('label label%s'%Vars[0])
        return
    Vars =  matches.matches(wrds,'br label ?')
    if Vars:
        Db.defineCode('    branch label%s'%Vars[0][1:])
        return

    Vars =  matches.matches(wrds,'call ? ( ... ) ? ( )')
    if Vars:
        if Vars[1]=='@sleep':
            Db.defineCode('    sleep()')
        else:
            Db.defineCode('    call %s'%Vars[1])
        return

    Vars =  matches.matches(wrds,'call ? ( ? ?  ) ? ')
    if Vars:
        Db.defineCall2(Vars)
        return
    Vars =  matches.matches(wrds,'? = call ? ? ( ? ?  ) ')
    if Vars:
        Db.defineCall1Assign(Vars)
        return
    Vars =  matches.matches(wrds,'call ? ? ( ? ? , ? ?  ) ? ')
    if Vars:
        Db.defineCall2(Vars)
        return
    Vars =  matches.matches(wrds,'call ? ? ( ? ? , ? ?  ) ')
    if Vars:
        Db.defineCall2(Vars)
        return

    Vars =  matches.matches(wrds,'ret ?')
    if Vars:
        Db.defineCode('return')
        return

    Vars =  matches.matches(wrds,'? = load ? , ? * ? , align 4')
    if Vars:
        Db.defineLoad(Vars)
        return

    Vars =  matches.matches(wrds,'? = fmul ? ?  , ?')
    if Vars:
        Db.defineBiop('fmul',Vars)
        return

    Vars =  matches.matches(wrds,'? = fcmp ? ? ?  , ?')
    if Vars:
        Db.defineFcmp(Vars)
        return
    Vars =  matches.matches(wrds,'? = icmp ? ? ?  , ?')
    if Vars:
        Db.defineIcmp(Vars)
        return
    Vars =  matches.matches(wrds,'}')
    if Vars:
        Db.defineCloseFunction()
        return
    Vars =  matches.matches(wrds,'define ? ? ( ) ? {')
    if Vars:
        Db.defineOpenFunction(Vars)
        return

    Vars =  matches.matches(wrds,'br i1 ? , label ? , label  ?')
    if Vars:
        Db.defineBranchCond(Vars)
        return

    Vars =  matches.matches(wrds,'store ? ? , ? * ? , align  4')
    if Vars:
        Db.defineStore(Vars)
        return

    Vars =  matches.matches(wrds,'? = add ? ? ? , ?')
    if Vars:
        Db.defineBiop('add',Vars)
        return
    Vars =  matches.matches(wrds,'? = fadd ? ? , ?')
    if Vars:
        Db.defineBiop('fadd',Vars)
        return
    Vars =  matches.matches(wrds,'? = fsub ? ? , ?')
    if Vars:
        Db.defineBiop('fsub',Vars)
        return
    Vars =  matches.matches(wrds,'? = and ? ? , ?')
    if Vars:
        Db.defineBiop('and',Vars)
        return
    Vars =  matches.matches(wrds,'? = sext ? ? to ?')
    if Vars:
        Db.defineBiop('sext',Vars)
        return
    Vars =  matches.matches(wrds,'declare ? ? ( ? ) ?')
    if Vars:
        Db.declares(Vars)
        return
    Vars =  matches.matches(wrds,'declare ? ? ( ? , ? ) ?')
    if Vars:
        Db.declares(Vars)
        return
    Vars =  matches.matches(wrds,'?  = common global [ ? x ? ] ? , align ?')
    if Vars:
        Db.defineArray(Vars)
        return
    Vars =  matches.matches(wrds,'?  = getelementptr inbounds [ ? x ? ] , [ ? x ? ] *  ? , ? ? , ?  ?')
    if Vars:
        Db.defineFetch(Vars)
        return

    print('failed %s'%str(wrds))
# failed ['%10', '=', 'getelementptr', 'inbounds', '[', '16', 'x', 'float', ']', ',', '[', '16', 'x', 'float', ']', '*', '@delay', ',', 'i64', '0', ',', 'i64', '%9']
if __name__ == '__main__': main()

