

import logs
import string

class adminWorkerClass:
    def __init__(self,Path):
        self.Path=Path

    def force(self,Sig,Val):
        if (type(Val)==types.StringType)and(Val[:2]=='0b'):
            veri.force('%s.%s'%(self.Path,Sig),Val)
        elif (type(Val)==types.StringType)and(Val[:2]=='0x'):
            veri.force('%s.%s'%(self.Path,Sig),Val)
        else:
            veri.force('%s.%s'%(self.Path,Sig),str(Val))
    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))
    def valid(self,Sig):
        return self.peek(Sig)==1

    def run(self):
        logs.log_info('run admin %s'%self.Path)

