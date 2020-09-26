

import logs
logs.TB = ''

class driverClass(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)

    def action(self,Txt):
        wrds = Txt.split()
        if wrds[0] == 'wr':
            Reg = wrds[1]
            Flt = float(wrds[2])
            Int = logs.float2binary(Flt)
            Str = 'tx w%s%08x'%(Reg,Int)
            uart = logs.getVar('uart')
            uart.action(Str)
        elif wrds[0] == 'add':
            Src0 = wrds[1]
            Src1 = wrds[2]
            Dst  = wrds[3]
            Str = 'tx oadd%s%s%s'%(Src0,Src1,Dst)
            uart = logs.getVar('uart')
            uart.action(Str)
        elif wrds[0] == 'mul':
            Src0 = wrds[1]
            Src1 = wrds[2]
            Dst  = wrds[3]
            Str = 'tx omul%s%s%s'%(Src0,Src1,Dst)
            uart = logs.getVar('uart')
            uart.action(Str)

        
    def run(self):
        return
        
dr = driverClass('',logs.getVar('Monitors'))

logs.setVar('dr',dr)



