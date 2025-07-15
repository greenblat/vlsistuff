#! /usr/bin/env python3
HelpString = '''
invocation:

genver.py  <infile> [<outfile>] [... more params passed to the infile]

this script can be used for any source language, better give outfile name
if it is not verilog.


this script generates verilog code from annotated pythoned 
verilog code.
cut out the example section and run the script on it.

all lines that start with # are special lines and python
executes them.   python section ends with bare #.

for longer pure python code, use "###" line to start the section 
and "###" to end the sectio,

#< is used in de-indent  pure verilog.


#AAA = argv(0)   <<< this code will assign to variable AAA the third param in invocation.
#BBB = argv(1)   <<< this code will assign to variable AAA the third param in invocation.
first param is the executable name (usually execme.py)
second param is the is the first user param.
noice that full ivocation line would be:
genver.py inputfile outputfile firstUserParam secondUserParam ....
if You use the above mechbism, in it is a good idea to append the module name with key parameter vars.
and also modify the output file name accordingly.


 kinda primitive macro definition:
#defcode CUCU  AAA BBB
wire AAA = !BBB;
#enddef

#code CUCU www aaa&bbb

# <>3+4<> will print 7


enjoy,
Ilia

Example:

module tx17out (input [7:0] chipid
#for I in range(17):
#    J = I+1
  ,input [15:0] pcktinJ 
  ,output reg  availI 
  ,output reg  [15:0] chI 
#    
);

#for I in range(17):
reg [15:0] holdI;
always begin
     availI = 1;
     chI = 0;
     wait(|pcktinI);
     holdI = pcktinI;
     availI = 0;
     #(top.pool.length[holdI]);
     chI = holdI;
     #1;
end
#    

#for I in range(17):
wire [15:0] cucuI = 0
#    for J in range(17):
    || aaaJ_I
#<
  ;
#

endmodule

# this is the end of the example!!!!
'''

import os,sys

PYST = '#'
PYRE = PYST+'<'

BigHead='# -*- encoding: UTF8 -*-\nimport os,sys\n'

INCLUDE = '''
def include(Fname):
    lines = open(Fname).read()
    print(lines)

'''
OPEN = '''
outFile = open("FNAME","w")
'''
    
BigHead += INCLUDE
def main():
    global PYST,PYRE
    if len(sys.argv)==1:
        print(HelpString)
        return
    Fname = sys.argv[1]
    if len(sys.argv)>2:
        FnameOut = sys.argv[2]
    else:
        w1 = Fname.split('/')
        w2 = w1[-1].split('.')
        Top=w2[0]
        FnameOut = '%s.v'%Top
    if '-pyst' in sys.argv:
        PYST = getOper(sys.argv,'-pyst')
        PYRE = PYRE.replace('#',PYST)
        
        
    Big2 = run(Fname,FnameOut,sys.argv[3:])
    Open = OPEN.replace('FNAME',FnameOut)
    Big2  = Open + Big2
    try:
        exec(Big2,globals())
    except:
        print(Big2)
        print("FAILED")
        exec(Big2)

def sameNameV(Fname):   
    w1 = Fname.split('/')
    w2 = w1[-1].split('.')
    Top=w2[0]
    Path = '/'.join(w1[:-1])
    FnameOut = '%s/%s.v'%(Path,Top)
    return FnameOut

def getOper(Argv,Key):
    if Key not in Argv: return False
    Ind = Argv.index(Key)
    return Argv[Ind+1]


def run(Fname,FnameOut,Args):
    File = open(Fname)
    lines = File.readlines()
    File.close()
    if not FnameOut:
        FnameOut = sameNameV(Fname)
    Big2 = runFromLines(lines,FnameOut,Args)
    return Big2

def runFromLines(lines,FnameOut,Args):
    global Code0,Strings
    Code0=[]
    Strings={}
    Big = [BigHead]
    lines=extract_codelins(lines)
    lines = expand_codelins(lines)
    prepare1(lines)
    Big.append('Strings={}')
    for X in Strings:
        Big.append("Strings['%s']='''"%X)
        XX = Strings[X]
        XX = rework_backs(XX)
        Big.append(XX)
        Big.append("'''")
    Big.append(Routines)
    for X in Code0:
        Big.append(X)

    Big = [FUNCTIONS] + Big 
    Big2 = '\n'.join(Big)
    Big2 = Big2.replace('\n\n','\n')
#    print(Big2)
    return Big2

#    Fout = open('execme.py','w')
#    Fout.write(FUNCTIONS)
#    for LL in Big:
#        if LL[-1]!='\n': LL += '\n'
#        Fout.write(LL)
#    Fout.close()
#    More = ' '.join(Args)
#    Work = 'python3 execme.py "%s" > %s'%(More,FnameOut)
#    os.system(Work)
#    os.system('/bin/rm  execme.py')

def rework_backs(Str):
    Str1 = Str.replace('\\n','\\\\n')
    return Str1
Bags={}
def extract_codelins(lines):
    state='idle'
    Bag = []
    res = []
    for line in lines:
        if (state=='idle'):
            if '#defcode' in line:
                wrds = line.split()
                state='work'
                Name=wrds[1]
                Bag=[wrds]
                Bags[Name]=Bag
            else:
                res.append(line)
        elif (state=='work'):
            if '#enddef' in line:
                state='idle'
                Bag=[]
            else:
                Bag.append(line)
    return res


Routines = '''

def get_argv(Name,Default):
    WW = sys.argv[1].split()
    for Arg in WW:
        if Arg.startswith(Name+'='):
            xx = Arg.split('=')
            try:
                return eval(xx[1])
            except:
                return xx[1]
    return Default


def argv(Ind):
    WW = sys.argv[1].split()
    if Ind<len(WW):
        return WW[Ind]
    return ''


def clog2(In):
    return len(bin(In))-2

Vars={}
def formati(Var,Val):
    if len(Val)==0:
        return '<>1<>'
    if len(Var)==0:
        return '<>2<>'
    if Val[0] in '0123456789':
        if (len(Var)>1)and(Var[1] in '0123456789'):
            if Var[0]=='X':
                V1 = '%x'%int(Val)
            elif (Var[0]=='B'):
                V1 = bin(int(Val))
                V1 = V1[2:]
            elif (Var[0]=='D'):
                V1 = str(int(Val))
            else:
                return Val
            Wid = int(Var[1])
            while len(V1)<Wid:
                V1 = '0'+V1
            return V1                
    return Val


def evalStuff(Str):
    wrds = Str.split('<>')
    if len(wrds)<3: return Str
    Varsi = {}
    for Var in Vars:
        Val = Vars[Var]
        try:
            Varsi[Var]=int(Val)
        except:
            pass
    for II in range(1,len(wrds),2):
        try:
            New = eval(wrds[II],{},Varsi)
            wrds[II] = str(New)
        except:
            try:
                exec("NxiX = %s"%wrds[II])
                wrds[II] = str(NxiX)
            except:
                print('// failed eval of "%s"'%(wrds[II]))
    Str2 = ''.join(wrds)
    return Str2


def print_Strings(Str):
    X = Strings[Str][:]
    X = evalStuff(X)



    if X[0]=='\\n':
        X = X[1:]
    res=[]
    for Var in Vars:
        res.append((len(Var),Var,Vars[Var]))
    res.sort()
    res.reverse()
    for _,Var,Val in res:
        X = X.replace(Var,formati(Var,Val))
    print(X[:-1],sep=" ", end="\\n", file=outFile)
        


'''

def expand_codelins(lines):
    res = []
    for line in lines:
        if '#code' in line:
            more = get_code(line)
            res.extend(more)
        else:
            res.append(line)
            
    return res


def get_code(Str):
    wrds = Str.split()
    Name = wrds[1]
    if Name not in Bags:
        print('name %s not in bags %s'%(Name,Bags.keys()))
        return []
    Mlines = Bags[Name]
    Header =Mlines[0]
    Mlines.pop(0)
    Vars = get_code_vars(Header)
    update_code_vars(Vars,wrds)
    res=[]
    print('// >mlines>>>>',Mlines)
    print('// >vars>>>>',Vars)
    for line in Mlines:
        for Var in Vars:
            line = line.replace(Var,Vars[Var])
        res.append(line)
    return res

def get_code_vars(Header):
    Vars={}
    for Var in Header:
        if '=' in Var:
            ww =Var.split('=')
            Vars[ww[0]]=ww[1]
        else:
            Vars[Var]=''
    return Vars

def update_code_vars(Vars,wrds):
    for wrd in wrds:
        if ('=' in wrd):
            ww =wrd.split('=')
            Vars[ww[0]]=ww[1]
    return Vars





def prepare1(lines):
    global Indent,Lnum
    state='idle'
    Str = ''
    Indent=''
    Lnum=0
    for line in lines:
        Lnum += 1
        if (state=='idle'):
            if (len(line)>3)and(line[0:3]=='###'):
                state='longcode'
                if (Str!=''):
                    Sname = strname()
                    Strings[Sname]=Str
                    Str=''
                    Code0.append("print_Strings('%s')\n"%Sname)
            elif (len(line)>0)and(line.startswith(PYST)):
                if (Str!=''):
                    Sname = strname()
                    Strings[Sname]=Str
                    Str=''
                    Code0.append("print_Strings('%s')\n"%Sname)
                Code0.append(line[len(PYST):])
                Indent = calc_indent(line[len(PYST):])
                seek_vars(line[len(PYST):])
                state='code'
            else:
                Str = Str + line
        elif (state=='longcode'):
            if (len(line)>3)and(line[0:3]=='###'):
                state='idle'
            else:
                Code0.append(line)
                Indent = calc_indent(line)
                seek_vars(line)
        elif (state=='code'):
            wrds = line.split()
            if (len(line)>0)and(line.startswith(PYST))and(Str!=''):
                Sname = strname()
                Strings[Sname]=Str
                Str=''
                Code0.append("%sprint_Strings('%s')\n"%(Indent,Sname))
                
            if (len(line)>0)and(len(wrds)>0)and(wrds[0].startswith(PYST))and(len(wrds)==1):
                state='idle'
#                Code0.append('Vars={}')    
                Indent=''
            elif (len(line)>2)and(line.startswith(PYRE)):
                Indent = Indent[4:]
                state='code'
            elif (len(line)>0)and(line.startswith(PYST)):
                Code0.append(line[len(PYST):])
                Indent = calc_indent(line[len(PYST):])
                seek_vars(line[len(PYST):])
            else:
                state='string'
                Str = Str + line
        elif (state=='string'):
            wrds = line.split()
            if (len(line)>0)and(line.startswith(PYST))and(Str!=''):
                Sname = strname()
                Strings[Sname]=Str
                Str=''
                Code0.append("%sprint_Strings('%s')\n"%(Indent,Sname))
                state='code'
                
            if (len(line)>2)and(line.startswith(PYRE)):
                Indent = Indent[4:]
                state='code'
            elif (len(line)>0)and(line.startswith(PYST))and(len(wrds)==1)and(len(wrds[0])==len(PYST)):
                state='idle'
#                Code0.append('Vars={}')    
                Indent=''
            elif (len(line)>0)and(line.startswith(PYST)):
                Code0.append(line[len(PYST):])
                Indent = calc_indent(line[len(PYST):])
                seek_vars(line[len(PYST):])
                state='code'
            else:
                state='string'
                Str = Str + line





    if (Str!=''):
        Sname = strname()
        Strings[Sname]=Str
        Str=''
        Code0.append("print_Strings('%s')\n"%Sname)
        

def seek_vars(line):
    wrds = line.split()
    if len(wrds)<3:
        pass
    elif wrds[0]=='for':
        Wrd = wrds[1]
        if ',' in Wrd:
            Wrds = Wrd.split(',')
            for Var in Wrds:
                Code0.append('%sVars["%s"]=str(%s)\n'%(Indent,Var,Var))    
        else:
            Code0.append('%sVars["%s"]=str(%s)\n'%(Indent,wrds[1],wrds[1]))    
    elif wrds[1]=='=':
        if ',' not in wrds[0]:
            Code0.append('%sVars["%s"]=str(%s)\n'%(Indent,wrds[0],wrds[0]))    
        else:        
            ww = wrds[0].split(',')
            for ww0 in ww:
                Code0.append('%sVars["%s"]=str(%s)\n'%(Indent,ww0,ww0))    

def calc_indent(line):
    wrds = line.split()    
    if len(wrds)==0:
        print('lnum=%d in file, fatal ident, aborting. '%(Lnum))
        sys.exit()
        
    ind = line.index(wrds[0])
    if wrds[0] in ['for','if','else:','elif']:
        ind += 4
    return ' '*ind
      
                
StrNum = 0
def strname():
    global StrNum
    N = 'str%d'%StrNum
    StrNum += 1
    return N
FUNCTIONS = '''

def bits(Prm): 
    return len(bin(Prm))-2

def apb_slave(AWID,DWID):
    print(\'\'\'
  ,input [15:0] paddr
  ,input       penable
  ,output [31:0] prdata
  ,output       pready
  ,input       psel
  ,output       pslverr
  ,input [31:0] pwdata
  ,input       pwrite

    \'\'\')

def axi_wr_master(PREF,AWID,DWID,LWID,IDWID):
    print(\'\'\'
    ,output [3:0] Pawid            
    ,output [31:0] Pawaddr
    ,output [7:0] Pawlen
    ,output [2:0] Pawsize
    ,output [1:0] Pawburst
    ,output [3:0] Pawcache
    ,output [3:0] Pawqos
    ,output [2:0] Pawprot
    ,output Pawvalid
    ,input Pawready
    ,output [DWID-1:0] Pwdata
    ,output [DWID/8-1:0] Pwstrb
    ,output Pwlast
    ,output Pwvalid
    ,input Pwready
    ,input [3:0] Pbid 
    ,input [1:0] Pbresp
    ,input Pbvalid
    ,output Pbready
    \'\'\'.replace('P',PREF))

def axi_rd_master(PREF,AWID,DWID,LWID,IDWID):
    print(\'\'\'
    ,output [3:0] Parid
    ,output [31:0] Paraddr
    ,output [7:0] Parlen
    ,output [2:0] Parsize
    ,output [1:0] Parburst
    ,output [3:0] Parcache
    ,output [3:0] Parqos
    ,output [2:0] Parprot
    ,output Parvalid
    ,input Parready
    ,input [3:0] Prid 
    ,input [DWID-1:0] Prdata
    ,input [1:0] Prresp
    ,input Prlast
    ,input Prvalid
    ,output Prready
    \'\'\'.replace('P',PREF))

def axi_wr_slave(PREF='',AWID=32,DWID=64,LWID=8,IDWID=4):
    print(\'\'\'
    ,input [3:0] Pawid            
    ,input [31:0] Pawaddr
    ,input [7:0] Pawlen
    ,input [2:0] Pawsize
    ,input [1:0] Pawburst
    ,input [3:0] Pawcache
    ,input [3:0] Pawqos
    ,input [2:0] Pawprot
    ,input Pawvalid
    ,output Pawready
    ,input [DWID-1:0] Pwdata
    ,input [DWID/8-1:0] Pwstrb
    ,input Pwlast
    ,input Pwvalid
    ,output Pwready
    ,output [3:0] Pbid 
    ,output [1:0] Pbresp
    ,output Pbvalid
    ,input Pbready
    \'\'\'.replace('P',PREF))

def axi_rd_slave(PREF='',AWID=32,DWID=64,LWID=8,IDWID=4):
    print(\'\'\'
    ,input [3:0] Parid
    ,input [31:0] Paraddr
    ,input [7:0] Parlen
    ,input [2:0] Parsize
    ,input [1:0] Parburst
    ,input [3:0] Parcache
    ,input [3:0] Parqos
    ,input [2:0] Parprot
    ,input Parvalid
    ,output Parready
    ,output [3:0] Prid 
    ,output [DWID-1:0] Prdata
    ,output [1:0] Prresp
    ,output Prlast
    ,output Prvalid
    ,input Prready
    \'\'\'.replace('P',PREF))

def axi_slave(PREF='',AWID=32,DWID=64,LWID=8,IDWID=4):
    axi_wr_slave(PREF,AWID,DWID,LWID,IDWID)
    axi_rd_slave(PREF,AWID,DWID,LWID,IDWID)




def axi_master(PREF='',AWID=32,DWID=64,LWID=8,IDWID=4):
    axi_wr_master(PREF,AWID,DWID,LWID,IDWID)
    axi_rd_master(PREF,AWID,DWID,LWID,IDWID)

def axi_rd_conn():
    print(\'\'\'
    ,arid(arid)
    ,araddr(araddr)
    ,arlen(arlen)
    ,arsize(arsize)
    ,arburst(arburst)
    ,arcache(arcache)
    ,arqos(arqos)
    ,arprot(arprot)
    ,arvalid(arvalid)
    ,arready(arready)
    ,rid(rid)
    ,rdata(rdata)
    ,rresp(rresp)
    ,rlast(rlast)
    ,rvalid(rvalid)
    ,rready(rready)
    \'\'\')

def axi_wr_conn():
    print(\'\'\'
    ,.awid(awid)
    ,.awaddr(awaddr)
    ,.awlen(awlen)
    ,.awsize(awsize)
    ,.awburst(awburst)
    ,.awcache(awcache)
    ,.awqos(awqos)
    ,.awprot(awprot)
    ,.awvalid(awvalid)
    ,.awready(awready)
    ,.wdata(wdata)
    ,.wstrb(wstrb)
    ,.wlast(wlast)
    ,.wvalid(wvalid)
    ,.wready(wready)
    ,.bid (bid )
    ,.bresp(bresp)
    ,.bvalid(bvalid)
    ,.bready(bready)
    \'\'\')


def apb_conn():
    print(\'\'\'
    ,.paddr(paddr)
    ,.penable(penable)
    ,.prdata(prdata)
    ,.pready(pready)
    ,.psel(psel)
    ,.pslverr(pslverr)
    ,.pwdata(pwdata)
    ,.pwrite(pwrite)

    \'\'\')

def syncfifo(NAME='syncfifo'):
    print(\'\'\'
syncfifo #(.WID(WID),.DEPTH(DEPTH)) NAME (
    .clk(clk),.rst_n(rst_n)
    ,.vldin(vldin)
    ,.din(din)
    ,.readout(readout)
    ,.empty(empty)
    ,.dout(dout)
    ,.full(full)
    ,.count(in_count)
);

    \'\'\'.replace('NAME',NAME))

'''


if (__name__ == '__main__'): main()
