#! /usr/bin/env python3
import os,sys,string

SETUP = {'file':'localparams','state':'state'}
def main():
    Fname = sys.argv[1]
    if len(sys.argv)>2:
        Prefix = sys.argv[2]
    else:
        Prefix = ''
    File = open(Fname)
    Lines = File.readlines()
    States = parseLines(Lines)
    Num = len(States)
    Wid = len(bin(Num))-2

    CODES = {}
    STATE = SETUP['state']
    for ind,State in enumerate(States):
        Ones = bin(ind).count('1')
        Ones = Ones & 3
        Code = (Ones<<Wid) + ind
        CODES[State] = Code
    Fout = open('%s%s.vh' % (Prefix,SETUP['file']),'w')
    for State in States:
        Fout.write('localparam %s = %d\'h%x;\n' % (State,Wid+2,CODES[State]))
    Fout.write('reg [%d:0] %s;\n' % (Wid+1,STATE))
    Fout.write('wire [1:0] %s_ones = 0 + ' % (STATE))
    Str = []
    for ind in range(Wid):
        Str.append('%s[%d]' % (STATE,ind))
    Fout.write(' %s ;\n' % ( '+'.join(Str)))
    Fout.write('assign %s_legal = %s[%d:%d] == %s_ones;\n' % (STATE,STATE,Wid+1,Wid,STATE))

    STR = NEXTFUNC.replace('WID',str(Wid+2-1))
    STR = STR.replace('222',str(Wid-1))
    STR = STR.replace('STATE',STATE)
    Str = []
    for ind in range(Wid):
        Str.append('count[%d]' % ind)
    STR = STR.replace('BITS','+'.join(Str))
    Fout.write(STR)
    Fout.close() 

    monitorModule(Prefix,CODES,Wid,SETUP['file'],SETUP['state'])
    stateInSetModule(Prefix,CODES,Wid,SETUP['file'],SETUP['state'])

def  monitorModule(Prefix,CODES,Wid,FILE,STATE):
    Fout = open('%s%s_mon.v' % (Prefix,FILE),'w')
    Max = 0
    for state in CODES:
        Max = max(Max,len(state))
    Fout.write('module %s%s_mon ( input [%d:0] %s, output [%d:0] STR);\n' % (Prefix,STATE,Wid+1,STATE,(Max-1)*8))

    Fout.write('assign STR = \n')
    for state in CODES:
        Code = CODES[state]
        Fout.write('    (%s == %d\'h%x) ? "%s" :\n' % (STATE,Wid+2,Code,state))

    Fout.write(' 0;\n')
    Fout.write('endmodule\n\n')
    Fout.close()

def stateInSetModule(Prefix,CODES,Wid,FILE,STATE):
    Fout = open('%s%s_in_set.v' % (Prefix,FILE),'w')
    Max = 0
    for state in CODES:
        Max = max(Max,len(state))
    Fout.write('module %s%s_in_set ( input [%d:0] %s, output vld);\n' % (Prefix,STATE,Wid+1,STATE))

    Fout.write('assign vld = \n      ')
    LL = []
    for state in CODES:
        Code = CODES[state]
        LL.append('(%s == %d\'h%x)' % (STATE,Wid+2,Code))
#        Fout.write('    (%s == %d\'h%x) ? 1 :\n' % (STATE,Wid+2,Code))
    Str = '\n    ||'.join(LL)
    Fout.write('%s;\n' %Str)
    Fout.write('endmodule\n\n')
    Fout.close()




NEXTFUNC = '''
// function [WID:0] next_STATE ( input [WID:0] state );
// reg [222:0] count;
// reg [1:0] ones;
// begin
//     count = state[222:0]+1;
//     ones = 0 + BITS ;
//     next_state = {ones,count};
// end
// endfunction
'''
def parseLines(Lines):
    States = []
    for line in Lines:
        wrds = line.split()
        if (len(wrds)>0) and (wrds[0][0] == '#'):
            if wrds[0] == '#file': SETUP['file'] = wrds[1]   
            elif wrds[0] == '#state': SETUP['state'] = wrds[1]   
            else:
                print('bad meta %s' % line[:-1])
            line = ''
            wrds = []
        if len(wrds) == 1:
            if wrds[0] not in States:
                States.append(wrds[0])
        elif len(wrds) == 2:
            Bus = mutual(wrds[0],wrds[1])
            Ind0 = wrds[0][len(Bus):]
            Ind1 = wrds[1][len(Bus):]
            try:
                Ind0 = eval(Ind0)
                Ind1 = eval(Ind1)
                if Ind0 > Ind1: 
                    Step = -1
                else:
                    Step = 1
                while Ind0 != Ind1:
                    States.append('%s%d' % (Bus,Ind0))
                    Ind0 += Step
                States.append('%s%d' % (Bus,Ind0))
            except:
                print('exception happened on %s' % line[:-1])
        elif len(wrds) > 0:
            print('error line "%s"' % (line[:-1]))
    return States            

def mutual(Astr,Bstr):
    Min = min(len(Astr),len(Bstr))
    for ii in range(Min):
        if Astr[ii] != Bstr[ii]:
            return Astr[:ii]



if __name__ == '__main__': main()
