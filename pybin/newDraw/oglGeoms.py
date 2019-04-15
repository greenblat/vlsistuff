

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import types,ctypes
from PIL import Image



def screenShot(Width,Height,Fname):
    print 'screenShot "%s"  %dx%d'%(Fname,Width,Height)
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(0,0,Width,Height,GL_RGB,GL_UNSIGNED_BYTE)
    image = Image.fromstring("RGB", (Width,Height), pixels)
    image = image.transpose( Image.FLIP_TOP_BOTTOM)
    image.save(Fname)




def fixCoord(Point):
    X = int(Point[0]/Glbs.wratio)
    Y = int(Point[1]/Glbs.hratio)
    return (X,Y)





def setLineWidth(Wid):
    glLineWidth(Wid)

def draw_segment(P0,P1):
   P0 = fixCoord(P0)
   P1 = fixCoord(P1)
   glBegin(GL_LINE_STRIP)
   glVertex2f(P0[0],P0[1])
   glVertex2f(P1[0],P1[1])
   glEnd()

def draw_line(P0,P1,Color):
   P0f = fixCoord(P0)
   P1f = fixCoord(P1)
   oglcolor(Color)
#   glLineWidth(2.0)
   glBegin(GL_LINE_STRIP)
   glVertex2f(P0f[0],P0f[1])
   glVertex2f(P1f[0],P1f[1])
   glEnd()

def draw_long_line(Points,Color):
    oglcolor(Color)
    glBegin(GL_LINE_STRIP)
    for (X,Y) in Points:
        (X,Y) = fixCoord((X,Y))
        glVertex2f(X,Y)
    glEnd()  

def draw_frect(X0,Y0,X1,Y1,Color):
    oglcolor(Color)
    (X0,Y0) = fixCoord((X0,Y0))
    (X1,Y1) = fixCoord((X1,Y1))
    glRectf(X0,Y0,X1,Y1)

def draw_rect(X0,Y0,X1,Y1,Color):
    oglcolor(Color)
    glBegin(GL_LINE_STRIP)
    (X0,Y0) = fixCoord((X0,Y0))
    (X1,Y1) = fixCoord((X1,Y1))
    glVertex2f(X0,Y0)
    glVertex2f(X1,Y0)
    glVertex2f(X1,Y1)
    glVertex2f(X0,Y1)
    glVertex2f(X0,Y0)
    glEnd()

def draw_xcircle(P0,Radii,Color):
    glPushMatrix()                    
    P0 = fixCoord(P0)
    (Radii,Radii0) = fixCoord((Radii,Radii))
    glTranslatef(P0[0], P0[1], 1.0)    
    oglcolor(Color)
    glutSolidSphere(Radii, 11, 11)   
    glutSolidSphere(Radii-1, 12, 12)   
    glutSolidSphere(Radii+1, 10, 10)   
    glPopMatrix()            

def draw_fcircle(P0,Radii,Color):
    (Radii,Radii0) = fixCoord((Radii,Radii))
    glPushMatrix()                    
    P0 = fixCoord(P0)
    glTranslatef(P0[0], P0[1], 1.0)    
    oglcolor(Color)
    gluDisk(gluNewQuadric(),0,Radii,10,10)
    glPopMatrix()            

def draw_circle(P0,Radii,Color):
    (Radii,Radii0) = fixCoord((Radii,Radii))
    glPushMatrix()                    
    P0 = fixCoord(P0)
    glTranslatef(P0[0], P0[1], 1.0)    
    oglcolor(Color)
    gluDisk(gluNewQuadric(),Radii-1,Radii,32,32)
    glPopMatrix()            


def draw_arc(P0,P1,P2,Color):
#    print 'arc',P0,P1,P2,Color
    return


def draw_horizontal(X0,X1,Y0,Color):
   oglcolor(Color)
   glBegin(GL_LINE_STRIP)
   (X0,Y0) = fixCoord((X0,Y0))
   (X1,Y0) = fixCoord((X1,Y0))
   glVertex2f(X0,Y0)
   glVertex2f(X1,Y0)
   glEnd()
#   print 'draw horizontal',X0,X1,Y0,Color

def draw_vertical(X,Y0,Y1,Color):
   oglcolor(Color)
   glBegin(GL_LINE_STRIP)
   (X,Y0) = fixCoord((X,Y0))
   (X,Y1) = fixCoord((X,Y1))
   glVertex2f(X,Y0)
   glVertex2f(X,Y1)
   glEnd()
#   print 'draw vert',X,Y1,Y0,Color

FONTS=[GLUT_BITMAP_8_BY_13,GLUT_BITMAP_9_BY_15,GLUT_BITMAP_HELVETICA_10,GLUT_BITMAP_HELVETICA_12,GLUT_BITMAP_HELVETICA_18,GLUT_BITMAP_TIMES_ROMAN_10,GLUT_BITMAP_TIMES_ROMAN_24]

def draw_label(Text,X,Y,Color,AnchorX='left',FontSize=12):
    (X,Y) = fixCoord((X,Y))
    blending = False 
    if glIsEnabled(GL_BLEND) :
        blending = True
    #glEnable(GL_BLEND)
    oglcolor(Color)
    glRasterPos2f(X,Y)
    for ch in Text :
        glutBitmapCharacter( GLUT_BITMAP_HELVETICA_10 , ctypes.c_int( ord(ch) ) ) 
    if not blending :
        glDisable(GL_BLEND) 
#    print 'draw label',X,Y,Color,Text


GLCOLORS = {}
GLCOLORS['white']=[255,255,255,255]
GLCOLORS['red']=[255,0,0,255]
GLCOLORS['green']=[0,255,0,255]
GLCOLORS['blue']=[0,0,255,255]
GLCOLORS['cyan']=[0,255,255,255]
GLCOLORS['magenta']=[255,0,255,255]
GLCOLORS['yellow']=[200,200,0,255]
GLCOLORS['black']=[0,0,0,255]
def xglcolor(Color):
    if Color in GLCOLORS:
        return GLCOLORS[Color]
    return xglcolor('black')

def oglcolor(Color):
    if type(Color)==types.StringType:
        List = xglcolor(Color)
    else:
        List = Color
    R = List[0]/255.0
    G = List[1]/255.0
    B = List[2]/255.0
    glColor3f(R,G,B)
    return [R,G,B]

#def draw_horizontal(X0,X1,Y0,Color):
#   oglcolor(Color)
#   glBegin(GL_LINE_STRIP)
#   glVertex2f(X0,Y0)
#   glVertex2f(X1,Y0)
#   glEnd()
##   print 'draw horizontal',X0,X1,Y0,Color

#def draw_vertical(X,Y0,Y1,Color):
#   oglcolor(Color)
#   glBegin(GL_LINE_STRIP)
#   glVertex2f(X,Y0)
#   glVertex2f(X,Y1)
#   glEnd()
#   print 'draw vert',X,Y1,Y0,Color
