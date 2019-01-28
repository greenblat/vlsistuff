
import string,types


class postscriptClass:
    def __init__(self,Fname,Db):
        self.mulx = 1.0
        self.muly = 1.0
        self.disty = 1.5
        self.totalx = 1000
        self.textSize = 0.8
        self.curY = 0
        self.waveOffset = 10
        self.labelOffset = 0.3
        self.trans = 0.2
        self.UpDown = 0.3
        self.Fname = Fname
        self.File = open(Fname,'w')
        self.Db = Db

    def open(self,PageX,PageY,Scale):
        PS0 = string.replace(PSOPEN,'XXXX',str(int(PageX)))
        PS1 = string.replace(PS0,'YYYY',str(int(PageY)))
        self.File.write(PS1)
        self.File.write('%.1f %.1f scale\n'%(Scale,Scale))



    def color(self,R,G,B):
        self.File.write('%.1f %.1f %.1f setrgbcolor\n'%(R,G,B))
        
    def setDash(self,A,B):
        self.File.write('[%s %s] 0 setdash\n'%(A,B))

    def fcircle(self,X0,Y0,R,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        self.File.write('N %.1f %.1f %.1f -180 180 arc F\n'%(X0,Y0,R))

    def aline(self,X0,Y0,X1,Y1,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        self.File.write('N %.2f %.2f M %.2f %.2f L S\n'%(X0,Y0,X1,Y1))


    def unsetTempColor(self):
        self.tempColor=False
    def setTempColor(self,Color):
        self.tempColor=Color

            
    def text(self,X,Y,Text,Color=(0.5,0.5,0.5),Size=1):
        self.color(Color[0],Color[1],Color[2])
        if Y=='up':
            Y = self.curY
        self.File.write('gsave N %.2f %.2f M %s %s scale (%s) show grestore\n'%(X,Y,Size*self.textSize,Size*self.textSize,str(Text)))

    def close(self):
        self.File.write('showpage\ngrestore\n%%EndPage: "x" 1\n')
        self.File.close()



PSOPEN = '''%!PS
gsave
<< /PageSize [XXXX YYYY] >> setpagedevice
%%Page: "x" 1
1 setlinejoin
1 setlinecap
/Courier findfont 1.0 scalefont setfont

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
2 2 translate
% 5 8 scale
'''

def getColor(Text):
    if Text=='red': return (1,0,0)
    if Text=='black': return (0,0,0)
    if Text=='white': return (1,1,1)
    if Text=='green': return (0,1,0)
    if Text=='blues': return (0,0,1)
    if Text=='yellow': return (0.8,0.8,0)
    return (0.3,0.3,0.3)

