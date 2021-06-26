
Psparams={}
def set_pscontext(File,Param,Val):
    if (Param in Psparams)and(Psparams[Param]==Val):
        return
    Psparams[Param]=Val
    if type(Val) is list:
        for x in Val:
            File.write(' %f'%(x))
        File.write(' %s\n'%(Param))
        if (Param=='setrgbcolor'):
            File.write('0 0 0 setrgbcolor\n')


PSOPEN = '''%!PS
gsave
%%Page: "x" 1
gsave
<< /PageSize [XXXX YYYY] >> setpagedevice
1 setlinejoin
1 setlinecap
/Courier findfont 8 scalefont setfont

/SF {/Courier findfont  25 magnif div scalefont setfont } def
/GS { gsave } def
/GR { grestore } def
/C { concat } def
/PICSLW 2.3 def
/max {  2 copy gt  {pop}{exch pop} ifelse } def
/magnif {matrix currentmatrix {abs} forall pop pop max max max } def
/SLW {magnif div  setlinewidth } def
/PSLW { MAGNIF magnif div setlinewidth } def
/M { moveto } def
/R { rotate } def
/L { lineto } def
/S { stroke } def
/SC { scale } def
/F { fill } def
/N { newpath } def
/T { translate } def
/ll_st_align {} def
/rl_st_align {dup stringwidth pop neg 0 rmoveto } def
0.5 SLW
'''
from dbase import get_context

def postscript_opening(File,Schem):
    [(Xl,Yl),(Xh,Yh)] = Schem.bbox()
    DDx = abs(Xh-Xl)
    DDy = abs(Yh-Yl)

    print('high x=%d y=%d low x=%d y=%d'%(Xh,Yh,Xl,Yl))



    xBaseSize = 1200.0
    Scale =xBaseSize/DDx

    sizeX = int(DDx*Scale)
    sizeY = int(DDy*Scale)

    PS0 = PSOPEN.replace('XXXX',str(sizeX))
    PS1 = PS0.replace('YYYY',str(sizeY))
    File.write(PS1)
        
    
    NewA = 0.98*Scale
    NewE = 0.98*Scale
    NewB = 0
    NewC = - (NewA *Xl)
    NewD = 0
    NewF = - NewE*Yl
    Pmatrix = [NewA,NewB,NewC,NewD,NewE,NewF]
    print('pmatrix %s'%str(Pmatrix))
    File.write('%.2f %.2f scale\n'%(Scale*0.8,Scale*0.8))
    File.write('%.2f %.2f translate\n'%(-Xl,-Yl))
    File.write('/Courier findfont 1 scalefont setfont\n')

    return sizeX,sizeY,Scale
   
def was_postscript_opening(File,Schem):
    [(Xl,Yl),(Xh,Yh)] = Schem.bbox()
    [Xpr,Ypr] = get_context('printer_box')
    Prt = max(Xpr,Ypr)
    DDx = Xh-Xl
    DDy = Yh-Yl
    if (DDx>DDy):
        Scale = (1.0 * Prt/DDx)
    else:
        Scale = (1.0 * Prt/DDy)

    sizeX = int(DDx*Scale)
    sizeY = int(DDy*Scale)
    print('sizexy',sizeX,sizeY,Scale)
    PS0 = PSOPEN.replace('XXXX',str(sizeX))
    PS1 = PS0.replace('YYYY',str(sizeY))
    File.write(PS1)
        
    
    NewA = 0.98*Scale
    NewE = 0.98*Scale
    NewB = 0
    NewC = 20 - (NewA *Xl)
    NewD = 0
    NewF = 20 - NewE*Yl
    Pmatrix = [NewA,NewB,NewC,NewD,NewE,NewF]

##    File.write('%f %f T\n'%(Xl-5*NewA,-Yh))
    File.write('%.2f %.2f scale\n'%(Scale*0.8,Scale*0.8))
    File.write('30 30 translate\n')
    File.write('/Courier findfont 1 scalefont setfont\n')

    return sizeX,sizeY,Scale


    if (DDy>=DDx):
        Xpr1 = Xpr
        Ypr1 = Ypr
        Rot='no'
    else:
        Xpr1 = Ypr
        Ypr1 = Xpr
        Rot='yes'
        
    NewA1 = 0.98*(Xpr1-20)/(Xh-Xl)
    NewE1 = 0.98*(Ypr1-20)/(Yh-Yl)
    AbsA = abs(NewA1)
    AbsE = abs(NewE1)
    Small = min(AbsA,AbsE)
    if (NewA1>0):
        NewA= -Small
    else:
        NewA=  Small
    if (NewE1>0):
        NewE= Small
    else:
        NewE= -Small


    NewB = 0
    NewC = 20 - (NewA *Xl)
    NewD = 0
    NewF = 60-NewE*Yl
    Pmatrix = [NewA,NewB,NewC,NewD,NewE,NewF]
    print('xh=%d xl=%d yh=%d yh=%d'%(Xh,Xl,Yh,Yl))
    if (Rot=='yes'):
        File.write('%f %f scale\n'%(Small,Small))
        File.write('90 rotate\n')
        File.write('%f %f T\n'%(-Xl+10,-Yh))
    else:
        File.write('%f %f scale\n'%(Small,-Small))
        File.write('%f %f T\n'%(Xl-5*NewA,-Yh))
    File.write('/Courier findfont 1 scalefont setfont\n')
   





def postscript_closing(File):
    File.write('showpage\ngrestore\n%%EndPage: "x" 1\n')


def postscript_aline(File,List,Color):
    if Color:
        set_pscontext(File,'setrgbcolor',Color)
    File.write('N %.2f %.2f M '%(List[0][0],List[0][1]))
    for i in range(1,len(List)):
        File.write('%.2f %.2f L '%(List[i][0],List[i][1]))
    File.write('S\n')



def postscript_circle(File,P0,P1,Color):
    set_pscontext(File,'setrgbcolor',Color)
    R0 = abs(P0[0]-P1[0])
    R1 = abs(P0[1]-P1[1])
    R = max(R0,R1)
    File.write('N %.1f %.1f %.1f -180 180 arc S\n'%(P0[0],P0[1],R))

def postscript_fcircle(File,P0,P1,Color):
    set_pscontext(File,'setrgbcolor',Color)
    R0 = abs(P0[0]-P1[0])
    R1 = abs(P0[1]-P1[1])
    R = max(R0,R1)
    File.write('N %.1f %.1f %.1f -180 180 arc F\n'%(P0[0],P0[1],R))

def postscript_text(File,Text,Point,Rot,Color,Size=1.0):
    set_pscontext(File,'setrgbcolor',Color)
    File.write('gsave N %.2f %.2f M %s -%s scale (%s) show grestore\n'%(Point[0],Point[1],Size,Size,Text))

