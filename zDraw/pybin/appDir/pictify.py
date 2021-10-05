#! /usr/bin/python

import os,sys

def main():
    global Cell
    Fname = sys.argv[1]
    Max = int(sys.argv[2])
    File = open(Fname)
    readfile(File)
    Cell = get_cell_name(Fname)
    Fout = open('%s.zpic'%Cell,'w') 
    Fout.write('picture %s\n'%Cell)
    Dx,Dy,Scale=make_limits(Max)
    output_pins(Fout,Dx,Dy,Scale)
    output_segments(Fout,Dx,Dy,Scale)
    output_texts(Fout,Dx,Dy,Scale)
    Fout.write('end\n')
    Fout.close()

def pictify(Glbs,Root,File):
    File.write('// placeholder for %s.zpic generation\n' % Root)
    File.close()




def make_limits(Max):
    MinX=999999
    MinY=999999
    MaxX=-999999
    MaxY=-999999
    for Owner in Pins:
        LL = Pins[Owner]
        Dir=LL[0]
        X=float(LL[1][0])
        Y=float(LL[1][1])
        MinX = min(X,MinX)
        MinY = min(Y,MinY)
        MaxX = max(X,MaxX)
        MaxY = max(Y,MaxY)
    for Seg in Segs:
        [(X0,Y0),(X1,Y1)]=Seg
        MinX = min(X0,MinX)
        MinY = min(Y0,MinY)
        MaxX = max(X0,MaxX)
        MaxY = max(Y0,MaxY)
        MinX = min(X1,MinX)
        MinY = min(Y1,MinY)
        MaxX = max(X1,MaxX)
        MaxY = max(Y1,MaxY)
    Dx = MaxX-MinX
    Dy = MaxY-MinY
    ScaleX = Max*1.0/Dx
    ScaleY = Max*1.0/Dy
    Scale = min(ScaleX,ScaleY)
    return MinX,MinY,Scale

def output_segments(Fout,Dx,Dy,Scale):
    Lines=Segs
    for Line in Lines:
        Fout.write('pic_aline list=')
        Pref=''
        for XY in Line:
            XX = remap(XY[0],Dx,Scale)
            YY = remap(XY[1],Dy,Scale)
            Fout.write('%s%.2f,%.2f'%(Pref,XX,YY))
            Pref=','
        Fout.write('\n') 

def remap(XY,Del,Scale):
     return (float(XY)-Del)*Scale

def output_texts(Fout,Dx,Dy,Scale):
    for Txt,Coords in Texts:
        X = Coords[0]
        Y = Coords[1]
        X0 = remap(X,Dx,Scale)
        Y0 = remap(Y,Dy,Scale)
        Fout.write('pic_text %s xy=%.1f,%.1f\n'%(Txt,X0,Y0))
        

def output_pins(Fout,Dx,Dy,Scale):
    for Owner in Pins:
        LL = Pins[Owner]
        Dir=LL[0]
        X=LL[1][0]
        Y=LL[1][1]
        try:
          Pin=LL[2]
        except:
            print('error! ilia: you forgot to name a pin  in %s'%Cell)
            Pin = 'error'
        X0 = remap(X,Dx,Scale)
        Y0 = remap(Y,Dy,Scale)
        Fout.write('pic_pin %s %s xy=%.1f,%.1f\n'%(Pin,Dir,X0,Y0))


Segs=[]
Pins={}
Texts=[]
def readfile(File):
    while 1:
        line = File.readline()
        if line=='':
            return
        wrds = line.split()
        if len(wrds)==0:
            pass
        elif (wrds[0]=='wire'):
            Coords = wrds[4][5:]
            List = Coords.split(',')
            Seg = [(float(List[0]),float(List[1])),(float(List[2]),float(List[3]))]
            Segs.append(Seg)
        elif (wrds[0]=='inst')and(wrds[1]=='input'):
            Name =wrds[2]
            Coords = wrds[3][3:]
            List = Coords.split(',')
            Pins[Name] =['i',List]
        elif (wrds[0]=='inst')and(wrds[1]=='output'):
            Name =wrds[2]
            Coords = wrds[3][3:]
            List = Coords.split(',')
            Pins[Name] =['o',List]
        elif (wrds[0]=='param')and(wrds[2]=='name'):
            Name = wrds[3]
            Owner = wrds[1]
            Pins[Owner].append(Name)
        elif (wrds[0]=='geom')and(wrds[1]=='text'):
####        geom text qn list=13.6,10.8
            Text = wrds[2]
            Coords = wrds[3][5:]
            List = Coords.split(',')
            Texts.append((Text,List))


def get_cell_name(Fname):
    ww = Fname.split('/')
    ww1 = ww[-1].split('.')
    return ww1[0]




if __name__ == '__main__':
    main()
