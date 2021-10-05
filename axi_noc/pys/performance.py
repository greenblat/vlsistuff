import logs
import veri


class performanceClass(logs.driverClass):
    def __init__(self,Path,Monitors,numSlaves):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Enable = True
        self.Name = 'Perf'
        self.Prefix = ''
        self.Suffix = ''
        self.SLAVES = []
        self.PerfAw = {}
        self.PerfW = {}
        self.PerfAr = {}
        self.PerfR = {}
        self.Firsts = {}
        self.Lasts = {}
        for ii in range(numSlaves):
            Slv = 'slv%d_' % ii
            self.SLAVES.append(Slv)
            self.PerfAw[Slv] = 0
            self.PerfW[Slv] = 0
            self.PerfAr[Slv] = 0
            self.PerfR[Slv] = 0
            self.Firsts[Slv] = 0
            self.Lasts[Slv] = 0

    def run(self):
        if not self.Enable: return
        self.accumulate_wr()
        self.accumulate_rd()


    def accumulate_wr(self):
        logs.setVar('wr_action',0)
        for Slv in self.SLAVES:
            if self.valid(Slv+'awvalid') and self.valid(Slv+'awready'):
                self.PerfAw[Slv] += 1
                if self.Firsts[Slv] == 0: 
                    self.Firsts[Slv] = logs.get_cycles()
                self.Lasts[Slv] = logs.get_cycles()

            if self.valid(Slv+'wvalid') and self.valid(Slv+'wready'):
                self.Lasts[Slv] = logs.get_cycles()
                self.PerfW[Slv] += 1
                logs.setVar('wr_action',1)

                    


    def accumulate_rd(self):
        for Slv in self.SLAVES:
            if self.valid(Slv+'arvalid') and self.valid(Slv+'arready'):
                self.PerfAr[Slv] += 1
                if self.Firsts[Slv] == 0: 
                    self.Firsts[Slv] = logs.get_cycles()
                self.Lasts[Slv] = logs.get_cycles()

            if self.valid(Slv+'rvalid') and self.valid(Slv+'rready'):
                self.Lasts[Slv] = logs.get_cycles()
                self.PerfR[Slv] += 1


    def action(self,Txt):
        if 'enable' in Txt: 
            self.Enable = True
            return
        if 'disable' in Txt: 
            self.Enable = False
            return
    def onFinish(self):
        for Slv in self.SLAVES:
            Duration = self.Lasts[Slv] - self.Firsts[Slv]
            Ws = self.PerfW[Slv]
            Aws = self.PerfAw[Slv]
            Rs = self.PerfR[Slv]
            Ars = self.PerfAr[Slv]
            logs.log_info('SLV %s:    dur=%d aws=%d ws=%d  ars=%d rs=%d' % (Slv,Duration,Aws,Ws,Ars,Rs))



    def busy(self):
        return False

