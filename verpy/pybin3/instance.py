

# -lower in sys.argv will make all external connections to lower case. Pins/Ports are unaffected.

import os,sys,string
import logs

import module_class 
import logs

def help_main(Env,Color=False,Volt=False):
    Mod = Env.Current
    if '-clean' in Env.params:
        cleanParameters(Mod)
    for Sig in Mod.nets:
        Dir,Wid = Mod.nets[Sig]
        print('wire %s %s;' % (module_class.pr_wid(Wid),Sig))

    Big = '\n\n%s %s (' % (Mod.Module,Mod.Module)
    LL = []
    for Sig in Mod.nets:
        Dir,Wid = Mod.nets[Sig]
        if externalDir(Dir):
            LL.append('.%s(%s)' % (Sig,Sig))

    LL.sort()
    More = '\n    ,'.join(LL)
    Big += More
    Big += '\n);\n'
    print(Big)

#    os.system(PREPARE_STRING) 


def externalDir(Dir):
    if 'input' in Dir: return True
    if 'output' in Dir: return True
    if 'inout' in Dir: return True
    return False











PREPARE_STRING = '''
    /bin/rm pymon.log0
    /bin/rm *.empty
    /bin/rm *.inst 
    /bin/rm lex.out
    /bin/rm db0.pickle
    /bin/rm yacc.log
    /bin/rm database.dump
    /bin/rm xyz*

'''



