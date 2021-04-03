


class plotClass:
    def __init__(self,Db,Ps,Svg,Png):
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
        self.Db = Db
        self.Ps = Ps
        self.Svg = Svg
        self.Png = Png

    def setScale(self,lastTime,numSigs):
        if numSigs==0: return
        dY = numSigs * self.disty
        dX = (lastTime + self.waveOffset)*self.mulx
        
        if dX>dY:
            XX = 1000.0
            YY = XX * (1.0*dY/dX)
        else:
            YY = 1000.0
            XX = YY * (1.0*dX/dY)

        ScaleY = YY/dY
        ScaleX = (XX/dX)
        Scale = min(ScaleX,ScaleY)

        XXX = Scale * dX
        YYY = Scale * dY
        Scale = 0.9 * Scale
        self.Ps.open(XXX,YYY,Scale)
        self.Svg.open(XXX,YYY,Scale)
        self.Png.open(XXX,YYY,Scale)

    def connect(self,X0,Prev,Data):
        if Prev==1:
            Start0 = self.curY+self.muly
            Start1 = self.curY+self.muly
        elif Prev==0:
            Start0 = self.curY
            Start1 = self.curY
        elif Prev in ['x','z']:
            Start0 = self.curY+self.muly/2
            Start1 = self.curY+self.muly/2
        else:
            Start0 = self.curY+0
            Start1 = self.curY+self.muly

        self.setColor('sig')
        if (Prev == 'break')or(Data == 'break'):
            pass
        elif (Data==1):
            self.aline(X0,Start0,(X0 + self.trans),self.curY+self.muly)
            self.aline(X0,Start1,(X0 + self.trans),self.curY+self.muly)
        elif (Data==0):
            self.aline(X0,Start0,(X0 + self.trans),self.curY)
            self.aline(X0,Start1,(X0 + self.trans),self.curY)
        elif (Data in ['x','z']):
            if Data=='x':
                self.setColor('x')
            elif Data=='z':
                self.setColor('z')
                self.setDash(0.2,0.2)
            self.aline(X0,Start0,(X0 + self.trans),self.curY+self.muly/2)
            self.aline(X0,Start1,(X0 + self.trans),self.curY+self.muly/2)
        else:            
            self.aline(X0,Start1,(X0 + self.trans),self.curY)
            self.aline(X0,Start0,(X0 + self.trans),self.curY+self.muly)

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

    def color(self,R,G,B):
        self.Ps.color(R,G,B)
        self.Svg.color(R,G,B)
        self.Png.color(R,G,B)

    def setDash(self,A,B):
        self.Ps.setDash(A,B)
        self.Svg.setDash(A,B)
        self.Png.setDash(A,B)

    def fcircle(self,X0,Y0,R,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        self.Ps.fcircle(X0,Y0,R)
        self.Svg.fcircle(X0,Y0,R)
        self.Png.fcircle(X0,Y0,R)

    def aline(self,X0,Y0,X1,Y1,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        self.Ps.aline(X0,Y0,X1,Y1)
        self.Svg.aline(X0,Y0,X1,Y1)
        self.Png.aline(X0,Y0,X1,Y1)

    def skipY(self):
        self.curY += self.disty

    def unsetTempColor(self):
        self.tempColor=False
    def setTempColor(self,Color):
        self.tempColor=Color

    def plot(self,Sig,Wave,Color=(0,0,0)):
        self.text(0,self.curY+self.muly/4,Sig,Color)
        Off = self.waveOffset*self.mulx
        X0 = Off
        Prev = 0
        self.unsetTempColor()
        for Item in Wave:
            self.setDash(1,0)
            if Item[0]!='mark':
                (Start,End,Data) = Item
            if Item[0]=='mark':
                self.Db.recordMark(Sig,Item[2],X0,self.curY)
            elif (Item[0]=='color'):
                Color = getColor(Item[2])
                self.setTempColor(Color)
            elif (Item[0]=='break'):
                self.aline(X0,-0.2+self.curY,X0+self.trans,self.curY+self.muly/2)
                self.aline(X0+self.trans,self.curY+self.muly/2,X0,self.curY+self.muly+0.2)
                self.aline(X0+self.trans*2,-0.2+self.curY,X0+self.trans*3,self.curY+self.muly/2)
                self.aline(X0+self.trans*3,self.curY+self.muly/2,X0+self.trans*2,self.curY+self.muly+0.2)
                Data = 'break'
                End = (X0+self.trans*2-Off)/self.mulx
            elif Data=='z':
                self.setDash(0.2,0.2)
                self.setColor('z')
                self.aline(X0+self.trans,self.curY+self.muly/2,(Off+End*self.mulx),self.curY+self.muly/2)
            elif Data=='x':
                self.setColor('x')
                self.aline(X0+self.trans,self.curY+self.muly/2,(Off+End*self.mulx),self.curY+self.muly/2)
            elif Data=='up':
                self.aline(X0+self.trans,self.curY,(Off + End*self.mulx),self.curY)
                self.aline(X0+self.trans,self.curY+self.muly,(Off + End*self.mulx),self.curY+self.muly)
                XX = X0+self.trans+self.UpDown*self.mulx
                self.setDash(0.2,0.2)
                while XX<(Off + End*self.mulx-self.UpDown*self.mulx):
                    self.aline(XX+self.UpDown*self.mulx,self.curY+self.muly,XX,self.curY)
                    XX += self.UpDown*self.mulx 
            elif Data=='down':
                self.aline(X0+self.trans,self.curY,(Off + End*self.mulx),self.curY)
                self.aline(X0+self.trans,self.curY+self.muly,(Off + End*self.mulx),self.curY+self.muly)
                self.setDash(0.2,0.2)
                XX = X0+self.trans+self.UpDown*self.mulx
                while XX<(Off + End*self.mulx-self.UpDown*self.mulx):
                    self.aline(XX,self.curY+self.muly,XX+self.UpDown*self.mulx,self.curY)
                    XX += self.UpDown*self.mulx 
            elif Data==0:
                self.setColor('sig')
                self.aline(X0+self.trans,self.curY,(Off+End*self.mulx),self.curY)
            elif Data==1:
                self.setColor('sig')
                self.aline(X0+self.trans,self.curY+self.muly,(Off + End*self.mulx),self.curY+self.muly)
            else:
                self.setColor('bus')
                self.aline(X0+self.trans,self.curY,(Off + End*self.mulx),self.curY)
                self.aline(X0+self.trans,self.curY+self.muly,(Off + End*self.mulx),self.curY+self.muly)
                if (type(Data) is str):
                    Data = Data.replace('"','')
                self.text(X0 + self.labelOffset*self.mulx,self.curY+self.muly/3,str(Data))
            if (Item[0]!='color')and(Item[0]!='mark'):
                self.connect(X0,Prev,Data)
                X0 = Off+End*self.mulx
                Prev = Data
        self.curY += self.disty

    def vgrid(self,Start,Step,Last,Color=(0.5,0.5,0.5)):
        X = Start
        self.setDash(0.1,0.1)
        self.color(Color[0],Color[1],Color[1])
        while X<=Last:
            X0 = X*self.mulx+self.waveOffset
            self.aline(X0,0,X0,self.curY+self.muly)
            X += Step
            
    def text(self,X,Y,Text,Color=(0.5,0.5,0.5),Size=1):
        if Y=='up':
            Y = self.curY
        self.Ps.text(X,Y,str(Text),Color,Size*self.textSize)
        self.Svg.text(X,Y,str(Text),Color,Size*self.textSize)
        self.Png.text(X,Y,str(Text),Color,Size*self.textSize)



    def vline(self,X,Color=(0.5,0.5,0.5),Dash=(1,0)):
        self.setDash(Dash[0],Dash[1])
        self.color(Color[0],Color[1],Color[2])
        X0 = X*self.mulx
        self.aline(X0,0,X0,self.curY+self.muly)
        
        

    def close(self):
        self.color(0,0.5,0)
        self.aline(self.waveOffset*self.mulx,0,self.waveOffset*self.mulx,self.curY+self.muly)
        self.text(0,self.curY+1.5,'ilia @v%s'%self.VERSION,(0.2,1.0,0.2),1.2)
        self.Ps.close()
        self.Svg.close()
        self.Png.close()




def getColor(Text):
    if Text=='red': return (1,0,0)
    if Text=='black': return (0,0,0)
    if Text=='white': return (1,1,1)
    if Text=='green': return (0,1,0)
    if Text=='blues': return (0,0,1)
    if Text=='yellow': return (0.8,0.8,0)
    return (0.3,0.3,0.3)

