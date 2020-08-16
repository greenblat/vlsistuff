#! /usr/bin/env python3
'''
    invocation:   ram_gen.py -width 10 -depth 20 [-name myram] [-help] [-mon] [-addr Addr] [-din Din] [-dout Dout] [-wr wr | ~wr] [-cs cs | ~cs] [-clk Clk]
    kmon will add $display lines to verilog to help keep track of writes/reads.
    -din -dout -addr -cs -wr  -clk : all these enable renaming of pins.
    -cs and -wr have option to have ~ infront. it makes them active low.
'''
import os,sys,string,types

def main():
    Params = parse_args()
    if 'help' in Params:
        print(__doc__)
        return
    create_defaults(Params)
    create_ram(Params)
def create_defaults(Params):
    if 'name' not in Params:
        Wid = paramx(Params,'width')
        Dep = paramx(Params,'depth')
        Name = 'ram%s_%s'%(Wid,Dep)
        Params['name']=Name
    for Pin in ['cs','wr','din','dout','addr','clk']:
        if Pin not in Params:
            Params[Pin]=Pin

    if 'wmask' not in Params:
        Params['wmask']=False

    if Params['cs'][0]=='~':
        Params['acs']='~'+Params['cs']
    else:
        Params['acs']=Params['cs']
        
    if Params['wr'][0]=='~':
        Params['awr']='~'+Params['wr']
        Params['negawr']=Params['wr']
    else:
        Params['awr']=Params['wr']
        Params['negawr']='~'+Params['wr']

ReplaceList = ['wmask','acs','negawr','awr','clk','addr','cs','wr','din','dout']

def createInstanceExample(File,Params,Wid,Dep,Name,Awid):
    if Params['wmask']:
        Stringx = InstMaskString
    else:
        Stringx = InstString
    Stringx = Stringx.replace('WID',str(Wid-1))
    Stringx = Stringx.replace('WAD',str(Awid-1))
    Stringx = Stringx.replace('NAME',Name)
    for Key in ReplaceList:
        KEY = Key.upper()
        Repl = paramx(Params,Key)
        if Repl:
            Stringx = Stringx.replace(KEY,Repl)
    File.write(Stringx)

def create_ram(Params):
    Wid = paramx(Params,'width')
    Dep = paramx(Params,'depth')
    Name = paramx(Params,'name')
    Awid = bits_needed(Dep)
    Fname = '%s.v'%(Name)
    print('>>>>>',Fname,Params,Name)
    File = open(Fname,'w')
    if Params['wmask']:
        Stringx = String0Mask
    else:
        Stringx = String0
    Stringx = Stringx.replace('WID',str(Wid-1))
    Stringx = Stringx.replace('WAD',str(Awid-1))
    Stringx = Stringx.replace('NAME',Name)
    for Key in ReplaceList:
        KEY = Key.upper()
        Repl = paramx(Params,Key)
        if Repl:
            Stringx = Stringx.replace(KEY,Repl)
    File.write(Stringx)
    File.write('reg [%d:0] mem [0:%d];\n'%(Wid-1,Dep-1))
    File.write('reg [%d:0] tmp;\n'%(Wid-1))
    if Dep<(1<<Awid):
        StrAddr = StringAddrPart 
    else:
        StrAddr = StringAddrFull 
    StrAddr = StrAddr.replace('ADDR',paramx(Params,'addr'))
    StrAddr = StrAddr.replace('DEPTH',str(paramx(Params,'depth')))
    File.write(StrAddr)

    if Params['wmask']:
        Stringx = String1Mask
    else:
        Stringx = String1
    Stringx = Stringx.replace('WID',str(Wid))
    for Key in ReplaceList:
        KEY = Key.upper()
        Repl = paramx(Params,Key)
        if Repl:
            Stringx = Stringx.replace(KEY,Repl)
    File.write(Stringx)
    if 'mon' in Params:
        Stringx = String2.replace('WID',str(Wid))
        for Key in ReplaceList:
            KEY = Key.upper()
            Repl = paramx(Params,Key)
            if Repl:
                Stringx = Stringx.replace(KEY,Repl)
        File.write(Stringx)
        
    File.write('endmodule\n')
    createInstanceExample(File,Params,Wid,Dep,Name,Awid)
    File.close()

InstString = '''
// example instance
// NAME NAME (.clk(CLK),.CS(CS),.WR(WR),.DIN(DIN),.DOUT(DOUT),.ADDR(ADDR));
'''
InstMaskString = '''
// example instance
// NAME NAME (.clk(CLK),.CS(CS),.WR(WR),.DIN(DIN),.DOUT(DOUT),.ADDR(ADDR),.WMASK(WMASK));
'''


String0 = '''
module NAME (input CLK,input CS,input WR
   ,input      [WID:0] DIN
   ,output     [WID:0] DOUT
   ,input     [WAD:0] ADDR
);
'''
String0Mask = '''
module NAME (input CLK,input CS,input WR
   ,input      [WID:0] DIN
   ,input      [WID:0] WMASK
   ,output     [WID:0] DOUT
   ,input     [WAD:0] ADDR
);
'''

StringAddrPart = '''
wire addr_ok = ((^ADDR)!==1'bx)&&(ADDR<DEPTH);
'''
StringAddrFull = '''
wire addr_ok = ((^ADDR)!==1'bx);
'''



String1 = '''
wire inps_ok = (^{CS,WR}!==1'bx)&&addr_ok;
assign #1 DOUT = tmp;
always @(posedge CLK) if (inps_ok && ACS && AWR) begin
    mem[ADDR]<=DIN;
end
always @(posedge CLK) begin
    if (inps_ok && ACS && NEGAWR) tmp <= mem[ADDR];
    else tmp <= WID'bx;
end
'''
String1Mask = '''
wire inps_ok = ((^{WMASK,CS,WR})!==1'bx)&&addr_ok;
assign #1 DOUT = tmp;
always @(posedge CLK) if (inps_ok && ACS && AWR) begin
    mem[ADDR]<=(WMASK & DIN)|(mem[ADDR] & ~WMASK);
end
always @(posedge CLK) begin
    if (inps_ok && ACS && NEGAWR) tmp <= mem[ADDR];
    else tmp <= WID'bx;
end
'''

String2 = '''
always @(posedge clk) begin
    if (inps_ok) begin
        if (ACS && AWR) begin
            $display(" @%d: ram %m write [%h] <= %h",$stime,ADDR,DIN);
        end
        if (ACS && NEGAWR) begin
            $display(" @%d: ram %m read %h <= [%h] ",$stime,mem[ADDR],ADDR);
        end
    end else if ($stime>1000) begin
        $display(" @%d: ram %m bad controls ADDR=%h CS=%h WR=%h",$stime,ADDR,CS,WR);
    end
end
'''

def parse_args():
    params={}
    fnames=[]
    state='idle'
    for X in sys.argv[1:]:
        if (state=='idle'):
            if (X[0]=='-'):
                state='param'
                Param = X[1:] 
            else:
                fnames += [X] 
        elif (state=='param'):
            if (X[0]=='-'):
                params[Param]='yes'
                state='param'
                Param = X[1:] 
            else:
                state='idle'
                params[Param]=mint(X)
    if (state=='param'):
        params[Param]='yes'
    if fnames!=[]:
        params['fnames']=fnames
    return params

def mint(X):
    try:
        return int(X)
    except:
        return X

def paramx(Params,Prm,Default=None):
    if Prm in Params:
        X = Params[Prm]
        if (type(X)is str)and(X[0]=='~'):
            return X[1:]
        try:
            return eval(X)
        except:
            return X
    if Default!=None:
        return Default
    print('ERROR! params was asked to get param=%s, not found and no default'%Prm)
    print('given params %s'%str(Params))
    print(__doc__)
    sys.exit()

def bits_needed(Int):
    Bin = bin(Int-1)[2:]
#    if (Bin[0]=='1')and('1' not in Bin[1:]):
#        return len(Bin)
    return len(Bin)



main()
