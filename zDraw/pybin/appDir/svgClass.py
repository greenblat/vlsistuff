



class svgClass:
    def __init__(self,Fname,Db):
        self.Fname = Fname
        self.File = open(Fname,'w')
#        self.File.write('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">\n')
        self.Db=Db
        self.Color = 'black'
        self.textSize = 1
        self.RGB = 0,0,0
        self.offsetX=10
        self.offsetY=10
        self.textOffset = 0
        self.Dash=0,0
        self.sizeX=1000
        self.sizeY=500
        self.Scale=1.0


    def open(self,sizeX,sizeY,Scale,Xl,Yl,Xh,Yh):
        self.sizeX=sizeX
        self.sizeY=sizeY
        self.Scale=Scale*0.9
        self.File.write('<svg width="%d" height="%d" xmlns="http://www.w3.org/2000/svg" version="1.1">\n'%(sizeX,sizeY+20))
        self.offsetX=-(Xl*self.Scale)
        self.offsetY=-(Yl*self.Scale)

    def close(self):
        self.File.write('</svg>\n')


    def prtx(self,X):
        return int(X*self.Scale)+self.offsetX

    def prty(self,Y):
        return self.sizeY -(0 + int(Y*self.Scale)+self.offsetY)

    def x_aline(self,List,Color=False):
        X0,Y0=List[0]
        for X1,Y1 in List[1:]:
            self.aline(X0,Y0,X1,Y1,Color)
            X0=X1
            Y0=Y1
    def x_circle(self,P0,P1,Color=False):
        R0 = abs(P0[0]-P1[0])
        R1 = abs(P0[1]-P1[1])
        R = max(R0,R1)
        self.circle(P0[0],P0[1],R,Color)

    def x_fcircle(self,P0,P1,Color=False):
        R0 = abs(P0[0]-P1[0])
        R1 = abs(P0[1]-P1[1])
        R = max(R0,R1)
        self.fcircle(P0[0],P0[1],R,Color)
        
#  <line x1="50" y1="50" x2="200" y2="200" stroke="blue" stroke-width="4" />
# style="stroke:rgb(255,0,0);stroke-width:2"
    def aline(self,X00,Y0,X1,Y1,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        X0 = self.prtx(X00)
        Y0 = self.prty(Y0)
        X1 = self.prtx(X1)
        Y1 = self.prty(Y1)
        if self.Dash[1]==0:
            self.File.write('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" />\n'%(X0,Y0,X1,Y1,self.prtColor()))
        else:
            self.File.write('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="1" stroke-dasharray="%d,%d" />\n'%(X0,Y0,X1,Y1,self.prtColor(),int(self.Dash[0]*self.Scale),int(self.Dash[1]*self.Scale)))

#  <circle cx="125" cy="125" r="75" fill="orange" />
    def fcircle(self,X0,Y0,R,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        X = self.prtx(X0)
        Y = self.prty(Y0)
        R = int(R*self.Scale)
        self.File.write('<circle cx="%d" cy="%d" r="%d" fill="%s" />\n'%(X,Y,R,self.prtColor()))

    def circle(self,X0,Y0,R,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        X = self.prtx(X0)
        Y = self.prty(Y0)
        R = int(R*self.Scale)
        self.File.write('<circle cx="%d" cy="%d" r="%d" stroke="%s" fill="white" />\n'%(X,Y,R,self.prtColor()))




    def text(self,X,Y,Text,Color=(0.5,0.5,0.5),Size=1):
        self.color(Color[0],Color[1],Color[2])
        if Y=='up':
            Y = self.curY
        X = self.prtx(X)
        Y = self.prty(Y)+self.textOffset
        self.File.write('<text x="%d" y="%d" fill="%s">%s</text>\n'%(X,Y,self.prtColor(),Text))

    def color(self,R,G,B):
        self.RGB = R,G,B
        
    def setDash(self,A,B):
#        self.File.write('[%s %s] 0 setdash\n'%(A,B))
        self.Dash = A,B
        return

    def setColor(self,Whose):
        if (Whose in [0,1,'sig','bus'])or((type(Whose) is str)and(Whose[0]=='"')):
            if self.tempColor:
                self.color(self.tempColor[0],self.tempColor[1],self.tempColor[2]);
                return
        if Whose in self.Db.params['color']:
            Color1 = self.Db.params['color'][Whose]
            if type(Color1) is str:
                Color = getColor(Color1)
            else:
                Color = Color1
            self.color(Color[0],Color[1],Color[2])
        else:
            print('color missing',Whose)


    def prtColor(self):
        Str = 'rgb(%d,%d,%d)'%(min(70,int(self.RGB[0])),min(30,int(self.RGB[1])),min(50,int(self.RGB[2])))
        return Str




def getColor(Text):
    if Text=='red': return (1,0,0)
    if Text=='black': return (0,0,0)
    if Text=='white': return (1,1,1)
    if Text=='green': return (0,1,0)
    if Text=='blues': return (0,0,1)
    if Text=='yellow': return (0.8,0.8,0)
    return (0.3,0.3,0.3)

Example = '''
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <rect x="25" y="25" width="200" height="200" fill="lime" stroke-width="4" stroke="pink" />
  <circle cx="125" cy="125" r="75" fill="orange" />
  <polyline points="50,150 50,200 200,200 200,100" stroke="red" stroke-width="4" fill="none" />
  <line x1="50" y1="50" x2="200" y2="200" stroke="blue" stroke-width="4" />
</svg>


'''



