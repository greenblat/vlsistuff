
import os,sys,string
import logs
import veri
class queueClass:
    def __init__(self,Monitors,Path='tb'):
        self.Queue = []
        Monitors.append(self)
        self.Path = Path
        self.waiting=0

    def force(self,Sig,Val):
        veri.force('%s.%s'%(self.Path,Sig),str(Val))

    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.Queue==[]: return

        Cmd = self.Queue.pop(0)
        wrds = string.split(Cmd)
        for ind,wrd in enumerate(wrds):
            if wrd=='finish':
                logs.log_info('finish from queue')
                veri.finish()
                sys.exit()
            if wrd=='wait':
                self.waiting = eval(wrds[ind+1])
                return
            
            if '=' in wrd:
                ww = string.split(wrd,'=')
                self.force(ww[0],eval(ww[1]))
