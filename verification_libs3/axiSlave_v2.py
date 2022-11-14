###############################################################################
# AXI Slave Version 2. modified by customer.  
###############################################################################

import string
import logs
import veri
# import pdb
# import pudb
import random
import os
import sys


class axiSlaveClass:

    coefDir = ""
    coefFile = ""

    def __init__(self, Path, Width, Monitors, prefix='', suffix=''):
        self.Path = Path
        self.Width = Width
        if Monitors != -1:
            Monitors.append(self)
        self.arqueue = []
        self.awqueue = []
        self.rqueue = []
        self.bqueue = []
        self.awlen = -1
        self.wid = -1
        self.waitread = 0
        self.bwaiting = 0
        self.bytex = 0x30
        self.prefix = prefix
        self.suffix = suffix
        self.Translates = {}
        self.Ram = {}
        self.bvalid_armed = False
        self.WAITREAD = 4
        self.wrEnabled = False
        self.rdEnabled = False
        logs.log_info('AXI enabled at startup: wr=%s rd=%s' % (self.wrEnabled, self.rdEnabled))
        self.Initial = True
        self.Name = '.'
        self.BVALIDS = 10
        # self.userDir = os.environ.get('USER_DIR')
        # self.coefDir = str(self.userDir) + '/ws/leaf_top/testbench/coefficients/'
        self.coefDir = os.environ.get('PWD') + '/'
        self.coefFile = self.coefDir + 'coefficients.mem'
        self.DBGRES = ''

        self.AWQSIZE = 1               # When reached Q size - AWREADY will go to "0" until the current access is finished.
        self.ARQSIZE = 1               # When reached Q size - ARREADY will go to "0" until the current access is finished.
        self.WREADY_WAIT_COND = True   # Activate WREADY toggling
        self.WREADY_UP_MIN = 3         # Minimum value for WREADY == 1
        self.WREADY_UP_MAX = 6         # Minimum value for WREADY == 1 
        self.WREADY_DN_MIN = 1         # Minimum value for WREADY == 0
        self.WREADY_DN_MAX = 3         # Minimum value for WREADY == 0
        self.wvalid_prev = 0           # wvalid previous value
        self.wready_up_cnt = 0         # Initial value of wready up counter
        self.wready_dn_cnt = 0         # Initial value of wready dn counter
        self.WREADY_WAIT_UP = random.randint(self.WREADY_UP_MIN,self.WREADY_UP_MAX) # randomize number of WREADY == 1 before going to "0"
        self.WREADY_WAIT_DN = random.randint(self.WREADY_DN_MIN,self.WREADY_DN_MAX) # randomize number of WREADY == 0 before going to "1"


    def busy(self):
        #        logs.log_info('AXI BUSY %s %s   %s %s %s %s'%(self.waitread,self.bwaiting,len(self.arqueue),len(self.awqueue),len(self.rqueue),len(self.bqueue)))
        if self.waitread > 0: return True
        if self.bwaiting > 0: return True
        if self.arqueue != []: return True
        if self.awqueue != []: return True
        if self.rqueue != []: return True
        if self.bqueue != []: return True
        return False

    def exists(self, Sig):
        if self.prefix != '': Sig = '%s%s' % (self.prefix, Sig)
        if self.suffix != '': Sig = '%s%s' % (Sig, self.suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        logs.log_debug('AXI DEBUG path=%s sig=%s exists=%s' % (self.Path, Sig, veri.exists('%s%s' % (self.Path, Sig))))
        return veri.exists('%s%s' % (self.Path, Sig))

    def peek(self, Sig):
        if self.prefix != '': Sig = '%s%s' % (self.prefix, Sig)
        if self.suffix != '': Sig = '%s%s' % (Sig, self.suffix)
        if Sig in self.Translates: Sig = self.Translates[Sig]
        return logs.peek('%s%s' % (self.Path, Sig))

    def force(self, Sig, Val):
        if self.prefix != '': Sig = '%s%s' % (self.prefix, Sig)
        if self.suffix != '': Sig = '%s%s' % (Sig, self.suffix)
        #        logs.log_info('DDDD %s >>%s>>%s>>%s'%(self.Name,Sig,Sig in self.Translates,list(self.Translates.keys())))
        if Sig in self.Translates: Sig = self.Translates[Sig]
        #        logs.log_info('AXI FORCE %s  %s'%(Sig,Val))
        veri.force('%s%s' % (self.Path, Sig), str(Val))

    def action(self, Text):
        Wrds = Text.split()
        if Wrds == []:
            pass
        if Wrds[0] == 'Enable':
            if Wrds[1] in ['0', 0]:
                self.rdEnabled = False
                self.wrEnabled = False
            elif Wrds[1] in ['1', 1]:
                self.rdEnabled = self.areWeConnected('arvalid')
                self.wrEnabled = self.areWeConnected('awvalid')
            logs.log_info('AXI enabled in sequence: wr=%s rd=%s  (%s)' % (self.wrEnabled, self.rdEnabled, Wrds))
        elif Wrds[0] == 'rdEnable':
            if Wrds[1] in ['0', 0]:
                self.rdEnabled = False
            elif not self.areWeConnected('arvalid'):
                self.rdEnabled = False
            elif Wrds[1] in ['1', 1]:
                self.rdEnabled = True
                self.force('arready', 1)
                self.force('rdata', 0)
                self.force('rlast', 0)
                self.force('rvalid', 0)
                self.force('rresp', 0)
        elif Wrds[0] == 'wrEnable':
            if Wrds[1] in ['0', 0]:
                self.wrEnabled = False
            elif not self.areWeConnected('awvalid'):
                self.wrEnabled = False
            else:
                self.wrEnabled = True
                self.force('awready', 1)
                self.force('bid', 0)
                self.force('bvalid', 0)
                self.force('bresp', 0)
                self.force('wready', 1)
        elif Wrds[0] == 'ramfile':
            coefFile = str(Wrds[1])
            logs.log_debug('Trying to open coefficients file: %s ' % coefFile)
            try:
                File = open(coefFile)
            except:
                logs.log_fatal('Failed to open coefficients file: %s ' % coefFile)
            lines = File.readlines()
            File.close()
            Addr = 0
            i    = 0
            for line in lines:
                wrds = line.split()
                for wrd in wrds:
                    if wrd[0] == '@':
                        Addr = int(wrd[1:], 16)
                        logs.log_info("Axi Ram: Load File : %s to DDR addr %08x" % (coefFile,Addr))

                    else:
                        if(i < 8):
                            logs.log_info("Axi Ram(%d): Write Addr %08x %016x" % (self.Width,Addr,int(wrd,16)))
                        i+=1
                        Addr = self.addWord(Addr, wrd)
            logs.log_info('Axi Ram: last address written %s ' % hex(Addr))

        elif Wrds[0] == 'wready_up':
            self.WREADY_UP_MIN = eval(Wrds[1])
            self.WREADY_UP_MAX = eval(Wrds[2])
            logs.log_info('ACTION: WREADY_UP_MIN = %d ; WREADY_UP_MAX = %d ' % (self.WREADY_UP_MIN,self.WREADY_UP_MAX))
        elif Wrds[0] == 'wready_dn':
            self.WREADY_DN_MIN = eval(Wrds[1])
            self.WREADY_DN_MAX = eval(Wrds[2])
            logs.log_info('ACTION: WREADY_DN_MIN = %d ; WREADY_DN_MAX = %d ' % (self.WREADY_DN_MIN,self.WREADY_DN_MAX))
        elif Wrds[0] == 'read_wait':
            self.WAITREAD = eval(Wrds[1])
        else:
            logs.log_error('command %s is not recognized by axiSlave.py class' % str(Wrds))

    def addWord(self, Addr, Word):
        Data = int(Word, 16)

        if (self.Width == 32):
            self.Ram[Addr] = Data & 0xff
            self.Ram[Addr + 1] = (Data >> 8) & 0xff
            self.Ram[Addr + 2] = (Data >> 16) & 0xff
            self.Ram[Addr + 3] = (Data >> 24) & 0xff
            Addr += 4
            return Addr

        elif (self.Width == 64):
            self.Ram[Addr] = Data & 0xff 
            self.Ram[Addr + 1] = (Data >> 8) & 0xff
            self.Ram[Addr + 2] = (Data >> 16) & 0xff
            self.Ram[Addr + 3] = (Data >> 24) & 0xff
            self.Ram[Addr + 4] = (Data >> 32) & 0xff
            self.Ram[Addr + 5] = (Data >> 40) & 0xff
            self.Ram[Addr + 6] = (Data >> 48) & 0xff
            self.Ram[Addr + 7] = (Data >> 56) & 0xff

            Addr += 8
            return Addr

    def areWeConnected(self, Sig):
        Yes = self.exists(Sig)
        return Yes == '1'

    def debug_monitor(self):
        if 0x2914000 not in self.Ram:
            for ii in range(32):
                self.Ram[0x2914000+ii] = ii
        Res = ''
        for ii in range(32):
            Res += ' %x' % (self.Ram[0x2914000+ii])
            
        if Res != self.DBGRES:
            logs.log_info('DBGRES %s' % (Res))
            self.DBGRES = Res


    def run(self):
        #        pudb.set_trace()

        #        veri.force('tracer.trace7',str(self.BVALIDS))
        #        if self.busy():
        #            logs.log_info('AXI BUSY %s %s   %s %s %s %s'%(self.waitread,self.bwaiting,len(self.arqueue),len(self.awqueue),len(self.rqueue),len(self.bqueue)))
        #### if self.Initial:
        ####     self.Initial = False
        ####     self.rdEnabled = self.areWeConnected('arvalid')
        ####     self.wrEnabled = self.areWeConnected('awvalid')
        ####     if self.rdEnabled:
        ####         self.force('arready', 0)
        ####         self.force('rdata', 0)
        ####         self.force('rlast', 0)
        ####         self.force('rvalid', 0)
        ####         self.force('rresp', 0)
        ####         self.force('rid', 0)

        ####     if self.wrEnabled:
        ####         self.force('awready', 0)
        ####         self.force('bid', 0)
        ####         self.force('bvalid', 0)
        ####         self.force('bresp', 0)
        ####         self.force('wready', 0)
        ####     logs.log_info('AXI %s : INITIAL rd=%s wr=%s conn=%s' % (self.Name, self.rdEnabled, self.wrEnabled, self.areWeConnected('awvalid')))

        if self.rdEnabled: self.reading()
        if self.wrEnabled: self.writing()
        if self.rdEnabled: self.sendrqueue()

    def sendrqueue(self):
        if not self.rdEnabled: return
        if self.waitread > 0:
            self.waitread -= 1
            self.idleread()
            return
        if self.rqueue == []:
            self.idleread()
            return
        if self.peek('rready') == 0:
            return
        if self.rqueue[0] == 'pop':
            self.rqueue.pop(0)
            self.arqueue.pop(0)
            self.idleread()
            return
        (rlast, rid, rdata) = self.rqueue.pop(0)
        if rlast == 'wait':
            self.waitread = rid
            logs.log_debug('axiSlave %s waitread %s' % (self.Name, rid))
            self.idleread()
            return

        self.force('rvalid', 1)
        self.force('rlast', rlast)
        self.force('rid', rid)
        self.force('rresp', 0)
        self.force('rdata', '0x' + rdata)

    def idleread(self):
        self.force('rvalid', 0)
        self.force('rlast', 0)
        self.force('rdata', 0)

    def reading(self):
        if len(self.arqueue) > self.ARQSIZE:
            self.force('arready', 0)
        else:
            self.force('arready', 1)
        if self.peek('arvalid') == 1 and self.peek('arready'):
            arid = self.peek('arid')
            arburst = self.peek('arburst')
            araddr = self.peek('araddr')
            arlen = self.peek('arlen')
            arburst = self.peek('arburst')
            arsize = self.peek('arsize')
            self.arqueue.append((arburst, araddr, arlen, arburst, arsize))
            self.rqueue.append(('wait', self.WAITREAD, 0))
            for ii in range(arlen):
                self.readQueue(ii, arburst, arsize, araddr, arid, 0)
            self.readQueue(arlen, arburst, arsize, araddr, arid, 1)
            self.rqueue.append('pop')

    def readQueue(self, ii, burst, arsize, addr, rid, rlast):
        Incr = 1 << arsize
        Mask = ~((1 << arsize) - 1)
        if burst == 0:
            Addr = addr
        else:
            Addr = ii * Incr + addr
        Addr1 = Addr & Mask
        if Addr1 != Addr:
            logs.log_warning('axiSlave %s read address is not aligned size=%d addrin=%08x' % (self.Name, arsize, Addr))
        rdata = ''
        takenram = 0
        for ii in range(Incr):
            Add = Addr1 + ii
            if Add in self.Ram:
                AA = '%02x' % (self.Ram[Add])
                takenram += 1
            else:
                AA = '%02x' % (self.bytex)
                self.bytex = (self.bytex + 1) & 0xff
            rdata = AA + rdata
        self.rqueue.append((rlast, rid, rdata))
        logs.log_debug('axiSlave %s taken from ram %d bytes  rdata=%s addr=%08x incr=%d addr1=%x size=%d' % (self.Name, takenram, rdata, Addr,Incr,Addr1,arsize))

    def writing(self):
        if self.Initial == True:
            self.Initial = False
            self.force('wready', 1)
        
        if self.bwaiting > 0:
            self.bwaiting -= 1
            if self.bwaiting == 1:
                self.force('bvalid', 1)
                self.BVALIDS -= 1
            else:
                self.force('bvalid', 0)
        elif self.bqueue != []:
            bid, bresp = self.bqueue.pop(0)
            if bid == 'wait':
                self.bwaiting = int(bresp)
                self.force('bvalid', 0)
                self.force('bid', 0)
                self.force('bresp', 0)
            else:
                self.force('bid', bid)
                self.force('bresp', int(bresp))
        else:
            self.force('bvalid', 0)

        if len(self.awqueue) > self.AWQSIZE:
            self.force('awready', 0)
        else:
            self.force('awready', 1)
        if self.peek('awvalid') == 1 and self.peek('awready') == 1:
            self.force('awready', 1)
            self.BVALIDS += 1
            awburst = self.peek('awburst')
            awid = self.peek('awid')
            awaddr = self.peek('awaddr')
            awlen = self.peek('awlen')
            awburst = self.peek('awburst')
            awsize = self.peek('awsize')
            self.awqueue.append((awburst, awaddr, awlen, awid, awsize))
            logs.log_debug('AXI %s >>>awvalid %x %x %x %x %x' % (self.Name, awburst, awaddr, awlen, awid, awsize))

        wvalid_cur = self.peek('wvalid')
        if self.wvalid_prev and wvalid_cur == 0:
            self.wready_up_cnt = 0
        self.wvalid_prev = wvalid_cur

        if wvalid_cur == 1 and self.WREADY_WAIT_COND:
            if self.wready_up_cnt < self.WREADY_WAIT_UP:
                self.wready_up_cnt += 1
                self.force('wready', 1)
                #logs.log_info('LIORB inside "1" ; axiSlave %s ; wready up counter =%d ' % (self.Name, self.wready_up_cnt))
            else:
                #logs.log_info('LIORB axiSlave %s ; was needed to wait up %d, wready up counter =%d ' % (self.Name, self.WREADY_WAIT_UP, self.wready_up_cnt))
                if self.wready_dn_cnt < self.WREADY_WAIT_DN:
                    self.force('wready', 0)
                    self.wready_dn_cnt += 1
                else:
                    #logs.log_info('LIORB axiSlave %s ; was needed to wait dn %d, wready dn counter =%d ' % (self.Name, self.WREADY_WAIT_DN, self.wready_dn_cnt))
                    self.wready_dn_cnt = 0
                    self.wready_up_cnt = 1
                    self.WREADY_WAIT_UP = random.randint(self.WREADY_UP_MIN,self.WREADY_UP_MAX)
                    self.WREADY_WAIT_DN = random.randint(self.WREADY_DN_MIN,self.WREADY_DN_MAX)
                    self.force('wready', 1)


        if wvalid_cur == 1 and self.peek('wready') == 1:
            logs.log_debug('AXI %s <<<<< wready=%d awlen=%d ' % (self.Name, self.wready_up_cnt, self.awlen))
            if self.awlen < 0:
                if len(self.awqueue) == 0:
                    logs.log_error('axiSlave awqueue empty and wvalid is on')
                else:
                    self.awburst, self.awaddr, self.awlen, self.wid, self.awsize = self.awqueue.pop(0)
            wstrb = self.peek('wstrb')
            wlast = self.peek('wlast')
            wdata = self.peek('wdata')
            logs.log_debug('axiSlave %s write wstrb=%x wid=%x wlast=%d wlen=%d awaddr=%x burst=%d wdata=%x' % (self.Name, wstrb, self.wid, wlast, self.awlen, self.awaddr, self.awburst, wdata))

            #logs.log_info('axiSlave %s write to ram addr=%x wdata=%x wstrb=%x ' % (self.Name, self.awaddr, wdata, wstrb))
            for ii in range(16):
                if ((wstrb >> ii) & 1) == 1:
                    Byte = (wdata >> (ii * 8)) & 0xff
                    self.Ram[self.awaddr + ii] = Byte
            self.awaddr += 1 << self.awsize
            if self.awlen == 0:
                self.awlen = -1
                if wlast != 1:
                    logs.log_error('axislave %s %s: %s   no last' % (self.Name, self.Path, self.prefix))
            else:
                self.awlen -= 1

            if (wlast == 1):  # and(not self.bvalid_armed):
                self.bqueue.append(('wait', random.randint(3, 3)))
                self.bqueue.append((self.wid, 0))
                self.bvalid_armed = True
        if (self.bvalid_armed):
            wlast = self.peek('wlast')
            if (wlast == 0):
                self.bvalid_armed = False

    ###########################################################################

    def setCoefDir(self, userCoefDir):

        if (os.path.exists(userCoefDir)):
            self.coefDir = userCoefDir
            logs.log_info('Coefficients directory set to: %s            ' % self.coefDir)
        else:
            logs.log_error('Coefficients directory does not exist: %s    ' % userCoefDir)
            logs.log_info('Using default path: %s                       ' % self.coefDir)

        return

    ###########################################################################


