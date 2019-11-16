#! /usr/bin/python

# this module turns state machine plan into state machine rtl/

import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Fout = open('state_machine.v','w')
    getFile(File)
    Fout.write(HEADER)
    for Flag in FLAGS:
        Fout.write('    ,output %s_flag\n'%(Flag))
    Fout.write(');\n')
    for ind,State in enumerate(STATES):
        St = 'ST_'+string.upper(State)
        Fout.write('wire [7:0] %s = %d;\n'%(St,ind))
    for Chr in CHARS:
        Fout.write('wire [7:0] CHR%s = 8\'h%02x;\n'%(Chr,ord(Chr)))

    Fout.write(STRING0)  
    ELSE = '    '
    for (State,Chr,Dstate,_) in STM:
        St = 'ST_'+string.upper(State)
        Dt = 'ST_'+string.upper(Dstate)
        Cond = condition(Chr)
        Fout.write('        %sif (validin && enable && (state==%s)%s) state <= %s;\n'%(ELSE,St,Cond,Dt))
        ELSE = 'else '
    Fout.write(STRING1)  

    for Flag in FLAGS:
        Fout.write('assign %s_flag = validin && enable && ( \n'%Flag)
        OR = '  '
        for (State,Chr,Dstate,Flgs) in STM:
            St = 'ST_'+string.upper(State)
            Cond = condition(Chr)
            for Flg in Flgs:
                if Flg==Flag:
                    Fout.write('      ((state==%s)%s) ? 1 : \n'%(St,Cond))
#                    Fout.write('    %s((state==%s)%s)\n'%(OR,St,Cond))
#                    OR = '||'

        Fout.write('   0 );\n')
    Fout.write('endmodule\n')
    Fout.close()
    
def condition(Chr):
    if Chr=='*': return ''
    if Chr=='HEX': return '&& hexvalid'
    if Chr=='!HEX': return '&& !hexvalid'
    return '&& (datain==CHR%s)'%(Chr)


STM = []
FLAGS = []
STATES = ['idle']
CHARS = []
def getFile(File):
    while 1:
        line = File.readline()
        if line=='': return
        wrds = string.split(line)
        if len(wrds)==0:
            pass
        else:
            work(wrds)
# ['waddr0', 'HEX', '->', 'waddr1', 'echo', 'pusha']

def work(wrds):
    State = wrds[0]
    if State not in STATES: STATES.append(State)
    Chr = wrds[1]
    if wrds[2]!='->':
        print 'error!!!!! %s'%str(wrds)
        return
    Dstate = wrds[3]
    for wrd in wrds[4:]:
        if wrd not in FLAGS: FLAGS.append(wrd)

    if ('HEX' not in Chr)and(Chr != '*')and (Chr not in CHARS):
        CHARS.append(Chr)

    STM.append((State,Chr,Dstate,wrds[4:]))



HEADER = '''
module state_machine (input clk, input rst_n, input [7:0] datain, input validin, input enable, output idle_state
'''

STRING0 = '''
reg [7:0] state;
assign idle_state = (state==ST_IDLE);
wire [7:0] CHR0 = 8'h30;
wire [7:0] CHR9 = 8'h39;
wire [7:0] CHRA = 8'h41;
wire [7:0] CHRF = 8'h46;
wire [7:0] CHRa = 8'h61;
wire [7:0] CHRf = 8'h66;
wire hexvalid =
    ((datain>=CHR0)&&(datain<=CHR9)) ? 1 :
    ((datain>=CHRA)&&(datain<=CHRF)) ? 1 :
    ((datain>=CHRa)&&(datain<=CHRf)) ? 1 :
    0;

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= ST_IDLE;
    end else begin
'''

STRING1 = '''
    end
end
'''


if __name__ == '__main__': main()


