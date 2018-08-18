


import logs
import string


class monitorXsClass:
    def __init__(self,Path,Str,Monitors):
        self.Path = Path
        self.List = string.split(Str)
        Monitors.append(self)

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def run(self):
        for Sig in self.List:
            Val = self.peek(Sig)
#            logs.log_info('%s %s'%(Sig,Val))
            if Val<0:
                logs.log_error('%s is X'%(Sig))
