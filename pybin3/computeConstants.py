#! /usr/bin/env python3
import os,sys,string
Path = os.path.abspath('.')
sys.path.append(Path)
from constants import constants
computed = {}
def main():
    computeConstants()
    Fout = open('constants.vhd','w')
    Fout.write('generic (\n')
    for Key in computed:
        Val = computed[Key]
        if Key != '__builtins__':
            Fout.write('    Constant %s : integer   := %s ; \n' % (Key,Val))
    Fout.write(') ;\n')
    Fout.close()

# pcieLanes        : integer     := C_NUM_PCIE_LANES

def computeConstants():
    for Str in constants:
        Val,_ = constants[Str]
        try:
            X = eval(Val,computed)
            computed[Str] = X 
        except:
            pass

    for Str in constants:
        Val,_ = constants[Str]
        try:
            X = eval(Val,computed)
            computed[Str] = X 
        except:
            pass
    for Str in constants:
        if Str in computed:
            Was,Pack = constants[Str]
            constants[Str] = str(computed[Str]),Pack





if __name__ == '__main__': main()
