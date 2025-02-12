#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Lines = File.readlines()
    Base = Fname.replace('.regfile','')
    ww = Base.split('/')
    Base = ww[-1]

    Frdl = open('%s.rdl' % Base,'w')
    Frdl.write('addrmap %s {\n addrspace = 0;\n' % Base)


    for line in Lines:
        wrds = line.split()
        if wrds==[]:
            pass
        elif wrds[0] == 'chip':
            pass
        elif wrds[0] == 'end':
            pass
        elif wrds[0] == 'ram':
            Name = wrds[1]
            Params = parseX(wrds)
            Wid = Params['wid']
            Depth = Params['depth']
            Str = RAM.replace('NAME',Name)
            Str = Str.replace('DEPTH',str(Depth))
            Str = Str.replace('WID',str(Wid))
            Frdl.write(Str)
        elif wrds[0] == 'reg':
            Name = wrds[1]
            Params = parseX(wrds)
            if Params['wid'] > 32:
                Wid = Params['wid']
                Ind = 0
                while Wid>32:
                    Params['wid'] = 32
                    makeReg(Name+'_'+str(Ind),Params,Frdl)
                    Ind += 1
                    Wid -= 32;
                if (Wid>0):
                    Params['wid'] = Wid
                    makeReg(Name+'_'+str(Ind),Params,Frdl)
            else:
                makeReg(Name,Params,Frdl)
        else:
            print('error %s' % wrds[0])
    for Reg in Regs:
        Modif = ''
        if Reg in Modifs: Modif = Modifs[Reg]
        Frdl.write('%s %s %s;\n' % (Modif,Reg,Reg))
    Frdl.write('};\n')
    Frdl.close()


Regs = []
Modifs = {}

def makeReg(Name,Params,Frdl):
    Access = Params['access']
    Wid = Params['wid']
    if 'desc' not in Params: Params['desc'] = '???'
    Desc = Params['desc']
    Desc = Desc.replace('.',' ')
    Desc = Desc.replace('"','')
    if 'reset' in Params:
        Rst = Params['reset']
    else:
        Rst = 0
    if Access == 'ro':
        Str = RO.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        Regs.append(Name)
    elif Access == 'rw':
        Str = RW.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        Regs.append(Name)
    elif Access == 'w1c':
        Str = W1C.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        for II in range(Wid):
            Frdl.write('  field { sw=rw; hw=w; intr; woclr; } bit%d = 1\'b0;\n' % (II))
        Frdl.write('};\n')

        Regs.append(Name)
    elif Access == 'external':
        Str = EXTERNAL.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        Regs.append(Name)
        Modifs[Name] = 'external'
    elif Access == 'rw_pulse':
        Str = RW_PULSE.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        Regs.append(Name)
    elif Access == 'ro_pulse':
        Str = RO_PULSE.replace('REG',Name)
        Str = Str.replace('DESC',Desc)
        Str = Str.replace('WID',str(Wid))
        Str = Str.replace('HI',str(Wid-1))
        Str = Str.replace('RST',str(Rst))
        Frdl.write('%s' % Str)
        Regs.append(Name)
    else:
        print("ERROR! access=%s reg=%s" % (Access,Name))

EXTERNAL = '''
   reg REG {
      regwidth = 32;
      desc = "DESC";
      field { sw=rw; hw=rw; ikwid; } value[HI:0] = WID'hRST;
   };
'''
RO = '''
   reg REG {
      regwidth = 32;
      desc = "DESC";
      field { sw=r; hw=w; } value[HI:0] = WID'hRST;
   };
'''
RW = '''
   reg REG {
      regwidth = 32;
      desc = "DESC";
      field { sw=rw; hw=r; } value[HI:0] = WID'hRST;
   };
'''
W1C = '''
reg REG {
      regwidth = 32;
      desc = "DESC";

'''

W1Cbit = '''
field { sw=rw; hw=r; woclr; } value[HI:HI] = WID'h0;
'''

RW_PULSE = '''
reg REG {
      regwidth = 32;
      desc = "DESC";
      field { sw=rw; hw=r; swmod; } value[HI:0] = WID'h0;
};
'''

RO_PULSE = '''
reg REG {
      regwidth = 32;
      desc = "DESC";
      field { sw=rw; hw=w; swrd; } value[HI:0] = WID'h0;
};
'''




RAM = '''
reg ram {
   field {sw=rw; hw=rw; we;} value[WID] = WID'b0;
};
external ram NAME[DEPTH];
'''

def parseX(wrds):
    res = {}
    for wrd in wrds:
        if '=' in wrd:
            ww = wrd.split('=')
            prm = ww[0]
            val = evalx(ww[1])
            res[prm] = val
    return res

def evalx(Wrd):
    try:
        return eval(Wrd)
    except:
        return Wrd



if __name__ == '__main__': main()
