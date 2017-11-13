#! /usr/bin/python
'''
 msgsim project: concat cell descriptions into one library file
'''

import os,sys,string

libDirectory = 'descriptions'

def main():
    global libDirectory
    if len(sys.argv)>1:
        libDirectory = sys.argv[1]

    List = os.listdir(libDirectory)
    Types=[]
    for Fname in List:
        if '.py' in Fname:
            Cell = Fname[:-3]
            Types.append(Cell)
    buildCellsLibrary(Types)



def copyLibIn(Type,Fout):
    Fname = '%s/%s.py'%(libDirectory,Type)
    missings = 0 
    if os.path.exists(Fname):
        Fin = open(Fname)
        lines = Fin.readlines()
        Fin.close()
        for line in lines:
            Fout.write(line)
    else:
        print '%s cell missing'%Type
        print 'make cell_descriptions/%s.py'%Type
        missings += 1
    return missings


def buildCellsLibrary(Types):
    Fout = open('cellsLibrary.py','w')
    Fout.write(libHeader)
    missings = 0 
    for Type in Types:
        missings += copyLibIn(Type,Fout)
    Fout.close()
    return missings


libHeader = '''

class cellDescClass:
    def __init__(self,Name):
        self.Name = Name
        self.Pins = {}
        self.params = {}
        self.pinsJobs = {}
        self.pinsFunc = {}
        self.Job='combi'
        self.properties = {}
        self.Delays={}
        self.arcs=[]

    def add_arc(self,Pin0,Pin1,Kind):
        self.arcs.append((Pin0,Pin1,Kind))
    def is_output(self,Pin):
        if Pin not in self.Pins: return False
        return self.Pins[Pin]=='output'
    def is_input(self,Pin):
        if Pin not in self.Pins: return False
        return self.Pins[Pin]=='input'

    def is_flop(self):
        return self.Job=='flipflop'


    def add_param(self,Param,Val):
        self.params[Param]=Val
    def add_pin(self,Pin,Dir):
        self.Pins[Pin]=Dir
    def add_pin_func(self,Pin,Func):
        self.pinsFunc[Pin]=Func
    def set_pin_job(self,Pin,Job):
        self.pinsJobs[Pin]=Job

    def set_job(self,Job):
        self.Job=Job

    def combi_in(self,Pin):
        if Pin not in self.Pins:
            return False 
        if self.Pins[Pin]!='input':
            return False 
        if Pin in self.pinsJobs:
            return False 
        return True

    def combi_out(self,Pin):
        if Pin not in self.Pins:
            return False 
        if self.Pins[Pin]!='output':
            return False 
        if Pin in self.pinsJobs:
            return False 
        return True
global CellLib
CellLib = {}

'''

main()

