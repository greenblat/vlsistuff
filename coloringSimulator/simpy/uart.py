


import sys
import logs3 as logs

def uart(Obj):
    if 'cycles' not in Obj.Context: 
        Obj.Context['cycles'] = 0
        Obj.Context['state'] = 'idle'

    Clk = Obj.vals('clk')
    if Clk[0]=='1': return [],[]

    Obj.Context['cycles'] += 1
    db = Obj.db
    if Obj.Context['cycles']==30:
        db.setNet('write_tx',0,'1')
        db.setNet('txdata',0,'11001100')
    if Obj.Context['cycles']==31:
        db.setNet('write_tx',0,'0')
    if Obj.Context['cycles']==800:
        db.setNet('write_tx',0,'1')
        db.setNet('txdata',0,'10101010')
    if Obj.Context['cycles']==801:
        db.setNet('write_tx',0,'0')

    txd = db.Nets['txd'].Value
    db.setNet('rxd',0,txd)

    rx_valid = db.Nets['rx_valid'].Value
    db.setNet('read_rx',0,rx_valid)
    if rx_valid=='1':
        rxdata = db.Nets['rxdata'].Value
        logs.log_info('rxdata=%s clk=%s'%(rxdata,Clk[1]['clk']))
        
    return [],[]

    

#  inst ram ram0 clk<clk a<addr[7:0] d<din[31:0] cs<ramcs we<wr q>dout[31:0] | depth=330 ;
def ramdrv(Obj):
    if 'cycles' not in Obj.Context: 
        Obj.Context['cycles'] = 0
        Obj.Context['waddr'] = 3
        Obj.Context['raddr'] = 3
        Obj.Context['data'] = 8
    if Obj.Vals['clk']=='0':
        Obj.Context['cycles'] += 1
        if Obj.Context['cycles']==100:
            sys.exit()
        Obj.Context['cycles'] += 1
        db = Obj.db
        db.setNet('ramcs',0,'1')
        if  Obj.Context['cycles']<50:
            db.setNet('addr',0,bin(Obj.Context['waddr'])[2:])
            db.setNet('din',0,bin(Obj.Context['data'])[2:])
            db.setNet('wr',0,'1')
            Obj.Context['data'] += 7
            Obj.Context['waddr'] +=1
        else:
            db.setNet('wr',0,'0')
            db.setNet('addr',0,bin(Obj.Context['raddr'])[2:])
            print('rd',Obj.Context['raddr'],Obj.Context['cycles'] )
            Obj.Context['raddr'] +=1
    return [],[]     
