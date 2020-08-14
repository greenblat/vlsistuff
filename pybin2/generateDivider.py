#! /usr/bin/python


import os,sys,string,math

PERSTAGE = 2
def main():

    if not os.path.exists('rtl3'): os.mkdir('rtl3')
    if len(sys.argv)==2:
        Fname = sys.argv[1]
        if os.path.exists(Fname):
            File = open(Fname)
            big = File.read()
            Macros = string.split(big)
            File.close()
            Fout = open('rtl3/dividers.v','w')
            for Macro in Macros: doTheWork(Macro,Fout)
            Fout.close()
        elif 'divider_' in Fname:
            Fout = open('rtl3/%s.v'%Fname,'w')
            byMacroName(Fname,Fout)
            Fout.close()
        elif 'divi_' in Fname:
            Fout = open('rtl3/%s.v'%Fname,'w')
            byMacroName(Fname,Fout)
            Fout.close()
    else:
        Aop = sys.argv[1]
        Bop = sys.argv[2]
        STAGES = int(sys.argv[3])
        Asigned,Awidth = parse0(Aop)
        Bsigned,Bwidth = parse0(Bop)
        Macro = 'divider_%s_%s_%s'%(Aop,Bop,STAGES)
        Fout = open('rtl3/%s.v'%Macro,'w')
        byMacroName(Macro,Fout)
        Fout.close()


def byMacroName(Macro,Fout,PERSTAGE=PERSTAGE):
    ww = string.split(Macro,'_')
    Aop = ww[1]
    Asigned,Awidth = parse0(Aop)
    Bop = ww[2]
    if len(ww)==4:
        STAGES = int(ww[3])
    elif len(ww)==3:
        STAGES = int(math.ceil(1.0*Awidth/PERSTAGE))
    else:
        print 'generateDivider expects either 3 params or 2 not "%s"'%(ww)
        return
    Bsigned,Bwidth = parse0(Bop)
    reportPipe(Macro,STAGES)

    if STAGES>2:
        bitsPerCycle = int(round(1.0*(Awidth)/(STAGES-2+1)))
        print 'here bitsper=%d stages=%d awidth=%d prestage=%d'%(bitsPerCycle,STAGES,Awidth,PERSTAGE)
        Puts = STAGES-2
        places = []
        for II in range(Puts):
            places.append(Awidth - bitsPerCycle*(1+II))

        if len(places)>2:
            Diff0 = places[-1]
            Diff1 = places[-2]-places[-1]
            if (Diff1-Diff0)>1:
                places[-1] +=1 
            elif (Diff0-Diff1)>1:
                places[-1] -=1 

    else:
        places=[]




    if 'udiv' in Macro:
        Fout.write(HEADER1_U%(Macro,Awidth-1,Bwidth-1,Awidth-1,Bwidth-2))
    else:
        Fout.write(HEADER1%(Macro,Awidth-1,Bwidth-1,Awidth-1,Bwidth-2))
    Fout.write('// stages=%d places=%s\n'%(STAGES,places))
    addReg(1,1,'vldin','vld1',Fout)
    widA = Awidth+Bwidth
    if Asigned:
        Fout.write('wire signA = ain[%d];\n'%(Awidth-1))
        Fout.write('wire [%d:0] absain = signA ? -ain : ain;\n'%(Awidth-1))
        addReg(widA,Awidth,'absain','ain1',Fout)
    else:
        addReg(widA,Awidth,'ain','ain1',Fout)

    if Bsigned:
        Fout.write('wire signB = bin[%d];\n'%(Bwidth-1))
        Fout.write('wire [%d:0] absbin = signB ? -bin : bin;\n'%(Bwidth-1))
        addReg(Bwidth,Bwidth,'absbin','bin1',Fout)
    else:
        addReg(Bwidth+1,Bwidth,'bin','bin1',Fout)

    if (Asigned and Bsigned):
        addReg(0,0,'signA^signB','sign1',Fout)
##        Fout.write('wire sign1 = signA ^ signB;\n')
    elif (Asigned):
##        Fout.write('wire sign1 = signA;\n')
        addReg(0,0,'signA','sign1',Fout)
    elif (Bsigned):
        addReg(0,0,'signB','sign1',Fout)
##        Fout.write('wire sign1 = signB;\n')
    elif 'udiv' in Macro:
        addReg(0,0,'negate','sign1',Fout)
##        Fout.write('wire sign1 = negate;\n')
        
    if ('udiv' in Macro) and (Asigned or Bsigned):
        print 'udiv macro (%s) should not have signed operands!!!!'%(Macro)
        sys.exit()


    keepSign = Asigned or Bsigned or ('udiv' in Macro)


    III = 1
    runW = widA
    hasRegs=''

    while III<Awidth:
        addStage(III,runW,Bwidth+1,Fout,keepSign,hasRegs)
        runW -= 1
        III += 1

        if III in places:
            hasRegs = 'pre_'
        else:
            hasRegs = ''

    addStage(III,runW,Bwidth+1,Fout,keepSign,'')
    if keepSign:
        Fout.write('wire [%d:0] signedres = (bin%d==0) ? %d\'b0 : sign%d ? -res%d : res%d ;\n'%(Awidth-1,III+1,Awidth,III+1,III+1,III+1))
        addReg(Awidth,Awidth,'signedres','out',Fout)
    else:
        Fout.write('wire [%d:0] res000 = (bin%d==0) ? %d\'b0 : res%d ;\n'%(Awidth-1,III+1,Awidth,III+1))
        addReg(Awidth,Awidth,'res000','out',Fout)
    addReg(Bwidth-1,Bwidth-1,'ain%d'%(III+1),'remainder',Fout)
    addReg(1,1,'vld%d'%(III+1),'vldout',Fout)
    Fout.write('endmodule\n')


HEADER1 = '''
module %s ( input clk,input rst_n,input en, input vldin,output reg vldout, input [%d:0] ain, input [%d:0] bin, output reg  [%d:0] out,output reg [%d:0] remainder);
'''
HEADER1_U = '''
module %s ( input clk,input rst_n,input en, input vldin,input negate, output reg vldout, input [%d:0] ain, input [%d:0] bin, output reg  [%d:0] out,output reg [%d:0] remainder);
'''

def addStage(Index,runWidth,Bwidth,Fout,keepSign,hasRegs=''):
    Hi = runWidth-1
    Lo = runWidth-Bwidth

    Fout.write('\n\nwire bit%d = (bin%d <= ain%d[%d:%d]);\n'%(Index, Index,Index,Hi,Lo))
    Fout.write('wire [%d:0] xhigh%d = ain%d[%d:%d]-bin%d;\n'%(Bwidth-1,Index,Index,Hi,Lo,Index))
    Fout.write('wire [%d:0] high%d = bit%d ? xhigh%d[%d:0] : ain%d[%d:%d] ;\n'%(Bwidth-2,Index,Index,Index,Bwidth-2,Index,Hi-1,Lo))
    XX = runWidth-Bwidth-2
    if XX== -1:
        Fout.write('wire [%d:0]  %sain%d = {high%d,ain%d[0]};\n'%(runWidth-2,hasRegs,Index+1,Index,Index))
    elif XX<0:
        Fout.write('wire [%d:0]  %sain%d = high%d;\n'%(runWidth-2,hasRegs,Index+1,Index))
    else:
        Fout.write('wire [%d:0]  %sain%d = {high%d,ain%d[%d:0]};\n'%(runWidth-2,hasRegs,Index+1,Index,Index,runWidth-Bwidth-1))
    if Index==1:
        Fout.write('wire %sres%d = bit%d;\n'%(hasRegs,Index+1,Index))
    else:
        Fout.write('wire [%d:0]  %sres%d = {res%d,bit%d};\n'%(Index-1,hasRegs,Index+1,Index,Index))

    if hasRegs!='':
        Fout.write('\n')
        addReg(runWidth-1,runWidth-1,'%sain%d'%(hasRegs,Index+1),'ain%d'%(Index+1),Fout)
        addReg(Bwidth,Bwidth,'bin%d'%Index,'bin%d'%(Index+1),Fout)
        addReg(Index,Index,'%sres%d'%(hasRegs,Index+1),'res%d'%(Index+1),Fout)
        addReg(1,1,'vld%d'%(Index),'vld%d'%(Index+1),Fout)
        if keepSign:
            addReg(1,1,'sign%d'%(Index),'sign%d'%(Index+1),Fout)
    else:
        Fout.write('wire [%d:0] bin%d = bin%d;\n'%(Bwidth-1,Index+1,Index))
        Fout.write('wire vld%d = vld%d;\n'%(Index+1,Index))
        if keepSign:
            Fout.write('wire sign%d = sign%d;\n'%(Index+1,Index))
        

def addReg(Width,widIn,nameIn,nameOut,Fout):
    if Width==widIn:
        In = nameIn
    else:
        In = "{%d'b0,%s}"%(Width-widIn,nameIn)
    if nameOut not in ['out','remainder','vldout']:
        if Width>1:
            Fout.write('reg [%d:0] %s;\n'%(Width-1,nameOut))
        else:
            Fout.write('reg %s;\n'%(nameOut))
    Fout.write('always @(posedge clk) if (en) %s <= %s;\n'%(nameOut,In))
#    Fout.write('inu_ff #(.DATA_WIDTH(%d)) %s_reg (.clk(clk),.rst_n(rst_n),.en(en),.d(%s),.q(%s));\n'%(Width,nameOut,In,nameOut))

def reportPipe(Macro,Depth):
    if not os.path.exists('pipelines'): os.mkdir('pipelines')
    Fout= open('pipelines/%s.depth'%Macro,'w')
    Fout.write('%s %d\n'%(Macro,Depth))
    Fout.close()


    

def parse0(Op):
    Signed = Op[0]=='s'
    Wid = int(Op[1:])
    return Signed,Wid

if (__name__ == '__main__'): main()


