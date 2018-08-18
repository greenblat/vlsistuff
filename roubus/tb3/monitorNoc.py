


import logs
import string
TWID = 5
AWID = 32
BWID = 4
DWID = 128

#mngmngt kinds
MSG_RESET = 0
MSG_ENUMERATE = 2
MSG_CONTROL = 4
MSG_REPORT = 6

TagMask = (1<<TWID)-1
BytesMask = (1<<BWID)-1
AddressMask = (1<<AWID)-1

class monitorNocClass:
    def __init__(self,Path,Str,Monitors):
        self.Path = Path
        self.List=[]
        self.Nick={}
        self.more(Str)
        Monitors.append(self)

    def more(self,Str):
        LL  = string.split(Str)
        for Item in LL:
            if '@' in Item:
                ww = string.split(Item,'@')
                self.List.append(ww[0])
                self.Nick[ww[0]]=ww[1]
            else:
                self.List.append(Item)
                self.Nick[Item]=Item




    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def run(self):
        for Sig in self.List:
        
            Val = self.peek(Sig)
            Nick = self.Nick[Sig]
            Kind = Val & 3
            if Val<0:
                logs.log_error('%s is X (%s) '%(Sig,Nick))
            elif Kind in [1,2,3]:
                Str = self.parse(Val)
                logs.log_info('>>>> %s %s %s'%(Sig,Nick,Str))
                if (Sig=='net7'):
                    logs.log_info('>>>> %s 0x%x'%(Sig,Val))
                    

    def parse(self,Msg):
        Kind = Msg & 3
        Msg = Msg >> 2
        Tags = Msg & TagMask
        Msg = Msg >> TWID
        Bytes = Msg & BytesMask
        Msg = Msg >> BWID
        Addr = Msg & AddressMask
        Msg = Msg >> AWID
        Data = Msg

        if Kind==1: Kind='read'
        elif Kind==2: Kind='write'
        elif Kind==3: Kind='mngmnt'
        else: Kind='idle'

        if Kind=='mngmnt':
            if Tags==MSG_RESET: Tags='reset'
            elif Tags==MSG_ENUMERATE: Tags='enumerate'
            elif Tags==MSG_CONTROL: Tags='control'
            elif Tags==MSG_REPORT: Tags='report'

        if Kind=='read':
            Return = Data & AddressMask
            DD = Data >> AWID
            Rbytes = DD & 0xffff
            Str = '%s %s bytes=%d addr=0x%x return=0x%x bytes=%d'%(Kind,Tags,Bytes,Addr,Return,Rbytes)
            return Str

        Str = '%s %s bytes=%d addr=0x%x data=0x%x'%(Kind,Tags,Bytes,Addr,Data)
        return Str

