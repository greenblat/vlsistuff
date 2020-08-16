#! /usr/bin/python

import os,sys,string
import logs

LIB_ABC = '/Users/ilia/clients/libs/synth_libs/small28.lib'
LIB_DFF = '/Users/ilia/clients/libs/synth_libs/dff28.lib'

LIB_ABC = '/Users/ilia/clients/yosys_libs/scmetro_abc.lib'
LIB_DFF = '/Users/ilia/clients/yosys_libs/scmetro_dff.lib'

LIB_ABC = '/Users/ilia/clients/yosys_libs/basic2.lib'
LIB_DFF = '/Users/ilia/clients/yosys_libs/basic2.lib'

INCFILE = '''
read_verilog -sv ALLRTL
hierarchy -check -top  TOP
check;
proc; opt; fsm; opt; memory; opt
check;

techmap; opt
dfflibmap -liberty LIB_DFF
abc -liberty  LIB_ABC

clean
write_verilog -noattr  TOP.glv

'''


FLAT = '''
flatten;
check;
opt;
check;
clean;
write_verilog TOP.flat
'''

SCHEME = '''
read_liberty  -lib  LIB_ABC ;
show -prefix ./sch ;
'''

def main():
    global LIB_DFF,LIB_ABC
    if len(sys.argv)==1:
        print helpString
        sys.exit()

    Args = logs.parse_args()
    print Args
    mvlgFile = Args['fnames'][0]
    wrds = string.split(mvlgFile,'/')
    wrds = string.split(wrds[-1],'.')
    Top = wrds[0]

    if '-top' in Args:
        Top = Args['-top'][0]

    if '-dff' in Args:
        LIB_DFF = Args['-dff'][0]

    if '-abc' in Args:
        LIB_ABC = Args['-abc'][0]


    STR = INCFILE

    if '-flat' in Args:
        STR += FLAT
    if '-scheme' in Args:
        STR += SCHEME

    wrds = string.split(mvlgFile,'.')
    if wrds[-1]=='mvlg':
        os.system('mvlg_to_one_file %s %s.all'%(mvlgFile,Top))
    else:
        os.system('/bin/cp %s %s.all'%(mvlgFile,Top))
    INC = string.replace(STR,'ALLRTL','%s.all'%(Top))
    INC = string.replace(INC,'TOP',Top)
    INC = string.replace(INC,'LIB_DFF',LIB_DFF)
    INC = string.replace(INC,'LIB_ABC',LIB_ABC)
    Finc = open('%s.inc'%Top,'w')
    Finc.write(INC)
    Finc.close()
    os.system('yosys -s %s.inc | tee log.yosys | tee %s.yosys.log '%(Top,Top))

helpString = '''
    run_yosys_mvlg.py module.mvlg   [ -flat] [ -top TOP] [-abc ABCLIB] [-dff DFFLIB]
    -flat will run flat stage at the end.
    "module.mvlg" - mvlg file named as top level module.
    -top : replace default top
    -abc : liberty file of COMBI cells
    -dff : liberty file of DFF cells
'''

main()





