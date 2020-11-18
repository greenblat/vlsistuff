

import logs

class monitorX:
    def __init__(self,Name):
        self.DONES = [0,0,0,0,0]
        self.COUNT = [0,0,0,0,0]
        self.SEQUENCE = [[],[],[],[],[]]
        self.Name = Name
        self.IDLES = 0
        self.Fout = open('%s.log'%Name,'w')
        self.Active = ['idle','idle','idle','idle','idle']
        self.Sequence = [0,0,0,0,0,0]
        self.PacketType = [0,0,0,0,0,0]
        self.ModuleId = [0,0,0,0,0,0]
        self.Segment = [0,0,0,0,0,0]

    def run(self,II,kchar,tdata,tlast,tready):
        self.Fout.write('%d %02x %016x %d %d   %s %d\n'%(II,kchar,tdata,tlast,tready,self.Active[II],self.COUNT[II]))
        if ((kchar & 0xf)==0xf)and((tdata & 0xffffffff)==0x5cfd5c1c)and(self.Active[II]=='idle'):
            self.Active[II] = 'packet'
            self.PacketType[II] = (tdata>>56)&0x7
            self.ModuleId[II]   = (tdata>>40)&0x1f
            self.Segment[II]   = (tdata>>32)&0x13
#            logs.log_info('START%s lane=%s dones=%s  count=%s (type=%d module=%d segment=%d)  ks=%02x td=%016x'%(self.Name,II,self.DONES[II],self.COUNT[II],self.PacketType[II],self.ModuleId[II],self.Segment[II],kchar,tdata))
            self.COUNT[II] = 1
        elif self.Active[II] ==  'packet':
            if ((kchar & 0xf0)==0xf0)and(((tdata>>32) & 0xffffffff)==0x5cfe5cfb):
                self.Active[II] = 'end'
            elif self.COUNT[II]==1:
                self.Sequence[II] = tdata & 0xffffffff
                logs.log_info('START%s: lane=%d dones=%d cnt=%d type=%d mod=%d seg=%d seq=%d'%(self.Name,II,self.DONES[II],self.COUNT[II],self.PacketType[II],self.ModuleId[II],self.Segment[II],self.Sequence[II]))
            self.COUNT[II] += 1
        elif self.Active[II] ==  'end':
                Key = 'type=%d mod=%d seg=%d seq=%d'%(self.PacketType[II],self.ModuleId[II],self.Segment[II],self.Sequence[II])
                self.SEQUENCE[II].append(Key)
                if (self.PacketType[II]==3)and(self.COUNT[II]!=687): logs.log_error('%s lane=%s packet 3 is not length 687 it is %d'%(self.Name,II,self.COUNT[II]))
                elif (self.PacketType[II]==1)and(self.COUNT[II]!=239): logs.log_error('%s lane=%s packet 1 is not length 239 it is %d'%(self.Name,II,self.COUNT[II]))
                logs.log_info('LASTS%s: lane=%d dones=%d cnt=%d type=%d mod=%d seg=%d seq=%d'%(self.Name,II,self.DONES[II],self.COUNT[II],self.PacketType[II],self.ModuleId[II],self.Segment[II],self.Sequence[II]))
                self.DONES[II] += 1
                self.COUNT[II] = 0
                self.IDLES = 0
                self.Active[II] = 'idle'
        elif ((kchar & 0xf0)==0xf0)and(((tdata>>32) & 0xffffffff)==0x5cfe5cfb):
            logs.log_error('EOF lane=%s %s without being active'%(II,self.Name))
        elif ((kchar & 0xf)==0xf)and((tdata & 0xffffffff)==0x5cfd5c1c):
            logs.log_error('SOF lane=%s %s without being active'%(II,self.Name))

