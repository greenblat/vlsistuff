#! /usr/bin/python3

import os,sys

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    ensure_exists('syntmp')
    readfile(File)
def readfile(File):
    while 1:
        line = File.readline()
        if line=='':
            return
        use_line1(line)    

state0='idle'
def use_line1(line):
    global state0
    if state0=='idle':
        if '/*' in line:
            if '*/' in line:
                ind0 = line.index('/*')
                ind1 = line.index('*/')
                line = line[:ind0]+line[ind1+3:]
                use_line2(line)
            else:
                ind0 = line.index('/*')
                line = line[:ind0]
                use_line2(line)
                state0 = 'incomment'
        else:
            use_line2(line)
    elif state0=='incomment':
        if '*/' in line:
            ind1 = line.index('*/')
            line = line[ind1+3:]
            use_line2(line)
            state0 = 'idle'
                
        
state1='init'
Header=[]
def use_line2(line):
    global state1,Opens
    if len(line)<2:
        return
    line = fix_base_line(line,state1)
    if state1=='init':
        if cell_line(line):
            state1='incell'
            Cell = cell_line(line)
            open_cell(Cell,line)
            Opens=1
            Header.append(' library (mylib) {\n')
        elif ok_line(line):
            pass
            # Header.append(line)
    elif (state1=='incell'):
        X = count_char(line,'{')
        Y = count_char(line,'}')
        Opens =Opens+X-Y
        if Opens==0:
            close_cell(line)
            state1='idle'
        else:
            add_cell_line(line)
    elif (state1=='idle'):
        if cell_line(line):
            state1='incell'
            Cell = cell_line(line)
            open_cell(Cell,line)
            Opens=1
NeedSemi = 'variable_1 variable_2 timing_sense related_pin tree_type'.split()
def fix_base_line(line,State):
    wrds = line.split()
    if len(wrds)==0: return line
    if doesntEndWithSemcolon(line):
        if wrds[0] in NeedSemi: return line[:-1]+';\n'
    return line

def doesntEndWithSemcolon(line):
    if ';' not in line: return True
    wrds = line.split()
    return wrds[-1][-1]!=';'


def open_cell(Cell,line):
    global Fout
    Fout = open('syntmp/%s.lib'%Cell,'w')
    print('open %s'%Cell)
    for line0 in Header:
        Fout.write('// '+line0)
    Fout.write(line)

def close_cell(line):
    Fout.write(line)
    Fout.write('// '+'}\n')
    Fout.close()
    
def has_bad_vibes(line):
    wrds = line.split()
    for Pattern in ['driver_waveform_fall','pg_pin','ccsn_first_stage','output_voltage_fall','propagated_noise_high','propagated_noise_low','dc_current','ccsn_last_stage','leakage_power','internal_power','output_current_fall','output_current_rise','fall_power','rise_power','receiver_capacitance1_fall','receiver_capacitance1_rise','receiver_capacitance2_rise','receiver_capacitance2_fall','cell_fall','cell_rise','fall_transition','rise_transition','operating_conditions','revision']:
        if Pattern in wrds:
            return True
    return False


Bads  =0
def add_cell_line(line):
    global Bads
    was=Bads
    if (Bads>0)or has_bad_vibes(line):
        X = count_char(line,'{')
        Y = count_char(line,'}')
        Bads =Bads+X-Y
        print('hasbadvibes',Bads,X,Y,line)



    if (Bads==0)and(was==0)and ok_line(line):
        Fout.write(line)

def ok_line(Line):
    if ('revision' in Line)and(';' in Line): return False
    return True

def count_char(Str,Char):
    cnt=0
    for X in Str:
        if X==Char:
            cnt += 1
    return cnt
def cell_line(line):
    line1 = line.replace('(',' ( ')
    line1 = line1.replace(')',' ) ')
    line1 = line1.replace('{',' { ')
    wrds = line1.split()
    if len(wrds)<5:
        return False
    if (wrds[0]=='cell')and(wrds[1]=='(')and(wrds[3]==')')and(wrds[4]=='{'):
        return  wrds[2].replace('"','')
    return False


def ensure_exists(Dir):
    if os.path.exists(Dir):
        return
    os.mkdir(Dir)

main()
