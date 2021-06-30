
# package to create vcd file

import logs

class vcdoutClass:
    def __init__(self,Fname):
        self.Fname = Fname
        self.Sigs = []
        self.Codes = {}
        self.Wids = {}
        self.Time = 0
        self.started = False

    def action(self,Txt):
        List = Txt.split()
        if List == []:
            return
        elif List[0] == 'sig':
            self.addSigs(List[1:])
        elif List[0] == 'start':
            self.start()
        elif List[0] == 'force':
            self.force(List[1],List[2])
        elif List[0] == 'atime':
            self.atime(List[1])
        elif List[0] == 'rtime':
            self.rtime(List[1])
        elif List[0] == 'close':
            self.close()
            

        
        

    def addSigs(self,Sigs):
        if self.started:
            logs.log_error('cannot add signals to vcd after starting')
            return
        if type(Sigs) is str:
            List = Sigs.split()
        else:
            List = Sigs
        while List != []:
            Sig = List.pop(0)
            if List == []:
                self.Sigs.append((Sig,1))
                self.Wids[Sig] = 1
            elif List[0][0] in '0123456789':
                Wid = eval(List.pop(0))
                self.Sigs.append((Sig,Wid))
                self.Wids[Sig] = Wid
            else:
                self.Sigs.append((Sig,1))
                self.Wids[Sig] = 1
            
    def start(self):
        self.started = True
        self.File = open(self.Fname,'w')
        self.File.write(VCD_HEADER)
        for ind,(Sig,Wid) in enumerate(self.Sigs):
            if Wid == 1:
                WW = ''
            else:
                WW = '[%d:0]' % (Wid-1)
            self.File.write('$var wire  %s %s %s %s $end\n'%(Wid,vcdCode(ind),Sig,WW))
            self.Codes[Sig] = vcdCode(ind)
        self.File.write(VCD_MIDDLE)

    def close(self):
        self.File.close()

    def force(self,Sig,Value):
        Wid = self.Wids[Sig]
        if Wid==1:
            self.File.write('%s%s\n' % (Value,self.Codes[Sig]))
        else:
            if Value == 'x':
                VV = 'x'*Wid
            elif Value == 'z':
                VV = 'z'*Wid
            else:
                VV = bin(eval(Value))[2:]
            self.File.write('b%s %s\n' % (VV,self.Codes[Sig]))
    def atime(self,Value):
        iValue = eval(Value)
        self.File.write('#%s\n' % (iValue))
        self.Time = iValue
    def rtime(self,Value):
        iValue = eval(Value)
        self.Time += iValue
        self.File.write('#%s\n' % (self.Time))

VCD_HEADER = '''
$date
    Thu Jun 24 22:09:48 2021
$end
$version
    Ilia VCD PY creator
$end
$timescale
    1ns
$end
$scope module top $end
'''

VCD_MIDDLE = '''
$upscope $end
$enddefinitions $end
#0
'''
def vcdCode(Ind):
    Res = ''
    xx = Ind % 94
    yy = int(Ind/94)
    Res = chr(xx + ord('!'))
    while yy != 0:
        xx = yy % 94
        yy = int(yy/94)
        Res += chr(xx + ord('!'))
    return Res


TEST = '''
    sig aaa 1 bbb 5 ccc 10 ddd eee fff
    start
    atime 10 
    force aaa 0 
    force ccc 7
    rtime 10 
    force aaa 1 
    force ccc 6
    rtime 15 
    force eee 1 
    force fff 0
    force ddd 0
    rtime 5 
    close
'''

def main():
    vcd = vcdoutClass('test.vcd')
    Tlines = TEST.split('\n')
    for Line in Tlines:
        vcd.action(Line)


if __name__ == '__main__':
    main()


    

