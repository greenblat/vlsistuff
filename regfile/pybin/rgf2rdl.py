#! /usr/bin/env python3

import sys,os
# read csv and make rdl.
def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Lines = File.readlines()
    File.close()
    Lines2 = workLines(Lines)
    splitWides(Lines2)
    if '/' in Fname:
        xw = Fname.split('/')
        Rgf = xw[-1].replace('.csv','')
    else:
        Rgf = Fnamereplace('.csv','')

    Foutname = Fname.replace('csv','rdl')
    Fout = open(Foutname,'w')
    Fout.write('addrmap %s {\n' % Rgf)
    Regs = workLines2(Fout,Lines2)

    for Reg in Regs:
        Fout.write('%s %s;\n' % (Reg,Reg))
    Fout.write('};\n')
    Fout.close()


def workLines(Lines):
    Lines2 = []
    for line in Lines:
        line = line.replace('"',' " ')
        ww  = line.split(',')
        if '"' in ww:
            ind = ww.index('"')
            Start = ww[:ind]
            End = ' '.join(ww[ind:])
            ww = Start+[End[:-1]]
        Lines2.append(ww)            
    return Lines2

def splitWides(Lines):
    Adding = 0
    ind = 0
    while ind<len(Lines):
        ww = Lines[ind]
        if ww[0] == 'reg':
            ww[6] = eval(ww[6])
            ww[6] += Adding
            ww[6] = hex(ww[6])
            Width = int(ww[2])
            if Width>32:
                ww[2] = 32
                Addr = ww[6]
                Diff = Width-32
                ww2 = ww[:]
                ww2[6] = hex(eval(Addr)+4)
                Adding += 4
                ww2[2] = Diff
                ww2[4] = ww2[4]+'_'
                Lines.insert(ind+1,ww2)
        ind += 1


def workLines2(Fout,Lines):
    Fields = []
    Regs = []
    for ind,ww in enumerate(Lines):
        if ww[0] == 'reg':
            Reg = ww[4]
            Access = ww[1]
            Width = ww[2]
            Addr = ww[6]
            Desc = ww[7][:-1]
            Default = ww[5].replace(' ','')
            Regs.append(Reg)
            if len(Lines) == (ind+1) or (Lines[ind+1][0] == 'reg'):
                generateSimpleReg(Fout,Reg,Access,int(Width),Addr,Default,Desc)
        elif ww[0] == 'field':
            Fld = (ww[4],ww[2],ww[3],ww[5].replace(' ',''),ww[7][:-1])
            Fields.append(Fld)
            if len(Lines) == (ind+1) or (Lines[ind+1][0] == 'reg'):
                generateFieldedReg(Fout,Reg,Access,Width,Addr,Desc,Fields)
                Fields = []
    return Regs

def generateSimpleReg(Fout,Reg,Access,Width,Addr,Default,Desc):
    Str = 'reg %s {\n' % Reg
    if Desc=='': Desc='"no desc"'
    if Default=='': Default='0x0'
    Str += '    name = %s;\n' % Desc
    if Access in ['wr','rw']:
        Str += '    field { sw=rw; hw=r; } nn[%s:0] = %s;\n' %(Width-1,Default)
    elif Access in ['wr_pulse','rw_pulse']:
        Str += '    field { sw=rw; swmod; hw=r; } nn[%s:0] = %s;\n' %(Width-1,Default)
    elif Access=='ro':
        Str += '    field { sw=r; hw=w; } nn[%s:0] = %s;\n' %(Width-1,Default)
    elif Access=='ro_pulse':
        Str += '    field { sw=r; swmod; hw=w; } nn[%s:0] = %s;\n' %(Width-1,Default)
    else:
        print("ERROR! %s %s %s %s %s " % (Reg,Access,Width,Addr,Desc))
    Str += '};\n'
    Fout.write(Str)

def generateFieldedReg(Fout,Reg,Access,Width,Addr,Desc,Fields):
    Str = 'reg %s {\n' % Reg
    Str += '    name = %s;\n' % Desc
    for (Fld,A,B,Default,Desc) in Fields:
        if Desc=='': Desc='"no desc"'
        if Default=='': Default='0x0'
        
        if Access in ['wr','rw']:
            Str += '    field { sw=rw; hw=r;i desc=%s; } %s%s = %s;\n' %(Desc,Fld,B,Default)
        elif Access in ['wr_pulse','rw_pulse']:
            Str += '    field { sw=rw; swmod; hw=r;desc=%s; } %s%s = %s;\n' %(Desc,Fld,B,Default)
        elif Access=='ro':
            Str += '    field { sw=r; hw=w;desc=%s; } %s%s = %s;\n' %(Desc,Fld,B,Default)
        elif Access=='ro_pulse':
            Str += '    field { sw=r; swmod; hw=w;desc=%s; } %s%s = %s;\n' %(Desc,Fld,B,Default)
        else:
            print("ERROR",Access)

    Str += '};\n'
    Fout.write(Str)

main()


