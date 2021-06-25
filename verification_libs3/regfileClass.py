#! /usr/bin/env python3

# setup file:
'''
field=mode rgf=dma reg=control bits=7:4 addr=0x5a reset=6

set=0x200 field=mode rgf=dma reg=control


'''

import sys,os
sys.path.append("/Users/ilia/vlsistuff/verification_libs3")
import logs

class regClass:
    def __init__(self,Rgf,Reg):
        self.Rgf = Rgf
        self.Reg = Reg
        self.Reset = -1
        self.Width = -1
        self.Value = -1
        self.fields = {}
        self.resets = {}
        self.values = {}
        self.Addr = 0
    def addField(self,Field,Bits):
        self.fields[Field] = Bits
        self.resets[Field] = 0
    def setReset(self,Field,Value):
        if Field == self.Reg:
            self.Reset = Value
            self.Value = Value
        else:
            self.resets[Field] = Value
            self.values[Field] = Value
    def setField(self,Field,Value):
        if Field == self.Reg:
            self.Value = Value
        else:
            self.values[Field] = Value
    def generate(self):
        if list(self.fields.keys()) == []:
            return self.Value
        Res = 0
        for Field in self.fields:
            Hi,Lo = self.fields[Field]
            Mask = (1<< (1+Hi-Lo))-1
            Val = ((self.values[Field] & Mask) << Lo)
            Res |= Val
        return Res




class rgfClass:
    def __init__(self,Name):
        self.Name = Name
        self.regs = {}
    def addReg(self,Reg):
        if Reg in self.regs: return
        self.regs[Reg] = regClass(self.Name,Reg)
    def addField(self,Reg,Field,Bits):
        self.regs[Reg].addField(Field,Bits)
    def setReset(self,Reg,Field,Value):
        if Reg == Field:
            self.regs[Reg].Reset = Value
        else:
            self.regs[Reg].setReset(Field,Value)
    def setWidth(self,Reg,Value):
        self.regs[Reg].Width = Value

class regfilesClass:
    def __init__(self):
        self.regfiles = {}
        self.SeqObj = False

    def action(self,Txt):
        Dir = parseLine(Txt)
        if not Dir: return
        if 'assign' in Dir:
            Rgf = self.regfiles[Dir['rgf']]
            Reg = Rgf.regs[Dir['reg']]
            X = Reg.generate()
            self.SeqObj.Translates[Dir['assign']] = X
            
        elif 'set' in Dir:
            self.assign_action(Dir)
        else:
            self.define_action(Dir)
    def assign_action(self,Dir):
        self.regfiles[Dir['rgf']].regs[Dir['reg']].setField(Dir['field'],Dir['set'])

    def define_action(self,Dir):
        Rgf = self.getprm('rgf',Dir,'must')
        Reg = self.getprm('reg',Dir,'must')
        if Rgf not in self.regfiles:
            self.regfiles[Rgf] = rgfClass(Rgf)
        self.regfiles[Rgf].addReg(Reg) 
        if 'copy' in Dir:
            X = self.regfiles[Rgf]
            Src = self.regfiles[Rgf].regs[Dir['copy']]
            self.regfiles[Rgf].regs[Reg].Value = Src.Value
            self.regfiles[Rgf].regs[Reg].Reset = Src.Reset
            self.regfiles[Rgf].regs[Reg].fields = Src.fields
            self.regfiles[Rgf].regs[Reg].resets = Src.resets
            self.regfiles[Rgf].regs[Reg].values = Src.values.copy()
        elif 'field' in Dir:
            self.regfiles[Rgf].addField(Reg,Dir['field'],self.getprm('bits',Dir,'must'))
            if 'reset' in Dir:
                self.regfiles[Rgf].setReset(Reg,Dir['field'],Dir['reset'])
        else:
            if 'reset' in Dir:
                self.regfiles[Rgf].setReset(Reg,Reg,Dir['reset'])
            if 'width' in Dir:
                self.regfiles[Rgf].setWidth(Reg,Dir['width'])

        if 'addr' in Dir:
            self.regfiles[Rgf].regs[Reg].Addr = Dir['addr']
            
    def getprm(self,Field,Dir,Default=0):
        if Field in Dir:
            return Dir[Field]
        if Default == 'must':
            logs.log_error('MUST "%s" is missing from %s'%(Field,Dir))
            return 0
        return Default
        

    def readSetupFile(self,Fname):
        File = open(Fname)
        Lines = File.readlines()
        File.close()
        for Line in Lines:
            self.action(Line)

    def report(self):
        for RgfName in self.regfiles:
            Rgf = self.regfiles[RgfName]
            for RegName in Rgf.regs:
                Reg = Rgf.regs[RegName]
                X = Reg.generate()
                logs.log_info('%s %s %x %x' % (RgfName,RegName,X,Reg.Addr))




def parseLine(line):
    Wrds = line.split()
    if Wrds == []: return False
    Res = {'flags':[]}
    for wrd in Wrds:
        if '=' in wrd:
            A,B = wrd.split('=')
            if ':' in B:
                Bs = B.split(':')
                Bl = list(map(eval,Bs))
                Res[A] = Bl
            elif B[0] in '-0123456789':                
                Bl = eval(B)
                Res[A] = Bl
            else:
                Res[A] = B
        else:
            Res['flags'].append(wrd)
    return Res


def main():
    rgfs = regfilesClass()
    Fname = sys.argv[1]
    rgfs.readSetupFile(Fname)
    rgfs.report()


if __name__ == '__main__':
    main()




