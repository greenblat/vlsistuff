#! /usr/bin/python

import os,sys,string,types
import instancesLib

NewName = os.path.expanduser('~')
sys.path.append('%s/pybin3'%NewName)
import module_class

def main():
    Fsetupname = sys.argv[1]
    File = open(Fsetupname)
    Lines = File.readlines()
    File.close()
    workLines(Lines)
#    db.wires()
#    db.dump()
    do_verilog()
#    db.graph()

def workLines(Lines):
    Big = ''
    for line in Lines:
        if '#' in line:
            line = line[:line.index('#')]
        Big += line[:-1]+' '
    Big = string.replace(Big,'->',' -> ')
    Lines = string.split(Big,';')
    for lnum,line in enumerate(Lines):
        wrds = string.split(line)
        if (len(line)<2)or(len(wrds)<1):
            pass
        elif wrds[0]=='default':
            setDefault(wrds[1:],lnum)
    Module = db.getDef('module','noc')
    db.Mod = module_class.module_class(Module)

    for lnum,line in enumerate(Lines):
        wrds = string.split(line)
        if (len(line)<2)or(len(wrds)<1):
            pass
        elif wrds[0][0] in ['#','/']:
            pass
        elif wrds[0]=='instance':
            addInstance(wrds[1:],lnum)
        elif '->' in line:
            addConns(wrds,lnum)
        elif wrds[0]=='default':
            pass
        else:
            log_error('unrecognized lnum=%d: "%s"'%(lnum,line))
            return


class dbClass:
    def __init__(self):
        self.instances={}
        self.conns={}
        self.defaults={}
        self.netnames={}
    def evalx(self,What):
        try:
            return eval(What)
        except:
            return What

    def dump(self):
        for Inst in self.instances:
            self.instances[Inst].dump()

    def graph(self):
        Module = self.getDef('module','noc')
        Fout = open('%s.dot'%Module,'w')
        Fout.write('digraph %s {\n'%Module)

        Ins = {}
        Ous = {}
        for Inst in self.instances:
            Obj = self.instances[Inst]
            for Pin in Obj.conns:
                Net = Obj.conns[Pin]
                if 'IN' in Pin:
                    Ins[Net]=Inst
                elif 'OUT' in Pin:
                    Ous[Net]=Inst
                else:
                   print '>>>>',Pin


        for Inst in self.instances:
            Obj = self.instances[Inst]
            Type = Obj.Type
            if 'type' in Obj.Props:
                Typev = Obj.Props['type']
            else:
                Typev = Type
            Dwid = db.getProp('DWID',Obj.Props)
            Depth = db.getProp('depth',Obj.Props,0)
            if Type=='admin':
                Fout.write('%s [color="red";label="%s/%s"];\n'%(Inst,Inst,Dwid))
            elif Depth>0:
                Fout.write('%s [color="green";label="%s/%s*%s"];\n'%(Inst,Inst,Depth,Dwid))
            else:
                Fout.write('%s [label="%s/%s"];\n'%(Inst,Inst,Dwid))
        for Net in Ins:
            To = Ins[Net]
            if Net in Ous:
                From = Ous[Net]
            else:
                From = Net
            Fout.write('%s -> %s;\n'%(From,To))

        Fout.write('}\n')
        Fout.close()
        os.system('dot %s.dot -Tpng -o%s.png'%(Module,Module))





    def getProp(self,Prop,Pool,Def=''):
        if Prop in Pool: return Pool[Prop]
        return self.getDef(Prop,Def)

    def getDef(self,Param,Def=''):
        if Param in self.defaults: return self.defaults[Param]
        if Def=='':
            log_error('getDef has no value for %s'%Param)
            return Param
        return Def
        

    def wires(self):
#        for Dir,Who in self.conns:
#            print 'wires %s %s <> %s '%(Dir,Who,self.conns[(Dir,Who)])

        Net = 0
        for (Dir,Who) in self.conns:
            if (Dir,Who) in self.netnames:
                Sig = self.netnames[(Dir,Who)]
            else:
                Sig = 'net%s'%Net
                Net += 1
            Other = self.conns[(Dir,Who)]
            Odir = otherDir(Dir)
            if type(Who)==types.StringType:
                Pin = Dir
                Inst = Who
            else:
                Pin = '%s%s'%(Dir,Who[1])
                Inst = Who[0]
            self.instances[Inst].addConn(Pin,Sig)

            if type(Other)==types.StringType:
                Pin = Odir
                Inst = Other
            else:
                Pin = '%s%s'%(Odir,Other[1])
                Inst = Other[0]

            self.instances[Inst].addConn(Pin,Sig)
                

    def extractWires(self,Big2):
        Bigw = ''
        Bigio = ''

        Wires={}
        Lines = string.split(Big2,'\n')
        Type = 'strange'
        Inst = 'strange'
        for line in Lines:
            for Chr in '.(),':
                line = string.replace(line,Chr,' %s '%Chr)
            wrds = string.split(line)
            if len(wrds)<2:
                pass
            elif wrds[1] in self.instances:
                Inst = wrds[1]
                Type = wrds[0]
            elif wrds[1] == '#':
                wrds1 = wrds[2:]
                Inst = extractInst(wrds[2:])
                if  Inst in self.instances:
                    Type = wrds[0]
                else:
                    log_error('inst %s not in instances "%s"'%(Inst,line))
            else:
                while '.' in wrds:
                    ind = wrds.index('.')
                    Pin = wrds[ind+1]
                    if (wrds[ind+2]=='(')and(wrds[ind+4]==')'):
                        Dir,WW = instancesLib.getPinWid(Type,Pin)
                        if WW=='WID':
                            try:
                                WW = int(self.instances[Inst].Props['wid'])
                            except:
                                WW = int(self.getDef('DWID'))
                            WW += 32+9+2
                                
                        Sig = wrds[ind+3]
                        if Sig[0] in '0123456789-':
                            pass
                        elif Sig not in Wires:
                            Wires[Sig]=WW
                            if Dir=='wire':
                                if int(WW)==1:
                                    Bigw += 'wire %s;\n'%(Sig)
                                else:
                                    Bigw += 'wire [%s-1:0] %s;\n'%(WW,Sig)
                            else:
                                if int(WW)==1:
                                    Bigio += '   ,%s %s\n'%(Dir,Sig)
                                else:
                                    Bigio += '   ,%s [%s-1:0] %s\n'%(Dir,WW,Sig)
                        elif (Wires[Sig]!=WW):
                            log_error('wire %s changed wid from %s to %s'%(Sig,Wires[Sig],WW))

                    wrds = wrds[ind+1:]
        return Bigio,Bigw



ADMIN =  [ 
     ('req_count','output',8)
    ,('req_data','input',64)
    ,('req_addr','input',3)
    ,('req_write','input',1)
    ,('resp_count','output',8)
    ,('resp_data','output',64)
    ,('resp_addr','input',3)
    ,('resp_read','input',1)
]

AXI_SLAVE = [
     ('awid','input',4)
    ,('awaddr','input',32)
    ,('awlen','input',8)
    ,('awsize','input',3)
    ,('awburst','input',2)
    ,('awcache','input',4)
    ,('awprot','input',3)
    ,('awvalid','input',0)
    ,('awready','output',0)
    ,('wdata','input',128)
    ,('wstrb','input',16)
    ,('wlast','input',0)
    ,('wvalid','input',0)
    ,('wready','output',0)
    ,('bid','output',4)
    ,('bresp','output',2)
    ,('bvalid','output',0)
    ,('bready','input',0)
    ,('arid','input',4)
    ,('araddr','input',32)
    ,('arlen','input',8)
    ,('arsize','input',3)
    ,('arburst','input',2)
    ,('arcache','input',4)
    ,('arprot','input',3)
    ,('arvalid','input',0)
    ,('arready','output',0)
    ,('rid','output',4)
    ,('rdata','output',128)
    ,('rresp','output',2)
    ,('rlast','output',0)
    ,('rvalid','output',0)
    ,('rready','input',0)
]



ADDITIONS = {}
ADDITIONS['rou_dbguart'] = [ ('rxd','input',1), ('txd','output',1)]
ADDITIONS['rou_admin']   = ADMIN
ADDITIONS['rou_axi_slave']   = AXI_SLAVE


def do_verilog():
    for Inst in db.Mod.insts:
        Obj = db.Mod.insts[Inst]
        if Obj.Type=='switch2':
            Obj.Type = 'rou_switch2'
        if Obj.Type=='admin':
            Obj.Type = 'rou_admin'
#            for (Net,Dir,Wid) in ADMIN:
#                db.Mod.add_sig(Net,Dir,Wid)
#                db.Mod.add_conn(Inst,Net,Net)
            db.Mod.add_conn(Inst,'seen_monitor',"1'b0")
        if Obj.Type in ADDITIONS:
            LLL = ADDITIONS[Obj.Type]
            if 'prefix' in Obj.specials:
                Pref = Obj.specials['prefix']
            else:
                Pref = ''
            for (Net,Dir,Wid) in LLL:
                db.Mod.add_sig(Pref+Net,Dir,Wid)
                db.Mod.add_conn(Inst,Net,Pref+Net)

    
        
    for Inst in db.Mod.insts:
        Obj = db.Mod.insts[Inst]
        for Prm in ['pages','id']:
            if Prm in Obj.params:
                Val = Obj.params.pop(Prm)
                if Prm=='id': Prm='whoami'
                Obj.conns[Prm]=Val
        for Prm in ['type']:
            if Prm in Obj.params: Obj.params.pop(Prm)
        for Prm in ['wid']:
            if Prm in Obj.params: 
                Val = Obj.params.pop(Prm)
                Obj.params['DWID']=Val
        for Pin in ['in','out','in0','in1','out0','out1']:
            expilictWires(Inst,Pin)


    insertClockChangers()

    Fout = open('%s.v'%db.Mod.Module,'w')
    db.Mod.dump_verilog(Fout)
    Fout.close()

def insertClockChangers():
    NetsOut,NetsIn={},{}
    for Inst1 in db.Mod.insts:
        Obj1 = db.Mod.insts[Inst1]
        Clk1 = Obj1.conns['clk']
        for Post in ['','0','1','2']:
            Pino = 'rou_out'+Post
            Pini = 'rou_in'+Post
            if Pino in Obj1.conns:
                Out = Obj1.conns[Pino]
                In = Obj1.conns[Pini]
                NetsOut[(Out,Post)]=Inst1,Clk1
                NetsIn[(In,Post)]=Inst1,Clk1
    for Net1,Post1 in NetsOut:
        Inst1,Clk1 = NetsOut[(Net1,Post1)]
        for Net2,Post2 in NetsIn:
            if Net2==Net1:
                Inst2,Clk2 = NetsIn[(Net2,Post2)]
                if Clk1!=Clk2:
                    insertClockChanger(Inst1,Clk1,'rou_out'+Post1,Inst2,Clk2,'rou_in'+Post2)


def insertClockChanger(Inst1,Clk1,Pino1,Inst2,Clk2,Pini2):
    Inst = 'chng_%s_%s'%(Inst1,Inst2)
    Obj = module_class.instance_class('rou_changeclk',Inst)
    db.Mod.insts[Inst]=Obj
    Obj.conns['clka']=Clk1
    Obj.conns['clkb']=Clk2
    Obj.conns['rsta_n']='rst_n'
    Obj.conns['rstb_n']='rst_n'

    Obj1 = db.Mod.insts[Inst1]
    Obj2 = db.Mod.insts[Inst2]
    Net1 = Obj1.conns[Pino1]

    _,Wid = db.Mod.nets[Net1]
    db.Mod.nets['%s_%s'%(Net1,Inst1)]= ('wire',Wid)
    db.Mod.nets['%s_%s'%(Net1,Inst2)]= ('wire',Wid)
    db.Mod.nets.pop(Net1)

    db.Mod.nets['%s_seen_%s'%(Net1,Inst1)]= ('wire',0)
    db.Mod.nets['%s_seen_%s'%(Net1,Inst2)]= ('wire',0)
    db.Mod.nets.pop(Net1+'_seen')

    db.Mod.nets['%s_ack_%s'%(Net1,Inst1)]= ('wire',2)
    db.Mod.nets['%s_ack_%s'%(Net1,Inst2)]= ('wire',2)
    db.Mod.nets.pop(Net1+'_ack')

    Obj1.conns['rou_out']='%s_%s'%(Net1,Inst1)
    Obj1.conns['rou_out_seen']= '%s_seen_%s'%(Net1,Inst1)
    Obj1.conns['ack_out']='%s_ack_%s'%(Net1,Inst1)

    Obj2.conns['rou_in']='%s_%s'%(Net1,Inst2)
    Obj2.conns['rou_in_seen']= '%s_seen_%s'%(Net1,Inst2)
    Obj2.conns['ack_in']='%s_ack_%s'%(Net1,Inst2)

    Obj.conns['roua_in']='%s_%s'%(Net1,Inst1)
    Obj.conns['roua_in_seen']= '%s_seen_%s'%(Net1,Inst1)
    Obj.conns['acka_in']='%s_ack_%s'%(Net1,Inst1)

    Obj.conns['roub_out']='%s_%s'%(Net1,Inst2)
    Obj.conns['roub_out_seen']= '%s_seen_%s'%(Net1,Inst2)
    Obj.conns['ackb_out']='%s_ack_%s'%(Net1,Inst2)


    return




def expilictWires(Inst,Pin):
    for Inst in db.Mod.insts:
        Obj = db.Mod.insts[Inst]
        if Pin in Obj.conns:
            Net = Obj.conns.pop(Pin)
            db.Mod.add_sig(Net,'wire',171)
            db.Mod.add_sig(Net+'_ack','wire',3)
            db.Mod.add_sig(Net+'_seen','wire',1)
            Obj.conns['rou_%s'%Pin]=Net
            Obj.conns['ack_%s'%Pin]=Net+'_ack'
            Obj.conns['rou_%s_seen'%Pin]=Net+'_seen'

#        if 'out' in Obj.conns:
#            Net = Obj.conns.pop('out')
#            db.Mod.add_sig(Net,'wire',171)
#            db.Mod.add_sig(Net+'_ack','wire',1)
#            db.Mod.add_sig(Net+'_seen','wire',1)
#            Obj.conns['rou_out']=Net
#            Obj.conns['ack_out']=Net+'_ack'
#            Obj.conns['rou_out_seen']=Net+'_seen'







def extractInst(wrds):
    while True:
        if wrds==[]: return 'bad'
        if len(wrds)>=3:
            if (wrds[0]==')')and(wrds[2]=='('):
                return wrds[1]
        wrds.pop(0)

    

def otherDir(Dir):
    if Dir[0]=='i': return 'OUT'
    return 'IN'

class instanceClass:
    def __init__(self,Inst,Type):
        self.Inst=Inst
        self.Type=Type
        self.Props={}
        self.conns={}
    def addConn(self,Pin,Net):
        if Pin in self.conns:
            log_error('addConn %s %s double pin=%s net=%s was=%s'%(self.Inst,self.Type,Pin,Net,self.conns[Pin]))
        self.conns[Pin]=Net

    def dump(self):
        print '>> %s type=%s %s conns:'%(self.Inst,self.Type,self.Props)
        for Pin in self.conns:
            print '       %s=%s'%(Pin,self.conns[Pin])
        print

db = dbClass()

def addInstance(wrds,lnum):
    Inst = wrds[0]
    Type = wrds[1]
    Obj = module_class.instance_class(Type,Inst)
    db.Mod.insts[Inst]=Obj
    db.instances[Inst]=Obj
    for wrd in wrds[2:]:
        if '=' in wrd:
            ww = string.split(wrd,'=')
            Var = ww[0]
            Val = db.evalx(ww[1])
            Obj.params[Var]=Val
            
        else:
            log_error('addInstance got "%s"'%str(wrds))
        
    if 'clk' not in Obj.params:
        Clk = db.getDef('clk','clk')
        Obj.conns['clk']=Clk
        db.Mod.add_sig(Clk,'input',1)
    else:
        Obj.conns['clk']=Obj.params['clk']
        db.Mod.add_sig(Obj.params['clk'],'input',1)
        Obj.params.pop('clk')
    Obj.conns['rst_n']='rst_n'
    db.Mod.add_sig('rst_n','input',1)


def addClockChange(Clka,Clkb):
    Inst = '%s_%s_chng'%(Clka,Clkb)
    Obj = module_class.instance_class('changeclk',Inst)
    db.instances[Inst]=Obj
    db.Mod.insts[Inst]=Obj
    Obj.conns['clka']=Clka
    Obj.conns['clkb']=Clkb
    return Inst



def addConns(wrds,lnum):
    if (len(wrds)==4)and(wrds[1]=='->')and('=' in wrds[3]):
        ww = string.split(wrds[3],'=')
        if ww[0]=='name':
            Name = ww[1]
        else:
            log_error('addConn explicit name got "%s"'%(str(wrds)))
            Name=''
        addConn(wrds[0],wrds[2],Name)
        return

    while len(wrds)>=3:
        if wrds[1]=='->':
            addConn(wrds[0],wrds[2])
            wrds = wrds[2:]
        else:
            log_error('addConns wrds=%s'%str(wrds))
            return
    if len(wrds)!=1:
        log_error('addConns wrds=%s'%str(wrds))

def legalInst(Inst):
    Inst0 = checkConn(Inst)
    if type(Inst0)!=types.StringType:
        Inst0 = Inst0[0]
    if Inst0 not in db.Mod.insts:
        log_error('addCon got inst=%s is not declared'%(Inst))
        sys.exit()

    

def addConn(From,To,Name=''):
    Fromx = checkConn(From)
    Tox = checkConn(To)
    Net = inventNet(Name)
    legalInst(From)
    legalInst(To)

    if type(Fromx)==types.StringType:
        Objf = db.Mod.insts[From]
        Objf.conns['out'] =  Net
    else:
        Objf = db.Mod.insts[Fromx[0]]
        Objf.conns['out'+Fromx[1]] =  Net
        
    if type(Tox)==types.StringType:
        Objt = db.Mod.insts[To]
        Objt.conns['in'] =  Net
    else:
        Objf = db.Mod.insts[Tox[0]]
        Objf.conns['in'+Tox[1]] =  Net


nnet = -1
def inventNet(Name):
    global nnet
    if Name!='': return Name
    nnet += 1
    return 'net%d'%nnet



#    Clka = db.getProp('clk',db.instances[Fromx].Props,'clk')
#    Clkb = db.getProp('clk',db.instances[Tox].Props,'clk')
#
#    if Clka!=Clkb:
#        CC = addClockChange(Clka,Clkb)
#        print '>>>>>',From,To,Fromx,Tox,Clka,Clkb
#    else:

#    db.conns[('IN',Tox)] = Fromx

def checkConn(Text):
    if ':' in Text:
        ww = string.split(Text,':')
        return (ww[0],ww[1])
    return Text

def setDefault(wrds,lnum):
    if len(wrds)==2:
        db.defaults[wrds[0]] = db.evalx(wrds[1])
    else:
        log_error('setDefault wrds=%s'%str(wrds))

def log_error(Txt):
    print 'Error! %s'%Txt


instancesLib.log_error = log_error








main()

    

