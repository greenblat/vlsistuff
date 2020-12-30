
import logs

STRING = '''

import logs
class MODULEClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
    def run(self):
'''

# driverMonitor('tb',Monitors)


def help_main(Env):
    Mod = Env.Current
    Fout = open('%sClass.py'%Mod.Module,'w')
    Fout.write(STRING.replace('MODULE',Mod.Module))
    Str = ''
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir:
            Str += '        %s = self.peek("%s")\n'%(Net,Net)
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'output' in Dir:
            Str += '        self.force("%s",0)\n'%(Net)

    Fout.write(Str) 
    Fout.close()



