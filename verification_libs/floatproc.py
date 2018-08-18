
import os,sys,string,types,math
import veri
import logs
import generic_disasm


class floatProcClass:
    def __init__(self,Path0,Path1,xProgram,rawAsmName,Name='float'):
        self.Path = Path0
        self.Path1 = Path1
        self.Name=Name
        self.proga={}
        self.progb={}
        self.loadProgram(xProgram)
        self.starting_run=False
        self.Values=[]
        self.Was = '0'*32
        self.Bits={}
        self.simul = simulClass(rawAsmName,Name)

    def reportValues(self):
        for Dst,Val in self.Values:
            logs.log_info('floatproc values %s %s %f'%(self.Name,Dst,Val))
        self.Values=[]

    def loadAssembler(self,fname):
        File = open(fname)
        while 1:
            line = File.readline()
            if line=='': 
                File.close()
                return
            wrds = string.split(line)
            if (len(wrds)>=4)and(wrds[0]=='set')and(wrds[2]=='='):
                Var = wrds[1]
                Num = getNum(wrds[3])
                if wrds[-1]=='bits':
                    self.Bits[Num]=Var
                

# set K_MIN_DIST_OPTIC_CENTER = R36;
#set distortedout = R14 ; // bits

    def loadProgram(self,fname):
        File = open(fname)
        Addr = 0
        while 1:
            line = File.readline()
            if line=='': 
                File.close()
                return
            if ':::' in line:
                ll = line[line.index(':::')+3:-1]
                ll = string.strip(ll)
                ww = string.split(ll,';')
                if len(ww) in [2,3]:
                    w0 = string.strip(ww[0])
                    w1 = string.strip(ww[1])
                    self.proga[Addr]=w0
                    self.progb[Addr]=w1
                    Addr += 1
                else:
                    print 'badloadprogramline',len(ww),ll


    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))
    def peek1(self,Sig):
        return logs.peek('%s.%s'%(self.Path1,Sig))

    def run(self):
        self.starting0()
        self.starting1()
        self.monside('a')
        self.monside('b')
        self.bitarray()
        self.bitarray2('a')
        self.bitarray2('b')
        finish_code = self.peek('a0_finish_code')
        if finish_code==1:
            self.reportValues()


    def starting0(self):
        paddr = self.peek('paddr')
        if (paddr!=0):
            if self.starting_run: return
            self.starting_run=True
            self.dispf('inputs',self.INPUTS0)
            self.simul.run()
        else:
            self.starting_run=False


    def starting1(self):
        valid_in = self.peek('valid_in')
        taken_in = self.peek('taken_in')
        if (taken_in==1)and(valid_in==1):
            self.dispf('inputs',self.INPUTS1)
#            self.simul.run()

    def dispf(self,Why,SIGS):
        List = string.split(SIGS)
        res = 'dispf %s = '%(Why)
        for Sig in List:
            Val = self.peek1(Sig)
            Flt = logs.binary2float(Val)
            res += ' %s=%f'%(Sig,Flt)
            self.simul.setVar(Sig,Flt)
        logs.log_info3('catchInputs %s %s'%(self.Name,res))



    def monside(self,Side):
        awrite = self.peek(Side+'write')
        if awrite==1:
            awdata = self.peek(Side+'wdata')
            awaddr = self.peek(Side+'waddr')
            done=False
            Addr = 0
            Cind = 0
            Opcode = 0
            for Ind in [6,5,3,2,1,0]:
                flagName = '%s%d_write_dst%d_flag'%(Side,Ind,Ind)
                Flag = self.peek(flagName)
                if Flag and not done:
                    done=True
                    Addr = logs.intx(veri.peek_mem('%s.paddress'%(self.Path),str(Ind)))
                    Cind = Ind
                    if Ind>0:
                        Opcode = logs.intx(veri.peek_mem('%s.%sopcodes'%(self.Path,Side),str(Ind-1)))
                    else:
                        Opcode = logs.intx(veri.peek_mem('%s.%sopcodes'%(self.Path,Side),str(Ind)))
            self.catchWrite(Side,awaddr,awdata,Addr,Opcode,Cind) 

            Cind=0
            reverse_awrite = self.peek('reverse_%swrite'%Side)
            if reverse_awrite==1:
                awdata = self.peek('reverse_'+Side+'wdata')
                awaddr = self.peek('reverse_'+Side+'waddr')
                done=False
                Addr = 0
                for Ind in [0,1,2,3,5,6]:
                    flagName = '%s%d_write_dst%d_flag'%(Side,Ind,Ind)
                    Flag = self.peek(flagName)
                    if Flag and not done:
                        done=True
                        Cind=Ind
                        Addr = logs.intx(veri.peek_mem('%s.paddress'%(self.Path),str(Ind)))
                        if Ind>0:
                            Opcode = logs.intx(veri.peek_mem('%s.%sopcodes'%(self.Path,Side),str(Ind-1)))
                        else:
                            Opcode = logs.intx(veri.peek_mem('%s.%sopcodes'%(self.Path,Side),str(Ind)))
                self.catchWrite(Side,awaddr,awdata,Addr,Opcode,Cind) 

    def catchWrite(self,Side,awaddr,awdata,Addr,Opcode,Ind):
        if Side=='a':
            if Addr in self.proga:
                Text = self.proga[Addr]
            else:
                Text = ' a empty'
        if Side=='b':
            if Addr in self.progb:
                Text = self.progb[Addr]
            else:
                Text = ' b empty'
        Asm = generic_disasm.disasm(Opcode)
        Dst = getDst(Text)
        Float = logs.binary2float(awdata)
        self.Values.append((Dst,Float))
        logs.log_info3('catchWrite %s side=%s reg=%d wdata=%08x  (%f) paddr=%d %08x (%d) %s    %s '%(self.Name,Side,awaddr,awdata,Float,Addr,Opcode,Ind,Text,Asm))
        if Dst!='empty':
            self.simul.checkVar(Dst,Float,awdata)


    def bitarray(self):
        Now = veri.peek('%s.bitarray'%(self.Path))
        if Now != self.Was:
            for ii,newBit in enumerate(Now):
                oldBit = self.Was[ii]
                if newBit!=oldBit:
                    logs.log_info3('catchBitWrite %s bit=%d new=%s'%(self.Name,31-ii,newBit))
        self.Was=Now


    def bitarray2(self,Side):
        Addr = logs.intx(veri.peek_mem('%s.paddress'%(self.Path),str(0)))
        if Side=='a':
            if Addr in self.proga:
                Text = self.proga[Addr]
            else:
                Text = ' a empty'
        if Side=='b':
            if Addr in self.progb:
                Text = self.progb[Addr]
            else:
                Text = ' b empty'
        Dst = getDst(Text)

        a_write_bits0_flag = self.peek('%s0_write_bits0_flag'%Side)
        if a_write_bits0_flag==1:
            a0_dst_field = self.peek('%s0_dst_field'%Side)
            if a0_dst_field>0:
                abitwdata = self.peek('bitfile.%sbitwdata'%Side)
                if a0_dst_field not in self.Bits:
                    self.Bits[a0_dst_field] = -1
                Var = self.Bits[a0_dst_field]
                logs.log_info3('catchBitWrite  side=%s dst=%d (%s) wdata=%s   "%s"'%(Side,a0_dst_field,Dst,abitwdata,Text))

        Addr = logs.intx(veri.peek_mem('%s.paddress'%(self.Path),str(1)))
        if Side=='a':
            if Addr in self.proga:
                Text = self.proga[Addr]
            else:
                Text = ' a empty'
        if Side=='b':
            if Addr in self.progb:
                Text = self.progb[Addr]
            else:
                Text = ' b empty'
        Dst = getDst(Text)
        a_compare_valid = self.peek('%s_compare_valid'%Side)
        if a_compare_valid==1:
            dst_field = self.peek('%s1_dst_field'%Side)
            if dst_field>0:
                wdata = self.peek('%s_compare_out'%Side)
                Var = self.Bits[dst_field]
                logs.log_info3('catchBitWrite  compare side=%s dst=%d (%s) wdata=%s  "%s"'%(Side,dst_field,Var,wdata,Text))
            

def getNum(Txt):
    while Txt[0] not in '0123456789':
        Txt = Txt[1:]
    while Txt[-1] not in '0123456789':
        Txt = Txt[:-1]
    return int(Txt)


def getDst(Text):
    ww = string.split(Text)
    if (len(ww)>2)and(ww[1]=='='):
        return ww[0]
    if 'empty' in Text: return 'empty'
    return 'oopst "%s"'%Text




class simulClass:
    def __init__(self,AsmFile,Name):
        self.Vars={}
        self.nets={}
        self.lines1=[]
        self.lines=[]
        self.loadAsmFile(AsmFile)
        self.Name=Name

    def loadAsmFile(self,AsmFile):
        File = open(AsmFile)
        while 1:
            line = File.readline()
            if line=='': 
                return
            line = string.replace(line,';',' ; ')
            wrds = string.split(line)
            if len(wrds)>0: self.useWrds(wrds)


    def useWrds(self,wrds):
        if wrds[0]=='declare':
            self.nets[wrds[1]]=(wrds[2],int(wrds[3]))
        elif wrds[0]=='set':
            return
        elif wrds[0]=='finish':
            self.lines.append(('finish','finish'))
        elif wrds[1]=='=':
            Dst = wrds[0]
            if wrds[-1]==';': wrds.pop(-1)
            self.lines.append((Dst,wrds[2:]))

    def run(self):
        for Dst,Src in self.lines:
            if Dst=='finish':
                self.finish()
            else:
                Val = self.evaluate(Src)
                self.setVar(Dst,Val)
        
    def finish(self):
        print 'finishing'

    def evaluate(self,Src):
            
        if type(Src)==types.IntType: return Src
        if type(Src)==types.StringType: 
            if Src=='R0': return 0
            if Src in self.Vars: return self.Vars[Src]
            if Src[0] in string.digits: return eval(Src)

            logs.log_info('vars %s'%str(self.Vars.keys()))
            logs.log_error('@%s guessing value of "%s" to 0'%(self.Name,Src))
            self.Vars[Src]=0
            veri.finish()
            return 0


        if type(Src)==types.ListType: 
            if len(Src)==1: return self.evaluate(Src[0])
            if len(Src)==2:
                if Src[0]=='sqrt': 
                    return math.sqrt(self.evaluate(Src[1]))
                if Src[0]=='sin': 
                    return math.sin(self.evaluate(Src[1]))
                if Src[0]=='cos': 
                    return math.cos(self.evaluate(Src[1]))
                if Src[0]=='arctan': 
                    return math.atan(self.evaluate(Src[1]))
                if Src[0]=='arcsin': 
                    Op = self.evaluate(Src[1])
                    if abs(Op)>1.0: return 0
                    return math.asin(Op)
                if Src[0]=='arccos': 
                    Op = self.evaluate(Src[1])
                    if abs(Op)>1.0: return 0
                    return math.acos(Op)
                if Src[0]=='abs': 
                    Op = self.evaluate(Src[1])
                    return abs(Op)





            if len(Src)==3:
                if Src[1]=='-':
                    return self.evaluate(Src[0])-self.evaluate(Src[2])
                if Src[1]=='+':
                    return self.evaluate(Src[0])+self.evaluate(Src[2])
                if Src[1]=='*':
                    return self.evaluate(Src[0])*self.evaluate(Src[2])
                if Src[1]=='/':
                    B = self.evaluate(Src[2])
                    if B==0: return 0
                    return self.evaluate(Src[0])/self.evaluate(Src[2])
                if Src[1]=='==':
                    return self.evaluate(Src[0])==self.evaluate(Src[2])
                if Src[1]=='!=':
                    return self.evaluate(Src[0])!=self.evaluate(Src[2])
                if Src[1]=='>':
                    return self.evaluate(Src[0])>self.evaluate(Src[2])
                if Src[1]=='<':
                    return self.evaluate(Src[0])<self.evaluate(Src[2])
                if Src[1]=='<=':
                    return self.evaluate(Src[0])<=self.evaluate(Src[2])
                if Src[1]=='&&':
                    return self.evaluate(Src[0]) and self.evaluate(Src[2])
                if Src[1]=='||':
                    return self.evaluate(Src[0]) or self.evaluate(Src[2])
                if Src[0]=='dist2':
                    A = self.evaluate(Src[1])
                    B = self.evaluate(Src[2])
                    X = math.sqrt(A*A+B*B)
                    return X
                if Src[0]=='min':
                    A = self.evaluate(Src[1])
                    B = self.evaluate(Src[2])
                    X = min(A,B)
                    return X
                if Src[0]=='max':
                    A = self.evaluate(Src[1])
                    B = self.evaluate(Src[2])
                    X = max(A,B)
                    return X
                if Src[0]=='sqdist':
                    A = self.evaluate(Src[1])
                    B = self.evaluate(Src[2])
                    X = (A*A+B*B)
                    return X

            if len(Src)==4:
                if Src[0]=='dist3':
                    A = self.evaluate(Src[1])
                    B = self.evaluate(Src[2])
                    C = self.evaluate(Src[3])
                    X = math.sqrt(A*A+B*B+C*C)
                    return X
            if len(Src)==5:
                if Src[1] in ['?','?bit']:
                    Cond  = self.evaluate(Src[0])
                    if Cond:
                        return self.evaluate(Src[2])
                    else:
                        return self.evaluate(Src[4])


        logs.log_error('@%s failed to parse %s'%(self.Name,Src))
        return 0

    def setVar(self,Var,Val):
        Var = string.replace(Var,'flt_','')
        logs.log_info('simul @%s setVar %s = %s'%(self.Name,Var,Val))
        self.Vars[Var]=Val

    def checkVar(self,Var,Val,Bin):
        if Var=='R1': return
        if Var not in self.Vars:
            logs.log_error('ilia! @%s checkvar got %s (%s) undefined in rtl'%(self.Name,Var,Val))
        elif closeEnough(Val,self.Vars[Var]):
            logs.log_correct('checkvar @%s ok on %s = %s 0x%08x (%s)'%(self.Name,Var,Val,Bin,self.Vars[Var]))
        else:
            logs.log_wrong('@%s checkvar on %s = %s 0x%08x (%s)'%(self.Name,Var,Val,Bin,self.Vars[Var]))
        
def closeEnough(A,B):
    if (A==0)and(B==0): return True
    if (A==0)and(B!=0): return False
    if (A!=0)and(B==0): return False
    Diff = abs(A-B)/abs(A+B)
    return Diff<0.02

def getVar(Asm,Side):
    WW = string.split(Asm,';')
    if Side=='a':
        Line = WW[0]
        ww = string.split(Line)
        return ww[0]
    if Side=='b':
        print '>>>>>>>>>>>>',Asm
        Line = WW[1]
        ww = string.split(Line)
        return ww[0]








