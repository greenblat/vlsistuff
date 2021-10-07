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
    Mod = Glbs.details[Root]
    Module = Mod.Module
    File.write('picture %s\n' % Module)
    Names = {}
    Params = {}
    for Key in Mod.params:
        Obj = Mod.params[Key]
        if (Obj.Param=='name')and(Obj.Value!='$inst'):
            Names[Obj.Owner]=Obj.Value
        elif Obj.Owner not in Params:
            Params[Obj.Owner]=[(Obj.Param,Obj.Value)]
        else:
            Params[Obj.Owner].append((Obj.Param,Obj.Value))
    Inps = {}
    Outs = {}
    Inouts = {}
    LongestIn = 0
    LongestOut = 0
    for Inst in Mod.instances:
        Obj = Mod.instances[Inst]
        Point = Obj.Point
        Rot   = Obj.Rot
        nInps,nOuts = 0,0
        if Obj.Type=='input':
            nInps +=1
            if Inst in Names:
                Inps[Names[Inst]]= Inst,Point,Rot
                LongestIn = max(LongestIn,len(Names[Inst]))
            else:
                Inps[Inst]=Inst,Point,Rot
                Names[Inst]=Inst
                LongestIn = max(LongestIn,len(Inst))
        elif Obj.Type=='output':
            nOuts +=1
            if Inst in Names:
                Outs[Names[Inst]]=Inst,Point,Rot
                LongestOut = max(LongestOut,len(Names[Inst]))
            else:
                Outs[Inst]=Inst,Point,Rot
                LongestOut = max(LongestOut,len(Inst))
                Names[Inst]=Inst,Point,Rot
        elif Obj.Type=='inout':
            if Inst in Names:
                Inouts[Names[Inst]]=Inst,Point,Rot
            else:
                Inouts[Inst]=Inst,Point,Rot
                Names[Inst]=Inst
    
    X0,Y0 = 1000,1000
    X1,Y1 = -1000,-1000
    for Inp in Inps:
        Point = Inps[Inp][1]
        X0 = min(X0,Point[0]) 
        X1 = max(X1,Point[0]) 
        Y0 = min(Y0,Point[1]) 
        Y1 = max(Y1,Point[1]) 
    for Out in Outs:
        Point = Outs[Out][1]
        X0 = min(X0,Point[0]) 
        X1 = max(X1,Point[0]) 
        Y0 = min(Y0,Point[1]) 
        Y1 = max(Y1,Point[1]) 

    Xspan = 2+(LongestIn+LongestOut+len(Module)) * 0.3

    ScaleX = Xspan/(X1-X0)
    ScaleY = 1.0/(Y1-Y0) * max(nInps,nOuts)
    Scale = max(ScaleX,ScaleY)
    print('xspan=%s scalex=%s scaley=%s' % (Xspan,ScaleX,ScaleY))
    MaxIn = -100
    MinOu = 1005
    MaxY  = -100
    for Inp in Inps:
        Point = list(Inps[Inp][1])
        Point[0] -= X0
        Point[1] -= Y0
        Point[0] *= ScaleX
        Point[1] *= ScaleY
        Point[0] = int(Point[0] * 10)/10.0
        Point[1] = int(Point[1] * 10)/10.0
        MaxIn = max(MaxIn,Point[0])
        MaxY = max(MaxY,Point[1])
        File.write('pic_pin %s i xy=%s,%s\n' % (nobus(Inp),Point[0],Point[1]))
        Inps[Inp] = Inp,Point,Inps[Inp][2]
    for Out in Outs:
        Point = list(Outs[Out][1])
        Point[0] -= X0
        Point[1] -= Y0
        Point[0] *= ScaleX
        Point[1] *= ScaleY
        Point[0] = int(Point[0] * 10)/10.0
        Point[1] = int(Point[1] * 10)/10.0
        MinOu = min(MinOu,Point[0])
        MaxY = max(MaxY,Point[1])
        File.write('pic_pin %s o xy=%s,%s\n' % (nobus(Out),Point[0],Point[1]))
        Outs[Out] = Out,Point,Outs[Out][2]

    File.write('pic_aline list=%s,-0.5,%s,%s\n' % (MaxIn+0.3,MaxIn+0.3,MaxY+0.5))
    File.write('pic_aline list=%s,-0.5,%s,%s\n' % (MinOu-0.3,MinOu-0.3,MaxY+0.5))
    File.write('pic_aline list=%s,%s,%s,%s\n' % (MaxIn+0.3,-0.5,MinOu-0.3,-0.5))
    File.write('pic_aline list=%s,%s,%s,%s\n' % (MaxIn+0.3,MaxY+0.5,MinOu-0.3,MaxY+0.5))

    for Inp in Inps:
        Inp,Point,Rot = Inps[Inp]
        File.write('pic_aline list=%s,%s,%s,%s\n' % (Point[0],Point[1],MaxIn+0.3,Point[1]))
        File.write('pic_text %s xy=%s,%s\n' % (Inp,MaxIn+0.4,Point[1]))

    for Out in Outs:
        Out,Point,Rot = Outs[Out]
        File.write('pic_aline list=%s,%s,%s,%s\n' % (Point[0],Point[1],MinOu-0.3,Point[1]))
        File.write('pic_text %s xy=%s,%s\n' % (Out,MinOu-0.3-(len(Out)*0.3),Point[1]))
    Half = (MaxIn + MinOu)/2 - len(Module)*0.3
    File.write('pic_text %s xy=%s,%s\n' % (Module,Half, MaxY/2))


    File.write('end\n')
    File.close()

def nobus(Txt):
    if '[' in Txt:
        return Txt[:Txt.index('[')]
    return Txt




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
