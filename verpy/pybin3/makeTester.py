####### This is template. change BASE and CLK ##########################
import os,sys
import veri

import io_signals
SIGS = io_signals.INS
OUS = io_signals.OUS

BASE = io_signals.BASE
CLK = BASE + '.' + io_signals.CLK

New = os.path.expanduser('~/vlsistuff/verification_libs3')
sys.path.append(New)
import logs

COMPARE = '''

task compare(input [31:0] aa, input [31:0] bb, input [127:0] sig);
begin
    if (cycles>2) begin
        if (aa==bb) begin
            $display("@%d: CORRECT! %s 0x%h ",cycles,sig,aa);
            corrects <= corrects + 1;
        end  else begin
            $display("@%d: WRONG! %s exp=%h act=%h ",cycles,sig,bb,aa);
            wrongs <= wrongs + 1;
        end
    end
end
endtask
'''

def conclusions():
    Fout.write('    #%d;\n' % TIMEDIFF[3])
    Fout.write('    $display("FINISHING: corrects = %d, wrongs = %d errors=%d",corrects,wrongs,errors);\n')
    Fout.write('if( (corrects>0)&(wrongs==0) & (errors==0)) $display("TEST PASSED!");\n')
    Fout.write('else  $display("TEST FAILED!");\n')
    Fout.write('    $finish;\n')
    Fout.write('end\n')
    Fout.close()
    Fcmp.write('    if (wrongs>0) $display("TEST FAILED wrongs=%d corrects=%d",wrongs,corrects);\n')
    Fcmp.write('    else if (corrects>0) $display("TEST SUCCESS wrongs=%d corrects=%d",wrongs,corrects);\n')
    Fcmp.write('end\n')
    Fcmp.write(COMPARE)
    Fcmp.close()
    if CURRENT[2]>1:
        Fout2.write('    repeat (%d) begin %s %s end\n' % (CURRENT[2],CURRENT[1][:-1],CURRENT[0][:-1]))
    else:
        Fout2.write('     %s %s\n' % (CURRENT[1][:-1],CURRENT[0][:-1]))
        
    Fout2.write('end\n')
    Fout2.close()
    logs.closeLogs()


def peekbin(Sig,Base=BASE):
    X = veri.peek('%s.%s'%(Base,Sig))
    return X

def peek(Sig,Base=BASE):
    Bin = peekbin(Sig,Base)
    WIDS[Sig] = len(Bin)
    return logs.intx(Bin)


def valid(Sig,Base=BASE):
    X = peekbin(Sig,Base)
    return X=='1'

wasTime = [0,0,0,0]
def timeDiff(Which):
    Now = veri.stime()
    Diff = Now-wasTime[Which]
    wasTime[Which] = Now
    return Diff

Fout = open('tester.include','w')
Fout2 = open('tester_clk.include','w')
Fcmp = open('tester_chk.include','w')
Fcmp.write('initial begin\n')
Fout.write('initial begin\n')
Fout2.write('initial begin\n')
cycles = 0

CLKLINES = ['','']
CURRENT = ['','',0]


def posedge():
    global cycles
    Diff = timeDiff(1)
#    Fout2.write('    #%d; clk = 1; cycles = cycles + 1;\n' % Diff)
    CLKLINES[1] = '    #%d; clk = 1; cycles = cycles + 1;\n' % Diff

VALUES = {}
OUTVALUES = {}
WIDS = {}
for Sig in SIGS: VALUES[Sig] = "x"
for Sig in OUS: OUTVALUES[Sig] = "x"

TIMEDIFF = [0,0,0,0,0,1]
CLOCKS = 0
def negedge():
    global CLOCKS
    Diff1 = timeDiff(1)
    CLKLINES[0] = '    #%d; clk = 0;\n' % Diff1
    if CURRENT[0] == '':
        CURRENT[0] = CLKLINES[0] 
        CURRENT[1] = CLKLINES[1] 
        CURRENT[2] = 1
    elif (CURRENT[0] == CLKLINES[0] ) and (CURRENT[1] == CLKLINES[1]):
        CURRENT[2] += 1
    elif (CURRENT[2] == 1):
        Fout2.write(CLKLINES[1])
        Fout2.write(CLKLINES[0])
    elif (CURRENT[2] > 1):
        Fout2.write('    repeat (%d) begin %s %s end\n' % (CURRENT[2],CURRENT[1][:-1],CURRENT[0][:-1]))
        CURRENT[2],CURRENT[1],CURRENT[2] = 1,CLKLINES[1],CLKLINES[0]
        


    Diff = timeDiff(2)
    TIMEDIFF[3] = Diff * 10
    dones = 0
    for Sig in SIGS:
        Now = peek(Sig)
        Was = VALUES[Sig]
        if Was != Now:
            dones += 1
    if dones>0:
        Fout.write('    #%d;\n' % (TIMEDIFF[2]+Diff))
        TIMEDIFF[2] = 0
        for Sig in SIGS:
            Now = peek(Sig)
            Was = VALUES[Sig]
            if Was != Now:
                Fout.write('     %s = %s%s;\n' % (Sig,WIDS[Sig],verilogvalue(Now)))
                VALUES[Sig] = Now
    else:
        TIMEDIFF[2] += Diff
            


    Diff = timeDiff(3)
    TIMEDIFF[4] = Diff * 10
    dones = 0
    for Sig in OUS:
        Now = peek(Sig)
        Was = OUTVALUES[Sig]
        if Was != Now:
            dones += 1
    if dones>0:
        Fcmp.write('    #%d;\n' % (TIMEDIFF[5]+Diff))
        TIMEDIFF[5] = 0
        for Sig in OUS:
            Now = peek(Sig)
            Was = OUTVALUES[Sig]
            if Was != Now:
                if Now>=0:
                    Fcmp.write('     compare(%s,%s%s,"%s"); \n' % (Sig,WIDS[Sig],verilogvalue(Now),Sig))
                OUTVALUES[Sig] = Now
    else:
        TIMEDIFF[5] += Diff
            



def verilogvalue(Now):
    if Now < 0 :
        return "'bx"
    return "'h%x" % Now 

veri.sensitive(CLK,'0','negedge()','0')
veri.sensitive(CLK,'1','posedge()','0')


