#! /usr/bin/env python3
import os,sys,string

Dir = os.path.dirname(__file__)
def main():
    Fname = sys.argv[1]
    Fout = open('cellLibrary.py','w')
    Fout.write(HEADER)
    Fout.close()
    os.system('/bin/rm -R syntmp')
    os.system('%s/split_synlib.py %s' % (Dir,Fname))
    List = os.listdir('syntmp')
    for Lib in List:
        os.system('%s/synlibMsg.py syntmp/%s' % (Dir,Lib))
        os.system('cat cell.descriptions >> cellLibrary.py')



HEADER = '''
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



if __name__ == '__main__': main()
