#! /usr/bin/env python3

import os,sys

ALW_HITS = {}
TGL_HITS = {}
def main():
    Fcovname = sys.argv[1]
    buildDb(Fcovname)
    Mvlg = sys.argv[2]
    readModules(Mvlg)

def readModules(Mvlg):
    File = open(Mvlg)
    Lines = File.readlines()
    File.close()
    for line in Lines:
        ww = line.split()
        if len(ww)>0:
            Fname = ww[0]
            File = open(Fname)
            Lines = File.readlines()
            File.close()
            Lines = cleanUp(Lines)
            workOnIt(Lines)

def cleanUp(Lines):
    Out = []
    NOS = []
    for ind,line in enumerate(Lines):
        if ind in NOS:
            pass
        elif ('include' in line) and ('covstep' in line):
            pass
        elif ('tgl_mon' in line):
            if ';' in line:
                pass
            elif ';' in Lines[ind+1]:
               NOS += [ind+1] 
            elif ';' in Lines[ind+2]:
               NOS += [ind+1],[ind+2]
        else:
            Out.append(line)
    return Out            



def workOnIt(Lines):
    if not os.path.exists('annotated'): os.mkdir('annotated')
    for ind,Line in enumerate(Lines):
        Line = Line.replace('(',' (')
        ww = Line.split()
        if (ww!=[]) and (ww[0] == 'module'):
            
            Module = ww[1]
            if Module in ALW_HITS:
                ALW = ALW_HITS[Module]
                TGL = TGL_HITS[Module]
                doTheJob(Module,Lines,ALW,TGL)
            else:
                print('MODULES missing',Module)
    
def doTheJob(Module,Lines,ALW,TGL):
    Fout = open('annotated/%s.md' % Module,'w')
    for ind,line in enumerate(Lines):
        linex = workOnLine(Module,line,ALW,TGL)
        if linex: Fout.write(linex)
    Fout.close()
        
SEQNUM = {}
def workOnLine(Module,line,ALW,TGL):
    if 'assign' in line:
        return assign_line(line,TGL)
    elif ('wire' in line) and ('=' in line):
        return wire_line(line,TGL)
    elif ('covstep' in line) and ('include' not in line):
        return covstep_line(line,ALW)
    elif ('covstep' in line) and ('include' in line):
        return ''
    elif ('<=' in line):
        line0 = line.replace('<=',' <= ')
        wrds = line0.split()
        Indx = wrds.index('<=')
        Dst = wrds[Indx-1]
        if Dst in ALW:
            if Module not in SEQNUM: SEQNUM[Module] = {}
            if Dst not in SEQNUM[Module]:  SEQNUM[Module][Dst] = 0
            Bin = SEQNUM[Module][Dst]
            SEQNUM[Module][Dst]  += 1
            if Bin in ALW[Dst]:
                print("XXXXX",Dst,Bin,ALW[Dst])
                if ALW[Dst][Bin] == 'missing':
                    return '<span style="color: red;">  %s </span>\n'% (line[:-1])
                elif ALW[Dst][Bin] == 'covered':
                    return '<span style="color: green;">  %s </span>\n'% (line[:-1])
                else:
                    return line
    return line

def wire_line(line,TGL):
    line0 = line.replace('=',' = ')
    line0 = line0.replace('[',' [')
    line0 = line0.replace(']','] ')
    wrds = line0.split()
    ind  = wrds.index('=')
    Dst = wrds[ind-1]
    if Dst in TGL:
        if TGL[Dst] == 'missed':
            return '<span style="color: red;">  %s </span>\n'% (line[:-1])
        elif TGL[Dst] == 'covered':
            return '<span style="color: green;">  %s </span>\n'% (line[:-1])
        else:
            return line
    else:
        return line



def assign_line(line,TGL):
    line = line.replace('=',' = ')
    ww = line.split()
    Dst = ww[1]
    if Dst in TGL:
        if TGL[Dst] == 'missed':
            return '<span style="color: red;">  %s </span>\n'% (line[:-1])
        elif TGL[Dst] == 'covered':
            return '<span style="color: green;">  %s </span>\n'% (line[:-1])
        else:
            return line
    else:
        return line


def buildDb(Fcovname):
    Fcov = open(Fcovname)
    Lines = Fcov.readlines()
    Fcov.close()
    for line in Lines:
        ww = line.split()
        if (len(ww)==5) and(ww[0] == 'ALWS:')and(ww[1] in ['missing','covered']):
            Module = ww[2]
            Sig    = ww[3]
            Ind    = int(ww[4])
            if Module not in ALW_HITS: ALW_HITS[Module] = {}
            if Sig not in  ALW_HITS[Module]:  ALW_HITS[Module][Sig] = {}
            ALW_HITS[Module][Sig][Ind] = ww[1]

        if (len(ww)==4) and(ww[0] == 'TGLS:')and(ww[1] in ['missing','covered']):
            Module = ww[2]
            Sig    = ww[3]
            if Module not in TGL_HITS: TGL_HITS[Module] = {}
            TGL_HITS[Module][Sig] = ww[1]


main()


