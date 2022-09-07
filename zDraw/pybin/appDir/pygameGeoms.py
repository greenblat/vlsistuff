
import sys
# sys.path.append('/opt/homebrew/Cellar/pillow/8.2.0/lib/python3.9/site-packages')
import pygame
# from PIL import Image



def screenShot(Width,Height,Fname):
    print('screenShot "%s"  %dx%d'%(Fname,Width,Height))
    screen = Glbs.get_context('screen')
    pygame.image.save(screen, Fname)
#    glReadBuffer(GL_FRONT)
#    pixels = glReadPixels(0,0,Width,Height,GL_RGB,GL_UNSIGNED_BYTE)
#    image = Image.fromstring("RGB", (Width,Height), pixels)
#    image = image.transpose( Image.FLIP_TOP_BOTTOM)
#    image.save(Fname)




def fixCoord(Point):
    X = int(Point[0]/Glbs.wratio)
    Y = int(Point[1]/Glbs.hratio)
    return (X,Y)




glLineWidth = 1
def setLineWidth(Wid):
    global glLineWidth
    Glbs.set_context('lineWidth',Wid)
    glLineWidth = int(Wid)


def getLineWidth():
    global glLineWidth
    Wid = Glbs.get_context('lineWidth')
    glLineWidth = int(Wid)




def draw_segment(P0,P1):
   P0 = fixCoord(P0)
   P1 = fixCoord(P1)
   draw_line(P0,P1,'black')

def draw_dashed_line(P0,P1,Color,dash_length=10):
    P0f = fixCoord(P0)
    P1f = fixCoord(P1)
    Color = oglcolor(Color)
    Screen = Glbs.get_context('screen')

    x1, y1 = P0f
    x2, y2 = P1f
    dl = dash_length

    if (x1 == x2):
        ycoords = [y for y in range(y1, y2, dl if y1 < y2 else -dl)]
        xcoords = [x1] * len(ycoords)
    elif (y1 == y2):
        xcoords = [x for x in range(x1, x2, dl if x1 < x2 else -dl)]
        ycoords = [y1] * len(xcoords)
    else:
        a = abs(x2 - x1)
        b = abs(y2 - y1)
        c = round(math.sqrt(a**2 + b**2))
        dx = dl * a / c
        dy = dl * b / c

#        xcoords = [x for x in numpy.arange(x1, x2, dx if x1 < x2 else -dx)]
#        ycoords = [y for y in numpy.arange(y1, y2, dy if y1 < y2 else -dy)]

    next_coords = list(zip(xcoords[1::2], ycoords[1::2]))
    last_coords = list(zip(xcoords[0::2], ycoords[0::2]))
    for (x1, y1), (x2, y2) in zip(next_coords, last_coords):
        start = (round(x1), round(y1))
        end = (round(x2), round(y2))
        pygame.draw.line(Screen, Color, start, end, glLineWidth)






def draw_line(P0,P1,Color):
    getLineWidth()
    P0f = fixCoord(P0)
    P1f = fixCoord(P1)
    Color = oglcolor(Color)
    Screen = Glbs.get_context('screen')
    pygame.draw.line(Screen,Color,P0f,P1f,glLineWidth)

def draw_long_line(Points,Color):
    Color = oglcolor(Color)
    Screen = Glbs.get_context('screen')
    getLineWidth()
    pygame.draw.lines(Screen,Color,False,Points,glLineWidth)


def draw_frect(X0,Y0,X1,Y1,Color):
    oglcolor(Color)
    (X0,Y0) = fixCoord((X0,Y0))
    (X1,Y1) = fixCoord((X1,Y1))
    Screen = Glbs.get_context('screen')
    getLineWidth()
    pygame.draw.lines(Screen,Color,True,Points,glLineWidth)

def draw_rect(X0,Y0,X1,Y1,Color):
    oglcolor(Color)
    glBegin(GL_LINE_STRIP)
    (X0,Y0) = fixCoord((X0,Y0))
    (X1,Y1) = fixCoord((X1,Y1))
    Screen = Glbs.get_context('screen')
    getLineWidth()
    pygame.draw.lines(Screen,Color,Points,glLineWidth)

def draw_xcircle(P0,Radii,Color):
    draw_circle(P0,Radii,Color,1)

def draw_fcircle(P0,Radii,Color):
    draw_circle(P0,Radii,Color,0)

def draw_circle(P0,Radii,Color,Width):
    (Radii,Radii0) = fixCoord((Radii,Radii))
    P0 = fixCoord(P0)
    Color = oglcolor(Color)
    Screen = Glbs.get_context('screen')
    pygame.draw.circle(Screen,Color,P0,Radii,Width)


def draw_arc(P0,P1,P2,Color):
    return


def draw_horizontal(X0,X1,Y0,Color):
   draw_line((X0,Y0),(X1,Y0),Color)

def draw_vertical(X,Y0,Y1,Color):
   draw_line((X,Y0),(X,Y1),Color)


def draw_text(Text,X,Y,Color,AnchorX='left',FontSize=36):
#    XXYY = (X,Y)
    (X,Y) = fixCoord((X,Y))
    Font  = Glbs.get_context('font')
    font = pygame.font.SysFont(Font, int(FontSize))
    Color = oglcolor(Color)
#    print('DRAWLABEL %s %d %d color=%s font=%s  "%s"' % (XXYY,X,Y,Color,font,Text))
    text = font.render(Text, True, Color, (255,255,255))
    textRect = text.get_rect()
    textRect.bottomleft = (X,Y)
    Screen = Glbs.get_context('screen')
    Screen.blit(text, textRect)

def draw_label(Text,X,Y,Color,AnchorX='left',FontSize=12):
#    XXYY = (X,Y)
    (X,Y) = fixCoord((X,Y))
    font = pygame.font.SysFont('times.ttf', int(FontSize))
    Color = oglcolor(Color)
#    print('DRAWLABEL %s %d %d color=%s font=%s  "%s"' % (XXYY,X,Y,Color,font,Text))
    text = font.render(Text, True, Color, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (Glbs.get_context('width') // 2, Y // 2)
    Screen = Glbs.get_context('screen')
    Screen.blit(text, textRect)

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
    if type(Color) is str:
        List = xglcolor(Color)
    else:
        List = Color
    R = List[0]
    G = List[1]
    B = List[2]

    return [R,G,B]

#def draw_horizontal(X0,X1,Y0,Color):
#   oglcolor(Color)
#   glBegin(GL_LINE_STRIP)
#   glVertex2f(X0,Y0)
#   glVertex2f(X1,Y0)
#   glEnd()

#def draw_vertical(X,Y0,Y1,Color):
#   oglcolor(Color)
#   glBegin(GL_LINE_STRIP)
#   glVertex2f(X,Y0)
#   glVertex2f(X,Y1)
#   glEnd()
