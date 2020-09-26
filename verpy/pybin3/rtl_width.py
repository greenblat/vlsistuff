
import types,string
from scan_rtl import  compute1
import logs
import traceback

def get_width(Net,Mod):
    if not Net:
        return 0
    X,Y=get_width2(Net,Mod)
    if X==0: X=32
    return X

def get_width2(Net,Mod):
    if type(Net) is int:
        return 32,needed_bits(Net)
    if type(Net) is str:
        if Net[0] in '0123456789': return get_width2(eval(Net),Mod)
        if Net in Mod.parameters:
            XX =  get_width2(Mod.parameters[Net],Mod)
            return XX
        if Net in Mod.localparams:
            XX =  get_width2(Mod.localparams[Net],Mod)
            return XX
        if Net in Mod.nets:
            (Dir,Wid)=Mod.nets[Net]
            if not Wid:
                return 1,1
            if Wid[0] in ('packed','double'):
                H1 = compute1(Wid[1][0],Mod)
                L1 = compute1(Wid[1][1],Mod)
                
                H2 = compute1(Wid[2][0],Mod)
                L2 = compute1(Wid[2][1],Mod)




                WW = (abs(H1-L1)+1)*(abs(H2-L2)+1)
                return WW,WW

            H = compute1(Wid[0],Mod)
            L = compute1(Wid[1],Mod)
            return abs(H-L)+1,abs(H-L)+1
    if isinstance(Net,(list,tuple)):
        if Net[0] == '*':
            Smax=0
            Smin=0
            for X in Net[1:]:
                Ymax,Ymin = get_width2(X,Mod)
                Smax += Ymax
                Smin += Ymin
            return Smax,Smin
        if Net[0] == '/':
            Smax,Smin = get_width2(Net[1],Mod)
            for X in Net[2:]:
                Ymax,Ymin = get_width2(X,Mod)
                Smax -= Ymax
                Smin -= Ymin
            return Smax,Smin

        if Net[0] in  ['>>','<<']:
            Ymax,Ymin = get_width2(Net[1],Mod)
            return  Ymax,Ymin

        if Net[0] in  ['+','-']:
            Max=1
            Min=32
            for X in Net[1:]:
                Ymax,Ymin = get_width2(X,Mod)
                Max = max(Ymax,Max)
                Min = min(Ymin,Min)
            return Max+1,Min
        if Net[0] in  ['!=','||','&&','!','>','==','>=','<=']:
            return 1,1
        if Net[0] in  ['~']:
            return get_width2(Net[1],Mod)
        if Net[0] in  ['|','&','^']:
            if len(Net)==2:
                return 1,1
            Max=1
            Min=9999
            for X in Net[1:]:
                Ymax,Ymin = get_width2(X,Mod)
                Max = max(Ymax,Max)
                Min = min(Ymin,Min)
            return Max,Min

        if Net[0] in ['hex','dig','bin']:
            if Net[1]=='':
                return 32,1
            else:
                X= compute1(Net[1],Mod)
            check_literal_goodness(Net,Mod)
            if X>0: return X,X
            if Net[0]=='bin':
                return 32,len(Net[2])
            if Net[0]=='dig':
                return 32,needed_bits(Net[2])
            if Net[0]=='hex':
                return 32,len(Net[2])*4
        if Net[0] == 'question':
            W0,W1 = get_width2(Net[2],Mod)
            W2,W3 = get_width2(Net[3],Mod)
            return max(W0,W2),min(W1,W3)
        if Net[0] == 'subbit':

            if (Mod.mems.keys()!=[])and(Net[1] in Mod.mems):
                Dir,Wid1,Wid2=Mod.mems[Net[1]]
                H = compute1(Wid1[0],Mod)
                L = compute1(Wid1[1],Mod)
                return H-L+1,H-L+1

            return 1,1
        if Net[0] == 'subbus':
            if len(Net)==3:
                H = compute1(Net[2][0],Mod)
                L = compute1(Net[2][1],Mod)
            else:
                H = compute1(Net[2],Mod)
                L = compute1(Net[3],Mod)
            return H-L+1,H-L+1
        if Net[0] == 'curly':
            sum0 = 0
            sum1 = 0
            if Net[1]=='repeat':
                Many = compute1(Net[2],Mod)
                Ymx,Ymn = get_width2(Net[3],Mod)
                return Ymx*Many,Ymn*Many

            for X in Net[1:]:
                Ymx,Ymn = get_width2(X,Mod)
                sum0 += Ymx
                sum1 += Ymn
            return sum0,sum1
        if Net[0] == 'repeat':
            W0,W1 = get_width2(Net[2],Mod)
            Many = compute1(Net[1],Mod)
            return W0*Many,W1*Many
        if Net[0] in ['<','>','<=','=<','>=','=>']:
            return 1,1
        if Net[0]=='functioncall':
           return 1,1



    logs.log_err('rtl_width get_width got %s, cannot determine the width'%str(Net))
    print(traceback.print_stack())
    return 1,1
        
def needed_bits(Int):
    if type(Int) is int:
        Str = bin(Int)[2:]
        return len(Str)
    else:
        try:
            II = int(Int)
            return needed_bits(II)
        except:
            logs.log_err('needed bits failed in on "%s"'%Int)
            return 0
        

def check_literal_goodness(Net,Mod):
    Wid1= compute1(Net[1],Mod)
    if Wid1==0: Wid1=32
    if Net[0]=='bin':
        Base=2
        Pr = "'b"
    elif Net[0]=='hex':
        Base=16
        Pr = "'h"
    elif Net[0]=='dig':
        Base=10
        Pr = "'d"
    else:
        logs.log_err('what ilia? %s'%Net)
        Base=16
        Pr = "'?"
    Net2 = Net[2].replace('_','')
    Net2 = Net2.replace('x','1')
    Net2 = Net2.replace('X','1')
    try:
        Lit = int(Net2,Base)
        Wid2 = needed_bits(Lit)
    except:
        logs.log_err('verilog literal  %s%s%s %s has strange chars in it'%(Net[1],Pr,Net[2],Net[1]))
        Wid2 = 32

    if Wid2>Wid1:
        logs.log_err('verilog literal  %s %s%s%s is too wide for width %s'%(Net,Net[1],Pr,Net[2],Net[1]))
    
