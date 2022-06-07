#! /usr/bin/env python3
helpString = '''
 usage:
ramLatchGen.py <RamName> <Data wid> <NumOfDatas> <LineWid>

'''
import os,sys,string

def main():
    if len(sys.argv) == 1:
        print(helpString)
        return
    Fname = sys.argv[1]
    Dwid = eval(sys.argv[2])
    Lines = eval(sys.argv[3])
    if len(sys.argv) == 4:
        Idwid = Dwid
    else:
        Idwid = eval(sys.argv[4])

    Bytes = int(Idwid/8)
    Bytes0 = int(Dwid/8)
    Fout = open("%s.v" % Fname,'w')
    Head = HEADER.replace('RAMX',Fname)
    Head = Head.replace("DWID",str(Dwid-1))
    MsbA = (Lines-1).bit_length()-1 
    Head = Head.replace("AWID",str(MsbA))
    Head = Head.replace("BYTES",str(Bytes0-1))

    Fout.write(Head)

    Defs = DEFS.replace('IDW',str(Idwid-1))
    if (Idwid == Dwid):
        Defs = Defs.replace('DEPTH',str(Lines-1))
        Aspect = 1
        LL = Lines
        LsbA = 0
    else:
        X = int(Idwid/Dwid)
        Aspect = X
        if X not in [1,2,4,8,16]:
            print('line width should be power2 multiple of DWID')
            return
        LL = int(Lines/X)
        Defs = Defs.replace('DEPTH',str(LL-1))
    Fout.write(Defs)
    for Byte in range(Bytes):
        Fout.write('reg [7:0] bytes%d [0:%d];\n' % (Byte,LL-1))

    Str = []

    if Aspect == 1:
        for X in range(Bytes-1,-1,-1):
            Str.append('bytes%d[addr]' % X)
        Str = ','.join(Str)
        Str0 = 'always @(posedge clk) if (!cen && wen) qqq <= {%s};\n' % (Str)
        Str0 += 'assign dout = qqq;\n'
        LsbA = 0
    elif Aspect == 2:
        Str0 = 'reg was0; always @(posedge clk) was0 <= addr[0];\n'
        for X in range(Bytes-1,-1,-1):
            Str.append('bytes%d[addr[%s:1]]' % (X,MsbA))
        Str = '\n   ,'.join(Str)
        Str0 += 'always @(posedge clk) if (!cen && wen) qqq <= {%s};\n' % (Str)
        Str0 += 'assign dout = was0 ? qqq[%s:%s] : qqq[%s:0];\n' % (Idwid-1,Dwid,Dwid-1)
        LsbA = 1
    elif Aspect == 4:
        Str0 = 'reg [1:0] was0; always @(posedge clk) was0 <= addr[1:0];\n'
        for X in range(Bytes-1,-1,-1):
            Str.append('bytes%d[addr[%s:2]]' % (X,MsbA))
        Str = '\n   ,'.join(Str)
        Str0 += 'always @(posedge clk) if (!cen && wen) qqq <= {%s};\n' % (Str)
        Str0 += 'assign dout = (was0==0) ? qqq[%s:0] : (was0==1) ? qqq[%s:%s] : (was0==2) ? qqq[%s:%s] : qqq[%s:%s];\n' % (
                 Dwid-1,2*Dwid-1,Dwid,3*Dwid-1,2*Dwid,4*Dwid-1,3*Dwid)
        LsbA = 2
    elif Aspect == 8:
        Str0 = 'reg [2:0] was0; always @(posedge clk) was0 <= addr[2:0];\n'
        for X in range(Bytes-1,-1,-1):
            Str.append('bytes%d[addr[%s:2]]' % (X,MsbA))
        Str = '\n   ,'.join(Str)
        Str0 += 'always @(posedge clk) if (!cen && wen) qqq <= {%s};\n' % (Str)
        Str0 += 'assign dout = (was0==0) ? qqq[%s:0]\n    : (was0==1) ? qqq[%s:%s]\n    : (was0==2) ? qqq[%s:%s]\n    : (was0==3) ? qqq[%s:%s]\n    : (was0==4) ? qqq[%s:%s]\n    : (was0==5) ? qqq[%s:%s]\n    : (was0==6) ? qqq[%s:%s]\n    : qqq[%s:%s];\n' % (
                 Dwid-1,2*Dwid-1,Dwid,3*Dwid-1,2*Dwid,4*Dwid-1,3*Dwid,5*Dwid-1,4*Dwid,6*Dwid-1,5*Dwid,7*Dwid-1,6*Dwid,8*Dwid-1,7*Dwid)
        LsbA = 3
    else:
        print('aspect %s not supported yet' % Aspect)
    Fout.write(Str0)
    for X in range(LL):
        Fout.write('always @* if (clk && !wen_l && (addr_l[%s:%s] == %d)) begin\n' % (MsbA,LsbA,X))
        M,L,Ind = 7,0,0
        Sign = '!'
        Pos = 0
        for Byte in range(Bytes):
            if (Aspect == 1):
                Fout.write('    if (bytew_l[%d]) bytes%d[%d] = din_l[%d:%d];\n' % (Ind,Byte,X,M,L))
            elif (Aspect == 2):
                if Byte >= Bytes0:
                    Sign = ' '
                Fout.write('    if (bytew_l[%d] && %saddr_l[0]) bytes%d[%d] = din_l[%d:%d];\n' % (Ind,Sign,Byte,X,M,L))
            elif (Aspect == 4):
                Pos = int(Byte/Bytes0)
                Fout.write('    if (bytew_l[%d] && (addr_l[1:0] == %s)) bytes%d[%d] = din_l[%d:%d];\n' % (Ind,Pos,Byte,X,M,L))
            elif (Aspect == 8):
                Pos = int(Byte/Bytes0)
                Fout.write('    if (bytew_l[%d] && (addr_l[2:0] == %s)) bytes%d[%d] = din_l[%d:%d];\n' % (Ind,Pos,Byte,X,M,L))
            else:
                print('Aspect %s not supported yet' % Aspect)

            L = (L+8) % Dwid
            M = L + 7
            Ind = (Ind+1) % Bytes0
        Fout.write('end\n')

    Fout.write('endmodule\n')
    Fout.close()




HEADER = '''

module RAMX (input clk, input cen, input wen
    ,input  [DWID:0] din
    ,input  [BYTES:0] bytew
    ,input  [AWID:0] addr
    ,output [DWID:0] dout
);

reg [DWID:0] din_l;
reg [BYTES:0] bytew_l;
reg [AWID:0] addr_l;
reg wen_l;
always @* if (!clk) begin
    din_l = din;
    bytew_l = bytew;
    addr_l = addr;
    wen_l = cen ? 1 : wen;
end



'''

DEFS  = '''
reg [IDW:0] qqq;
'''



if __name__ == '__main__': main()
