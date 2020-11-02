
USAGE = ''' 
import avalonMaster
avl = avalonMaster.avalonMaster('tb',Monitors)

avl.wait(100)
avl.makeRead(Addr0,Size=2)
avl.makeWrite(Addr1,Wdata)
avl.finish(100)

IMPORTANT: full form: avl.makeRead(Addr0,4,2)
avl.makeRead(Address,Size,Queue)

default is queue 1. so  if there is a long wait, and You need to inject
reads/writes in the middle, specify second queue: avl.makeRead(Address,4,2)

'''



import os,sys,string
import logs
import veri

class avalonMasterClass:
    def __init__(self,Path,Monitors):
        self.Path = Path
        Monitors.append(self)
        self.Queue=[]
        self.Queue2=[]
        self.waiting=0
        self.bwaiting=0
        self.Translates={}
        self.Prefix = ''
        self.Defines={}
        self.Comments=[]

    def peek(self,Sig):
        if self.Prefix!='': Sig = '%s%s'%(self.Prefix,Sig)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        return logs.peek('%s.%s'%(self.Path,Sig))
    def force(self,Sig,Val):
        if self.Prefix!='': Sig = '%s%s'%(self.Prefix,Sig)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        veri.force('%s.%s'%(self.Path,Sig),str(Val))


    def wait(self,Many):
        self.Queue.append('wait %s'%Many)
    def finish(self,Many=20):
        self.Queue.append('wait %s'%Many)
        self.Queue.append('finish')

    def print(self,Text,Queue=1):
        if Queue==1:
            self.Queue.append('print %s'%(Text))
        elif Queue==2:
            self.Queue2.append('print %s'%(Text))
        else:
            logs.log_error('QUEUE can be 1 or 2, not "%s"'%Queue)

    def write(self,Address,Wdata,Wstrb=0xff,Queue=1):
        if Queue==1:
            self.Queue.append('force avl_write=1 avl_address=%s avl_writedata=%s'%(Address,Wdata))
            self.Queue.append('force_cond !avl_waitrequest avl_write=0 avl_address=0')
        elif Queue==2:
            self.Queue2.append('force awvalid=1 awaddr=%s'%(Address))
            self.Queue2.append('force awvalid=0 awaddr=0')
            self.Queue2.append('force wvalid=1 wdata=%s wstrb=%s '%(Wdata,Wstrb))
            self.Queue2.append('force wvalid=0 wdata=0 wstrb=0')
        else:
            logs.log_error('QUEUE can be 1 or 2, not "%s"'%Queue)


    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        self.runQueue()


    def runQueue(self):
        if self.Queue==[]: return
        Cmd = self.Queue.pop(0)
        wrds = Cmd.split()
        logs.log_info('qu=%d  cmd="%s" wait=%d'%(len(self.Queue),Cmd,self.waiting))
        if wrds==[]:
            pass
        elif (wrds[0]=='wait'):
            self.waiting = int(wrds[1])
        elif (wrds[0]=='print'):
            logs.log_info('avalonMaster: %s'%' '.join(wrds[1:]))
        elif (wrds[0]=='finish'):
            logs.log_info('veri finish from axi Master')
            veri.finish()
            sys.exit()
        elif (wrds[0]=='force_cond'):
            Net = wrds[1]
            if Net[0] == '!':
                Cond = self.peek(Net[1:])
                if Cond!=0: 
                    self.Queue.insert(0,Cmd)
                    return
            else:
                Cond = self.peek(Net)
                if Cond!=1: 
                    self.Queue.insert(0,Cmd)
                    return
            for wrd in wrds[2:]:
                ww = wrd.split('=')
                Var = ww[0]
                Val = self.evalit(ww[1])
                self.force(Var,Val)
        elif (wrds[0]=='force'):
            for wrd in wrds[1:]:
                ww = wrd.split('=')
                Var = ww[0]
                Val = self.evalit(ww[1])
                self.force(Var,Val)
        else:
            logs.log_error('runQueue cannot deal with "%s"'%Cmd)

    def evalit(self,Expr):
        try:
            Val = eval(Expr,self.Defines)
        except:
            logs.log_error('eval of "%s" failed, on %s'%(Expr,self.Defines.keys()))
            Val=0
        return Val

    def readSequence(self,Fname):
        File = open(Fname)
        while True:
            line = File.readline()
            if line=='': return
            wrds = line.split()
            if wrds==[]:
                pass
            elif (wrds[0][0]=='#'):
                pass
            elif (wrds[0]=='finish'):
                self.Queue.append('finish')
#                logs.log_info('queue append finish')
            elif (wrds[0]=='wait'):
                self.Queue.append(line)
            elif (wrds[0]=='include'):
                self.readSequence(wrds[1])
            elif (wrds[0]=='define'):
                Var = wrds[1]
                Val = self.evalit(wrds[2])
                self.Defines[Var]=Val
                self.Defines[Val.upper()]=Val
            elif (wrds[0]=='write'):
                Addr = self.evalit(wrds[1])
                Data = self.evalit(wrds[2])
                self.makeWrite(Addr,Data)
            elif (wrds[0]=='read'):
                Addr = self.evalit(wrds[1])
                self.makeRead(Addr)

                                    





