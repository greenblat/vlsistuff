


import synlib_functions

inMsgString0 = '''
int CELL_delays(A_cells *self,int Src,int Dst,char Dval);
int CELL_setups(A_cells *self,int Src,int Dst,char Dval);
'''

inMsgString1 = '''
void inMsgCELL(A_cells *self,A_msgs *Msg,char Val){
    int Changed =  inMsgFirst(self,Msg,Val);
    if (!Changed) return;
    int Pin = (*Msg).Pin;
'''

outMsgString1 = '''
void inMsgCELL(A_cells *self,A_msgs *Msgx,char Val){
    A_msgs *Msg = getPinMsg(self,0);
    (*Msg).Time=0;
    sendOut(self,Msg,getPinVal(self,0),0,0);
}
'''



initString = '''
long init_CELLX(long Inst,int *delays,int *setups) {
    A_cells *self = new_cells(NUM);
    (*self).nextp = (long) allCells;
    allCells = self;
    (*self).Cell = qqai("CELLX");
    (*self).job = qqai("JOB");
    (*self).Inst=Inst;
    (*self).inMsg=(long) inMsgCELLX;
    (*self).fireAtInit = FIRE;
    (*self).delayFunc=(long) CELLX_delays;
    (*self).setupFunc=(long) CELLX_setups;
    int self0=0;
    while (delays[self0]>=0) self0++;
    int self1=0;
    while (setups[self1]>=0) self1++;
   
    int *dly = malloc(self0*sizeof(int));
    for (int ii=0;ii<self0;ii++) dly[ii]=delays[ii];
    (*self).delays = dly;

    int *stp = malloc(self1*sizeof(int));
    for (int ii=0;ii<self1;ii++) stp[ii]=setups[ii];
    (*self).setups = stp;
    A_pinarr *pp = toPins(self);
'''

more0 = '''
    pp[NUM].pinname=qqai("PIN");
    pp[NUM].pindir=qqai("DIR");
    pp[NUM].pinMsg= (long) new_msgs();
    pp[NUM].job= qqai("JOB");

'''

more1 = '''
    makePredicateLong("instance",qqia(Inst),(long) self);
    return (long) self;
}
'''



def cell_dump_msgsim_c(self,Fcc,pythonConnection):
    self.singleOutput=False
    Busses = self.busses.keys()
    for Bus in Busses:
        Dir = self.busses[Bus]['direction']
        bType = self.busses[Bus]['bus_type']
        What = self.Types[bType]
        Width = int(What['bit_width'])
        print('bus',Bus,Dir,bType,What)
        for ii in range(Width):
            Pin = '%s[%d]'%(Bus,ii)
            self.pins[Pin]={'direction':Dir}

    Pins = list(self.pins.keys())
    if (len(Pins)==1):
        Pin = Pins[0]
        if (self.pins[Pin]['direction']=='output'):
            FFF = self.pins[Pin]['function']
            Func = makeCfunc(FFF,Pins)
            self.singleOutput=True
            self.singleFunc=FFF
    if self.ff:
        Reg = self.ff[0][0]
        Regn = self.ff[0][1]
        Pins.append(Reg)
        Pins.append(Regn)
        Pins.append('next')
        self.pins[Reg]={'direction':'output'}
        self.pins[Regn]={'direction':'output'}
        self.pins['next']={'direction':'output'}
    if self.latch:
        Reg = self.latch[0][0]
        Regn = self.latch[0][1]
        Pins.append(Reg)
        Pins.append(Regn)
        Pins.append('next')
        self.pins[Reg]={'direction':'output'}
        self.pins[Regn]={'direction':'output'}
        self.pins['next']={'direction':'output'}

    Pins.sort()
    Numpins = len(Pins)
    Fcc.write('//pinsOrder["%s"] =  %s\n'%(self.Name,str(Pins))) 
    Fcc.write('//Pairs %s\n'%str(self.pairs))

    Funcs = dumpOutputs(self,Pins)
    Str0 = inMsgString0.replace('CELL',self.Name)
    Str1 = inMsgString1.replace('NUM',str(Numpins))
    Str1 = Str1.replace('CELL',self.Name)
    Str0 = Str0+Str1
    if self.ff:
        Str0 += dump_ff(self,Pins)
        self.Job = 'flipflop'
    elif self.latch:
        self.Job = 'latch'
        Str0 += dump_latch(self,Pins)
    elif self.statetable:
        Str0 += dump_statetable(self,Pins)
        if 'clock_gating_integrated_cell' in self.pairs:
            self.Job = 'gated_clock'
        else:
            self.Job = 'statetable'
    elif self.memory:
        self.Job = 'memory'
        Str0 += dump_memory(self,Pins)
    elif pythonConnection:
        self.Job = 'python'
        Str0 += dump_memory(self,Pins)
    else:
        self.Job = 'combi'
    


    Str0 += '    A_msgs *Msg1;\n'
    Str0 += '    int keepMsg=0;\n'
    if self.memory or pythonConnection:
        Str0 += '    if (fifoPtr>0) {\n        keepMsg=1;\n'
        Str0 += '        usePinsFifo(self,Msg,Pin);\n    }\n'
    Str0 += Funcs
    Str0 += '    if (!keepMsg) { del_msgs(Msg);}\n'
    Str0 +='}\n'
    if self.singleOutput:
        Str0 = outMsgString1.replace('CELL',self.Name)

    StrC = initString
    if self.singleOutput:
        StrC = StrC.replace('CELLX_delays','1')
        StrC = StrC.replace('CELLX_setups','1')
        StrC = StrC.replace('FIRE','1')
    else:
        StrC = StrC.replace('FIRE','0')

    if pythonConnection:
        StrC = StrC.replace('CELLX_delays','1')
        StrC = StrC.replace('CELLX_setups','1')


    StrC = StrC.replace('CELLX',self.Name)
    StrC = StrC.replace('JOB',self.Job)
    StrC = StrC.replace('NUM',str(Numpins))


    for ind,Pin in enumerate(Pins):
        if Pin in self.pins:
            Dir = self.pins[Pin]['direction']
            tmp = more0.replace('NUM',str(ind))
            tmp = tmp.replace('PIN',Pin)
            tmp = tmp.replace('DIR',Dir)
            if self.singleOutput:
                tmp += '    A_msgs *Msgx = (A_msgs *) pp[0].pinMsg;  (*Msgx).Val= %s;\n'%(self.singleFunc)
                tmp += '     (*Msgx).isWhat = qqai("supply");\n'
            if ('clock' in self.pins[Pin])and(self.pins[Pin]['clock']=='true'):
                tmp = tmp.replace('JOB','clock')
            elif ('clock_gate_clock_pin' in self.pins[Pin])and(self.pins[Pin]['clock_gate_clock_pin']=='true'):
                tmp = tmp.replace('JOB','clock')
            elif self.singleOutput:
                tmp = tmp.replace('JOB','supply')
            else:
                tmp = tmp.replace('JOB','notspecified')

            StrC += tmp
            StrC += '// %s\n'%(str(self.pins[Pin]))
    for ind,Pin in enumerate(Pins):
        StrC += '    makePredicateLong("pinnum","%s %s",%d);\n'%(self.Name,Pin,ind)
    StrC += more1     
    Fcc.write(Str0+StrC)

def dump_memoryPy(self,Pins): 
    Str = '    char message[1000],more1[1000];\n    msgs_string(Msg,more1);sprintf(message,"%sModel(\'%%s\',\'%%s\',\'%%ld\')",qqia((*self).Inst),more1,simTime);\n    PyRun_SimpleString(message);\n'%(self.Name)
    return Str

def dump_memoryC(self,Pins): 
    Str = ''
    for ii in range(self.dataWidth):
        Str += '    if (Pin==%d) { }\n'
    for ii in range(self.addrWidth):
        Str += '    if (Pin==%d) { }\n'
    Str += '    if ((Pin==%d)&&(Val==1)&&(CEN==1)) {\n'%(Pins.index('CLK'))
    Str += '    }\n'
    return Str





def dump_memory(self,Pins): 
    return dump_memoryPy(self,Pins)

def dump_ff(self,Pins):
    Reg = self.ff[0][0]
    Regn = self.ff[0][1]
    Clocked='0'
    Clear = False
    Preset = False
    for (Prm,Var) in self.ff[1]:
        if Prm=='clocked_on':
            Clocked = Var
        if Prm=='next_state':
            Next = Var
            print('>>next state>>>>>>',Next)
        if Prm=='clear':
            Clear = Var
            if (Clear[0]=='(')and(Clear[-1]==')'):
                Clear = Clear[1:-1]
            self.PinJobs[Var]='reset'
        if Prm=='preset':
            Preset = Var
            if (Preset[0]=='(')and(Preset[-1]==')'):
                Preset = Preset[1:-1]
            self.PinJobs[Preset]='set'
    Bef = Next
    print('>>>>>>>>',Next)
    Nextf = makeCfunc(Next,Pins)
    Clockedf = makeCfunc(Clocked,Pins)
    ClockedInd = pinNum(Clocked,Pins)
    RegInd = pinNum(Reg,Pins)
    RegnInd = pinNum(Regn,Pins)
    if ' ' in Next:
        NextInd =  Pins.index('next')
    elif Next in Pins:
        NextInd = Pins.index(Next)
    else:
        NextInd = Pins.index('next')
    print("<><>",Next,Nextf,NextInd,Pins)
    if Preset and (Preset[0]=='!'):
        PresetInd = Pins.index(Preset[1:])
    elif (Preset)and(Preset in Pins):
        PresetInd = Pins.index(Preset)
    elif (Preset):
        print( 'pin "%s" is not a pin of cell %s'%(Preset,self.Name))
    if Clear and (Clear[0]=='!'):
        ClearInd = Pins.index(Clear[1:])
    elif (Clear):
        ClearInd = Pins.index(Clear)
    Str = '\n\n//ffff\n'
    Str += '    A_msgs *IQMsg = getPinMsg(self,%s);\n'%(RegInd)
    Str += '    A_msgs *IQNMsg = getPinMsg(self,%s);\n'%(RegnInd)

    if (Clocked[0]=='!'):
        CondHold = '(getPinVal(self,%d)==0)'%(ClockedInd)
    else:
        CondHold = '(getPinVal(self,%d)==1)'%(ClockedInd)


    if ' ' in Next:
        Str +=     '        char next = %s;\n'%(makeCfunc(Next,Pins))
        Str +=     '        A_msgs *NextMsg = getPinMsg(self,%s);\n'%(Pins.index('next'))
        Nextf = 'next'
        self.dataPin = NextInd
        Str +=     '//      printf("%ld inst=%lx newmsg was=%d now=%d pin=%d val=%d\\n",simTime,(long) self,(*NextMsg).Val,next,Pin,(*Msg).Val);\n'
        Str +=     '        if ((*NextMsg).Val != next) {\n'
        Str +=     '//          printf("%ld inst=%lx next change was=%d now=%d pin=%d\\n",simTime,(long) self,(*NextMsg).Val,next,Pin);\n'
        Str +=     '            char was = (*NextMsg).Val;\n'
        Str +=     '            msgs_copy(Msg,NextMsg); (*NextMsg).Val=next;\n'
        Str +=     '            if ((was<4)&&%s) checkHoldSlack(self,%s,%s);\n'%(CondHold,NextInd,ClockedInd)
        Str +=     '        } else if (Pin!=%d) msgs_copy(Msg,NextMsg);\n'%ClockedInd
    else: 
        self.dataPin = NextInd
        Str +=     '        if (Pin==%d) { \n'%(NextInd)
        Str +=     '            if (getPinVal(self,%d)<4) && %s) checkHoldSlack(self,%s,%s);\n'%(NextInd,CondHold,NextInd,ClockedInd)
        Str +=     '        }\n'
    El = ''
    if Preset: presetf = getCval(Preset,Pins)
    if Clear: 
        clearf = getCval(Clear,Pins)
    if Preset and (Preset[0]=='!'):
        Str +=     '        %s if (%s==0){\n'%(El,presetf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=1;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=0;\n   }'
        El='else'
    elif Preset:
        Str +=     '        %s if (%s==1){\n'%(El,presetf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=1;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=0;\n   }'
        El='else'
    if Clear and (Clear[0]=='!'):
        Str +=     '        %s if (%s==0){\n'%(El,clearf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=0;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=1;\n   }'
        El='else'
    elif Clear:
        Str +=     '        %s if (%s==1){\n'%(El,clearf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=0;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=1;\n    }'
        El='else'
    if Clocked[0]=='!':
        Str +=     '        %s if ((Pin==%s)&&(Val==0)) {\n'%(El,ClockedInd)
        Str +=     '            checkSetupHold(self,%s,%s,Msg);\n'%(self.dataPin,ClockedInd)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=%s;\n'%Nextf
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=msg_not(%s);\n'%Nextf
        Str +=     '            (*IQNMsg).isWhat=qqai("flipflop");\n'
        Str +=     '            (*IQNMsg).whatSource=(*self).Inst;\n'
        Str +=     '            (*IQMsg).isWhat=qqai("flipflop");\n'
        Str +=     '            (*IQMsg).whatSource=(*self).Inst;\n   }'
        El='else'
    else:
        Str +=     '        %s if ((Pin==%s)&&(Val==1)){\n'%(El,ClockedInd)
        Str +=     '            checkSetupHold(self,%s,%s,Msg);\n'%(self.dataPin,ClockedInd)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=%s;\n'%Nextf
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=msg_not(%s);\n'%Nextf
        Str +=     '            (*IQNMsg).isWhat=qqai("flipflop");\n'
        Str +=     '            (*IQNMsg).whatSource=(*self).Inst;\n'
        Str +=     '            (*IQMsg).isWhat=qqai("flipflop");\n'
        Str +=     '            (*IQMsg).whatSource=(*self).Inst;\n   }'
        El='else'
    Str +=     '        else { del_msgs(Msg);return;}\n'
    Str +=     '        (*Msg).whatSource = (*self).Inst;\n'
    Str +=     '        if ((*Msg).isWhat == qqai("reset")) (*Msg).isWhat = qqai("flipflop_reset"); else (*Msg).isWhat = qqai("flipflop");\n'
    Str += '\n\n//ffff\n'
    return Str

def dump_latch(self,Pins):
    Reg = self.latch[0][0]
    Regn = self.latch[0][1]
    Clocked='0'
    Next= '0'
    Clear = False
    Preset = False
    for (Prm,Var) in self.latch[1]:
        if Prm=='enable':
            Clocked = Var
        if Prm=='data_in':
            Next = Var
        if Prm=='clear':
            Clear = Var
        if Prm=='preset':
            Preset = Var
    Bef = Next
    Nextf = makeCfunc(Next,Pins)
    Clockedf = makeCfunc(Clocked,Pins)
    ClockedInd = pinNum(Clocked,Pins)
    RegInd = replacePinNum(Reg,Pins)
    RegnInd = pinNum(Regn,Pins)
    NextInd = pinNum(Next,Pins)
    if Preset and (Preset[0]=='!'):
        PresetInd = Pins.index(Preset[1:])
    elif (Preset):
        PresetInd = Pins.index(Preset)
    if Clear and (Clear[0]=='!'):
        ClearInd = Pins.index(Clear[1:])
    elif (Clear):
        ClearInd = Pins.index(Clear)
    Str = '\n\n//ffff\n'
    Str += '    A_msgs *IQMsg = getPinMsg(self,%s);\n'%(RegInd)
    Str += '    A_msgs *IQNMsg = getPinMsg(self,%s);\n'%(RegnInd)
    if ' ' in Nextf:
        Str +=     '        char next = %s;\n'%(Nextf)
        Str +=     '        setPinValTime(self,%s,next);\n'%(Pins.index('next'))
        Nextf = 'next'
        self.dataPin = NextInd
        Str +=     '        if (%s != next) {\n'%(makeCfunc('next',Pins))
        Str +=     '            Msg.copy(next)\n'
        Str +=     '            checkHoldSlack(self,%s,%s)\n'%(NextIndaClockedInd,)
        Str +=     '            }\n'
    else: 
        self.dataPin = NextInd
        Str +=     '        if (Pin==%d) { \n'%(NextInd)
        Str +=     '            checkHoldSlack(self,%s,%s);\n'%(NextInd,ClockedInd)
        Str +=     '            }\n'
    El = ''
    if Preset: presetf = getCval(Preset,Pins)
    if Clear: 
        clearf = getCval(Clear,Pins)
    if Preset and (Preset[0]=='!'):
        Str +=     '        %s if (%s==0){\n'%(El,presetf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=1;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=0;\n   }'
        El='else'
    elif Preset:
        Str +=     '        %s if (%s==1){\n'%(El,presetf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=1;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=0;\n   }'
        El='else'
    if Clear and (Clear[0]=='!'):
        Str +=     '        %s if (%s==0){\n'%(El,clearf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=0;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=1;\n   }'
        El='else'
    elif Clear:
        Str +=     '        %s if (%s==1){\n'%(El,clearf)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=0;\n'
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=1;\n    }'
        El='else'
    if Clocked[0]=='!':
        Str +=     '        %s if ((Pin==%s)&&(Val==0)) {\n'%(El,ClockedInd)
        Str +=     '            checkSetupHold(self,%s,%s,Msg);\n'%(self.dataPin,ClockedInd)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=%s;\n'%Nextf
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=msg_not(%s);\n'%Nextf
        Str +=     '            (*IQNMsg).isWhat=qqai("latch");\n'
        Str +=     '            (*IQNMsg).whatSource=(*self).Inst;\n'
        Str +=     '            (*IQMsg).isWhat=qqai("latch");\n'
        Str +=     '            (*IQMsg).whatSource=(*self).Inst;\n   }'
        El='else'
    else:
        Str +=     '        %s if ((Pin==%s)&&(Val==1)){\n'%(El,ClockedInd)
        Str +=     '            checkSetupHold(self,%s,%s,Msg);\n'%(self.dataPin,ClockedInd)
        Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=%s;\n'%Nextf
        Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=msg_not(%s);\n'%Nextf
        Str +=     '            (*IQNMsg).isWhat=qqai("latch");\n'
        Str +=     '            (*IQNMsg).whatSource=(*self).Inst;\n'
        Str +=     '            (*IQMsg).isWhat=qqai("latch");\n'
        Str +=     '            (*IQMsg).whatSource=(*self).Inst;\n   }'
        El='else'
    Str +=     '        %s if (%s==1){\n'%(El,Clockedf)
    Str +=     '            msgs_copy(Msg,IQMsg); (*IQMsg).Val=%s;\n'%Nextf
    Str +=     '            msgs_copy(Msg,IQNMsg); (*IQNMsg).Val=msg_not(%s);\n'%Nextf
    Str +=     '            (*IQNMsg).isWhat=qqai("latch");\n'
    Str +=     '            (*IQNMsg).whatSource=(*self).Inst;\n'
    Str +=     '            (*IQMsg).isWhat=qqai("latch");\n'
    Str +=     '            (*IQMsg).whatSource=(*self).Inst;\n   }'
    Str +=     '        else { del_msgs(Msg); return;}\n'
    Str +=     '        (*Msg).isWhat=qqai("latch");\n'
    Str +=     '        (*Msg).whatSource=(*self).Inst;\n'
    Str += '\n\n//ffff\n'
    return Str



def dump_statetable(self,Pins):
    print('statetable',self.statetable)
    Stx = self.statetable[0]
    St0 = Stx[0]
    Vars = St0.replace('"','')
    St1 = Stx[1]
    Vars = St0.replace('"','')
    Qs   = St1.replace('"','')
    Vars = Vars.strip()
    Vars = Vars.split()
    Qs = Qs.strip()
    Qs = Qs.split()
    Ta2 = self.statetable[1]
    Ta1 = Ta2[0]
    print('info statetable Qs',Qs,'vars',Vars,self.statetable[1])
    if Ta2[0]=='"':
        Ta2 = Ta2.replace('"','')
        Table = Ta2.replace('\\','')
        Lines = Table.split(',')
    elif Ta1[0]=='table':
        Table = Ta1[1]
        if Table[0]=='"':
            Table=Table[1:]
        if Table[-1]=='"':
            Table=Table[:-1]
        Table = Table.replace('\\','')
        Lines = Table.split(',')
    else:
        print('errors!!! stateable')
        return '// state table error'

    Str = '// stateable vars=%s qs=%s\n'%(str(Vars),str(Qs))
    Str +='long Code = getPinVcdCode(self,%s);\n'%replacePinNum(Qs[0],Pins)
    VV = Vars+Qs
    for Var in VV:
        if Var != Qs[0]:
            Str += 'char %s = getPinVal(self,%s);\n'%(Var,replacePinNum(Var,Pins))
    Str += ' char %s = \n'%Qs[0]
    for Line in Lines:
        Line = Line.strip()
        Line = Line.replace(':','')
        LL = Line.split()
        Expr,New = synlib_functions.match_table(VV,LL,self.Name)
        if New:
            Str += '         (%s) ? %s :\n'%(Expr,New)
    Str += '   getPinVal(self,%s);\n'%replacePinNum(Qs[0],Pins)
    Str += '   setPinValTime(self,%s,%s);\n'%(replacePinNum(Qs[0],Pins),Qs[0])
    Str += '   vcdValue(Code,%s,simTime);\n'%Qs[0]
    return Str


def dumpOutputs(self,Pins):
    Numpins = len(Pins)

    Str=''

    for ind,Out in enumerate(Pins):
        Dir = self.pins[Out]['direction']
        if Dir=='output':
            FFF = False
            if 'function' in self.pins[Out]:
                FFF = self.pins[Out]['function']
            elif 'state_function' in self.pins[Out]:
                FFF = self.pins[Out]['state_function']
            if FFF:
                Func = makeCfunc(FFF,Pins)
                Str +='    char %s_now = %s;\n'%(Out,Func)
                Str +='    if (%s_now!= getPinVal(self,%s)) {\n'%(Out,ind)
                Str +='        Msg1 = (keepMsg) ? msgs_duplicate(Msg) : Msg;\n'
                Str +='        sendOut(self,Msg1,%s_now,Pin,%s);\n'%(Out,ind)
                Str +='        keepMsg=1;\n'
                Str +='    }\n'
    return Str

def makeCfunc(inFunc,Pins):
    Func = synlib_functions.funcify(inFunc,{})
    Func = synlib_functions.pythonizeFunc(Func)
    Func = Func.replace('self.pinMsg','(*self).pinMsg')
    Func = Func.replace('["','[')
    Func = Func.replace('"]',']')
    Func = replacePinNum(Func,Pins)
    return Func

def getCval(Pin,Pins):
    if Pin[0]=='!': Pin=Pin[1:]
    Num = replacePinNum(Pin,Pins)
    res = 'getPinVal(self,%s)'%Num
    return res

def pinNum(Pin,Pins):
    if Pin[0]=='!': Pin=Pin[1:]
    if Pin in Pins:
        return Pins.index(Pin)
    print('wrong pinNum for "%s" %s'%(Pin,Pins))
    return 0
    
def replacePinNum(Func,Pins):
    AA = Func.replace('[',' [ ')
    AA = AA.replace(']',' ] ')
    wrds = AA.split()
    for ind,wrd in enumerate(wrds):
        if wrd in Pins:
            pos = Pins.index(wrd)
            wrds[ind]=str(pos)
    Str = ' '.join(wrds)
    Str = Str.replace(' [ ','')
    Str = Str.replace(' ] ','')
    return Str


def cell_dump_description(self,Fout,pythonConnection):
    Fout.write('Desc = cellDescClass("%s")\n'%self.Name)
    for Key in self.pairs:
        Fout.write('Desc.properties["%s"] = "%s"\n'%(Key,self.pairs[Key]))
    Keys = list(self.pins.keys())
    Keys.sort()
    Fout.write('Desc.pinOrder = %s\n'%(str(Keys)))
    for (To,Fr,Kind) in self.arcs:
        Fout.write('Desc.add_arc("%s","%s","%s")\n'%(Fr,To,Kind))
    if len(self.pins.keys())==1:
        Pin = self.pins.keys()[0]
        if (self.pins[Pin]['direction']=='output'):
            Func = self.pins[Pin]['function']
            if Func == '1':
                Fout.write('Desc.set_job("supply1")\n')
            elif Func == '0':
                Fout.write('Desc.set_job("supply0")\n')
    
            


    if len(self.pins.keys())==2:
        for Pin in self.pins:
            Dir = self.pins[Pin]['direction']
            if (Dir=='output'):
                Func = self.pins[Pin]['function']
                if '!' in Func:
                    Fout.write('Desc.set_job("inv") # %s\n'%Func)
                else:
                    Fout.write('Desc.set_job("buf") # %s\n'%Func)
                

    elif len(self.pins.keys())==1:
        Pin = self.pins.keys()[0]
        Dir = self.pins[Pin]['direction']
        try:
            Func = synlib_functions.funcify(self.pins[Pin]['function'])
            if Dir=='output':
                Fout.write('Desc.set_job("supply%s")\n'%Func)
        except:
            pass
            
        

    if 'area' in self.pairs:
        Fout.write('Desc.add_param("area",%s);\n'%(self.pairs['area']))
    for Pin in self.pins:
        Dir = self.pins[Pin]['direction']
        if ('clock' in self.pins[Pin])and(self.pins[Pin]['clock']=='true'):
            Fout.write('Desc.set_pin_job("%s","clock")\n'%(Pin))
        if Pin in self.PinJobs:
            Fout.write('Desc.set_pin_job("%s","%s")\n'%(Pin,self.PinJobs[Pin]))
        if Dir in ['input','output']:
            Fout.write('Desc.add_pin("%s","%s")\n'%(Pin,Dir))
        if Dir=='output':
            try:
                Func = synlib_functions.funcify(self.pins[Pin]['function'])
            except:
                Func='unknown'
            Fout.write('Desc.add_pin_func("%s","%s")\n'%(Pin,Func))
            
    if self.ff:
        Fout.write('Desc.set_job("flipflop")\n')
    if self.latch:
        Fout.write('Desc.set_job("latch")\n')
    if self.statetable:
        Fout.write('Desc.set_job("statetable")\n')
    if self.memory:
        Fout.write('Desc.set_job("memory")\n')
    if pythonConnection:
        Fout.write('Desc.set_job("python")\n')

#    Jobs = self.pin_jobs()
#    for Pin in Jobs:
#        if Jobs[Pin]=='reset':
#            Fout.write('Desc.set_pin_job("%s","reset")\n'%(Pin))
#        if Jobs[Pin]=='clock':
#            Fout.write('Desc.set_pin_job("%s","clock")\n'%(Pin))
    Fout.write('CellLib["%s"]=Desc\n'%self.Name)
    
