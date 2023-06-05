

import dump_instance
import os

def help_main(Env):
    Env.params['-tb'] = True
    if '-override' in Env.params:
        pass
    elif os.path.exists('comp'):
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        return
        
    if '-color' in Env.params:
        dump_instance.help_main(Env,'color')
    else:
        dump_instance.help_main(Env)
