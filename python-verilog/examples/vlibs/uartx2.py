
import logs
import veri


class uartx2Class:
    def __init__(self,Path,Aluka=False):
        self.Path = Path
        self.Aluka=Aluka
        self.reset()

    def reset(self):
        self.txqueue=[]
        self.rxqueue=[]
        self.tx_empty=1
        self.force('tx_empty',1)
        self.force('txd',1)
        self.force('status',2)
        self.force('rxdata',0)
        self.force('rx_valid',0)
        self.txstate='idle'
        self.rxstate='idle'
        self.txcount=0
        self.rxcount=0
        self.rxstring=''
        self.txstring=''

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def force(self,Sig,Val):
        if self.Aluka:
            Now = self.peek(Sig)
            if str(Val)!=str(Now):
                logs.log_wrong('aluka %s  sig=%s   exp=%s act=%s'%(self.Path,Sig,Val,Now))
#            else:
#                logs.log_correct('aluka %s  sig=%s   exp=%s act=%s'%(self.Path,Sig,Val,Now))
            return
        return veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def run(self):
        if self.peek('rst_n')==0:
            self.reset()
            return
        if self.peek('write_tx')==1:
            txdata = self.peek('txdata')
            self.txqueue.append(txdata)
            
        if self.txstate=='idle':
            if self.txqueue!=[]:
                self.txstate='work'
                self.txstring = '0'+logs.bin8(self.txqueue.pop(0))+'11'
        elif self.txstate=='work':
            self.force('txd',self.txstring[0])
            self.txstring = self.txstring[1:]
            self.txcount=0
            self.txstate='wait'
        elif self.txstate=='wait':
            self.txcount += 1
            if self.txcount==self.peek('baudrate'):
                if self.txstring=='':
                    self.txstate='idle'
                else:
                    self.txstate='work'


        if self.txqueue==[]:
            self.force('tx_empty',1)
        else:
            self.force('tx_empty',0)



        if self.rxqueue!=[]:
            self.force('rxdata',self.rxqueue[0])
            self.force('rx_valid',1)
            

        if (self.peek('read_rx')==1)and(self.rxqueue!=[]):
            self.rxqueue.pop(0)
            if self.rxqueue==[]:
                self.force('rx_valid',0)


        logs.asciiForce('tb.rxstate',self.rxstate)
        logs.asciiForce('tb.txstate',self.txstate)

        if self.rxstate=='idle':
            rxd = self.peek('rxd')
            if rxd==0:
                self.rxstate='open'
                self.rxcount=0
                self.rxstring=''
        elif self.rxstate=='open': 
            self.rxcount += 1
            if self.rxcount==(self.peek('baudrate')/2):
                rxd = self.peek('rxd')
                if rxd==0:
                    self.rxstate = 'accumulate'
                    self.rxcount = 0
                else:
                    self.rxstate = 'idle'
        elif self.rxstate=='accumulate':
            self.rxcount += 1
            if self.rxcount==self.peek('baudrate'):
                self.rxstring += str(self.peek('rxd'))
                self.rxcount = 0
                if len(self.rxstring)==8:
                    self.rxstate='closing'
        elif self.rxstate=='closing':
            self.rxcount += 1
            if self.rxcount==self.peek('baudrate'):
                if self.peek('rxd')==0:
                    self.rxstate='badclosing'
                    logs.log_error('badclosing')
                else:
                    self.rxqueue.append(int(self.rxstring,2))
                self.rxcount = 0
                self.rxstate='idle'
                self.rxstring=''
        elif self.rxstate=='badclosing': 
            self.rxcount += 1
            if self.rxcount==self.peek('baudrate'):
                self.rxcount = 0
                self.rxstate='idle'
                self.rxstring=''
                    
        veri.force('tb.marker',str(len(self.rxstring)))
        veri.force('tb.marker2',str(len(self.txstring)))
                





'''
module py_uartx2 (
     input [15:0] baudrate
    ,input    clk 
    ,input [7:0] control
    ,input    rst_n
    ,input    read_rx
    ,input    rxd 
    ,input [7:0] txdata
    ,input    write_tx
    ,output reg    rx_valid
    ,output reg [7:0] rxdata
    ,output reg [7:0] status
    ,output reg    tx_empty
    ,output reg    txd 
);
initial begin
    rx_valid = 0;
    rxdata = 0;
    status = 0;
    tx_empty = 0;
    txd = 0;
end
endmodule
'''
