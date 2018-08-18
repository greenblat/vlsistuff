
import string
import logs
import veri
import verilog


class antClass:
    def __init__(self,Path,Id):
        self.Path=Path
        self.Id = Id
        self.baseAddress= 0
        self.Array = {}
        self.queueOut = []
        self.sendingActive = False
        logs.log_info('created %s %s'%(Path,Id))

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        return veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def run(self):
        base = self.peek('base_address')    
        if base!=self.baseAddress:
            self.baseAddress = base
            logs.log_info('change in base address to %x of %s   %s '%(base,self.Path,self.Id))
        msg_in = self.peek('msg_in')    
        if (msg_in & 3)!=0:
            (Cmd,Tags,Bytes,Addr,Data) = verilog.parseMsg(msg_in)
            AddrIn = Addr-self.baseAddress
            logs.log_info('ant %s  cmd=%s tags=%x bytes=%x addr=%08x (in %08x) data=%x'%(self.Path,verilog.cmdKind(Cmd),Tags,Bytes,Addr,AddrIn,Data))
            if Cmd==2:
                self.writes(Bytes,AddrIn,Data)
            elif Cmd==1:
                self.reads(Bytes,AddrIn,Data)

            self.force('msg_in_ack',1)
        else:
            self.force('msg_in_ack',0)
        self.useQueue()

    def useQueue(self):
        ack = self.peek('msg_out_ack')
        if not self.sendingActive:
            if self.queueOut==[]: 
                self.force('msg_out',0)
                return
            Msg = self.queueOut.pop(0)
            self.force('msg_out',Msg)
            self.sendingActive= (ack==0)
        elif (ack==1):
            veri.force('msg_out',0)
            self.sendingActive= False
            
            



    def writes(self,Bytes,Addr,Data):
        for ii in range(Bytes):
            self.Array[Addr] = Data & 0xff
            Addr += 1
            Data = Data >> 8

    def reads(self,Bytes,AddrIn,AddrOut):
        while Bytes>=8:
            self.makeRead(8,AddrIn,AddrOut)
            Bytes -= 8
            AddrIn += 8
            AddrOut += 8
        if Bytes>0:
            self.makeRead(Bytes,AddrIn,AddrOut)


    def makeRead(self,Bytes,AddrIn,AddrOut):
        Data = 0
        Addr = AddrOut
        for ii in range(Bytes):
            Byte = self.byte(AddrIn)
            Data |= (Byte<<(ii*8))
            AddrIn += 1
        self.sendMsg('write',0,Bytes,Addr,Data)

    def byte(self,Addr):
        if Addr in self.Array:
            return self.Array[Addr]
        return 0

    def sendMsg(self,Cmd,Tags,Bytes,Addr,Data):
        Word0 = verilog.buildMsg(Cmd,Tags,Bytes,Addr,Data)        
        self.queueOut.append(Word0)



class ramClass(antClass):
    def __init__(self,Path,Id):
        antClass.__init__(self,Path,Id)
        self.Ram = {}

        



    

