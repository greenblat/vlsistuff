

import os,sys,string,random,types
import veri
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
import logs
Monitors=[]
cycles=0


import antClass
import axiMaster
axi = axiMaster.axiMasterClass('tb',Monitors)
axi.wait(150)
#  def makeWrite(self,Burst,Len,Address,Size=4):
axi.makeWrite(2,2,0x6808,4)
axi.wait(150)
axi.makeRead(2,2,0x6808,4)

import monitorNoc

monnoc = monitorNoc.monitorNocClass('tb.dut','net5@cpu->sw net6@sw0->admin net7@sw1->ant7 net9@dbg->axi net10@axi->ant8 net11@ant8.out net12@sw.in1',Monitors)
monnoc.more('net2@ant2->ant3 net3_ant4@ant3->ant4 net4@ant4->cpu')
monnoc.more('net1_ant1@ant1->clk net1_ant2@clk->ant2  net0@admin->ant1')

def negedgea():
    return
def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>1000):
        logs.log_info('finishing on timeout')
        veri.finish()
    rst_n = veri.peek('tb.rst_n')
    if (rst_n!='1'):
        return

    if (cycles==30):
        veri.listing('tb','100','deep.list')
        initial()

    if (cycles>30):
        for Mon in Monitors: Mon.run()
        runQueue()
        monitorResp()

ANTS = {}

def ant_operator(Id,Path):
    PP = logs.bin2str(Path)
    ID = logs.intx(Id)
#    logs.log_info('ant_operator %s %s'%(PP,ID))
    if (ID<=0):
        pass
    elif (ID not in ANTS):
        ANTS[ID] = antClass.antClass(PP,ID)
    else:
        ANTS[ID].run()

def cpu_operator(Id,Path):
    PP = logs.bin2str(Path)
    ID = logs.intx(Id)
#    logs.log_info('ant_operator %s %s'%(PP,ID))
    if (ID<=0):
        pass
    elif (ID not in ANTS):
        ANTS[ID] = antClass.antClass(PP,ID)
    else:
        ANTS[ID].run()

def ram_operator(Id,Path):
    PP = logs.bin2str(Path)
    ID = logs.intx(Id)
#    logs.log_info('ram_operator %s %s'%(PP,ID))
    if (ID<=0):
        pass
    elif ID not in ANTS:
        ANTS[ID] = antClass.ramClass(PP,ID)
    else:
        ANTS[ID].run()


Queue = []

tagTypes = { 'reset':0,'enumerate':2,'controls':4,'report':6 }

def buildMsg(Cmd,Tags,Bytes,Addr,Data):
    Word0 = 0
    if type(Cmd)==types.IntType:
        Word0 = Cmd
    elif Cmd=='read':
        Word0 = 1
    elif Cmd=='write':
        Word0 = 2
    elif Cmd=='mng':
        Word0 = 3
    else:
        logs.log_error('reqMsg got cmd=%s'%Cmd)

    if type(Tags)==types.IntType:
        Word0 |= Tags<<2
    elif (Tags in tagTypes):
        Word0 |= (tagTypes[Tags]<<2)
    elif (Tags=='reset'):
        Word0 |= 0<<2
    elif (Tags=='enumerate'):
        Word0 |= 2<<2
    elif (Tags=='controls'):
        Word0 |= 4<<2
    elif (Tags=='report'):
        Word0 |= 6<<2
        
    checkField("bytes",Bytes,4)
    checkField("tags",Tags,5)
    Word0 |= (Bytes<<7)
    Word0 |= (Addr<<11)
    Word0 |= (Data<<43)
    return Word0

def reqMsg(Cmd,Tags,Bytes,Addr,Data):
    Word0 = buildMsg(Cmd,Tags,Bytes,Addr,Data)
    wrQueue(0,Word0 & 0xffffffffffffffff)
    wrQueue(1,(Word0>>64) & 0xffffffffffffffff)
    wrQueue(2,(Word0>>128) & 0xffffffffffffffff)

def checkField(Name,Val,Width):
    if type(Val)!=types.IntType: return
    A = bin(Val)
    X = len(A)-2
    if X>Width:
        logs.log_error('checkField width violartion field=%s exp=%d act=%d'%(Name,Width,X))

def wrQueue(Addr,Data):
    Queue.append(('force','req_addr',Addr))
    Queue.append(('force','req_data',Data))
    Queue.append(('force','req_write',1))
    Queue.append(('wait',1))
    Queue.append(('force','req_write',0))

waiting = 0
def runQueue():
    global waiting
#    if len(Queue)>0:
#        logs.log_info('waiting=%d cmd0=%s len=%d '%(waiting,Queue[0],len(Queue)))
#    else:
#        logs.log_info('waiting=%d cmd0=0 len=%d '%(waiting,len(Queue)))
    if (waiting>0):
        waiting -= 1
        return

    while Queue!=[]:
        Cmd = Queue.pop(0)
        if Cmd[0]=='wait':
            waiting = int(Cmd[1])-1
            return
        if Cmd[0]=='finish':
            logs.log_info('finishing on queue command')
            sys.exit()
            veri.finish()
            return
        if Cmd[0] == 'force':
            veri.force('tb.'+Cmd[1],str(Cmd[2]))
#            logs.log_info('forcing %s %s'%(Cmd[1],Cmd[2]))
        else:
            logs.log_error('bad queue directive "%s"'%str(Cmd))


def initial():
    veri.force('tb.bready','1')
#    reqMsg('mng','controls',0,0,234)
    Queue.append(('wait',20))
    reqMsg('mng','enumerate',0,0,0)
    Queue.append(('wait',500))
#    reqMsg('write','0',8,0x5000,0x34567890abc)
#    Queue.append(('wait',100))
#    reqMsg('read','0',0,0x5000,0x0000+(2<<32))
#    Queue.append(('wait',100))
#    Queue.append(('wait',500))
    Queue.append(('finish',0))

    
respState='idle'
def monitorResp():
    global respState,data0,data1,data2
    resp_count = logs.peek('tb.resp_count')
    if (resp_count==0)and(respState=='idle'):
        veri.force('tb.resp_read','0')
    else:
        if respState=='idle':
            veri.force('tb.resp_read','1')
            veri.force('tb.resp_addr','0')
            respState='1'
        elif respState=='1':
            data0 = logs.peek('tb.resp_data')
            veri.force('tb.resp_addr','1')
            respState='2'
        elif respState=='2':
            data1 = logs.peek('tb.resp_data')
            veri.force('tb.resp_addr','2')
            respState='3'
        elif respState=='3':
            data2 = logs.peek('tb.resp_data')
            respState='4'
            Msg = data0 | ( data1<<64) | (data2<<128)
            logs.log_info('resp fifo %x '%(Msg))
            (Cmd,Tags,Bytes,Addr,Data) = parseMsg(Msg)
            logs.log_info('responce cmd=%s tags=%x bytes=%x addr=%08x data=%x'%(cmdKind(Cmd),Tags,Bytes,Addr,Data))
            veri.force('tb.resp_addr','3')
        elif respState=='4':
            respState='idle'
            veri.force('tb.resp_addr','0')

        
def cmdKind(Cmd):
    if (Cmd==1): return 'read'
    if (Cmd==2): return 'write'
    if (Cmd==3): return 'mng'
    return 'strange'

def parseMsg(Msg):
    Cmd = Msg & 3
    Tags = (Msg>>2) & 0x1f
    Bytes = (Msg>>7) &  0xf
    Addr  = (Msg>>11) &  0xffffffff
    Data  = (Msg>>43)
    if Cmd==1:
        MoreBytes = Data>>32
        Bytes = MoreBytes<<4 + Bytes
        Data = Data & 0xffffffff
    return (Cmd,Tags,Bytes,Addr,Data)


def cucu():
    veri.force('tb.req_addr','0')
    veri.force('tb.req_data','0')
    veri.force('tb.req_write','0')
    veri.force('tb.resp_addr','0')
    veri.force('tb.resp_read','0')
    req_count = logs.peek('tb.req_count')
    resp_count = logs.peek('tb.resp_count')
    resp_data = logs.peek('tb.resp_data')
