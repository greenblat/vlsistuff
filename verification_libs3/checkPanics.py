# discover INGRESS and EGRESS units and enabled channels.

import logs
import veri
import sys


class checkPanics(logs.driverClass):
    def __init__(self,Path,Monitors):
        logs.driverClass.__init__(self,Path,Monitors)
        self.onFinishDone = False
        self.Activated = False
        self.Panics = []
        self.PanicsHappened={}



    def run(self):
        if self.Activated:
            self.scanPanics()
        elif logs.peek('tb.cycles')>40:
            self.action('start ',[])

    def busy(self):
        return False

    def onFinish(self):
        if self.onFinishDone: return
        self.onFinishDone = True
        for Panic in self.PanicsHappened:
           logs.log_error('PANICED %s' % (Panic,self.PanicsHappened[Panic]))



    def action(self,Txt,Orig=[]):
        wrds = Txt.split()
        if wrds == []: return

        if wrds[0] in ['start','init']:
            self.Activated = True
            File = open('deep.list')
            line = File.readline()
            while line!='':
                wrds = line.split()
                if (len(wrds)>1)and(wrds[0] in ['net:','reg:']):
                    Sig = wrds[1]
                    if '.panic' in Sig:
                        self.Panics.append(Sig)
                        print("PPP",Sig)
                line = File.readline()
            return

        if wrds[0] in ['check']:
            self.scanPanics()
            return

        logs.log_error('checkPanics got %s' % Txt)

    def scanPanics(self):
        for Panic in self.Panics:
            Val = logs.peek(Panic)
            if Val!=0:
                logs.log_error('PANIC %s %s' % (Panic,Val))
                if Panic not in self.PanicsHappened:
                    self.PanicsHappened[Panic] = logs.peek('tb.cycles')



