


from pygameGeoms import setLineWidth,draw_line,draw_text,draw_circle,draw_arc,draw_fcircle,draw_frect,draw_rect,draw_dashed_line


def render_point(Matrix,Point,Color):
    X,Y = Point
    render_aline(Matrix,[(X-0.05,Y),(X+0.05,Y)],Color)
    render_aline(Matrix,[(X,Y-0.05),(X,Y+0.05)],Color)

def render_line(Matrix,Line,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    X0=Line[0][0]
    Y0=Line[0][1]
    for i in range(len(Line)-1):
        X1 =  X0 + Line[i+1][0]    
        Y1 =  Y0 + Line[i+1][1]    
        (X2,Y2) =  world_coord(Matrix,(X0,Y0))
        (X3,Y3) =  world_coord(Matrix,(X1,Y1))
        draw_line((X2,Y2),(X3,Y3),Color)
        X0=X1
        Y0=Y1

def render_dashed_aline(Matrix,Line,Color,Dash=10):
    setLineWidth(Glbs.get_context('lineWidth'))
    for i in range(len(Line)-1):
        P0 =  world_coord(Matrix,Line[i])
        P1 =  world_coord(Matrix,Line[i+1])
        draw_dashed_line(P0,P1,Color,Dash)

def render_aline(Matrix,Line,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    for i in range(len(Line)-1):
        P0 =  world_coord(Matrix,Line[i])
        P1 =  world_coord(Matrix,Line[i+1])
        draw_line(P0,P1,Color)

def render_circle(Matrix,Point0,Point1,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    X0,Y0 =  world_coord(Matrix,Point0)
    X1,Y1 =  world_coord(Matrix,Point1)
    Radii = max(abs(X0-X1),abs(Y0-Y1))
    draw_circle((X0,Y0),Radii,Color,1)
    return

def render_arc(Matrix,Point0,Point1,Point2,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    P0 =  world_coord(Matrix,Point0)
    P1 =  world_coord(Matrix,Point1)
    P2 =  world_coord(Matrix,Point2)
    print('arc %s %s %s %s'%(P0,P1,P2,Color))
    draw_arc(P0,P1,P2,Color)
    return


def render_fcircle(Matrix,Point0,Point1,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    X0,Y0 =  world_coord(Matrix,Point0)
    X1,Y1 =  world_coord(Matrix,Point1)
    draw_fcircle((X0,Y0),abs(X1-X0),Color)
    return


def render_text(Matrix,Text,XY,Rot,Size,Color,Align):
    if Glbs.get_context('useVectorText'):
        setLineWidth(Glbs.get_context('vectorTextWidth'))
        render_vector_text(Matrix,Text,XY,Rot,Size,Color,Align)
        return

    [A,A1,_,B1,B,_]=Matrix
    Min = min(abs(A),abs(B))
    if Min<0.1:
        Min = min(abs(A1),abs(B1))
    Size1 = 3*Min*Size
    P0 =  world_coord(Matrix,tuple(XY))
    draw_text(Text,P0[0],P0[1],Color,'left',Size1)

def signme(Dd):
    if Dd>0: return 1
    if Dd<0: return -1
    return 0

from drawVectorText import make_text_vectors
def render_vector_text(Matrix,Text,XY,Rot,Size,Color,Align):
    Big = make_text_vectors(Text,XY,Align,Size)
    for Seg in Big:
        P0 =  world_coord(Matrix,Seg[0])
        P1 =  world_coord(Matrix,Seg[1])
        draw_line(P0,P1,Color)




def render_frect(Matrix,Rect,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    X0,Y0 =  world_coord(Matrix,Rect[0])
    X1,Y1 =  world_coord(Matrix,Rect[1])
    draw_frect(X0,Y0,X1,Y1,Color)

def render_rect(Matrix,Rect,Color):
    setLineWidth(Glbs.get_context('lineWidth'))
    X0,Y0 =  world_coord(Matrix,Rect[0])
    X1,Y1 =  world_coord(Matrix,Rect[1])
    draw_rect(X0,Y0,X1,Y1,Color)




def compute_matrix(MatrixIn,Point,Rot):
    Matrix1 = translate_move(Point,MatrixIn)
    Matrix2 = translate_rotate(Rot,Matrix1)
    return Matrix2

def screen2schem(Point):
    Matrix=Glbs.get_context('matrix')
    Imatrix = matrix_inverse(Matrix)

#    After =  world_coord_fl(Imatrix,(Point[0],Glbs.height-Point[1]))
    After =  world_coord_fl(Imatrix,Point)
#    print('screen2schem screen=%s schem=%s'%(Point,After))
    return After

def schem2screen(Point):
    Matrix=Glbs.get_context('matrix')
    (X,Y)= world_coord(Matrix,Point)
    return (X,Y)

def world_coord_fl(Matrix,Point):
    [A,B,C,D,E,F] = Matrix
    (X0,Y0)=Point
    X1 = A*X0+B*Y0+C
    Y1 = D*X0+E*Y0+F
    return (X1,Y1)
def world_coord(Matrix,Point):
    [A,B,C,D,E,F] = Matrix
    if type(Point) is not tuple:
        return 0,0
    (X0,Y0)=Point
    X1 = int(A*X0+B*Y0+C)
    Y1 = int(D*X0+E*Y0+F)
    return (X1,Y1)

def artwork_coord(X,Y):
    Imatrix = Glbs.get_context('imatrix')
    [A,B,C,D,E,F] = Imatrix
    X1 = 1.0*(A*X+B*Y+C)
    Y1 = 1.0*(D*X+E*Y+F)
    X1 = grid_it(X1)
    Y1 = grid_it(Y1)
    return (X1,Y1)

def grid_it(Float):
    Grid = Glbs.get_context('grid')
    X = int((Float/Grid)+0.5)
    return Grid*X


def translate_mag(Mag,Matrix):
    [A1,B1,C1,D1,E1,F1] = Matrix  
    A2 = Mag * A1
    B2 = Mag * B1
    D2 = Mag * D1
    E2 = Mag * E1
    LLL = [A2,B2,C1,D2,E2,F1]
    return LLL
    
def translate_move(XY,Matrix):
    (X,Y) = XY
    return matrix_mult([1,0,X,0,1,Y],Matrix)

def translate_rotate(Rot,Matrix):
    [A1,B1,C1,D1,E1,F1] = Matrix  
    if (Rot[0]=='f'):
        A1 = -A1
        Rot=Rot[1:]
    if (Rot=='r0'):
        return [A1,B1,C1,D1,E1,F1]
    if (Rot=='r270'):
        A2 = 0 - B1
        B2 = A1
        D2 = 0 - E1
        E2 = D1
        return [A2,B2,C1,D2,E2,F1]
    if (Rot=='r180'):
        A2 = 0 - A1
        B2 = 0 - B1
        D2 = 0 - D1
        E2 = 0 - E1
        return [A2,B2,C1,D2,E2,F1]

    if (Rot=='r90'):
        A2 = B1
        B2 = 0 - A1
        D2 = E1
        E2 = 0 - D1
        return [A2,B2,C1,D2,E2,F1]

    if (Rot=='ry'):
        A2 = 0 - A1
        D2 = 0 - D1
        return [A2,B1,C1,D2,E1,F1]
    if (Rot=='rx'):
        B2 = 0 - B1
        E2 = 0 - E1
        return [A1,B2,C1,D1,E2,F1]
    print('rotation invalid "%s"'%Rot)
    return Matrix


def matrix_mult(Mat1,Mat2):
    [A1,B1,C1,D1,E1,F1] = Mat1
    [A2,B2,C2,D2,E2,F2] = Mat2
    A3 =  A1*A2+D1*B2
    B3 =  B1*A2+E1*B2
    C3 =  C1*A2+F1*B2+C2
    D3 =  A1*D2+D1*E2
    E3 =  B1*D2+E1*E2
    F3 =  C1*D2+F1*E2+F2
    return [A3,B3,C3,D3,E3,F3]



def matrix_inverse(Matrix):
    [A,B,C,D,E,F] = Matrix
    Denom = (A*E-B*D)
    if (Denom==0):
        return
    Ax =  (E / Denom)
    Bx =  -(B / Denom)
    Cx =  ((B*F-E*C) / Denom)
    Dx =  -(D / Denom)
    Ex =  (A / Denom)
    Fx =  ((D*C-F*A) / Denom)
    Inverse = [Ax,Bx,Cx,Dx,Ex,Fx]
    return Inverse



   



