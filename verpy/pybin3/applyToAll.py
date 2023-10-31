# run same app on all 
# pyver.py -do applyToAll -action "DIRECTORY ENDIND APP"

import os,sys

def help_main(Env):
    if '-action' not in Env.params:
        print('EXTITING!!! need -action "DIRECTORY ENDIND APP" to do the job')
        return
    if '-action' in Env.params:
        LL = Env.params['-action']
        wrds = LL[0].split()
        List = os.listdir(wrds[0])
        for Fname in List:
            if Fname.endswith('.'+wrds[1]):
                os.system('pyver.py %s/%s -do %s -do clean' % (wrds[0],Fname,wrds[2]))
    
