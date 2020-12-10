

import veri


ind = 0
def run_spice(Str):
    global ind
    ind += 1
    wrds = Str.split()
    Func = wrds[1]
    Path = wrds[0]
    eval('%s("%s","%s")'%(Func,Path,Str))
    return

#    WW = Str.split('|')
#    INS = WW[1].split()
##    print('>>PYTHON>>>>str=%s>>>>ins="%s">>>>'%(Str,str(INS)))
#    if (INS[0]=='1'):
#        veri.force('out[0]',str((ind>>2)&1))
#        veri.force('out[1]',str((ind>>1)&1))
#        veri.force('out[2]',str(ind&1))

Was = 'x'
Count = 0
def cntrl(Path,Str):
    global Was,Count
    print('CONTROL',Path,Str,ind)
    X = Str.split('|')
    X = X[1]
    X = X.split()

    if X[1]!='1': 
#        forces('0000')
        return

    print('>>BEF>>>',Count,Was,X)
    if (X[0]=='1')and(Was != '1'):
        print('>INCR>>>>',Count,Was,X)
        Y = ('000'+bin(Count)[2:])[-4:]
        if Count>3:
            forces(Y)
        Count += 1
    print('>>>>>',Count,Was,X)
    Was = X[0]


def forces(FF):
    veri.force('0',FF[3])
    veri.force('1',FF[2])
    veri.force('2',FF[1])
    veri.force('3',FF[0])

def bbb(Path,Str):
    print('BBB',Path,Str)
