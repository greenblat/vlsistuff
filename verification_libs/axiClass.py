import os,sys,string
import veri
import logs
import my_random
class axiClass:
    def __init__(self,Monitors):
        self.queue=[]
        self.waiting=0
        Monitors.append(self)

    def run(self):
        if len(self.queue)>10:
            veri.force('tb.freak_arready','0')
        else:
            veri.force('tb.freak_arready','1')
       
        freak_arvalid = logs.peek('tb.freak_arvalid')
        if (freak_arvalid==1)and(len(self.queue)<=10):
            freak_araddr = logs.peek('tb.freak_araddr')
            freak_arid = logs.peek('tb.freak_arid')
            self.queue.append((freak_araddr,freak_arid))
            logs.log_info('drive arid=%d %x %d araddr=%x len=%d'%(freak_arid,freak_arid>>6,freak_arid&0x3f,freak_araddr,(len(self.queue)<=10)))
            monitorIds('drive',freak_arid)
        
        if self.waiting: 
            veri.force('tb.freak_rvalid','0')
            self.waiting -= 1
            return

        if len(self.queue)==0: return
        self.waiting=2        
        Pos = my_random.randi(0,len(self.queue)-1)
        Pos = 0
        (addr,id)=self.queue.pop(Pos)
        veri.force('tb.freak_rvalid','1')
        veri.force('tb.freak_rid',str(id))
        veri.force('tb.freak_rdata',str(addr))
        logs.log_info('rvalid id=%x %x %d    rdata=%x'%(id,id>>6,id&0x3f,addr))
        monitorIds('rsp',id)


class monIdClass:
    def __init__(self,Kind):
        self.Kind=Kind
        self.patches={}
        self.whose={}
    def getPatch(self,Id):
        Whose = Id>>6
        Patch = Id & 0x3f
        if Whose not in self.patches:
            self.patches[Whose]=43*[0]
            self.whose[Whose]=0
        self.patches[Whose][Patch] += 1
        if self.patches[Whose][Patch]>4:
            logs.log_error('monIdClass kind=%s whose=%d patch=%d number=%d longer than four'%(self.Kind,Whose,Patch,self.patches[Whose][Patch]))
        elif self.patches[Whose][Patch]==4:
            self.whose[Whose] += 1
            histo = [0,0,0,0,0]
            for ii in range(len(self.patches[Whose])):
                Many =  self.patches[Whose][ii]
                while Many>=len(histo):
                    histo.append(0)
                histo[Many] += 1
            logs.log_info('monIdClass %s %d histo %s'%(self.Kind,Whose,histo))
            if self.whose[Whose]==43:
                logs.log_info('clear whose=%s it has 43 pathces'%Whose)
                self.whose.pop(Whose)
                self.patches.pop(Whose)
                

        if len(self.patches.keys())>2:
            logs.log_error('monIdClass kind=%s whose=%s too many frames'%(self.Kind,self.patches.keys()))



monis={}
def monitorIds(Kind,Id):
    if Kind not in monis:
        monis[Kind]=monIdClass(Kind)
    monis[Kind].getPatch(Id)
    


