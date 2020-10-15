

import logs
def parseBin(Bin,Params,Signed=True):
    Num = Params[0]
    Len = len(Bin)
    One = int(Len/Num)
    LL = []
    while Bin != '':
        Head = Bin[:One]
        Bin = Bin[One:]
        if len(Params)==1:
            if Signed:
                Hsig = logs.intxsigned(Head)
                if Hsig==9999:
                    logs.log_error('NNNNNNNN %s %s bin=%s params=%s'%(Head,Hsig,Bin,Params))
            else:
                Hsig = logs.intx(Head)
            LL.append(Hsig)
        else:
            Lhd = parseBin(Head,Params[1:],Signed)
            LL.append(Lhd)

    return LL

def complex_mult(IQ0,IQ1):
    II = IQ0[1] * IQ1[1] - IQ0[0] * IQ1[0]
    QQ = IQ0[1] * IQ1[0] + IQ0[0] * IQ1[1]
    return (II,QQ)
def complex_add(IQ0,IQ1):
    II = IQ0[0] + IQ1[0]
    QQ = IQ0[1] + IQ1[1]
    return (II,QQ)


def vxw(Ant,Weights):
    Sum = [0,0]
    if Weights==0: return Sum 
    for II in range(len(Ant)):
        Sample = Ant[II]
        Weight = Weights[II]
        Res = complex_mult(Sample,Weight)
        Sum = complex_add(Sum,Res)
    return Sum 


