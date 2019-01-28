#! /usr/bin/python

import os,sys,string
import png
import math


from drawVectorText import make_text_vectors



class pngClass:
    def __init__(self,Fname,Db):
        self.File = open(Fname,'wb')
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
        self.Mat=False



    def open_gray(self,sizeX,sizeY,Scale):
        sizeX = int(sizeX*2)
        sizeY = int(sizeY*2)
        self.pngWriter = png.Writer(sizeX, sizeY, greyscale=True)
        self.Mat = matrixClass(sizeX,sizeY)
        self.Scale=Scale*2
        self.sizeX=sizeX
        self.sizeY=sizeY


    def open(self,sizeX,sizeY,Scale):
        sizeX = int(sizeX*2)
        sizeY = int(sizeY*2)
        self.pngWriter = png.Writer(sizeX, sizeY)
        self.Mat = matrixClass(sizeX*3,sizeY)
        self.Scale=Scale*2
        self.sizeX=sizeX
        self.sizeY=sizeY






    def close(self):
        if self.Mat:
            self.pngWriter.write(self.File,self.Mat.Mat)
        self.File.close()

    def prtx(self,X):
        return int(X*self.Scale)+self.offsetX

    def prty(self,Y):
        return self.sizeY -(0 + int(Y*self.Scale)+self.offsetY)

    def aline(self,X0,Y0,X1,Y1,Color=False):
        if Color:
            self.color(Color[0],Color[1],Color[2])
        X0 = self.prtx(X0)
        Y0 = self.prty(Y0)
        X1 = self.prtx(X1)
        Y1 = self.prty(Y1)
        D0 = int(self.Scale*self.Dash[0])
        D1 = int(self.Scale*self.Dash[1])
        self.Mat.line(X0,Y0,X1,Y1,self.prtColor(),D0,D1)

    def mline(self,List,Color=False,Dash=False):
        res = []
        for XY in List:
            X,Y = self.prtx(XY[0]),self.prty(XY[1])
            res.append((X,Y))
        D0 = int(self.Scale*self.Dash[0])
        D1 = int(self.Scale*self.Dash[1])
        if not Dash: D1=0
        self.Mat.aline(res,self.prtColor(),D0,D1)
            

    def circle(self,X0,Y0,R,Color=False):
        R0 = int(self.Scale*R)
        R0SQ = R0*R0
        Xl = self.prtx(X0)
        Yl = self.prty(Y0)
        for X in range(Xl-R0,Xl+R0+1):
            for Y in range(Yl-R0,Yl+R0+1):
                Dist = (X-Xl)*(X-Xl)+(Y-Yl)*(Y-Yl)
                if (Dist <= R0SQ)and(Dist>=(R0SQ-1)):
                    self.Mat.pixel(X,Y,self.prtColor())

    def fcircle(self,X0,Y0,R,Color=False):
        R0 = int(self.Scale*R)
        Xl = self.prtx(X0)
        Yl = self.prty(Y0)
        for X in range(Xl-R0,Xl+R0+1):
            for Y in range(Yl-R0,Yl+R0+1):
                Dist = (X-Xl)*(X-Xl)+(Y-Yl)*(Y-Yl)
                if Dist <= (R0*R0):
                    self.Mat.pixel(X,Y,self.prtColor())
       
    def text(self,X,Y,Text,Color=(0.5,0.5,0.5),Size=1):
        Big = make_text_vectors(Text,(X,Y),'left',Size/2)
        for List in Big:
            self.mline(List,Color,0)

    def color(self,R,G,B):
        self.RGB = R,G,B
        return

    def setDash(self,A,B):
        self.Dash = A,B
        return

    def prtColorGrey(self):
        Df = (self.RGB[0] * self.RGB[0]) + (self.RGB[1] * self.RGB[1]) + (self.RGB[2] * self.RGB[2]) 
        Dist = min(255,int(255*math.sqrt(Df/3)))
        return Dist

    def prtColor(self):
        Dist = min(255,int(255*self.RGB[0])),min(255,int(255*self.RGB[1])),min(255,int(255*self.RGB[2]))
        return Dist






class matrixClass:
    def __init__(self,X,Y):
        self.Mat = mat(X,Y)
        self.mX=X
        self.mY=Y

    def pixel(self,X,Y,Color):
        self.Mat[Y][3*X+0]=Color[0]
        self.Mat[Y][3*X+1]=Color[1]
        self.Mat[Y][3*X+2]=Color[2]


    def line(self,X0,Y0,X1,Y1,Color,Dash1=0,Dash0=0):
        Df = (X0-X1)*(X0-X1) + (Y0-Y1)*(Y0-Y1)
        Dist = int(math.sqrt(Df)+0.5)
         
        for Ind in range(Dist):
            X = Ind*(X1-X0)/Dist +X0
            Y = Ind*(Y1-Y0)/Dist +Y0
            if (Y>=0)and(X>0)and(Y<self.mY)and((3*X)<self.mX):
                if Dash0==0:
                    self.Mat[Y][3*X+0]=Color[0]
                    self.Mat[Y][3*X+1]=Color[1]
                    self.Mat[Y][3*X+2]=Color[2]
                else:
                    DD = (Dash1+Dash0)
                    Pos = Ind % DD
                    if Pos<Dash1:
                        self.Mat[Y][3*X+0]=Color[0]
                        self.Mat[Y][3*X+1]=Color[1]
                        self.Mat[Y][3*X+2]=Color[2]

                    

    def aline(self,List,Color,D0,D1):
        X0,Y0 = List[0]
        for X1,Y1 in List[1:]:
            self.line(X0,Y0,X1,Y1,Color,D0,D1)
            X0,Y0=X1,Y1
        

def mat(Sizex,Sizey):
    Mat=[]
    for Y in range(Sizey):
        Line = []
        for X in range(Sizex):
            Line.append(255)
        Mat.append(Line)
    return Mat




