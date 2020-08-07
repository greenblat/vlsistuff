
import logs
import veri
import string

class avlMasterClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.state=='write':
            if self.valid('avl_waitrequest'): return
            self.state='idle'
            self.force('avl_write',0)
            self.force('avl_read',0)
            self.force('avl_writedata',0)
            self.force('avl_address',0)
            self.force('avl_byteenable',0)
            return
        elif self.state=='read':
            if self.valid('avl_waitrequest'): return
            self.force('avl_write',0)
            self.force('avl_read',0)
            self.force('avl_writedata',0)
            self.force('avl_address',0)
            self.force('avl_byteenable',0)
            if self.valid('avl_readdatavalid'): 
                self.state='idle'
                rdata = self.peek('avl_readdata')
                logs.log_info('reading %08x'%rdata)
            return

        if self.Queue==[]: return

        Cmd = self.Queue.pop(0)
        wrds = Cmd.split()
        if wrds[0]=='write':
            Addr = eval(wrds[1])
            Wdata = eval(wrds[2])
            self.force('avl_write',1)
            self.force('avl_read',0)
            self.force('avl_writedata',Wdata)
            self.force('avl_address',Addr)
            self.force('avl_byteenable',0xffffffff)
            self.state='write'
            self.waiting = 1
        elif wrds[0]=='read':
            Addr = eval(wrds[1])
            self.force('avl_write',0)
            self.force('avl_read',1)
            self.force('avl_writedata',0)
            self.force('avl_address',Addr)
            self.force('avl_byteenable',0)
            self.state='read'
            self.waiting = 1
        elif wrds[0]=='wait':
            self.waiting = eval(wrds[1])
            return
        elif wrds[0]=='finish':
            veri.finish()
            
        


    avl_readdata = logs.peek('tb.avl_readdata')
    avl_readdatavalid = logs.peek('tb.avl_readdatavalid')
    avl_waitrequest = logs.peek('tb.avl_waitrequest')

