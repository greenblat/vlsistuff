#! /usr/bin/env python3
import os,sys,string

SETUP = {'file':'localparams','state':'state'}
def main():
    Fname = sys.argv[1]
    if len(sys.argv)>2:
        Prefix = sys.argv[2]
    else:
        Prefix = ''
    if Fname.endswith('.py'):
        File = open(Fname)
        Long = File.read()
        File.close()
        LLL = {}
        exec(Long,LLL)
        States = LLL['States']
    else:
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

    createCase(Prefix,CODES,Wid,SETUP['file'],SETUP['state'])
    createTxGood(Prefix,CODES,Wid,SETUP['file'],SETUP['state'])
    createCsv(Prefix,CODES,Wid,SETUP['file'],SETUP['state'])

def createCase(Prefix,CODES,Wid,Fname,State):
    Fout = open('%s%s_case.v' % (Prefix,Fname),'w')
    LL = []
    for St in CODES:
        Num = CODES[St] & 0xff
        LL.append((Num,St))
    LL.sort()
    for ind,(_,State) in enumerate(LL):
        if ind == (len(LL)-1):
            Next = 'IDLE'
        else:
            _,Next = LL[ind+1]
        Fout.write('        %s : begin state <= %s; end\n' % (State,Next))
    Fout.close()
KNOWNS = {'SOF':0,'IDE':0,'FDF':1,'XLF':1,'resXL':0,'ADH':1,'DH1':1,'DH2':1,'DL1':0,'FCP3':1,'FCP2':1,'FCP1':0,'FCP0':0,'DAH':1,'AH1':1,'AL1':0,'AH2':1,'ACK':1,'ACKDELIM':1}
KNOWNS.update( { 'EOF7':1,'EOF6':1,'EOF5':1,'EOF4':1,'EOF3':1,'EOF2':1,'EOF1':1 })
KNOWNS.update( { 'IDLE':1,'PENDINGD':1, 'INTERMISSION0':1,'INTERMISSION1':1, 'INTERMISSION2':1  })
KNOWNS.update( { 'ERROR0':0,'ERROR1':0,'ERROR2':0,'ERROR3':0,'ERROR4':0,'ERROR5':0,'ERROR6':0,'ERROR7':0 })
KNOWNS.update( { 'OVERLOAD0':0,'OVERLOAD1':0,'OVERLOAD2':0,'OVERLOAD3':0,'OVERLOAD4':0,'OVERLOAD5':0,'OVERLOAD6':0, 'OVERLOAD7':0,'SEC':'sec' })
BUSSED = { 'DF':'df','SDT':'sdt','ID':'id','SBC':'sbc','DLC':'dlc','PCRC':'pcrc','VCID':'vcid','FCRC':'fcrc','AF':'af','DATA':'actual_databyte'}

def createCsv(Prefix,CODES,Wid,Fname,State):
    Fout = open('%s%s.csv' % (Prefix,Fname),'w')
    Fout.write('| num | code | state | skip | rate | value |\n')
    LL = []
    for St in CODES:
        Num = CODES[St] & 0xff
        LL.append((Num,St))
    LL.sort()
    Skip = 'skip5'
    Rate = 'cl'
    id = 0
    for _,State in LL:
        Value = ''
        if State in KNOWNS: Value = KNOWNS[State]
        elif (bussed(State)):
            Value = bussed(State)

            
        Fout.write('| %s | %s | %s | %s | %s | %s |\n'% (hex(id),hex(CODES[State]),State,Skip,Rate,Value))
        if State == 'ADH': Rate = 'xl'
        if State == 'FCP0': Rate = 'cl'
        if State == 'DL1': Skip = 'skip10'
        if State == 'FCRC0': Skip = 'none'
        id += 1
    Fout.close()

def bussed(State):
    for Bus in BUSSED:
        if State.startswith(Bus):
            Ind0 = int(State[len(Bus):])
            if Bus == 'ID': Ind0 -= 18
            Res = '%s[%s]' % (BUSSED[Bus],Ind0)
            return Res
    return False

def createTxGood(Prefix,CODES,Wid,Fname,State):
    Fout = open('%s%s_tx.v' % (Prefix,Fname),'w')
    Fout.write('assign canb_tx_good =\n')
    LL = []
    for St in CODES:
        Num = CODES[St] & 0xff
        LL.append((Num,St))
    LL.sort()
    for _,State in LL:
        Fout.write('    (state == %s) ? 0 :\n' % State)

    Fout.close()



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
