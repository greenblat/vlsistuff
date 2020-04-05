
import sys

def uart(Obj):
    print('uart')
    return [],[]

def funcx(Obj):
    print('XXXXX funcx doing',Obj.Inst)
    return [],[]


def funcy(Obj):
    print('funcy doing',Obj.Inst)
    db = Obj.db
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
