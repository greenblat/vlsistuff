

# X0,Y0 is end of arrow, X1,Y1 is the tip point of the arrow.
import math
def make_arrow(X0,Y0,X1,Y1,Len):
    Dx = X1-X0
    Dy = Y1-Y0
    if Dx==0:
        X2 = X1-(Len/2)
        X3 = X1+(Len/2)
        if Dy>0:
            Y2 = Y1-Len
            Y3 = Y1+Len
        else:
            Y3 = Y1-Len
            Y2 = Y1+Len
        return (X2,Y2),(X3,Y3)

    if Dy==0:
        Y2 = Y1-(Len/2)
        Y3 = Y1+(Len/2)
        if Dx>0:
            X2 = X1-Len
            X3 = X1+Len
        else:
            X3 = X1-Len
            X2 = X1+Len
        return (X2,Y2),(X3,Y3)

    Angle = math.atan(Dx/Dy)
    Angp = Angle+toRadian(10)
    Angn = Angle-toRadian(10)
#    print pangle(Angle),pangle(Angp),pangle(Angn)
    
    Sinp = (math.sin(Angp)*Len)
    Cosp = (math.cos(Angp)*Len)
    Sinn = (math.sin(Angn)*Len)
    Cosn = (math.cos(Angn)*Len)


    if (X1>X0)and(Y1>Y0):
        X2 = X1-Sinp
        Y2 = Y1-Cosp
        X3 = X1-Sinn
        Y3 = Y1-Cosn
        Quad = 1
    elif (X1>X0)and(Y1<Y0):
        X2 = X1+Sinp
        Y2 = Y1+Cosp
        X3 = X1+Sinn
        Y3 = Y1+Cosn
        Quad = 2
    elif (X1<X0)and(Y1>Y0):
        X2 = X1-Sinp
        Y2 = Y1-Cosp
        X3 = X1-Sinn
        Y3 = Y1+Cosn
        Quad = 3
    elif (X1<X0)and(Y1<Y0):
        X2 = X1+Sinp
        Y2 = Y1+Cosp
        X3 = X1+Sinn
        Y3 = Y1+Cosn
        Quad = 4

#    print 'quad=%d'%Quad,
#    printIt(((X2,Y2),(X3,Y3)),X1,Y1)
    return (X2,Y2),(X3,Y3)
        

def toRadian(Angle):
    return (Angle/360.0)*2*math.pi

def pangle(Angle):
    return (360 * Angle)/(2*math.pi)


def printIt(XY,X,Y):
    (X0,Y0),(X1,Y1) = XY
    print '%.1f %1.f        %.1f %.1f            -===   %.1f %1.f'%(X0,Y0,X1,Y1,X,Y)

def main():
    XY = make_arrow(0,0,10,10,2)
    printIt(XY,10,10)

    XY = make_arrow(0,0,-10,10,2)
    printIt(XY,-10,10)

    XY = make_arrow(0,0,-10,-10,2)
    printIt(XY,-10,-10)

    XY = make_arrow(0,0,10,-10,2)
    printIt(XY,10,-10)
if __name__ == '__main__':
    main()


