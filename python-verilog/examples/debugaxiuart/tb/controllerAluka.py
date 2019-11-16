



import string
import logs
import veri
import types


class controllerClass:
    def __init__(self,Path,Monitors):
        self.Path = Path
        Monitors.append(self)
        self.txQueue=[]
        self.axiQueue = []
        self.rgfQueue = []

        self.axiSize = 2
        self.addrIncr = 1
        self.Addr = 0x1000
        self.Bytes = 0x10

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def run(self):
        return
#        self.runTx()
#        self.runRx()
#        self.runAxi()
#        self.runRgf()


    


    def runRgf(self):
        if self.rgfQueue==[]:
            self.force('rgf_sel',0)
            self.force('rgf_wr',0)
            return
        (Wr,Addr,Wdata) = self.rgfQueue.pop(0)
        if Wr=='wr': Wr=1
        else: Wr=0
        self.force('rgf_sel',1)
        self.force('rgf_wr',Wr)
        self.force('rgf_addr',Addr)
        self.force('rgf_wdata',Wdata)



    def runAxi(self):
        if (self.axiQueue==[]): 
            self.force('drct_rd',0)
            self.force('drct_wr',0)
            return

        Dir,Addr,Bytes = self.axiQueue.pop(0)
        if Dir=='wr':
            self.force('drct_wr',1)
            self.force('drct_rd',0)
            self.force('drct_wr_rmt_addr_incr',1)
            self.force('drct_wr_rmt_addr',Addr)
            self.force('drct_wr_bytes',Bytes)
            self.force('drct_wr_rmt_size',2)
        elif Dir=='rd':
            self.force('drct_wr',0)
            self.force('drct_rd',1)
            self.force('drct_rd_rmt_addr_incr',1)
            self.force('drct_rd_rmt_addr',Addr)
            self.force('drct_rd_bytes',Bytes)
            self.force('drct_rd_rmt_size',2)




    def runRx(self):
        return

    def runTx(self):
        if self.txQueue==[]: 
            self.force('tx_fifo_write',0)
            return

        if self.peek('tx_fifo_full')==1: 
            self.force('tx_fifo_write',0)
            return


        Char = self.txQueue.pop(0)
        self.force('tx_fifo_write',1)
        self.force('tx_fifo_data',Char)
        return




    def action(self,Str):
        Wrds  = string.split(Str)
        if Wrds[0]=='uart':
           Str  = 'tx '+Wrds[1]+'%02x'%eval(Wrds[2])+(hex(eval(Wrds[3])))[2:]+'.'
           self.uart.action(Str)

        elif Wrds[0]=='tx':
            for Wrd in Wrds[1:]:
                self.send(Wrd)
        elif Wrds[0]=='axiwr':
            self.Bytes = eval(Wrds[1])
            self.Addr = eval(Wrds[2])
            self.axiQueue.append(('wr',self.Addr,self.Bytes))
        elif Wrds[0]=='axird':
            self.Bytes = eval(Wrds[1])
            self.Addr = eval(Wrds[2])
            self.axiQueue.append(('rd',self.Addr,self.Bytes))
        elif Wrds[0]=='rgf':
            self.rgfQueue.append((Wrds[1],eval(Wrds[2]),eval(Wrds[3])))
        else:
            logs.log_error('action of cmtroller %s'%str(Wrds))

    def send(self,Byte):
        if type(Byte)==types.StringType:
            if len(Byte)==1:
                Byte = ord(Byte)
                self.send(Byte)
                return
            else:
                for Chr in Byte:
                    self.send(Chr)
                return
        self.txQueue.append(Byte)


