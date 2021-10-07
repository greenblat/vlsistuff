

import os,sys,math,copy
from renders import screen2schem,schem2screen

from drawVectorText import make_text_vectors
from pygameGeoms import screenShot
import helpString
import logs

UnitMatrix = [1,0,0,0,1,0]

RED_COLOR=[255,0,0]
INSTANCE_COLOR=[150,150,0]
defaultPicTextSize = 0.15

def get_context(Param,Default=None):
    if Param in Glbs.contexts:
        return Glbs.contexts[Param]
    if (Default!=None):
        set_context(Param,Default)
        return Default

def set_context(Param,Value):
    Glbs.contexts[Param]=Value
    if (Param=='matrix'):
        Imatrix = matrix_inverse(Value)
        set_context('imatrix',Imatrix)
        recompute_proximity()
    if (Param=='state')and(Value=='idle'):
        Glbs.set_context('banner',Glbs.Banner)
def unset_context(Param):
    if Param in Glbs.contexts:
        Glbs.contexts.pop(Param)

from renders import matrix_inverse
from schem import PICTURES

def init():
    set_context('screen_proximity',10.0)
    set_context('matrix',[1,0,0,0,1,0])
    set_context('pics_lib','.')
    set_context('linewidth',1)
    set_context('state','idle')
    set_context('wire_color',[0,255,0])
    set_context('pic_color',[255,255,0])
    set_context('param_color',[0,150,150])
    set_context('geom_color',[0,0,255])
    set_context('instance_color',INSTANCE_COLOR)
    set_context('root',False)
    set_context('view',False)
    set_context('width',WID)
    set_context('height',HEI)
    set_context('redraw',True)
    set_context('proximity',0.2)
    set_context('printer_box',[1000,1000])
    set_context('pic_text_size',defaultPicTextSize)
    set_context('param_text_size',0)
    set_context('geom_text_size',1.0)
    set_context('banner','iDraw: greenblat@mac.com +972-54-4927322')
    set_context('grid',0.5)
    set_context('shyParams',['name','size'])
    set_context('lineWidth',1.5)
    set_context('vectorTextWidth',1.0)
    state='idle'
    lines = PICTURES.split('\n')
    Mod=False
    for  line in lines:
        state,Mod=work_on_line(line,state,Mod)


def recompute_proximity():
    Sprox = get_context('screen_proximity')
    X0,Y0 = screen2schem((0,0))
    X1,Y1 = screen2schem((Sprox,Sprox))
    Prox = min(abs(X0-X1),abs(Y0-Y1))
    if (Prox<0.1):
        Prox=0.1
    set_context('proximity',Prox)


def pdraw_current():
    Root=get_context('root')
    Matrix = Glbs.details[Root].get_matrix()
    set_context('matrix',Matrix)
    Glbs.details[Root].draw(Matrix)
    if (Glbs.details[Root].is_touched=='Q'):
        render_text(UnitMatrix,'Dont You want to save first? (another Q will exit)',(100,100),'r0',5,RED_COLOR,'left')
        Glbs.details[Root].touched(False)

from postscript import *
from svgClass import svgClass
def postscript_current():
    Root=get_context('root')
    File = open('%s.ps'%Root,'w')
    logs.log_info('writing postscript file "%s.ps"'%Root)
    sizeX,sizeY,Scale = postscript_opening(File,Glbs.details[Root])
    [(Xl,Yl),(Xh,Yh)]=Glbs.details[Root].bbox()
    Svg  = svgClass('%s.svg'%Root,False)
    Svg.open(sizeX,sizeY,Scale,Xl,Yl,Xh,Yh)
    Glbs.Svg = Svg
    Glbs.details[Root].postscript(File)
    postscript_closing(File)
    Svg.close()
    File.close()

from renders import render_line, render_aline,render_circle,render_text,compute_matrix,translate_mag,translate_rotate,translate_move,matrix_mult,render_fcircle,render_arc,world_coord_fl,world_coord,render_frect,render_rect




class InstanceClass:
    def __init__(self,Father,Type,Inst,Point=(0,0),Rot='r0'):
        self.Father=Father
        self.Type=Type
        self.Inst=Inst
        self.Point=Point
        self.Rot=Rot
        self.Mag=1.0
        self.bbox0=False
        self.selected=False

    def origin(self):
        return self.Point
    def make_selected(self,What):
        self.selected=What

    def draw(self,Matrix):
        Mat0 = translate_mag(self.Mag,UnitMatrix)
        Mat1 = translate_move(self.Point,Mat0)
        Mat2 = translate_rotate(self.Rot,Mat1)
        Mat3 = matrix_mult(Mat2,Matrix)
        if self.selected:
            Color=RED_COLOR
        else:
            Color = get_context('instance_color')
        if self.Type in Glbs.pictures:
            Glbs.pictures[self.Type].draw(Mat3,Color)
        elif Glbs.try_load_picture(self.Type):
            Glbs.pictures[self.Type].draw(Mat3,Color)
        else:
            logs.log_error('no picture of %s'%self.Type)
        if self.Father.drawBoxes:
            Bbox = self.bbox()
            X0,Y0=Bbox[0]
            X1,Y1=Bbox[1]
            List = [(X0,Y0),(X0,Y1),(X1,Y1),(X1,Y0),(X0,Y0)]
            render_aline(Matrix,List,get_context('geom_color'))


    def postscript(self,File):
        Color = get_context('instance_color')
        Mat3 = instmatrix(self.Mag,self.Point,self.Rot,UnitMatrix)
        if self.Type in Glbs.pictures:
            Glbs.pictures[self.Type].postscript(File,Mat3,Color)



    def save(self,File):
        File.write('inst %s %s xy=%.1f,%.1f'%(self.Type,self.Inst,self.Point[0],self.Point[1]))
        if (self.Rot!='r0'):
            File.write(' rot=%s'%self.Rot)
        File.write('\n')

    def bbox(self):
        if (self.bbox0): 
            return self.bbox0
        if self.Type not in Glbs.pictures:
            Ok = Glbs.try_load_picture(self.Type)
            if Ok:
                return self.bbox()
            else:
                logs.log_error('could not bbox "%s". using some default'%(self.Type))
                self.bbox0 = [self.Point,(self.Point[0]+1,self.Point[1]+1)]
                return self.bbox0
        self.bbox0=[self.Point,self.Point]
        BB = Glbs.pictures[self.Type].bbox()
        Mat0 = translate_mag(self.Mag,UnitMatrix)
        Mat1 = translate_move(self.Point,Mat0)
        Mat2 = translate_rotate(self.Rot,Mat1)
        P0 = world_coord_fl(Mat2,BB[0])
        P1 = world_coord_fl(Mat2,BB[1])
        BB0 = merge_bbox([P0,P0],[P1,P1])
        self.bbox0=merge_bbox(self.bbox0,BB0)
        return self.bbox0

    def move(self,Dx,Dy):
        X0 = grid_it(self.Point[0])
        Y0 = grid_it(self.Point[1])
        X1 = X0+Dx
        Y1 = Y0+Dy
        X2,Y2 = putOnGrid((X1,Y1))
        self.Point = X2,Y2
        self.bbox0=False
        self.recompute_wires()
        Root=get_context('root')
        for Key in Glbs.details[Root].params:
            if Glbs.details[Root].params[Key].Owner==self.Inst:
                Glbs.details[Root].params[Key].move(Dx,Dy)

    def rotate(self,What):
        NewRot = merge_rot(self.Rot,What)
        self.Rot=NewRot
        self.bbox0=False
        self.recompute_wires()


    def it_is_me(self,Wire):
        ww = Wire.split('.')
        return ww[0]==self.Inst
        
    def recompute_wires(self):
        for Wire in self.Father.wires:
            WW = self.Father.wires[Wire]
            Start=WW.Start
            if self.it_is_me(Start):
                X,Y = get_pin_location(self.Father.Module,Start)
                self.Father.wires[Wire].List = [(X,Y)]+self.Father.wires[Wire].List[1:]
#                self.Father.wires[Wire].List =[]
            End=WW.End
            if self.it_is_me(End):
                X,Y = get_pin_location(self.Father.Module,End)
                self.Father.wires[Wire].List.pop(-1)
                self.Father.wires[Wire].List.append((X,Y))
#                self.Father.wires[Wire].List =[]
        

class WireClass:
    def __init__(self,Father,Name,Start,End,List):
        self.Name=Name
        self.Father=Father
        self.Start=Start
        self.End=End
        self.List=List[:]
        self.bbox0=False
        self.selected=False

    def make_selected(self,What):
        self.selected=What

    def get_wire_list(self):
        if (self.List==[]):
            P0=get_pin_location(self.Father.Module,self.Start)
            P1=get_pin_location(self.Father.Module,self.End)
            self.List=[P0,P1]
        return self.List

    def origin(self):
        L = self.get_wire_list()
        return L[0]

    def draw(self,Matrix):
        self.get_wire_list()
        if self.selected:
            Color=RED_COLOR
        else:
            Color=get_context('wire_color')
        render_aline(Matrix,self.List,Color)

    def postscript(self,File):
        self.get_wire_list()
        postscript_aline(File,self.List,get_context('wire_color'))
        Glbs.Svg.x_aline(self.List,get_context('wire_color'))


    def save(self,File):
        File.write('wire %s %s %s '%(self.Name,self.Start,self.End))
        if (self.List!=[]):
            File.write('list=%.1f,%.1f'%(self.List[0][0],self.List[0][1]))
            for (X,Y) in self.List[1:]:
                File.write(',%.1f,%.1f'%(X,Y))
        File.write('\n')
        return

    def bbox(self):
        if self.bbox0:
            return self.bbox0
        List = self.get_wire_list()
        self.bbox0 = bbox_aline(List)
        return self.bbox0

class GeomClass:
    def __init__(self,Kind,Name,List,Rot):
        self.Name=Name
        self.Kind=Kind
        self.List=List[:]
        self.bbox0=False
        self.Rot=Rot
        self.selected=False

    def origin(self):
        return self.List[0]
    def draw(self,Matrix):
        if (self.Kind=='line'):
            render_aline(Matrix,self.List,get_context('geom_color'))
        elif (self.Kind=='rect'):
            X0,Y0=self.List[0]
            X1,Y1=self.List[1]
            List = [(X0,Y0),(X0,Y1),(X1,Y1),(X1,Y0),(X0,Y0)]
            render_aline(Matrix,List,get_context('geom_color'))
        elif (self.Kind=='frect'):
            render_frect(Matrix,self.List,get_context('geom_color'))
        elif (self.Kind=='circle'):
            render_circle(Matrix,self.List[0],self.List[1],get_context('geom_color'))
        elif (self.Kind=='fcircle'):
            render_fcircle(Matrix,self.List[0],self.List[1],get_context('geom_color'))
        elif (self.Kind=='text'):
            NN = self.Name.replace('|',' ')
            Color = get_context('geom_color')
            if self.selected:
                Color='red'
            Mat3 = instmatrix(1,self.List[0],self.Rot,Matrix)
            render_text(Mat3,NN,[0,0],'r0',get_context('geom_text_size'),Color,'left')
        else:
            logs.log_error('unknown geom kind = %s'%(self.Kind))
        if self.Father.drawBoxes:
            Bbox = self.bbox()
            X0,Y0=Bbox[0]
            X1,Y1=Bbox[1]
            List = [(X0,Y0),(X0,Y1),(X1,Y1),(X1,Y0),(X0,Y0)]
            render_aline(Matrix,List,get_context('geom_color'))

    def postscript(self,File):
        if (self.Kind=='line'):
            postscript_aline(File,self.List,get_context('wire_color'))
            Glbs.Svg.x_aline(self.List,get_context('wire_color'))
        else:
            NN = self.Name.replace('|',' ')
            set_pscontext(File,'setrgbcolor',get_context('geom_color'))
            Big = make_text_vectors(NN,self.List[0],'left',get_context('geom_text_size'))
            for Seg in Big:
                postscript_aline(File,Seg,False)
                Glbs.Svg.x_aline(Seg,False)

    def bbox(self):
        if self.bbox0:
            return self.bbox0
        elif self.Kind in ['line','rect']:
            self.bbox0 = bbox_aline(self.List)
        elif self.Kind in ['text']:
            self.bbox0=[self.List[0],(self.List[0][0]+0.5,self.List[0][1]+0.5)]
        else:
            logs.log_error('bbox failed on geom %s %s'%(self.Kind,self.Name))
            self.bbox0=[(0,0),(1,1)]
        return self.bbox0
    def move(self,Dx,Dy):
        for ind,(X,Y) in enumerate(self.List):
            self.List[ind]= (self.List[ind][0]+Dx,self.List[ind][1]+Dy)
        self.bbox0=False

    def save(self,File):
        File.write('geom %s %s '%(self.Kind,self.Name))
        if (self.List!=[]):
            File.write('list=%.1f,%.1f'%(self.List[0][0],self.List[0][1]))
            for (X,Y) in self.List[1:]:
                File.write(',%.1f,%.1f'%(X,Y))
        File.write(' rot=%s\n' % self.Rot)
        return

    def rotate(self,What):
        NewRot = merge_rot(self.Rot,What)
        self.Rot=NewRot

    def make_selected(self,What):
        self.selected=What

class ParamClass:
    def __init__(self,Father,Owner,Param,Value,Point=(0,0),Rot='r0'):
        self.Father=Father
        self.Owner=Owner
        self.Param=Param
        self.Value=Value
        self.Point=Point
        self.Rot=Rot
        self.bbox0=False
        self.Size=0.3
        self.selected=False

    def draw(self,Matrix):
        if (self.selected):
            Color=RED_COLOR
            (_,Owner)=self.Father.find_owner(self.Owner)
            if (Owner):
                P2 = Owner.origin()
                render_aline(Matrix,[self.Point,P2],RED_COLOR)
            else:
                logs.log_error('orphan param %s, orphan of %s'%(self.Param,self.Owner))
        else:
            Color = get_context('param_color')
        PrmSize = Glbs.get_context('param_text_size')
        if PrmSize==0:
            PrmSize=self.Size
#        Mat2 = translate_rotate(self.Rot,UnitMatrix)
#        Mat3 = matrix_mult(Mat2,Matrix)
        Mat3 = instmatrix(1,self.Point,self.Rot,Matrix)
        if self.Param in Glbs.get_context('shyParams') and Glbs.useShyParams:
            if (self.Param=='name')and(self.Value=='$inst'):
                Value = self.Owner
            else:
                Value = self.Value
            render_text(Mat3,Value,[0,0],'r0',PrmSize,Color,'left')
        else:
            render_text(Mat3,'%s=%s'%(self.Param,self.Value),[0,0],'r0',PrmSize,Color,'left')
        if self.Father.drawBoxes:
            Bbox = self.bbox()
            X0,Y0=Bbox[0]
            X1,Y1=Bbox[1]
            List = [(X0,Y0),(X0,Y1),(X1,Y1),(X1,Y0),(X0,Y0)]
            render_aline(Mat3,List,get_context('geom_color'))


    def postscript(self,File):
        PrmSize = Glbs.get_context('param_text_size')
        if PrmSize==0:
            PrmSize=self.Size
        if (self.Param=='name')and(self.Value=='$inst'):
            Value = self.Owner
        else:
            Value = self.Value

        Mat3 = instmatrix(1,self.Point,self.Rot,UnitMatrix)
#        Mat4 = instmatrix(1,self.Point,self.Rot,Matrix)
#        Mat5 = instmatrix(1,[0,0],self.Rot,UnitMatrix)
        if Glbs.useVectorText:
            set_pscontext(File,'setrgbcolor',get_context('param_color'))
            Big = make_text_vectors(Value,[0,0],'left',PrmSize)
            for Seg in Big:
                Line2 = translate_aline(Mat3,Seg)
                postscript_aline(File,Line2,'red')
#                Line2 = translate_aline(UnitMatrix,Seg)
#                postscript_aline(File,Line2,False)
                Glbs.Svg.x_aline(Line2)
        else:
            postscript_text(File,Value,self.Point,self.Rot,get_context('param_color'),PrmSize)

    def bbox(self):
        if self.bbox0:
            return self.bbox0
        if self.Father.matrix: 
            Mult = self.Father.matrix[0]
        else:
            Mult = 10.0
        Size = 1.0*self.Size/Mult
        self.bbox0=[self.Point,(self.Point[0]+(Size*len(self.Value))/3,self.Point[1]+Size)]
        return self.bbox0
    def save(self,File):
        File.write('param %s %s %s xy=%.1f,%.1f rot=%s\n'%(self.Owner,self.Param,self.Value,self.Point[0],self.Point[1],self.Rot))
        return
    def make_selected(self,What):
        self.selected=What
    def move(self,Dx,Dy):
        self.Point = self.Point[0]+Dx,self.Point[1]+Dy
        self.bbox0=False

    def rotate(self,What):
        NewRot = merge_rot(self.Rot,What)
        print('>>>>>> %s %s %s %s' % (self.Rot,NewRot,self.Owner,self.Param))
        self.Rot=NewRot
        self.bbox0=False


class PictureClass:
    def __init__(self,Picture,Pins=[],Alines=[],Lines=[],Texts=[]):
        self.Picture=Picture
        self.alines=Alines[:]
        self.lines=Lines[:]
        self.subs=[]
        self.pins={}
        self.circles=[]
        self.fcircles=[]
        self.props={}
        self.geoms=[]
        self.texts=Texts[:]
        self.bbox0=False
        for (Pin,Dir,XY) in Pins:
            self.pins[Pin]=(Dir,XY)
    def draw(self,Matrix,Color='none'):
        if Color=='none':    
            Color = get_context('pic_color')
        for Aline in self.alines:
            render_aline(Matrix,Aline,Color)
        for Line in self.lines:
            render_line(Matrix,Line,Color)
        for (Text,Point,Rot,Size,Align) in self.texts:
            render_text(Matrix,Text,Point,Rot,Size,Color,Align)
        for ((X0,Y0),(X1,Y1)) in self.circles:
            render_circle(Matrix,(X0,Y0),(X1,Y1),Color)
        for ((X0,Y0),(X1,Y1)) in self.fcircles:
            render_fcircle(Matrix,(X0,Y0),(X1,Y1),Color)
        for (Sub,Point) in self.subs:
            Matrix2 = compute_matrix(Matrix,Point,'r0')
            Glbs.pictures[Sub].draw(Matrix2,Color)
        for (Which,List) in self.geoms:
            if (Which=='circle'):
                render_circle(Matrix,List[0],List[1],Color)
            elif (Which=='fcircle'):
                render_fcircle(Matrix,List[0],List[1],Color)
            elif (Which=='arc'):
                Aline = arc2aline(List[1],List[0],List[2])
                render_aline(Matrix,Aline,Color)
            elif (Which=='uarc'):
                Cx = (List[0][0]+List[1][0])/2
                Cy = (List[0][1]+List[1][1])/2

                Aline = arc2aline((Cx,Cy),List[1],List[0])
                render_aline(Matrix,Aline,Color)
            elif (Which=='darc'):
                Cx = (List[0][0]+List[1][0])/2
                Cy = (List[0][1]+List[1][1])/2
                Aline = arc2aline((Cx,Cy),List[1],List[0])
                Aline=[]
                render_aline(Matrix,Aline,Color)
            elif (Which=='aline'):
                render_aline(Matrix,List,Color)
            else:
                logs.log_error('missing pygame pic geom %s in %s'%(Which,self.Picture))
    def postscript(self,File,Matrix,Color):
        if Color=='none':    
            Color = get_context('pic_color')
        for Aline in self.alines:
            Line2 = translate_aline(Matrix,Aline)
            postscript_aline(File,Line2,Color)
            Glbs.Svg.x_aline(Line2,Color)
        for Line in self.lines:
            Line2 = translate_line(Matrix,Line)
            postscript_aline(File,Line2,Color)
            Glbs.Svg.x_aline(Line2,Color)
        for ((X0,Y0),(X1,Y1)) in self.circles:
            Line2 = translate_aline(Matrix,[(X0,Y0),(X1,Y1)])
            postscript_circle(File,Line2[0],Line2[1],Color)
            Glbs.Svg.x_circle(Line2[0],Line2[1],Color)
        for ((X0,Y0),(X1,Y1)) in self.fcircles:
            Line2 = translate_aline(Matrix,[(X0,Y0),(X1,Y1)])
            postscript_fcircle(File,Line2[0],Line2[1],Color)
            Glbs.Svg.x_fcircle(Line2[0],Line2[1],Color)
        for (Sub,Point) in self.subs:
            Matrix2 = compute_matrix(Matrix,Point,'r0')
            Glbs.pictures[Sub].postscript(File,Matrix2,Color)
        for (Which,List) in self.geoms:
            if Which=='aline':
                Line2 = translate_aline(Matrix,List)
                postscript_aline(File,Line2,Color)
                Glbs.Svg.x_aline(Line2,Color)
            elif (Which=='arc'):
                Aline = arc2aline(List[1],List[0],List[2])
                Line2 = translate_aline(Matrix,Aline)
                postscript_aline(File,Line2,Color)
                Glbs.Svg.x_aline(Line2,Color)
            else:
                logs.log_error('missing postscript pic geom %s in %s'%(Which,self.Picture))

        for (Text,Point,Rot,Size,Align) in self.texts:
            if Glbs.useVectorText:
                NN = Text.replace('|',' ')
                set_pscontext(File,'setrgbcolor',Color)
                Big = make_text_vectors(NN,Point,Align,Size)
                for Seg in Big:
                    Line2 = translate_aline(Matrix,Seg)
                    postscript_aline(File,Line2,False)
                    Glbs.Svg.x_aline(Line2,Color)
            else:
                P0 =  world_coord_fl(Matrix,Point)
                postscript_text(File,Text,P0,'fr0',Color,Size)


    def bbox(self):
        if (self.bbox0):
            return self.bbox0
        for Line in self.lines:
            BB = bbox_line(Line)
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,BB)
            else:
                self.bbox0=BB
        for Aline in self.alines:
            BB = bbox_aline(Aline)
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,BB)
            else:
                self.bbox0=BB
        for Pin in self.pins:
            (_,XY)=self.pins[Pin]
            BB=[XY,XY]
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,BB)
            else:
                self.bbox0=BB
        for S0 in self.subs:
            (Sub,(Xm,Ym))=S0
            BB0 = Glbs.pictures[Sub].bbox()
            [(X0,Y0),(X1,Y1)]=BB0
            BB1 = [(X0+Xm,Y0+Ym),(X1+Xm,Y1+Ym)]
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,BB1)
            else:
                self.bbox0=BB1
        for ((X0,Y0),(X1,Y1)) in self.circles+self.fcircles:
            Radii = max(abs(X0-X1),abs(Y0-Y1))
            BB = [((X0-Radii),(Y0-Radii)),((X0+Radii),(Y0+Radii))]
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,BB)
            else:
                self.bbox0=BB
        for _,XY,_,_,_ in self.texts:
            if (self.bbox0):
                self.bbox0=merge_bbox(self.bbox0,[XY,XY])
            else:
                self.bbox0=[XY,XY]
            
             


        if (not self.bbox0):
            logs.log_error('picture %s failed to build bbox'%(self.Picture))
            self.bbox0=[(-1,-1),(1,1)]
        return self.bbox0

    def add_aline(self,Aline):
        self.alines.append(Aline)
    def add_line(self,Line):
        self.lines.append(Line)
    def add_circle(self,Line):
        self.circles.append(Line)
    def add_fcircle(self,Line):
        self.fcircles.append(Line)
    def add_text(self,Text,XY,Rot,Size=defaultPicTextSize,Align='left'):
        self.texts.append((Text,XY,Rot,Size,Align))
    def add_pin(self,Pin,Dir,XY):
        self.pins[Pin]=(Dir,XY)
    def add_pic_prop(self,Prop,XY):
        self.props[Prop]=XY
    def add_pic_sub(self,Sub,XY):
        self.subs.append((Sub,XY))
    def add_pic_geom(self,Which,XY):
        self.geoms.append((Which,XY))



class DetailClass:
    def __init__(self,Module):
        self.Module=Module
        self.params={}
        self.wires={}
        self.instances={}
        self.geoms={}
        self.bbox0=False
        self.matrix=False
        self.is_touched=False
        self.drawBoxes=False

    def copy(self):
        Copy = DetailClass(self.Module)
        Copy.bbox0 = self.bbox0
        Copy.matrix = self.matrix
        Copy.is_touched = False
        Copy.drawBoxes =  False
        Copy.params = copy.deepcopy(self.params)
        Copy.wires = copy.deepcopy(self.wires)
        Copy.instances = copy.deepcopy(self.instances)
        Copy.geoms = copy.deepcopy(self.geoms)
        return Copy

    def isDiff(self,Other):
        if self.params != Other.params: return True
        if self.wires != Other.wires: return True
        if self.instances != Other.instances: return True
        if self.geoms != Other.geoms: return True
        return False

    def touched(self,What):
        self.is_touched=What
        if What: Glbs.graphicsChanged=True
        if What: self.bbox0=False

    def add_instance(self,Type,Inst,Point=(0,0),Rot='r0'):
        self.instances[Inst]=InstanceClass(self,Type,Inst,Point,Rot)
        return self.instances[Inst]

    def add_geom(self,Kind,Name,List,Rot='r0'):
        self.geoms[Name]=GeomClass(Kind,Name,List,Rot)
        self.geoms[Name].Father=self

    def add_param(self,Owner,Param,Value,Point=(0,0),Rot='r0'):
        Key = '%s %s'%(Owner,Param)
        self.params[Key]=ParamClass(self,Owner,Param,Value,Point,Rot)
    def add_wire(self,Name,Start,Stop,List):
        self.wires[Name]=WireClass(self,Name,Start,Stop,List)

    def draw(self,Matrix):
        for Inst in self.instances:
            self.instances[Inst].draw(Matrix)
        for Name in self.geoms:
            self.geoms[Name].draw(Matrix)
        for Wire in self.wires:
            self.wires[Wire].draw(Matrix)
        for Key in self.params:
            self.params[Key].draw(Matrix)

    def nodesStats(self):
        self.NODES = {}
        for Wire in self.wires:
            Start = self.wires[Wire].Start
            End = self.wires[Wire].End
            if Start not in self.NODES: self.NODES[Start] = 0
            if End   not in self.NODES: self.NODES[End] = 0
            self.NODES[Start] += 1
            self.NODES[End] += 1

    def postscript(self,File):
        self.nodesStats()
        for Inst in self.instances:
            if (Inst in self.NODES) and (self.instances[Inst].Type == 'node')and(self.NODES[Inst] == 2):
                pass
            else:
                self.instances[Inst].postscript(File)
        for Name in self.geoms:
            self.geoms[Name].postscript(File)
        for Wire in self.wires:
            self.wires[Wire].postscript(File)
        for Key in self.params:
            self.params[Key].postscript(File)



    def find_owner(self,Inst):
        if Inst in self.instances:
            return 'inst',self.instances[Inst]
        if Inst in self.geoms:
            return 'geom',self.geoms[Inst]
        return False,False


    def bbox(self):
        if (self.bbox0):
            return self.bbox0
        for Inst in self.instances:
            BB = self.instances[Inst].bbox()
            self.update_bbox(BB)
        for Name in self.geoms:
            BB=self.geoms[Name].bbox()
            self.update_bbox(BB)
        for Wire in self.wires:
            BB=self.wires[Wire].bbox()
            self.update_bbox(BB)
        for Key in self.params:
            BB=self.params[Key].bbox()
            self.update_bbox(BB)
        if not self.bbox0:
            self.bbox0=[(0,0),(20,20)]
        return self.bbox0

    def get_matrix(self):
        if self.matrix:
            return self.matrix
        BB = self.bbox()
        (X0,Y0)=BB[0]
        (X1,Y1)=BB[1]
        if (X1==X0):
            Scalex=100
        else:
            Scalex = 0.90 * get_context('width')/(X1-X0)
        if (Y1==Y0):
            Scaley=100
        else:
            Scaley = 0.90 * get_context('height')/(Y1-Y0)
        Scale = min(Scalex,Scaley)
        Yoff = min(Y0,Y1)*Scale
        self.matrix = [Scale,0,-X0*Scale,0,-Scale,Yoff+get_context('height')]
        return self.matrix

    def set_matrix(self,Matrix):
        self.matrix=Matrix

    def invent_inst_name(self,Type):
        Key = self.Module+'_instance_of_'+Type
        InstI = get_context(Key,0)
        set_context(Key,InstI+1)
        Inst = '%s_%d'%(Type,InstI)
        if Inst in self.instances:
            return self.invent_inst_name(Type)
        return Inst

    def update_bbox(self,Bbox):
        if not Bbox:
            return
        if not self.bbox0:
            self.bbox0=Bbox[:]
            return

        [(X0,Y0),(X1,Y1)]=self.bbox0
        [(X2,Y2),(X3,Y3)]=Bbox
        self.bbox0= [(min(X0,X2),min(Y0,Y2)),(max(X1,X3),max(Y1,Y3))]

    def save(self,File):
        File.write('schematic %s\n'%self.Module)
        for Inst in self.instances:
            self.instances[Inst].save(File)
        for Name in self.geoms:
            self.geoms[Name].save(File)
        for Wire in self.wires:
            self.wires[Wire].save(File)
        for Key in self.params:
            self.params[Key].save(File)
        File.write('end\n')
        self.touched(False)

    def where_inst(self,Inst):
        if Inst not in self.instances:
            logs.log_error('unknown instance %s'%(Inst))
            return
        P0 = self.instances[Inst].Point
        return P0

    def where_pin(self,Inst,Pin):
        if Inst not in self.instances:
            logs.log_error('unknown instance %s'%(Inst))
            return
        P0 = self.instances[Inst].Point
        Rot = self.instances[Inst].Rot
        Type = self.instances[Inst].Type
        Mag = self.instances[Inst].Mag
            
        Mat0 = translate_mag(Mag,UnitMatrix)
        Mat1 = translate_move(P0,Mat0)
        Mat2 = translate_rotate(Rot,Mat1)

        if Type not in Glbs.pictures:
            Glbs.try_load_picture(Type)

        if Type in Glbs.pictures:
            if Pin in Glbs.pictures[Type].pins:
                (_,P0)=Glbs.pictures[Type].pins[Pin]
                P1 = world_coord_fl(Mat2,P0)
                return P1
            else:
                logs.log_error('no pin %s picture of %s'%(Pin,Type))
                return (0,0)
        else:
            logs.log_error('no picture of %s'%Type)
            return (0,0)

    def select_pin(self,ScrPoint):
        Point = screen2schem(ScrPoint)
        for Inst in self.instances:
            BB=self.instances[Inst].bbox()
            if close_enough(BB,Point):
                Type = self.instances[Inst].Type
                Pic = Glbs.pictures[Type]
                if (list(Pic.pins.keys())==[]):
                    return Inst,self.instances[Inst].Point
                Closest,Best = -1,0
                Pnt=False
                for Pin in Pic.pins:
                    Px = self.where_pin(Inst,Pin)
                    Dist = distance(Px,Point)
                    if (Closest<0):
                        Closest,Best=Dist,Pin
                        Pnt = Px
                    elif (Dist<Closest):
                        Closest,Best=Dist,Pin
                        Pnt = Px
                print('CLOSE',Pic.pins,Inst,Best,Pnt)
                if Best == 0:
                    return Inst,Pnt
                return Inst+'.'+Best,Pnt

        for Wire in self.wires:
            List = self.wires[Wire].get_wire_list()
            for i in range(0,len(List)-1):
                if point_close_to_section(Point,List[i],List[i+1]):
                    Pnew = point_on_section(Point,List[i],List[i+1])
                    Root=get_context('root')
                    Nnst = Glbs.details[Root].invent_inst_name('node')
                    Pnew = putOnGrid(Pnew)
                    Glbs.details[Root].add_instance('node',Nnst,Pnew)
                    Stop = self.wires[Wire].End
                    self.wires[Wire].End=Nnst
                    self.wires[Wire].List= List[:i+1]+[Pnew]
                    self.wires[Wire].bbox0=False
                    wName = Glbs.wireName()
                    while wName in Glbs.details[Root].wires:
                        wName = Glbs.wireName()
                    self.add_wire(wName,Nnst,Stop,[Pnew]+List[i+1:])
                    return Nnst,Pnew
        return False,False

    def select_object(self,Point):
        for Key in self.params:
            BB=self.params[Key].bbox()
            if close_enough(BB,Point):
                return ('param',Key)
        for Inst in self.instances:
            BB=self.instances[Inst].bbox()
            if close_enough(BB,Point):
                return ('instance',Inst)
        for Name in self.geoms:
            BB=self.geoms[Name].bbox()
            if close_enough(BB,Point):
                return ('geom',Name)
        for Wire in self.wires:
            List = self.wires[Wire].get_wire_list()
            for i in range(0,len(List)-1):
                if point_close_to_section(Point,List[i],List[i+1]):
                    return 'wire',Wire
        return False,False

    def wipe_out_instance(self,Inst):
        Keys = list(self.params.keys())
        for Param in Keys:
            if self.params[Param].Owner==Inst:
                self.params.pop(Param)
        Keys = list(self.wires.keys())
        for Wire in Keys:
            if belongs_together(self.wires[Wire].Start,Inst):
                self.wires.pop(Wire)
            elif belongs_together(self.wires[Wire].End,Inst):
                self.wires.pop(Wire)

    def select_enclosed(self,P0,P1):
        List=[]
        for Inst in self.instances:
            BB = self.instances[Inst].bbox()
            if bbox_inside(BB,[P0,P1]):
                List.append(Inst)
        return List
                
    def move_group(self,List,Dx,Dy):
        for Inst in List:
            if Inst in self.instances:
                self.instances[Inst].move(Dx,Dy)
#                for Key in self.params:
#                    if self.params[Key].Owner==Inst:
#                        self.params[Key].move(Dx,Dy)
                



def point_on_section(Point,Pa,Pb):
    print('point_on_section',Point,Pa,Pb)
    return Point

def belongs_together(Wire,Inst):
    if (Inst==Wire):
        return True
    if ('.' in Wire):
        ww = Wire.split('.')
        if (ww[0]==Inst):
            return True
    return False
    
def load_dbase_string(Big):
    state='idle'
    Mod=False
    Lines=Big.split('\n')
    for line in Lines:
        state,Mod=work_on_line(line,state,Mod)
    Glbs.graphicsChanged=True

def extract_dir(Fname):
    if '/' not in Fname:
        return '.'
    ww = Fname.split('/')
    return '/'.join(ww[:-1])

def load_dbase_file(Fname):
    if os.path.exists(Fname):
        File=open(Fname)
        Bef = list(Glbs.details.keys())
        load_dbase_file__(File)

        New=[]
        Aft = list(Glbs.details.keys())
        for X in Aft:
            if X not in Bef:
                New.append(X)
        Dir = extract_dir(Fname)
        for Sch in New:
            Glbs.associated_dir[Sch]=Dir

        Glbs.graphicsChanged=True
    elif ('.' not in Fname)and(os.path.exists('%s.zdraw'%Fname)):
        File=open('%s.zdraw'%Fname)
        load_dbase_file__(File)
        Glbs.graphicsChanged=True
    else:
        print('cannot open "%s"'%Fname)
        return False

def load_dbase_file__(File):
    if not File:
        return
    state='idle'
    Mod=False
    while 1:
        line = File.readline()
        if (len(line)==0):
            return
        state,Mod=work_on_line(line,state,Mod)
def splitLine(line):
    wrds = line.split()
    Wrds = []
    state = 'idle'
    for Wrd in wrds:
        if (state=='idle'):
            if (Wrd[0] == '"')and(Wrd[-1]!='"'):
                Token = Wrd
                state = 'work'
            else:
                Wrds.append(Wrd)
        elif (state=='work'):
            Token += ' '+Wrd
            if Wrd[-1]=='"':
                Wrds.append(Token)
                Token = ''
                state = 'idle'
    if state == 'work':
        Wrds.append(Token)
    return Wrds

def work_on_line(line,state,Mod):
    wrds = splitLine(line)
    if (len(wrds)==0):
        return state,Mod
    elif (wrds[0][0]=='#'):
        return state,Mod
    elif (len(wrds)>0):
        if (wrds[0]=='schematic'):
            Schem=wrds[1]
            set_context('root',Schem)
            set_context('view','detail')
            Mod = DetailClass(Schem)
            Glbs.details[Schem]=Mod
            state='schematic'
        elif (wrds[0]=='picture'):
            Pic=wrds[1]
            Mod = PictureClass(Pic)
            Glbs.pictures[Pic]=Mod
            state='picture'
        elif (wrds[0]=='inst'):
            Type=wrds[1]
            Inst=wrds[2]
            XY = get_xy(wrds[3:],(0,0))
            Rot = get_param(wrds[3:],'rot','r0')
            Mod.add_instance(Type,Inst,XY,Rot)
            Mag = float(get_param(wrds[3:],'mag',1.0))
            Mod.instances[Inst].Mag=Mag
        elif (wrds[0]=='wire'):
            Name = wrds[1]
            Start=wrds[2]
            Stop=wrds[3]
            List = get_list(wrds[4:])
            Mod.add_wire(Name,Start,Stop,List)
        elif (wrds[0]=='geom'):
            Kind=wrds[1]
            Name=wrds[2]
            List = get_list(wrds[3:])
            Rot = get_param(wrds[4:],'rot','r0')
            Mod.add_geom(Kind,Name,List,Rot)
        elif (wrds[0]=='param'):
            Owner=wrds[1]
            Param=wrds[2]
            Value=wrds[3]
            XY = get_xy(wrds[4:],(0,0))
            Rot = get_param(wrds[4:],'rot','r0')
            Mod.add_param(Owner,Param,Value,XY,Rot)
        elif (wrds[0]=='pic_aline'):
            XY = get_list(wrds[1:])
            Mod.add_aline(XY)
        elif (wrds[0]=='pic_line'):
            XY = get_list(wrds[1:])
            Mod.add_line(XY)
        elif (wrds[0]=='pic_text'):
            String=wrds[1]
            XY = get_xy(wrds[2:],(0,0))
            Rot = get_param(wrds[2:],'rot','r0')
            Size = get_param(wrds[2:],'size',defaultPicTextSize)
            Align = get_param(wrds[2:],'align','left')
            Mod.add_text(String,XY,Rot,Size,Align)
        elif (wrds[0]=='pic_pin'):
            Pin=wrds[1]
            Dir=wrds[2]
            XY = get_xy(wrds[3:],(0,0))
            Mod.add_pin(Pin,Dir,XY)
        elif (wrds[0]=='pic_circle'):
            XY = get_list(wrds[1:])
            Mod.add_circle(XY)
        elif (wrds[0]=='pic_fcircle'):
            XY = get_list(wrds[1:])
            Mod.add_fcircle(XY)
        elif (wrds[0]=='pic_geom'):
            Which =wrds[1]
            XY = get_list(wrds[2:])
            Mod.add_pic_geom(Which,XY)
        elif (wrds[0]=='pic_sub'):
            Which = wrds[1]
            XY = get_xy(wrds[2:])
            Mod.add_pic_sub(Which,XY)
        elif (wrds[0]=='pic_prop'):
            Which = wrds[1]
            XY = get_list(wrds[2:])
            Mod.add_pic_prop(Which,XY)
        elif (wrds[0]=='end'):
            state='idle'
        else:
            logs.log_error('unknown line in file %s'%(line))
    return state,Mod

def get_param(wrds,Param,Default):
    for P in wrds:
        if ((Param+'=') in P)and(P.index((Param+'='))==0):
            Len = len(Param+'=')
            Val = P[Len:]
            return Val
    return Default
            
def get_xy(wrds,Default=[0,0]):
    XY = get_param(wrds,'xy',False)
    if not XY:
        return Default
    XY1 = XY.split(',')
    return float(XY1[0]),float(XY1[1])

def get_list(wrds):
    XY = get_param(wrds,'list',False)
    if not XY:
        return []
    List1 = XY.split(',')
    res=[]
    while List1!=[]:
        X0=float(List1.pop(0))
        Y0=float(List1.pop(0))
        res.append((X0,Y0))
    return res
    


def bbox_line(List):
    X0=List[0][0]
    Y0=List[0][1]
    X1=List[0][0]
    Y1=List[0][1]
    Xrun=X0
    Yrun=Y0
    for (X,Y) in List[1:]:
        Xrun += X
        Yrun += Y
        X0 = min(X0,Xrun)
        Y0 = min(Y0,Yrun)
        X1 = max(X1,Xrun)
        Y1 = max(Y1,Yrun)
    return [(X0,Y0),(X1,Y1)]

def bbox_aline(List):
    if type(List) is not list:
        return [(0,0),(1,1)]
    try:
        X0=List[0][0] ; X1=X0
        Y0=List[0][1] ; Y1=Y0
    except:
        return [(0,0),(1,1)]
    try:
        for (X,Y) in List:
            X0 = min(X0,X)
            Y0 = min(Y0,Y)
            X1 = max(X1,X)
            Y1 = max(Y1,Y)
        return [(X0,Y0),(X1,Y1)]
    except:
        return [(0,0),(1,1)]

import sys

K_UP = 1073741906
K_DOWN = 1073741905
K_RIGHT= 1073741903
K_LEFT = 1073741904

def ppoint(PP):
    return '(%.1f,%.1f)'%(PP[0],PP[1])

def use_mousemove(X,Y):
    if 'grouping' in Glbs.contexts:
        Root=get_context('root')
        PP = screen2schem((X,Y))
        Was = get_context('last_group_mouse_selected',PP)
        [_,_,List]=get_context('grouping')
        if type(List) is not list:
            logs.log_error('no group defined yet %s %s' % (type(List),List))
            return
            
        Dx = PP[0]-Was[0]
        Dy = PP[1]-Was[1]
        Glbs.details[Root].move_group(List,Dx,Dy)
        Glbs.details[Root].touched(True)
        set_context('last_group_mouse_selected',PP)
        return

    return   # dont jump us
    if 'last_mouse_selected' not in Glbs.contexts: return
    (What,Inst,WasX,WasY) = get_context('last_mouse_selected')
    Root=get_context('root')
    PP = screen2schem((X,Y))
    if (What=='instance'):
        if Inst in Glbs.details[Root].instances:
            Glbs.details[Root].instances[Inst].move(PP[0]-WasX,PP[1]-WasY)
            Glbs.details[Root].touched(True)
            Glbs.details[Root].instances[Inst].make_selected(False)
                        
    elif (What=='param'):
        Glbs.details[Root].params[Inst].move(PP[0]-WasX,PP[1]-WasY)
        Glbs.details[Root].params[Inst].make_selected(False)
        Glbs.details[Root].touched(True)
    elif (What=='geom'):
        Glbs.details[Root].geoms[Inst].move(PP[0]-WasX,PP[1]-WasY)
        Glbs.details[Root].geoms[Inst].make_selected(False)
        Glbs.details[Root].touched(True)
    elif (What):
        logs.log_error('dont know(4) to move "%s"'%What)
        if 'last_mouse_selected' in Glbs.contexts:
            Glbs.contexts.pop('last_mouse_selected')
    set_context('last_mouse_selected',(What,Inst,PP[0],PP[1]))

def use_mousedown(X,Y):
    Root=get_context('root')
    State = get_context('state')
    (Who,Inst)= select_object((X,Y))
    Psch = screen2schem((X,Y))
    set_context('last_mouse_selected',(Who,Inst,Psch[0],Psch[1]))
  
    if Who=='instance':
        print(ppoint(Psch),(X,Y),Who,Inst,Glbs.details[Root].instances[Inst].Type,Glbs.details[Root].instances[Inst].Point)
        Kind = Glbs.details[Root].instances[Inst].Type
    elif Who=='wire':
        print(ppoint(Psch),(X,Y),Who,Inst,Glbs.details[Root].wires[Inst].Start,Glbs.details[Root].wires[Inst].End)
        Kind = ''
    elif Who=='param':
        Kind = Glbs.details[Root].params[Inst].Value
    else:
        print(ppoint(Psch),(X,Y),Who,Inst)
        Kind = '??'
    set_context('banner','%s :mouse at %.2f %.2f %s %s %s: %s'%(Root,X,Y,Who,Kind,Inst,State))


def duplicate_inst(From,PP):
    Root=get_context('root')
    Obj = Glbs.details[Root].instances[From]
    Type = Obj.Type
    Inst = Glbs.details[Root].invent_inst_name(Type)
#    PP = screen2schem((X,Y))
    New = Glbs.details[Root].add_instance(Type,Inst,PP)
    New.Rot=Obj.Rot
    Glbs.details[Root].touched(True)
    Glbs.graphicsChanged=True
    Keys = list(Glbs.details[Root].params.keys())
    for Key in Keys:
        Prm = Glbs.details[Root].params[Key]
        if Prm.Owner==From:
            Px,Py = Prm.Point
            Ox,Oy = Obj.Point
            Nx,Ny = PP
            Xx = Nx + (Px-Ox)
            Yy = Ny + (Py-Oy)
            Value=Prm.Value
            if Prm.Param!='name':
                Glbs.details[Root].add_param(Inst,Prm.Param,Value,(Xx,Yy),Prm.Rot)
            else:
                Glbs.details[Root].add_param(Inst,Prm.Param,Inst,(Xx,Yy),Prm.Rot)



def use_keystroke(Uni,Ord,XY):
#    print('KEY',Uni,Ord,XY)
    X,Y = XY
    if Uni != '':
        Glbs.lastKeys.append(Uni)
        while len(Glbs.lastKeys)>3:
            Glbs.lastKeys.pop(0)
    Glbs.graphicsChanged=True
    Root=get_context('root')
    State = get_context('state')
    if (Uni=='t'):
        center_display(X,Y)
        Glbs.graphicsChanged = True
    elif (Uni == '0'):
        Glbs.details[Root].matrix=False
        Glbs.graphicsChanged = True
        
    elif (Ord == 27):
        if 'last_mouse_selected' in Glbs.contexts:
            Glbs.contexts.pop('last_mouse_selected')
    elif (Ord in [ K_RIGHT,K_LEFT,K_UP,K_DOWN]):
        Grid = get_context('grid')
        if (Ord==K_RIGHT):
            Dx,Dy=Grid,0
        elif (Ord==K_LEFT):
            Dx,Dy=-Grid,0
        elif (Ord==K_DOWN):
            Dx,Dy=0,-Grid
        elif (Ord==K_UP):
            Dx,Dy=0,Grid
        if 'grouping' in Glbs.contexts:
            [_,_,List]=get_context('grouping')
            if type(List) is not list:
                logs.log_error('no group defined yet')
                return
                
            Glbs.details[Root].move_group(List,Dx,Dy)
            Glbs.details[Root].touched(True)
            Glbs.undoValid = True
            return


        (Who,Inst)= select_object((X,Y))
        if (Who):
            Glbs.graphicsChanged=True
            if (Who=='instance'):
                Glbs.details[Root].instances[Inst].move(Dx,Dy)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (Who=='geom'):
                Glbs.details[Root].geoms[Inst].move(Dx,Dy)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (Who=='param'):
                Glbs.details[Root].params[Inst].move(Dx,Dy)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            else:
                logs.log_error('dont know(2) to move who="%s" inst="%s"'%(Who,Inst))
    elif (Ord<128)and(((len(str(Uni))==1)and(str(Uni) in '123456789'))or(Uni in ['Z','z'])):
        if (Uni=='Z'):
            Uni=2
        elif (Uni=='z'):
            Uni=7
        
        Was = screen2schem((X,Y))
        Mid = schem2screen(Was)
        Mag = 0.5+(int(Uni)-1)*0.25
        Mat = get_context('matrix')
        New2 = matrix_mult(Mat,[Mag,0,0,0,Mag,0])
        Glbs.details[Root].set_matrix(New2)
        set_context('matrix',New2)
        Now = schem2screen(Was)
#        Now = (Now[0],Glbs.height-Now[1])
        center_display(Now[0],Now[1])
        Glbs.graphicsChanged = True
    elif (Uni=='Q'):
        if (len(Glbs.lastKeys)>=2)and(Glbs.lastKeys[-2]=='Q'):
            sys.exit()
        Touched=[]
        for Who in Glbs.details:
            if Glbs.details[Who].is_touched:
                Touched.append(Who)
        if Touched!=[]:
            print('some schems are not saved. %s'%Touched)
            print('type another Q to exit')
        else:
            sys.exit()
    elif (Uni in ['r','R','f','F']):
        (Who,Inst)= select_object((X,Y))
        if (Who):
            if (Who=='instance'):
                Glbs.details[Root].instances[Inst].rotate(Uni)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (Who=='geom'):
                Glbs.details[Root].geoms[Inst].rotate(Uni)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (Who=='param'):
                Glbs.details[Root].params[Inst].rotate(Uni)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            else:
                print('dont know to rotate "%s"'%Who)
        else:
            print('dont know to rotate "%s"'%Who)

    elif (Uni=='c'):
        (Who,Inst)= select_object((X,Y))
        if (Who=='instance'):
            Type = Glbs.details[Root].instances[Inst].Type
            set_context('copying',('type',(Type,Inst)))
            Glbs.set_context('banner','%s: copying %s %s'%(Root,Type,Inst))
        elif (Who=='param'):
            set_context('copying',('param',Inst))
            Glbs.set_context('banner','%s: copying param "%s"'%(Root,Inst))
    elif (Uni=='s'):
        PP = screen2schem((X,Y))
        if 'grouping' in Glbs.contexts:
            [_,_,List]=get_context('grouping')
            print('copying list',List)
            lx=1000000
            ly=1000000
            for From in List:
                Obj = Glbs.details[Root].instances[From]
                lx = min(lx,Obj.Point[0])
                ly = min(ly,Obj.Point[1])
                
            for From in List:
                Obj = Glbs.details[Root].instances[From]
                Dx = PP[0]+Obj.Point[0]-lx
                Dy = PP[1]+Obj.Point[1]-ly
                duplicate_inst(From,(Dx,Dy))


            Glbs.details[Root].touched(True)
            Glbs.undoValid = True
            unset_context('grouping')
        elif ('copying' in Glbs.contexts):
            What,Info=get_context('copying')
            if What=='type':
                Type,From=Info
                PP = putOnGrid(PP)
                duplicate_inst(From,PP)
                Glbs.undoValid = True
            elif What=='param':
                (Who,Inst)= select_object((X,Y))
                if Who=='instance':
                    Obj = Glbs.details[Root].instances[Inst]
                    Nx,Ny = Obj.Point
                    Prm = Glbs.details[Root].params[Info]
                    Px,Py = Prm.Point
                    Was = Glbs.details[Root].instances[Prm.Owner]
                    Ox,Oy = Was.Point
                    Xx = Nx + (Px-Ox)
                    Yy = Ny + (Py-Oy)
                    Glbs.details[Root].add_param(Inst,Prm.Param,Prm.Value,(Xx,Yy),Prm.Rot)
                    Glbs.undoValid = True
    elif (Uni=='B'):
        Glbs.details[Root].drawBoxes = not Glbs.details[Root].drawBoxes
        Glbs.graphicsChanged=True

    elif (Uni=='D'):
        (Who,Inst)= select_object((X,Y))
        if Who=='instance':
            Type = Glbs.details[Root].instances[Inst].Type
            load_schematics(Type)
            Glbs.loadStack.append(Root)
    elif (Uni=='H'):
        print(helpString.helpString)
    elif (Uni=='U'):
        if Glbs.loadStack!=[]:
            Root =  Glbs.loadStack.pop(-1)
            load_schematics(Root)
    elif (Uni=='X'):    # undo
        if len(Glbs.undoStack)>1:
            set_context('state','idle')
            unset_context('moving')
            unset_context('deleting') 
            unset_context('grouping')
            Glbs.redoStack.append(Glbs.details[Root].copy())
            Glbs.undoStack.pop(-1)
            Glbs.details[Root] = Glbs.undoStack.pop(-1)
            Glbs.details[Root].is_touched = False
            Glbs.graphicsChanged=True
        else: 
            logs.log_info('at the first change %s' % Root)
            
    elif (Uni=='Y'):    # redo
        if len(Glbs.redoStack)>1:
            set_context('state','idle')
            unset_context('moving')
            unset_context('deleting') 
            unset_context('grouping')
            Glbs.undoStack.append(Glbs.details[Root].copy())
            Glbs.details[Root] = Glbs.redoStack.pop(-1)
            Glbs.details[Root].is_touched = False
            Glbs.graphicsChanged=True
        else: 
            logs.log_info('at the first change %s' % Root)
        
    elif (Uni=='m'):
        if 'grouping' in Glbs.contexts:
            logs.log_error('no moving, while grouping. press "q" first')
            return
        (Who,Inst)= select_object((X,Y))
        PP = screen2schem((X,Y))
        if (Who):
            if (Who=='instance'):
                Glbs.details[Root].instances[Inst].make_selected(True)
                set_context('moving',('instance',Inst,PP[0],PP[1]))
                set_context('state','moving inst')
                Glbs.details[Root].touched(True)
                Glbs.set_context('banner','%s: moving %s %s'%(Root,Who,Inst))
            elif (Who=='param'):
                Glbs.details[Root].params[Inst].make_selected(True)
                set_context('moving',('param',Inst,PP[0],PP[1]))
                set_context('state','moving param')
                Glbs.set_context('banner','%s: moving param %s %s'%(Root,Who,Inst))
                Glbs.details[Root].touched(True)
            elif (Who=='geom'):
                Glbs.details[Root].geoms[Inst].make_selected(True)
                set_context('moving',('geom',Inst,PP[0],PP[1]))
                set_context('state','moving geom')
                Glbs.set_context('banner','%s: moving geom %s %s'%(Root,Who,Inst))
                Glbs.details[Root].touched(True)
            else:
                Glbs.set_context('banner','%s: dont know(5) to move who="%s" %s'%(Root,Who,Inst))
                logs.log_info('dont know(3) to move "%s %s"'%(Who,Inst))
    elif (Uni=='d'):
        if 'grouping' in Glbs.contexts:
            [_,_,List]=get_context('grouping')
            print('deleting list',List)
            for Who in List:
                Glbs.details[Root].instances.pop(Who)
                Glbs.details[Root].wipe_out_instance(Who)
            Glbs.details[Root].touched(True)
            unset_context('grouping')
            return
            
            
        (Who,Inst)= select_object((X,Y))
        if (Who):
            if (Who=='instance'):
                Glbs.details[Root].instances[Inst].make_selected(True)
                set_context('deleting',('instance',Inst))
                set_context('state','deleting inst')
                Glbs.set_context('banner','%s: deleting inst %s %s'%(Root,Who,Inst))
                print('deleting instance %s'%Inst)
                Glbs.details[Root].touched(True)
            elif (Who=='param'):
                Glbs.details[Root].params[Inst].make_selected(True)
                set_context('deleting',('param',Inst))
                set_context('state','deleting param')
                Glbs.set_context('banner','%s: deleting param %s %s'%(Root,Who,Inst))
                Glbs.details[Root].touched(True)
            elif (Who=='wire'):
                Glbs.details[Root].wires[Inst].make_selected(True)
                set_context('deleting',('wire',Inst))
                set_context('state','deleting wire')
                Glbs.details[Root].touched(True)
                Glbs.set_context('banner','%s: deleting wire %s %s'%(Root,Who,Inst))
            elif (Who=='geom'):
                Glbs.details[Root].geoms[Inst].make_selected(True)
                set_context('deleting',('geom',Inst))
                set_context('state','deleting geom')
                Glbs.details[Root].touched(True)
                Glbs.set_context('banner','%s: deleting geom %s %s'%(Root,Who,Inst))
            else:
                print('dont know to delete "%s"'%Who)
    elif (Uni=='q'):
        set_context('state','idle')
        Glbs.graphicsChanged=True
        if 'moving' in Glbs.contexts:
            (What,Who,WasX,WasY)=get_context('moving')
            Root=get_context('root')
            if (What=='instance'):
                Glbs.details[Root].instances[Who].make_selected(False)
            elif (What=='param'):
                Glbs.details[Root].params[Who].make_selected(False)
            unset_context('moving')
        elif 'deleting' in Glbs.contexts:
            (What,Who)=get_context('deleting')
            Root=get_context('root')
            if (What=='instance'):
                Glbs.details[Root].instances[Who].make_selected(False)
            elif (What=='param'):
                Glbs.details[Root].params[Who].make_selected(False)
            elif (What=='wire'):
                Glbs.details[Root].wires[Who].make_selected(False)
            elif (What=='geom'):
                Glbs.details[Root].geoms[Who].make_selected(False)
            unset_context('deleting')
        elif 'grouping' in Glbs.contexts:
            unset_context('grouping')

    elif (Uni=='e'):
        set_context('state','idle')
        Glbs.set_context('banner',Glbs.Banner)
        Glbs.graphicsChanged=True
        PP = screen2schem((X,Y))
        PP = putOnGrid(PP)
        if 'moving' in Glbs.contexts:
            (What,Who,WasX,WasY)=get_context('moving')
            Root=get_context('root')
            if (What=='instance'):
                Glbs.details[Root].instances[Who].move(PP[0]-WasX,PP[1]-WasY)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
                Glbs.details[Root].instances[Who].make_selected(False)
#                for Key in Glbs.details[Root].params:
#                    if Glbs.details[Root].params[Key].Owner==Who:
#                        Glbs.details[Root].params[Key].move(PP[0]-WasX,PP[1]-WasY)
                        
            elif (What=='param'):
                Glbs.details[Root].params[Who].move(PP[0]-WasX,PP[1]-WasY)
                Glbs.details[Root].params[Who].make_selected(False)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (What=='geom'):
                Glbs.details[Root].geoms[Who].move(PP[0]-WasX,PP[1]-WasY)
                Glbs.details[Root].geoms[Who].make_selected(False)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            unset_context('moving')
        if 'deleting' in Glbs.contexts:
            (What,Who)=get_context('deleting')
            if (What=='instance'):
                Glbs.details[Root].instances.pop(Who)
                Glbs.details[Root].wipe_out_instance(Who)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (What=='param'):
                Glbs.details[Root].params.pop(Who)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (What=='wire'):
                Glbs.details[Root].wires.pop(Who)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif (What=='geom'):
                Glbs.details[Root].geoms.pop(Who)
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            elif(Who):
                print('dont know to delete "%s"'%Who)
            unset_context('deleting')
        if ('wiring' in Glbs.contexts): 
            (InstPin0,P0,List)=get_context('wiring')
            InstPin1,P1 = Glbs.details[Root].select_pin((X,Y))
#            print('>>>>>',InstPin1,P1,"   ",InstPin0,'p0',P0,'list',List)
            if (InstPin1):
                wName = Glbs.wireName()
                while wName in Glbs.details[Root].wires:
                    wName = Glbs.wireName()
                    
                Glbs.details[Root].add_wire(wName,InstPin0,InstPin1,[P0]+List+[P1])
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            print('end wiring',InstPin1,P1,InstPin0,P0,List)
            Glbs.details[Root].touched(True)
            Glbs.undoValid = True
            Glbs.graphicsChanged=True
            unset_context('wiring')
        if ('grouping' in Glbs.contexts): 
            [P0,_,_] = get_context('grouping')
            Psch = screen2schem((X,Y))
            set_context('grouping',[P0,Psch,_])
            Included = Glbs.details[Root].select_enclosed(P0,Psch)  
            set_context('grouping',[P0,Psch,Included])
            Glbs.set_context('banner','%s: grouping (%d)'%(Root,len(Included)))

    elif (Uni=='w'):
        Root=get_context('root')
        InstPin,Point = Glbs.details[Root].select_pin((X,Y))
        if (InstPin):
            set_context('wiring',(InstPin,Point,[]))
            Glbs.set_context('banner','%s: wiring from %s %s'%(Root,InstPin,Point))


    elif (Uni=='n'):
        Root=get_context('root')
        Psch = screen2schem((X,Y))
        Psch = putOnGrid(Psch)
        Inst = Glbs.details[Root].invent_inst_name('node')
        Glbs.details[Root].add_instance('node',Inst,Psch)
        Glbs.details[Root].touched(True)
        Glbs.undoValid = True
    elif (Uni=='.'):
        if 'wiring' in Glbs.contexts:
            (InstPin,Point,List)=get_context('wiring')
            Psch = screen2schem((X,Y))
            Psch = putOnGrid(Psch)
            Inst = Glbs.details[Root].invent_inst_name('node')
            wName = Glbs.wireName()
            while wName in Glbs.details[Root].wires:
                wName = Glbs.wireName()
            Glbs.details[Root].add_wire(wName,InstPin,Inst,[Point]+List+[Psch])
            Glbs.details[Root].add_instance('node',Inst,Psch)
            Glbs.details[Root].touched(True)
            set_context('wiring',(Inst,Psch,[]))
            Glbs.undoValid = True

    elif (Uni=='p'):
        Root=get_context('root')
        (Who,Inst)= select_object((X,Y))
        Psch = screen2schem((X,Y))
        if Who in ['instance','wire']:
            if len(Glbs.params_queue)>0:
                Value = Glbs.params_queue.pop(0)
                Glbs.details[Root].add_param(Inst,Glbs.paramName,Value,(Psch[0]+2,Psch[1]+2))
                Glbs.details[Root].touched(True)
                Glbs.undoValid = True
            else:
                print('add params to queue first')

        else:
            print('?? add params to %s %s'%(Who,Inst))

    elif (Uni=='T'):
        put_schem_text(X,Y)
        Glbs.undoValid = True
    elif (Uni=='G'):
        if 'moving' in Glbs.contexts:
            logs.log_error('no grouping while in moving. press "q" first.')
            return
        if ('grouping' not in Glbs.contexts):
            Psch = screen2schem((X,Y))
            set_context('grouping',[Psch,0,0])
            set_context('state','group')
            set_context('banner','%s : start grouping'%(Root))
        else:
            unset_context('grouping')
            set_context('state','idle')
            set_context('banner','%s : unset grouping'%(Root))
    elif (Uni == 'V'):
        Glbs.useVectorText = not Glbs.useVectorText;
    elif (Uni == 'C'):
        screenShot(get_context('width'),get_context('height'),get_context('screenShotFileName','screenshot.png'))
    elif (Uni == 'P'):
        Glbs.useShyParams = not Glbs.useShyParams;
        Glbs.graphicsChanged=True
    elif (Uni == 'S'):
        if Root in Glbs.associated_dir:
            Fname = '%s/%s.zdraw'%(Glbs.associated_dir[Root],Root)
        else:
            Fname = '%s.zdraw'%Root
        logs.log_info('saving %s to %s file'%(Root,Fname))
        File = open(Fname,'w')
        Glbs.details[Root].save(File)
        File.close()
        Glbs.details[Root].touched(False)
        Glbs.undoValid = False

    elif (Uni in ['l']):
        (Who,Inst)= select_object((X,Y))
        PP = screen2schem((X,Y))
        if (Who):
            if (Who=='instance'):
                Root=get_context('root')
#                Glbs.details[Root].instances[Inst].make_selected(True)
                Me = Glbs.details[Root].instances[Inst]
                Wires = Glbs.details[Root].wires
                Others = []
                for Wire in Wires:
                    WW = Wires[Wire]
                    Start=WW.Start
                    End=WW.End
                    if Inst == Start:
                        Others.append(WW.List[1])
                        Others.append(WW.List[-2])
                    elif Inst == End:
                        Others.append(WW.List[-2])
                        Others.append(WW.List[1])
                Points = []
                for Px in Others:
                    Dist = distance(Px,Me.Point)
                    if Dist> 0.001:
                        Points.append(Px)

                print('MORE WORK - divide into Verticals and Horizontals ALIGN %s (%s) %s  %s    list  %s' % (Who,Inst,Me.Type,Me.Point,Points))
            else:
                print('align works only on some instances (%s) %s ' % (Who,Inst))

    elif (Uni in ['v','g','i','o']):
        if Uni=='v':
            What='vcc'
        elif Uni=='i':
            What='input'
        elif Uni=='o':
            What='output'
        else:
            What='gnd'
        Root=get_context('root')
        Inst = Glbs.details[Root].invent_inst_name(What)
        Spoint = screen2schem((X,Y))
        Spoint = putOnGrid(Spoint)
        Glbs.details[Root].add_instance(What,Inst,Spoint)
        X+=0.5
        Y+=0.5
        Glbs.details[Root].touched(True)
        Glbs.details[Root].bbox0=False
        Glbs.undoValid = True
    elif (Uni=='a'):
        if len(Glbs.adding_queue)==0:
            print('add types (pictures) names to queue first')
            print('loaded pictures')
            List = list(Glbs.pictures.keys())
            List += Glbs.loadable_pictures()
            List.sort()
            while List != []:
                if len(List)<10:
                    print(' '.join(List))
                    List = []
                else:
                    print(' '.join(List[:10]))
                    List = List[10:]



        else:
            What = Glbs.adding_queue.pop(0)
            bad=False
            if What not in Glbs.pictures:
                Ok = Glbs.try_load_picture(What)
            else:
                Ok = True
            if Ok and What in Glbs.pictures:
                Root=get_context('root')
                Inst = Glbs.details[Root].invent_inst_name(What)
                Spoint = screen2schem((X,Y))
                Spoint = putOnGrid(Spoint)
                Glbs.details[Root].add_instance(What,Inst,Spoint)
                X+=0.5
                Y+=0.5
                Glbs.details[Root].touched(True)
                Glbs.details[Root].bbox0=False
                Glbs.undoValid = True
            else:
                logs.log_error('unknown picture type = %s cannot instance'%(What))
                bad=True
            if bad:
                Pics = list(Glbs.pictures.keys())
                Pics.sort()
                logs.log_info('known pictures:')
                while len(Pics)>5:
                    logs.log_info('  %s'%(' '.join(Pics[:5])))
                    Pics = Pics[5:]
                logs.log_info('  %s'%(' '.join(Pics)))
    elif Uni == '':
        if Ord not in [0x400000e1]:
            logs.log_info('key ord (%d) not used'%(Ord))
    else:
        logs.log_info('key "%s" (%d) not used'%(Uni,ord(Uni)))

def put_schem_text(X,Y):
    Spoint = screen2schem((X,Y))
    Root=get_context('root')
    if len(Glbs.adding_queue)==0:
        print('add texts to queue first (use "add something" in terminal)')
    else:
       What = Glbs.adding_queue.pop(0)
       Glbs.details[Root].add_geom('text',What,[Spoint])
       Glbs.details[Root].touched(True)
       Glbs.details[Root].bbox0=False
    


def center_display(Xw,Yw):
    W = get_context('width')
    H = get_context('height')
    H2 = H/2 
    W2 = W/2 
#    print('center_display %s %s screen=%s %s'%(Xw,Yw,W,H))

    Dx = -(Xw-W2)
    Dy = -(Yw-H2)

    Root=get_context('root')
    Mat = Glbs.details[Root].matrix
    New = matrix_mult([1,0,Dx,0,1,Dy],Mat)
    New2 = matrix_mult(Mat,[1,0,Dx,0,1,Dy])

    Glbs.details[Root].set_matrix(New2)

    return

   

def merge_bbox(Bbox0,Bbox1):
    [(X0,Y0),(X1,Y1)]=Bbox0
    [(X2,Y2),(X3,Y3)]=Bbox1
    return [(min(X0,X2),min(Y0,Y2)),(max(X1,X3),max(Y1,Y3))]

def get_pin_location(Module,Conn):
    ww = Conn.split('.')
    Mod = Glbs.details[Module]
    if (len(ww)==1):
        return Mod.where_inst(Conn)
    elif (len(ww)==2):
        return Mod.where_pin(ww[0],ww[1])
    logs.log_error('bogus connection %s'%(Conn))
    return (0,0)

def select_object(Point):
    SchPoint = screen2schem(Point)
    Root=get_context('root')
#    print('select_object screen=%s schem=%s matrix=%s'%(Point,SchPoint,Glbs.get_context('matrix')))
    return Glbs.details[Root].select_object(SchPoint)

def close_enough(BB,Point):
    [(X0,Y0),(X1,Y1)]=BB
    Xm,Ym = Point
    Prox=get_context('proximity')
    if ((Xm>=(X0-Prox))and(Xm<=(X1+Prox))and(Ym>=(Y0-Prox))and(Ym<=(Y1+Prox))):
        return True
    return False

def point_close_to_section(Point,P0,P1):
    if (P0[0]==P1[0]):    # vertical line
        Dx = abs(P0[0]-Point[0])
        if (Dx<=get_context('proximity')):
            if (Point[1]>=min(P0[1],P1[1]))and(Point[1]<=max(P0[1],P1[1])):
                return True
    elif (P0[1]==P1[1]):    # horizontal line
        Dy = abs(P0[1]-Point[1])
        if (Dy<=get_context('proximity')):
            if (Point[0]>=min(P0[0],P1[0]))and(Point[0]<=max(P0[0],P1[0])):
                return True
    else:
        Prox = get_context('proximity')
        Dis = pdis(P0,P1,Point)
        if (Dis>Prox):
            return False
        X0= min(P0[0],P1[0])
        X1= max(P0[0],P1[0])
        if (Point[0]<(X0-Prox)):
            return False
        if (Point[0]>(X1+Prox)):
            return False
        return True
    return False






from math import sqrt, fabs
def pdis(a, b, c): 
    t = b[0]-a[0], b[1]-a[1]           # Vector ab
    dd = sqrt(t[0]**2+t[1]**2)         # Length of ab
    t = t[0]/dd, t[1]/dd               # unit vector of ab
    n = -t[1], t[0]                    # normal unit vector to ab
    ac = c[0]-a[0], c[1]-a[1]          # vector ac
    return fabs(ac[0]*n[0]+ac[1]*n[1]) # Projection of ac to n (the minimum distance)

    
def distance(P0,P1):
    Dx = fabs(P0[0]-P1[0])
    Dx2 = Dx*Dx
    Dy = fabs(P0[1]-P1[1])
    Dy2 = Dy*Dy
    D2 = Dx2+Dy2
    return math.sqrt(D2)





def merge_rot(Rot,New):
    if Rot[0]=='f':
        Rot=Rot[1:]
        Flip='f'
    else:
        Flip=''

    if (New=='f'):
        if (Flip=='f'):
            Flip=''
        else:
            Flip='f'
        
    Was = int(Rot[1:])
    if (New=='r'):
        Was += 90
    elif (New=='R'):
        Was -= 90
    if (Was>=360):
        Was -=360
    elif (Was<0):
        Was +=360
    Ok =  Flip+'r'+str(Was)
    return Ok

def instmatrix(Mag,Point,Rot,Matrix):
    Mat0 = translate_mag(Mag,UnitMatrix)
    Mat1 = translate_move(Point,Mat0)
    Mat2 = translate_rotate(Rot,Mat1)
    Mat3 = matrix_mult(Mat2,Matrix)
    return Mat3




def translate_line(Matrix,Line):
    X0=Line[0][0]
    Y0=Line[0][1]
    Res=[]
    for i in range(len(Line)-1):
        X1 =  X0 + Line[i+1][0]        
        Y1 =  Y0 + Line[i+1][1]        
        (X2,Y2) =  world_coord_fl(Matrix,(X0,Y0))
        (X3,Y3) =  world_coord_fl(Matrix,(X1,Y1))
        if (i==0):
            Res.append((X2,Y2))
        Res.append((X3,Y3))
        X0=X1
        Y0=Y1
    return Res
def translate_aline(Matrix,Line):
    Res=[]
    for i in range(len(Line)-1):
        P0 =  world_coord_fl(Matrix,Line[i])
        P1 =  world_coord_fl(Matrix,Line[i+1])
        if (i==0):
            Res.append(P0)
        Res.append(P1)
    return Res 

def bbox_inside(BB0,BB1):
    if not point_inside(BB0[0],BB1):
        return False
    return point_inside(BB0[1],BB1)

def point_inside(Point,Bbox):
    [P0,P1]=Bbox
    if (Point[0]<P0[0]): return False
    if (Point[1]<P0[1]): return False
    if (Point[0]>P1[0]): return False
    if (Point[1]>P1[1]): return False
    return True


def grid_it(Float):
    Grid = get_context('grid')
    if Float>=0:
        X = int((Float/Grid)+0.5)
    else:
        X = int((Float/Grid)-0.5)
    return Grid*X


def arc2aline(Center,P0,P1):
    Ind0 = circle_index(Center,P0)
    Ind1 = circle_index(Center,P1)
    Next = (Ind0+1) % 40
    DistSq = ((Center[0]-P0[0])*(Center[0]-P0[0])) + ((Center[1]-P0[1])*(Center[1]-P0[1]))
    Radii = math.sqrt(DistSq)
    Scale = Radii/1024
    X0,Y0 = P0
    Aline = [(X0,Y0)]
    while Ind0!=Ind1:
        cX0,cY0 = CIRCLE_TABLE[Ind0]
        cX1,cY1 = CIRCLE_TABLE[Next]
        Dx = (cX1-cX0)*Scale
        Dy = (cY1-cY0)*Scale
        X0 += Dx
        Y0 += Dy
        Aline.append((X0,Y0))
        Ind0 = Next
        Next = (Ind0+1) % 40
    return Aline        

def circle_index(Center,Point):
    dX = Point[0]-Center[0]
    dY = Point[1]-Center[1]
    if dX==0:
        if dY>0: return 10
        return 30
    elif dY==0:
        if dX>0: return 0
        return 20
    if (dX>0)and(dY>0):
        LL,HH = 0,10
    elif (dX<0)and(dY>0):
        LL,HH = 10,20
    elif (dX<0)and(dY<0):
        LL,HH = 20,30
    elif (dX>0)and(dY<0):
        LL,HH = 30,40

    Ratio = 1.0*dX/dY
    Best=10000000
    Bind = 0

    for ii in range(LL,HH):
        xx,yy = CIRCLE_TABLE[ii]
        if yy!=0:
            Rii = 1.0*xx/yy 
            Dsq = (Rii-Ratio)*(Rii-Ratio)
            if Dsq<Best:
                Best=Dsq
                Bind = ii
    return Bind

def putOnGrid(Point):
    Grid = get_context('grid')
    X0 = int( 0.5 + (Point[0] / Grid))
    X1 = X0 * Grid
    Y0 = int( 0.5 + (Point[1] / Grid))
    Y1 = Y0 * Grid
    logs.log_info('Point %f %f   %f %f' % (Point[0],Point[1],X1,Y1))
    return X1,Y1


CIRCLE_TABLE = [(0,0)]*40
CIRCLE_TABLE[0]=(1024,0)
CIRCLE_TABLE[1]=(1011,160)
CIRCLE_TABLE[2]=(973,316)
CIRCLE_TABLE[3]=(912,464)
CIRCLE_TABLE[4]=(828,601)
CIRCLE_TABLE[5]=(724,724)
CIRCLE_TABLE[6]=(601,828)
CIRCLE_TABLE[7]=(464,912)
CIRCLE_TABLE[8]=(316,973)
CIRCLE_TABLE[9]=(160,1011)
CIRCLE_TABLE[10]=(0,1024)
CIRCLE_TABLE[11]=(-160,1011)
CIRCLE_TABLE[12]=(-316,973)
CIRCLE_TABLE[13]=(-464,912)
CIRCLE_TABLE[14]=(-601,828)
CIRCLE_TABLE[15]=(-724,724)
CIRCLE_TABLE[16]=(-828,601)
CIRCLE_TABLE[17]=(-912,464)
CIRCLE_TABLE[18]=(-973,316)
CIRCLE_TABLE[19]=(-1011,160)
CIRCLE_TABLE[20]=(-1024,0)
CIRCLE_TABLE[21]=(-1011,-160)
CIRCLE_TABLE[22]=(-973,-316)
CIRCLE_TABLE[23]=(-912,-464)
CIRCLE_TABLE[24]=(-828,-601)
CIRCLE_TABLE[25]=(-724,-724)
CIRCLE_TABLE[26]=(-601,-828)
CIRCLE_TABLE[27]=(-464,-912)
CIRCLE_TABLE[28]=(-316,-973)
CIRCLE_TABLE[29]=(-160,-1011)
CIRCLE_TABLE[30]=(0,-1024)
CIRCLE_TABLE[31]=(160,-1011)
CIRCLE_TABLE[32]=(316,-973)
CIRCLE_TABLE[33]=(464,-912)
CIRCLE_TABLE[34]=(601,-828)
CIRCLE_TABLE[35]=(724,-724)
CIRCLE_TABLE[36]=(828,-601)
CIRCLE_TABLE[37]=(912,-464)
CIRCLE_TABLE[38]=(973,-316)
CIRCLE_TABLE[39]=(1011,-160)

