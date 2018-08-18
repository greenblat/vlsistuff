
import string

NETWIDS = string.split('''
* clka 1
* clkb 1
* rou_in_seen 1
* rou_out_seen 1
* seen_monitor 1
* pages 16
* whoami 32
* rou_in WID
* rou_out WID
* ack_in 3
* ack_out 3

* rou*_in WID
* rou*_out WID
* ack*_in 3
* ack*_out 3

* msg_in  WID    input
* msg_out  WID   output
* msg_in_ack  1  output
* msg_out_ack  1 input
rou_admin resp_count 8  output
rou_admin resp_data 64  output
rou_admin resp_addr 3  input
rou_admin resp_read 1  input

rou_admin req_count 8  output
rou_admin req_data 64  input
rou_admin req_addr 3  input
rou_admin req_write 1  input

''','\n')

def getPinWid(Type,Pin):
    for line in NETWIDS:
        wrds = string.split(line)
        if len(wrds) in [3,4]:
            if len(wrds)==4:
                Dir = wrds[3]
            else:
                Dir = 'wire'
            if (wrds[0]==Type)or(wrds[0]=='*'):
                if (Pin==wrds[1]):
                    return Dir,wrds[2]
                if ('*' in wrds[1]) and matchit(Pin,wrds[1]): 
                    return Dir,wrds[2]
                

    log_error('getPinWid failed for %s %s'%(Type,Pin))
    return 'wire',1

def matchit(Txt,Pattern):
    if Pattern=='*': return True
    if Txt==Pattern: return True
    wrds = string.split(Pattern,'*')
    while wrds!=[]:
        if wrds[0]=='*': wrds.pop(0)
        elif wrds[0] not in Txt: 
            return False
        else:
            ind  = Txt.index(wrds[0])+len(wrds[0])
            Txt = Txt[ind:]
            wrds.pop(0)
    return True
ADMIN = '''
rou_admin #(.DWID(DWIDPY)) INST (.clk(CLK),.rst_n(rst_n)
    ,.rou_in(IN),.rou_out(OUT),.ack_in(ack_IN),.ack_out(ack_OUT)
    ,.rou_in_seen(IN_seen) ,.rou_out_seen(OUT_seen)

    ,.req_count(req_count)
    ,.req_data(req_data)
    ,.req_addr(req_addr)
    ,.req_write(req_write)

    ,.resp_count(resp_count)
    ,.resp_data(resp_data)
    ,.resp_addr(resp_addr)
    ,.resp_read(resp_read)
    ,.pages(PAGES),.whoami(SELF_ID)
    ,.seen_monitor(1'b1)
);
'''

ANT = '''
ANT #(.DWID(DWIDPY)) INST (.clk(CLK),.rst_n(rst_n)
    ,.rou_in(IN),.rou_out(OUT),.ack_in(ack_IN),.ack_out(ack_OUT)
    ,.rou_in_seen(IN_seen) ,.rou_out_seen(OUT_seen)
    ,.pages(PAGES),.whoami(SELF_ID)
);
'''

RAM = '''
rou_ram #(.DWID(DWIDPY),.DEPTH(DEPTHPY)) INST (.clk(clk),.rst_n(rst_n)
    ,.rou_in(IN),.rou_out(OUT),.ack_in(ack_IN),.ack_out(ack_OUT)
    ,.rou_in_seen(IN_seen) ,.rou_out_seen(OUT_seen)
);
'''

CLKCHANGE = '''
rou_changeclk #(.DWID(DWIDPY)) INST (.clka(CLKA),.rsta_n(rst_n)
    ,.roua_in(IN0) ,.roua_in_seen(IN0_seen),.acka_in(ack_IN0)
    ,.clkb(CLKB),.roub_out(OUT0),.roub_out_seen(OUT0_seen),.ackb_out(ack_OUT0)
);
'''



SWITCH2 = '''
rou_switch2 #(.DWID(DWIDPY)) INST (.clk(clk),.rst_n(rst_n)
    ,.rou0_in(IN0),.rou0_out(OUT0),.ack0_in(ack_IN0),.ack0_out(ack_OUT0),.rou_in0_seen(IN0_seen) ,.rou_out0_seen(OUT0_seen)
    ,.rou1_in(IN1),.rou1_out(OUT1),.ack1_in(ack_IN1),.ack1_out(ack_OUT1),.rou_in1_seen(IN1_seen) ,.rou_out1_seen(OUT1_seen)
);
'''


SWITCH3 = '''
rou_switch3 #(.DWID(DWIDPY)) INST (.clk(clk),.rst_n(rst_n)
    ,.rou0_in(IN0),.rou0_out(OUT0),.ack0_in(ack_IN0),.ack0_out(ack_OUT0)
    ,.rou1_in(IN1),.rou1_out(OUT1),.ack1_in(ack_IN1),.ack1_out(ack_OUT1)
    ,.rou2_in(IN2),.rou2_out(OUT2),.ack2_in(ack_IN2),.ack2_out(ack_OUT2)
);
'''


SWITCH4 = '''
rou_switch4 #(.DWID(DWIDPY)) INST (.clk(clk),.rst_n(rst_n)
    ,.rou0_in(IN0),.rou0_out(OUT0),.ack0_in(ack_IN0),.ack0_out(ack_OUT0)
    ,.rou1_in(IN1),.rou1_out(OUT1),.ack1_in(ack_IN1),.ack1_out(ack_OUT1)
    ,.rou2_in(IN2),.rou2_out(OUT2),.ack2_in(ack_IN2),.ack2_out(ack_OUT2)
    ,.rou3_in(IN3),.rou3_out(OUT3),.ack3_in(ack_IN3),.ack3_out(ack_OUT3)
);
'''


BASEINSTANCES = {}
BASEINSTANCES['admin'] = ADMIN
BASEINSTANCES['ant'] = ANT
BASEINSTANCES['ram'] = RAM
BASEINSTANCES['changeclk'] = CLKCHANGE
BASEINSTANCES['switch2'] = SWITCH2
BASEINSTANCES['switch3'] = SWITCH3
BASEINSTANCES['switch4'] = SWITCH4



def getInst(Type):
    if Type in BASEINSTANCES:
        return BASEINSTANCES[Type]

    if ('ant' in Type)and(Type.index('ant')==0):
        Base = BASEINSTANCES['ant']
        Base = string.replace(Base,'ANT',Type)
        return Base

    log_error('getInst: no base for "%s"'%(Type))
    return ''
    


