

import dump_instance
import os

def help_main(Env):
    Env.params['-tb'] = True
    if os.path.exists('comp'):
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        print('COMP FILE EXISTS. DONT WANT TO OVERWRITE. EXITING')
        return
        
    dump_instance.help_main(Env)
