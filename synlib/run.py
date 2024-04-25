#! /usr/bin/env python3
''' 
    demo script to turn liberty files to python database of cells.
    ilia greenblat@mac.com
'''

import os,sys

# helpers
def makeDir(Dir):
    if os.path.exists(Dir): return
    os.mkdir(Dir)

def cellifyList(List,Ext):
    res=[]
    for Name in List:
        ww = Name.split('.')
        if (len(ww)==2)and(ww[1]==Ext):
            res.append(ww[0])
    return res 



# now goto work

# all executables are in directory llbin. they all are python, except llbin/synlib_lexer
# this line compiles it:  (it needs to be run only once). afterwords you can comment it out.
# os.system('llbin/compile_lexer')

os.system('~/vlsistuff/synlib/llbin/split_synlib.py ../PandR/sky130hd/sky130_fd_sc_hd__ss_n40C_1v40.lib')
# replace my demo lib with some real libs. add new line for each lib.
# add similar line for each cell library: os.system('llbin/split_synlib.py important_files/slow.lib')
# now, after previous command directory syntmp should have file .lib for each cell in library

List0 =cellifyList(os.listdir('syntmp'),'lib')

makeDir('descriptions')
List1 = cellifyList(os.listdir('descriptions'),'py')
List1 = []

for Cell in List0:
    if (Cell not in List1):
        print('CELL',Cell)
        os.system('~/vlsistuff/synlib/llbin/synlibMsg.py syntmp/%s.lib'%(Cell))
        os.system('/bin/rm msgsim_cells.ccc')
        os.system('/bin/mv cell.descriptions descriptions/%s.py'%(Cell))
        sys.exit()

os.system('~/vlsistuff/synlib/llbin/assemblyCellLibrary.py')





os.system('/bin/rm yacc.log lex.out db0.pickle ttt.ttt db1.pickle')

# at this point you should have  file called "cellsLibrary.py" 
# it has cell description for each cell in the library in python format.


