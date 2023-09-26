
import string,os,sys

import module_class
import newRtl
import logs
import dumpUser

class connectivityClass:
    def __init__(self,Glbs,Root):
        if type(Root) is str:
            self.Mod = Glbs.details[Root]
        else:
            print('IAM %s' % str(type(Root)))
            self.Mod = Root
            
        self.Module = self.Mod.Module
        self.Names={}
        self.Params={}
        self.Nodes={}
        self.Wnodes={}
        self.Inps={}
        self.Outs={}
        self.Inouts={}
        self.Conns={}
        self.hard_assigns = []
        self.Glbs = Glbs
        self.prepares()
        self.emptyConns()
    
    def prepares(self):
        for Key in self.Mod.params:
            Obj = self.Mod.params[Key]
            if (Obj.Param=='name')and(Obj.Value!='$inst'):
                self.Names[Obj.Owner]=Obj.Value
            elif Obj.Owner not in self.Params:
                self.Params[Obj.Owner]=[(Obj.Param,Obj.Value)]
            else:
                self.Params[Obj.Owner].append((Obj.Param,Obj.Value))

        for Inst in self.Mod.instances:
            Obj = self.Mod.instances[Inst]
            if Obj.Type=='input':
                if Inst in self.Names:
                    self.Inps[self.Names[Inst]]=Inst
                else:
                    self.Inps[Inst]=Inst
                    self.Names[Inst]=Inst
            elif Obj.Type=='output':
                if Inst in self.Names:
                    self.Outs[self.Names[Inst]]=Inst
                else:
                    self.Outs[Inst]=Inst
                    self.Names[Inst]=Inst
            elif Obj.Type=='inout':
                if Inst in self.Names:
                    self.Inouts[self.Names[Inst]]=Inst
                else:
                    self.Inouts[Inst]=Inst
                    self.Names[Inst]=Inst

            elif Obj.Type=='node':
                self.Nodes[Inst]=[]
            elif Obj.Type=='antenna':
                self.Nodes[Inst]=[]
            elif Obj.Type=='vcc':
                self.Names[Inst]='vcc'
                self.Nodes[Inst]=[]
            elif Obj.Type=='gnd':
                self.Names[Inst]='gnd'
                self.Nodes[Inst]=[]
            elif Inst in self.Params:
                Params = self.Params[Inst]
                ind = 0
                while ind < len(Params):
                    (Prm,Val) = Params[ind]
                    if Prm == 'conns':
                        if Inst not in self.Conns:
                            self.Conns[Inst]={}
                        LL = Val.split(',')
                        for Pair in LL:
                            PinNet = Pair.split('=')
                            self.Conns[Inst][PinNet[0]] = PinNet[1]
                        Params.pop(ind)
                    else:
                        ind += 1

        EndPoints = {}                    
        for Wire in self.Mod.wires:
            Obj = self.Mod.wires[Wire]
            Start = Obj.Start
            End = Obj.End
            if '.' in Start:
                if Start not in EndPoints: EndPoints[Start] = []
                EndPoints[Start].append(Wire)
            if '.' in End:
                if End not in EndPoints: EndPoints[End] = []
                EndPoints[End].append(Wire)
        for EndP in EndPoints:
            if len(EndP)>1:
                self.Nodes[EndP] = EndPoints[EndP]


        for Wire in self.Mod.wires:
            self.Wnodes[Wire]=[]
            Obj = self.Mod.wires[Wire]
            Start = Obj.Start
            End = Obj.End
            if Start in self.Nodes:
                self.Wnodes[Wire].append(Start)
                if Wire not in self.Nodes[Start]:
                    self.Nodes[Start].append(Wire)
            if End in self.Nodes:
                self.Wnodes[Wire].append(End)
                if Wire not in self.Nodes[End]:
                    self.Nodes[End].append(Wire)
    
        for Wire in self.Mod.wires:
            Obj = self.Mod.wires[Wire]
            Start = Obj.Start
            End = Obj.End
            if Start in self.Names:
                Wname = self.Names[Start]
                self.Names[Wire]=Wname
                for Node in self.Wnodes[Wire]:
                    for Wire1 in self.Nodes[Node]:
                        self.Names[Wire1]=Wname
            if End in self.Names:
                Wname = self.Names[End]
                self.Names[Wire]=Wname
                for Node in self.Wnodes[Wire]:
                    for Wire1 in self.Nodes[Node]:
                        self.Names[Wire1]=Wname
    

        self.spread_the_joy()
        for Wire in self.Mod.wires:
            if Wire not in self.Names:
                self.Names[Wire]=Wire
                self.spread_the_joy()
    
        for Wire in self.Mod.wires:
            Obj = self.Mod.wires[Wire]
            Start = Obj.Start
            End = Obj.End
    
            if Wire in self.Names:
                Wname=self.Names[Wire]
            else:
                Wname=Wire
                
            if '.' in Start:
                pp = Start.split('.')
                Pin = pp[1]
                Inst=pp[0]
                if Inst not in self.Conns:
                    self.Conns[Inst]={}
                self.Conns[Inst][Pin]=Wname
    
            if '.' in End:
                pp = End.split('.')
                Pin = pp[1]
                Inst=pp[0]
                if Inst not in self.Conns:
                    self.Conns[Inst]={}
                self.Conns[Inst][Pin]=Wname

    def emptyConns(self): 
        for Inst in self.Mod.instances:
            Obj = self.Mod.instances[Inst]
            Pic = Obj.Type
            if Inst not in self.Conns: self.Conns[Inst] = {}
            if (Pic in ['antenna','vcc','gnd','input','output','node'])or('logo' in Obj.Type):
                pass
            elif not self.Glbs:
                pass
            elif Pic in self.Glbs.pictures:
                Pins = self.Glbs.pictures[Pic].pins
                for Pin in Pins:
                    if Pin not in self.Conns[Inst]:
                        self.Conns[Inst][Pin]=''
                    

    def spread_the_joy(self):
        dones=1
        while dones:
            dones=0
            for Node in self.Nodes:
                List = self.Nodes[Node]
                Name=False
                for Wire in List:
                    if Wire in self.Names:
                        Name=self.Names[Wire]
                if Name:
                    for Wire in List:
                        if Wire not in self.Names:
                            self.Names[Wire]=Name
                            dones +=1


    def dumpVerilogHeader(self,File):
        Params = []
        All = []
#        for Bus in self.Inps | self.Outs | self.Inouts:
        for Bus in { **self.Inps, **self.Outs, **self.Inouts}:
            if '[' in Bus:
                Prms = extractWireParams(Bus)
                All.extend(Prms)
        if All!=[]:
            Used = []
            for Prm in All:
                if Prm not in Used:
                    Params.append('parameter %s=1' % Prm)
                    Used.append(Prm)
            Params = '#(%s) ' % (', '.join(Params))

        File.write('module %s%s (' % (self.Mod.Module,Params))
        Pref=' '
        for Inp in self.Inps:
            Rinp = reworkPort(Inp)
            File.write('    %sinput %s\n'%(Pref,Rinp))
            Pref=','
        for Out in self.Outs:
            Rout = reworkPort(Out)
            File.write('    %soutput %s\n'%(Pref,Rout))
            Pref=','
        for Out in self.Inouts:
            Rout = reworkPort(Out)
            File.write('    %sinout %s\n'%(Pref,Rout))
            Pref=','
        File.write(');\n')
        
    def getDelay(self,Inst):
        if Inst in self.Params:
            Params = self.Params[Inst]
            for (Prm,Val) in Params:
                if Prm=='delay': return '#(%s) ' % Val
        return ''

    def createModuleClass(self):
        self.Modx = module_class.module_class(self.Mod.Module)
        for Inp in self.Inps:
            self.Modx.add_sig(Inp, "input", 0)
        for Out in self.Outs:
            self.Modx.add_sig(Out, "output", 0)
        for Out in self.Inouts:
            self.Modx.add_sig(Out, "inout", 0)

        for Pragma in self.Mod.geoms:
            Txt = Pragma
            Txt = Txt.replace('"', "")
            if "<assign>" in Txt:
                Txt = Txt[8:]
                Txt = Txt.strip()
                Txt = Txt.replace("  ", " ")
                Wrds = Txt.split("=")
                Dst = Wrds[0].strip()
                Src = " ".join(Wrds[1:])
                self.Modx.add_sig(Dst, "wire", 0)
                self.Modx.hard_assigns.append((Dst, Src, "", ""))
            elif Txt.startswith("parameter"):
                X = Txt.replace("parameter ", "")
                W = X.split("=")
                if len(W) == 2:
                    try:
                        W1 = eval(W[1])
                    except Exception:
                        W1 = W[1]
                    self.Modx.parameters[W[0]] = W1
                else:
                    logs.log_error("parameter string '%s' is wrong" % Txt)
        for Inst in self.Mod.instances:
            Obj = self.Mod.instances[Inst]
            Type = Obj.Type
            Obj.conns = {}
            if Inst in self.Conns:
                Pins = self.Conns[Inst]
                Obj.conns = Pins
            if Type in ["gnd", "vcc"]:
                pass
            elif Type in ["antenna", "input", "output", "node", "inout"]:
                pass
            else:
                self.Modx.add_inst(Type, Inst)
                if Inst in self.Conns:
                    Pins = self.Conns[Inst]
                    for Pin in Pins:
                        if Type not in self.Glbs.pictures:
                            self.Glbs.try_load_picture(Type)
                        if Pin in self.Glbs.pictures[Type].pins:
                            Sig = Pins[Pin]
                            self.Modx.add_conn(Inst, Pin, Sig)
            if Inst in self.Params:
                Params = self.Params[Inst]
                for (Prm, Val) in Params:
                    self.Modx.add_inst_param(Inst, Prm, Val)
        return self.Modx

    def dumpVerilog(self,File,Rtl,User):
        if User:
            dumpUser.dumpUser(self,self.Mod,File)
        elif Rtl:
            self.createModuleClass()
            newRtl.createNewRtl(self.Modx)
            self.Modx.dump_verilog(File)
        else:
            print('CCCCCC')
            Modx = self.createModuleClass()
            Modx.dump_verilog(File)
#            self.dumpVerilogHeader(File)
#            self.dumpGlvVerilog(File)
#            File.write('endmodule\n')

    def dumpGlvVerilog(self,File):
        for Inst in self.Mod.instances:
            self.dumpInstance(Inst,File)

        for DstSrc in self.hard_assigns:
            Dst = DstSrc[0]
            Src = DstSrc[1]
            File.write('assign %s = %s;\n' % (Dst,Src))

    def dumpInstance(self,Inst,File):
        Obj = self.Mod.instances[Inst]
        if Inst in self.Names:
            Name = self.Names[Inst]
        else:
            Name = Obj.Inst
        if Obj.Type == 'concat':
            OO = self.Conns[Inst]['o']
            I0 = self.Conns[Inst]['i0']
            I1 = self.Conns[Inst]['i1']
            File.write('assign %s = {%s,%s};\n' % (OO,I1,I0))

        elif (Obj.Type not in ['vcc','gnd','antenna','input','output','inout','node'])and('logo' not in Obj.Type)and('ilia' not in Obj.Type):
            if Inst in self.Params:
                PP = []
                for Prm,Val in self.Params[Inst]:
                    Val1 = make_legal(Val)
                    Str='.%s(%s)'%(Prm,Val1)
                    if Prm!='name': PP.append(Str)
                ObjParams = '#(%s)'%(','.join(PP))
            else:
                ObjParams= '#(%d,%d)'%(Obj.Point)
                ObjParams= ''
            File.write('%s %s %s ('%(Obj.Type,ObjParams,Name))
            if Inst in self.Conns:
                Pref = ''
                Pins  = self.Conns[Inst]
                for Pin in Pins:
                    File.write(' %s.%s(%s)\n'%(Pref,Pin,Pins[Pin]))
                    Pref = ','
                 
            File.write(');\n')

    def __createModuleClass(self):
        self.Modx = module_class.module_class(self.Mod.Module)
        for Inp in self.Inps:
            self.Modx.add_sig(Inp,'input',0)
        for Out in self.Outs:
            self.Modx.add_sig(Out,'output',0)
        for Out in self.Inouts:
            self.Modx.add_sig(Out,'inout',0)

        for Pragma in self.Mod.geoms:
            Txt = Pragma
            Txt = Txt.replace('"','')
            if '<assign>' in Txt:
                Txt = Txt[8:]
                Txt = Txt.strip()
                Txt = Txt.replace('  ',' ')
                Wrds = Txt.split('=')
                Dst = Wrds[0].strip()
                Src = ' '.join(Wrds[1:])
                self.Modx.add_sig(Dst,'wire',0)
                self.Modx.hard_assigns.append((Dst,Src,'',''))
        for Inst in self.Mod.instances:
            Obj = self.Mod.instances[Inst]
            Type = Obj.Type
            Obj.conns = {}
            Dly = self.getDelay(Inst)
            if Inst in self.Conns:
                Pins  = self.Conns[Inst]
                Obj.conns = Pins
            if Type in ['antenna','gnd','vcc','input','output','node','inout']:
                pass
            else:
                self.Modx.add_inst(Type,Inst)
                if Inst in self.Conns:
                    Pins  = self.Conns[Inst]
                    for Pin in Pins:
                        Sig = Pins[Pin]
                        self.Modx.add_conn(Inst,Pin,Sig)
            if Inst in self.Params:
                Params = self.Params[Inst]
                for (Prm,Val) in Params:
                    self.Modx.add_inst_param(Inst,Prm,Val)


    def findSpiceParams(self):
        res=[]
        for Key in self.Mod.params:
            Obj = self.Mod.params[Key]
            if (Obj.Param=='size')and('param' in Obj.Value):
                Val = Obj.Value[6:-1]
                if ',' in Val:
                    xx = Val.split(',')
                elif '/' in Val:
                    xx = Val.split('/')
                else:
                    xx = [Val]
                for x in xx:
                    if x not in res:
                        res.append(x)
        res.sort()
        return res


    def dumpSpice(self,File):
        File.write('* spice of %s\n'%(self.Mod.Module))
        File.write('.subckt %s\n'%self.Mod.Module)
        mPins = list(self.Inps.keys())+list(self.Outs.keys())
        mPins.extend(['gnd','vcc'])
        mPins.sort()
        extParams = self.findSpiceParams()
        for Inp in mPins:
            File.write('+    %s\n'%(Inp))
        for Prm in extParams:
            File.write('+ %s=0\n'%(Prm))
        File.write('\n')
        File.write('*.PININFO gnd:I vcc:I')
        for Pin in self.Inps:
            File.write(' %s:I' % Pin)
        for Pin in self.Outs:
            File.write(' %s:O' % Pin)
        File.write('\n')
            
        Types,Maxes = assembleArgvTypes()

        for Inst in self.Mod.instances:
            Obj = self.Mod.instances[Inst]
            if Inst in self.Names:
                Name = self.Names[Inst]
            else:
                Name = Obj.Inst
            if Inst not in self.Params:  
                self.Params[Inst] = {}
            if (Obj.Type in ['antenna','vcc','gnd','input','output','node'])or('logo' in Obj.Type):
                pass
            elif Obj.Type == 'nmos':
                WL = widthAndLength(self.Params[Inst],self.Glbs)
                II = self.Conns[Inst]['i']
                OO = self.Conns[Inst]['o']
                GG = self.Conns[Inst]['g']
                Actual = Types[Obj.Type]
                Bulk = getBulk(self.Params[Inst],'gnd')
                File.write('m%s %s %s %s %s %s %s\n'%(Name,II,GG,OO,Bulk,Actual,WL))
            elif Obj.Type=='pmos':
                WL = widthAndLength(self.Params[Inst],self.Glbs)
                II = self.Conns[Inst]['i']
                OO = self.Conns[Inst]['o']
                GG = self.Conns[Inst]['g']
                Actual = Types[Obj.Type]
                Bulk = getBulk(self.Params[Inst],'vcc')
                File.write('m%s %s %s %s %s %s %s\n'%(Name,II,GG,OO,Bulk,Actual,WL))
            elif Obj.Type=='res':
                OO = self.Conns[Inst]['p']
                II = self.Conns[Inst]['n']
                RR = get_size(self.Params[Inst])
                File.write('r%s %s %s %s\n'%(Name,II,OO,RR))
            elif Obj.Type=='cap':
                OO = self.Conns[Inst]['p']
                II = self.Conns[Inst]['n']
                RR = get_size(self.Params[Inst])
                File.write('c%s %s %s %s\n'%(Name,II,OO,RR))
            elif Obj.Type=='coil':
                OO = self.Conns[Inst]['p']
                II = self.Conns[Inst]['n']
                RR = get_size(self.Params[Inst])
                File.write('l%s %s %s %s\n'%(Name,II,OO,RR))


            else:
                File.write('x%s / %s $PINS'%(Name,Obj.Type))
                if Inst in self.Conns:
                    Pins  = self.Conns[Inst]
                    Pins['vcc']='vcc'
                    Pins['gnd']='gnd'
                    Keys = list(Pins.keys())
                    Keys.sort()
                    for Pin in Keys:
                        File.write(' %s=%s'%(Pin,Pins[Pin]))
#                File.write(' %s'%(Obj.Type))
#                if Inst in self.Params:
#                    WL = complexWidthAndLength(self.Params[Inst])
#                    File.write(' %s\n'%WL)
#                else:
                File.write('\n')
        File.write('.ends\n')
        File.write('* x%s \n'%self.Mod.Module)
        for Inp in mPins:
            File.write('*+    %s\n'%(Inp))
        File.write('*+ %s\n\n'%self.Mod.Module)
        self.dumpPicture()


    def dumpPicture(self):
        Current = self.Mod
        Mxin=0
        Mxout=0
        for Net in self.Inps:
            Mxin = max(Mxin,len(Net))
        for Net in self.Outs:
            Mxout = max(Mxout,len(Net))

        inKeys = list(self.Inps.keys())
        inKeys.sort()
        ouKeys = list(self.Outs.keys())
        ouKeys.sort()
        Fout = open('%s.zpic'%Current.Module,'w')
        Fout.write('picture %s\n'%Current.Module)
        Max = max(len(inKeys),len(ouKeys))
        PinSpace=1.0
        H1 = Max*PinSpace + 1.0
        Mxl1 = Mxin+Mxout+1
        Mxl = max(Mxl1,len(Current.Module))
        W1 = max(3,Mxl/2.9)
        Fout.write('pic_aline list=0.5,0,0.5,%.1f,%.1f,%.1f,%.1f,0,0.5,0\n'%(H1,W1,H1,W1))
        Off = (H1-(len(inKeys)-1)*PinSpace)/2
        for ind,Name in enumerate(inKeys):
            Fout.write('pic_line list=0,%.1f,0.5,0\n'%(Off+ind*PinSpace))
            Fout.write('pic_pin %s i xy=0,%.1f\n'%(Name,Off+ind*PinSpace))
            Fout.write('pic_text %s xy=0.6,%.1f\n'%(Name,Off+ind*PinSpace))
        
        Off = (H1-(len(ouKeys)-1)*PinSpace)/2
        for ind,Name in enumerate(ouKeys):
            Fout.write('pic_line list=%.1f,%.1f,0.5,0\n'%(W1,Off+ind*1))
            Fout.write('pic_pin %s i xy=%.1f,%.1f\n'%(Name,W1+0.5,Off+ind*1))
            Fout.write('pic_text %s xy=%.1f,%.1f align=right\n'%(Name,W1,Off+ind*1))
        Fout.write('pic_text %s xy=%.1f,%.1f\n'%(Current.Module,0.5,H1+0.2))
        Fout.write('end\n')
        Fout.close()

def reworkPort(Out):
    if '[' not in Out: return Out
    Xs = Out.split('[')
    Ret = '[%s %s' % (Xs[1],Xs[0])
    return Ret


def ensureExists(Obj,Inst,Pins):
    Pins = Pins.split()
    for Pin in Pins:
        if Pin not in Obj.conns:
            Obj.conns[Pin] = '0'
            print('ensurePinExists %s / %s  is missing %s pin connection' % (Inst,Obj.Type,Pin))


def typicalConns(Conns,Op):
    Ins = ['','','','','','','','','','']
    O = ''
    for Pin in Conns.keys():
        if Pin[0] == 'o':
            O = Conns[Pin]
        elif Pin[0] == 'i':
            Ind = int(Pin[1:])
            Ins[Ind]  = Conns[Pin]
    Ins2 = []
    for In in Ins:
        if In == 'vcc':
            Ins2.append('1')
        elif In == 'gnd':
            Ins2.append('0')
        elif In != '':
            Ins2.append(In)
    Bet = ' %s ' % Op
    Inss = Bet.join(Ins2)
    return O,Inss

def getBulk(Params,Default):
    for Prm,Val in Params:
        if Prm=='bulk':
            return Val
    return Default
def assembleArgvTypes():
    Maxes = {}
    Maxes['nmos']= 200
    Maxes['pmos']= 200
    Maxes['nmoshv']= 200
    Maxes['pmoshv']= 200
    Types = {}
    Types['nmos']='nmos'
    Types['pmos']='pmos'
    Types['nmoshv']='nch_hv'
    Types['pmoshv']='pch_hv'
    ind=1
    while ind<len(sys.argv):
        if sys.argv[ind]=='-t':
            X = sys.argv[ind+1]
            if '=' in X:
                WW = X.split('=')
                Types[WW[0]]=WW[1]
            else:
                print('-t %s should be of form nmos=nch'%X)
        elif sys.argv[ind]=='-m':
            X = sys.argv[ind+1]
            if '=' in X:
                WW = X.split('=')
                Maxes[WW[0]]=float(WW[1])
            else:
                print('-m %s should be of form nmos=200'%X)
        ind +=1
    return Types,Maxes


def complexWidthAndLength(Params):
    for Prm,Val in Params:
        if Prm=='size':
            res=''
            ww = Val.split(',')
            for Wrd in ww:
                if Wrd[0] in 'npNP':
                    Side=Wrd[0]
                    xx = Wrd[1:].split('/')
                else:
                    Side=''
                    xx = Wrd.split('/')
                if len(xx)==2:
                    W = xx[0]+'e-6'
                    L = xx[1]+'e-6'
                else:
                    W = xx[0]+'e-6'
                    L = '0.18e-6'
                res +=' %sW=%s %sL=%s'%(Side,W,Side,L)
            return res
    return ''
            


def widthAndLength(Params,Glbs):
    Diff = 5.0e-7
    for Prm,Val in Params:
        if Prm=='size':
            if 'param' in Val:
                Val = Val[6:-1]
                xx = Val.split('/')
                W=xx[0]
                L=xx[1]
                AD = '(%s*%.2e)'%(W,Diff)
                PD = '(2*(%s+%s))'%(W,L)
                AS = AD
                PS = PD
                return 'W=%s L=%s AS=%s AD=%s PD=%s PS=%s'%(W,L,AD,AS,PD,PS)
            xx = Val.split('/')
            if len(xx)==2:
                W = xx[0]+'e-6'
                L = xx[1]+'e-6'
                AD = float(W)*Diff
                AS = AD
                PD = 2*(float(W)+float(L))
                PS = PD
                return 'W=%s L=%s AS=%.2e AD=%.2e PD=%.2e PS=%.2e'%(W,L,AD,AS,PD,PS)
            else:
                LL = Glbs.get_context('default_mos_l')
                return 'W=%s L=%s' % (Val,LL)
            
    return 'W=1 L=1'


def get_size(Params,Default='10'):
    for Prm,Val in Params:
        if Prm=='size':
            return  Val
    return Default
    


def make_legal(Txt):
    if (Txt[0] in string.ascii_letters):
        return Txt

    if Txt[0] in string.digits:
        try:
            x = int(Txt)
            return Txt
        except:
            return '_%s'%Txt
    return Txt

def extractWireParams(Bus):
    Prms = []
    X = Bus.replace('[',' ')
    X = X.replace(':',' ')
    X = X.replace(']',' ')
    X = X.replace('-',' ')
    Wrds = X.split()
    for Y in Wrds[1:]:
        if Y[0] not in '0123456789':
            Prms.append(Y)
    return Prms
