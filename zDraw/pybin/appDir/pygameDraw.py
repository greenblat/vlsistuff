
VERSION = '08oct2021'
WID,HEI = 1200,600

import os,sys,time,traceback

import pygame

import threading
import re
import cmd

import pygameGeoms
import dbase
dbase.WID = WID
dbase.HEI = HEI
import renders

import helpString 
from dumpFormats import connectivityClass
import drawVectorText
import pictify
import copy
import logs

import cmd  
class cmdxClass(cmd.Cmd):
    def do_quit(self,aaa):
        print('thanks and see you again')
        Glbs.finished=True
        stopRunning()
        sys.exit()
        return True 
    def do_help(self,aaa):
        logs.log_info(helpString.helpString)


    def emptyline(self):
        print('emptyline')
        return False
    def default(self,Txt):
        wrds = dbase.splitLine(Txt)
        if len(wrds)>0:
            use_command_wrds(wrds)
            CommandsHistory.append(Txt)
        return False



class GlobalsClass:
    def __init__(self):
        self.reset()

    def reset(self):
        self.history=[]
        self.Banner='Draw: greenblat@mac.com +972-54-4927322  v:%s' % VERSION
        self.finished=False
        self.INIT = (WID,HEI)
        self.width=self.INIT[0]
        self.height=self.INIT[1]
        self.panelOffset=20
        self.graphicsChanged = True
        self.details={}
        self.pictures={}
        self.contexts={}
        self.adding_queue=[]
        self.adding_text_queue=[]
        self.params_queue=[]
        self.paramName='name'
        self.wireNumName=0
        self.set_context('backgroundColor','white')
        self.associated_dir={}
        self.useVectorText=True
        self.useShyParams=True
        self.fontShrink = 0.8
        self.pleaseExit=False
        self.listed={}
        self.lastKeys=[]
        self.loadStack=[]
        self.wratio = 1.0
        self.hratio = 1.0
        self.undoStack = []
        self.redoStack = []
        self.undoValid = False
        self.imported = {}
        self.drawGrid = 0

    def wireName(self):
        self.wireNumName += 1
        return 'wire%d'%self.wireNumName

    def get_context(self,Param,Default=None):
        if Param in self.contexts:
            return self.contexts[Param]
        if (Default!=None):
            self.set_context(Param,Default)
            return Default
    
    def set_context(self,Param,Value):
        self.contexts[Param]=Value
        if (Param=='matrix'):
            Imatrix = matrix_inverse(Value)
            self.set_context('imatrix',Imatrix)
            recompute_proximity()
    def unset_context(Param):
        self.contexts.pop(Param)
    

    def try_load_picture(self,Pic):
        if Pic in self.pictures:
            return
        Dirs = self.get_context('pics_lib')
        for Extension in ['zlib','zpic']:
            if type(Dirs) is list:
                for Dir in Dirs:
                    Fname = '%s/%s.%s'%(Dir,Pic,Extension)
                    if os.path.exists(Fname):
                        dbase.load_dbase_file(Fname)
                        return True

            elif type(Dirs) is str:
                Fname = '%s/%s.%s'%(Dirs,Pic,Extension)
                if os.path.exists(Fname):
                    dbase.load_dbase_file(Fname)
                    return True

            Fname = '%s.%s'%(Pic,Extension)
            if os.path.exists(Fname):
                dbase.load_dbase_file(Fname)
                return True
        return False

    def loadable_pictures(self):                
        Dirs = self.get_context('pics_lib')
        Res = []
        if type(Dirs) is list:
            for Dir in Dirs:
                LL = os.listdir(Dir)
                for Fname in LL:
                    if '.zpic' in Fname:
                        Cell = Fname[:-5]
                        if Cell not in self.pictures:
                            Res.append(Cell)
        elif type(Dirs) is str:
            if not os.path.exists(Dirs): 
                logs.log_warning('no pics directory "%s"'%Dirs)
                return []
            LL = os.listdir(Dirs)
            for Fname in LL:
                if '.zpic' in Fname:
                    Cell = Fname[:-5]
                    if Cell not in self.pictures:
                        Res.append(Cell)
        return Res 


Glbs = GlobalsClass()
dbase.Glbs = Glbs
pygameGeoms.Glbs = Glbs
renders.Glbs = Glbs
drawVectorText.Glbs=Glbs
def main():
    dbase.init()
    load_init_file()
    was_minus=False
    ind=1
    while ind < len(sys.argv):
        Fname = sys.argv[ind]
        if Fname[0]=='-':
            was_minus=True
        if not was_minus:
            Fnamex = figure_out_the_file(Fname)
            if not Fnamex:
                logs.log_error('file "%s" cant be read'%Fname)
            elif not Fnamex.endswith('.zdraw'):
                logs.log_error('file "%s" should have extension zdraw'%Fnamex)
            elif os.path.exists(Fnamex):
                logs.log_info('file "%s" read'%Fnamex)
                dbase.load_dbase_file(Fnamex)
            else:
                logs.log_error('file "%s" cant be read'%Fnamex)
            ind += 1
        else:
            if Fname=='-do':
                ind += 1
                What = sys.argv[ind]
                use_command_wrds([What])
                ind += 1
            elif Fname in ['-source','-include']:
                ind += 1
                What = sys.argv[ind]
                use_command_wrds(['include',What])
                ind += 1
            else:
                logs.log_error('"%s" not known'%sys.argv[ind])
                ind += 1
            
            
#    Thr = threading.Thread.start(execute_terminal_commands)
    thread1.start()
    work()
    

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        execute_terminal_commands()

thread1 = myThread(1,'xterm',1)

def load_init_file():
    found=False
    homepath = '%s/.zdrawrc'%(os.path.expanduser('~'))
    herepath = '%s/.zdrawrc'%(os.path.abspath('.'))
    logs.log_info('home %s'%homepath)
    logs.log_info('here %s'%herepath)
    if os.path.exists(homepath):
        read_init_file(homepath)
        logs.log_info('home dir .zdrawrc loaded')
        found=True
    if os.path.exists(herepath):
        read_init_file(herepath)
        logs.log_info('pwd dir .zdrawrc loaded')
        found=True
    if not found:
        logs.log_warning('no .zdrawrc loaded')


def doesntHaveExtension(Txt):
    ww = Txt.split('/')
    Fname = ww[-1]
    return not (endsWith(Fname,'.zdraw')or endsWith(Fname,'.zpic'))


def figure_out_the_file(Fname):
    Fname  = os.path.expanduser(Fname)
    Fname  = os.path.abspath(Fname)
    if os.path.exists(Fname):
        return Fname
    if doesntHaveExtension(Fname):
        if os.path.exists(Fname+'.zdraw'):
            return  Fname+'.zdraw'
        if os.path.exists(Fname+'.zlib'):
            return Fname+'.zlib'
        if os.path.exists(Fname+'.zpic'):
            return Fname+'.zpic'
    if Fname in Glbs.listed:
        Fname = Glbs.listed[Fname]+'/'+Fname
        return Fname
    if Fname+'.zdraw' in Glbs.listed:
        Fname = Glbs.listed[Fname+'.zdraw']+'/'+Fname+'.zdraw'
        return Fname
    if Fname+'.zpic' in Glbs.listed:
        Fname = Glbs.listed[Fname+'.zpic']+'/'+Fname+'.zpic'
        return Fname
    return False

def read_init_file(Fname):
    File = open(Fname)
    while 1:
        line = File.readline()
        if (len(line)==0):
            return
        line = line.replace('=',' = ')
        wrds = line.split()
        if (len(wrds)>0)and(wrds[0]=='load'):
            Fname = figure_out_the_file(wrds[0])
            if not Fname:
                logs.log_error('file "%s" cant be read'%Fname)
            else:
                dbase.load_dbase_file(Fname)
        elif (len(wrds)>=2)and(wrds[0] == 'import'):
            import_command(wrds[1])
        elif (len(wrds)>=2)and(wrds[0] == 'pics_lib'):
            Was = dbase.get_context('pics_lib')
            for wrd in wrds[1:]:
                Was.append(wrd)
            dbase.set_context('pics_lib',Was) 
        elif (len(wrds)==2):
            Param = wrds[0]
            Value=wrds[1]
#            logs.log_info('read_init_file set context "%s" "%s"'%(Param,Value))
            if (',') in Value:
                W1 = Value.split(',')
                ll = []
                for X in W1:
                    ll.append(makenum(X))
                dbase.set_context(Param,ll)
            elif (Value[0] in '0123456789'):
                dbase.set_context(Param,makenum(Value))
            else:
                dbase.set_context(Param,Value)
        elif(len(wrds)>0):
            logs.log_warning('read_init_file got "%s" . not valid.'%(' '.join(wrds)))
                
def makenum(Txt):
    try:
        if '.' in Txt:
            return float(Txt)
        return int(Txt)
    except:
        return Txt



JUSTPASS = [771,770,4352,32774,32775,32770,32776,32785,32768,32784,32777,32783,32779,32778,32786]

running =True
import time
def work():
    global running
    pygame.init()
    pygame.display.set_caption("zDraw ver %s" % VERSION)
    screen = pygame.display.set_mode((WID,HEI),pygame.RESIZABLE)
    screen.fill((255,255,255))
#    screen.blit(pygame.transform.rotate(screen, 180), (0, 0))
    Glbs.set_context('screen',screen)
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type in JUSTPASS:
                pass
            elif event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            elif event.type == pygame.KEYDOWN: # key down
                Pos = pygame.mouse.get_pos()
                Dict = event.dict
                if 'text' in Dict:
                    on_key_press(event.dict['text'],ord(event.dict['text']),Pos)
                elif 'unicode' in Dict:
                    on_key_press(event.dict['unicode'],event.dict['key'],Pos)
                else:
                    print('error keydown',event.type,event.dict)
            elif event.type == pygame.KEYUP:
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN: # mouse down
                on_mouse_press(event.button, [],event.pos)
            elif event.type == pygame.MOUSEBUTTONUP: # mouse up
                pass
            elif event.type == pygame.MOUSEMOTION: # mouse move
                Pos = pygame.mouse.get_pos()
                on_mouse_move(Pos)
            elif event.type == 1: # focus in/out
                pass
            elif event.type == pygame.VIDEORESIZE: # resize
#                displayInfo = pygame.display.Info()
#                dpSize = (displayInfo.current_w, displayInfo.current_h)
                Glbs.set_context('width',event.w)
                Glbs.set_context('height',event.h)
#                set_context('width',displayInfo.current_w)
#                set_context('height',displayInfo.current_h)
            else:
                Pos = pygame.mouse.get_pos()
                print(event.type," type",Pos,event.dict)
        on_draw()
        pygame.display.flip()
        time.sleep(0.2) 




def on_mouse_move(XY):
    X,Y = XY
    dbase.use_mousemove(X,Y)
    Glbs.graphicsChanged=True

def on_resize(width,height):
    Glbs.width=width
    Glbs.height=height
    Glbs.wratio = 1.0 * width / Glbs.INIT[0]
    Glbs.hratio = 1.0 * height / 480.0

    Glbs.set_context('width',width)
    Glbs.set_context('height',height)
    Glbs.graphicsChanged=True

def update_graphics():
#    glViewport(0,0,Glbs.width,Glbs.height)
    if Glbs.finished:
        print('graphics bye bye') 
        stopRunning()
        sys.exit()
    if not Glbs.graphicsChanged:
        return
    Glbs.graphicsChanged=False
    Glbs.longest=0

def stopRunning():
    global running
    running = False


def initFun():
#    glClear(GL_COLOR_BUFFER_BIT)
    Color = Glbs.get_context('backgroundColor')
    RGB = pygameGeoms.oglcolor(Color)
#    glClearColor(RGB[0],RGB[1],RGB[2],1.0)
#    glColor3f(0.0,0.0, 0.0)
#    glMatrixMode(GL_PROJECTION)
#    glLoadIdentity()
#    gluOrtho2D(0.0,Glbs.width,0.0,Glbs.height)



def on_draw():
    if Glbs.finished:
        print('graphics bye bye')
        stopRunning()
        sys.exit()
    if not Glbs.graphicsChanged:
        return
    update_graphics()
    Root=Glbs.get_context('root')
    if (Glbs.undoValid):  #  or (Glbs.undoStack == []) or (Glbs.details[Root].isDiff(Glbs.undoStack[-1])):
        print('>>>',len(Glbs.undoStack))
        Glbs.undoStack.append(Glbs.details[Root].copy())
        Glbs.undoValid = False
    initFun()
    Screen = Glbs.get_context('screen')
    Screen.fill((255,255,255))
    WW,HH = int(Glbs.width*Glbs.wratio),int(Glbs.height*Glbs.hratio)
    pygameGeoms.draw_label(Glbs.get_context('banner',Glbs.Banner),200,15,'magenta','center',13)
    pygameGeoms.draw_horizontal(0,WW,20,'magenta')
    pygameGeoms.oglcolor('black')
    dbase.pdraw_current()




CommandsHistory=[]


#def was_execute_terminal_commands():
#    Glbs.IntrLoop = cmdxClass()
#    Glbs.IntrLoop.prompt='?:'
#    Glbs.IntrLoop.cmdloop('hello')
#



def execute_terminal_commands():
    Intr = cmdxClass()
    Intr.prompt='?:'
    Intr.cmdloop('hello')



def execute_terminal_commands__():
    while 1:
        Txt = input('?:')
        Txt = Txt.replace('=',' ')
        wrds = dbase.splitLine(Txt)
        if len(wrds)>0:
            use_command_wrds(wrds)
            CommandsHistory.append(Txt)

#def do_command_line():
#    Txt = input('?:')
#    wrds = Txt.split()
#    if len(wrds)==0:
#        return
#    use_command_wrds(wrds)
#    do_command_line()

def use_command_wrds(wrds):
    try:
        __use_command_wrds(wrds)
    except Exception:
        logs.log_error('command "%s" kinda crashed it' % ' '.join(wrds))
        X = sys.exc_info()
        traceback.print_exception(etype=X[0],value=X[1],tb=X[2])

def import_command(Fname):
    Fname  = os.path.expanduser(Fname) 
    Fname  = os.path.abspath(Fname) 
    if not Fname.endswith('.py'):
        logs.log_error('import expect filename ending with .py')
    else:
        Command,Function = my_importing(Fname)
        if Command:
            Glbs.imported[Command] = Function

def __use_command_wrds(wrds):
    if len(wrds)==0:
        return
    if wrds[0]=='history':
        for LL in Glbs.history:
            print(LL)
        return
    else:
        Glbs.history.append(' '.join(wrds))
    Root=Glbs.get_context('root')

    if wrds[0] in Glbs.imported:
        Glbs.imported[wrds[0]](wrds)
    elif wrds[0] in ['import']:
        import_command(wrds[1])
#        Fname  = os.path.expanduser(wrds[1]) 
#        Fname  = os.path.abspath(Fname) 
#        if not Fname.endswith('.py'):
#            logs.log_error('import expect filename ending with .py')
#        else:
#            Command,Function = my_importing(Fname)
#            if Command:
#                Glbs.imported[Command] = Function

    elif wrds[0] in ['source','include']:
        Fname  = os.path.expanduser(wrds[1]) 
        Fname  = os.path.abspath(Fname) 
        try: 
            Lines = open(Fname).readlines()
            for line in Lines:
                wrds0 = line.split()
                use_command_wrds(wrds0)
        except:
            logs.log_error('failed to open include file "%s" ' % Fname)
            X = sys.exc_info()
            traceback.print_exception(etype=X[0],value=X[1],tb=X[2])

    elif wrds[0] in ['quit','exit']:
        Glbs.details[Root].touched('Q')
        Glbs.pleaseExit=True
        Glbs.finished=True
        stopRunning()
        sys.exit()
    elif wrds[0] in ['zpicslib','picslib']:
        Dirs = Glbs.get_context('pics_lib')
        if type(Dirs) is str:
            Dirs = [Dirs]
        for Wrd in wrds[1:]:
            Fname  = os.path.expanduser(Wrd) 
            Fname  = os.path.abspath(Fname) 
            if os.path.exists(Fname):
                if Fname not in Dirs:
                    Dirs.append(Fname)
            else:
               logs.log_errorprint('Failed to add "%s" to legal paths, as it cannot be opened' % Fname)
        Glbs.set_context('pics_lib',Dirs)
        print('PICSLIBS: %s' % str(Dirs))


    elif wrds[0]=='rename':
        New = wrds[1]
        Glbs.details[New] = copy.deepcopy(Glbs.details[Root])
        Glbs.details[New].Module = New
        Glbs.set_context('root',New)
        Glbs.graphicsChanged=True
        Glbs.undoStack = []
        Glbs.redoStack = []
        
    elif wrds[0]=='save':
        if len(wrds)>1:
            WW = wrds[1].split('/')
            if WW[-1].startswith(Root):
                if '.zdraw' not in WW[1]:
                    Fname =   wrds[1]+'.zdraw'
                Fname =  wrds[1]
            else:
                Fname =  wrds[1]+'/'+Root+'.zdraw'
            Fname  = os.path.expanduser(Fname) 
            Fname  = os.path.abspath(Fname) 
        elif Root in Glbs.associated_dir:
            Fname = '%s/%s.zdraw'%(Glbs.associated_dir[Root],Root)
        else:
            Fname = '%s.zdraw'%Root
        logs.log_info('saving %s to %s file'%(Root,Fname))
        try:
            File = open(Fname,'w')
            Glbs.details[Root].save(File)
            File.close()
            Glbs.details[Root].touched(False)
        except:
            logs.log_info('Failed to open "%s" for saving' % Fname)
    elif wrds[0]=='change':
        List = list(Glbs.details.keys())
        List.sort()
        if len(wrds)==1:
            logs.log_info('available schematics: %s'%' '.join(List))
        elif(wrds[1] in List) :
            Glbs.set_context('root',wrds[1]) 
            Glbs.graphicsChanged=True
        else:
            logs.log_error('"%s" is not loaded. use new to open new drawing'%wrds[1])
    elif wrds[0]=='delete':
        if (Root!='opening'):
             Glbs.details.pop(Root)
             Glbs.set_context('root','opening') 
             Glbs.graphicsChanged=True
    elif wrds[0] == 'V':
        Glbs.useVectorText = not Glbs.useVectorText;
        Glbs.graphicsChanged=True
    elif wrds[0] in ['plot','print']:
        dbase.postscript_current()
    elif 'new' in wrds[0]:
        if len(wrds) != 2:
            logs.log_error('new needs schematic name')
        else:
            Root = wrds[1]
            Glbs.set_context('root',Root)
            Glbs.details[Root] = dbase.DetailClass(Root)
            Glbs.graphicsChanged=True
            Glbs.undoStack = []
            Glbs.redoStack = []
    elif 'load' in wrds[0]:
        if len(wrds)==1:
            logs.log_info('loaded schematics:  %s'%str(list(Glbs.details.keys())))
#            logs.log_info('loaded pictures:  %s'%str(list(Glbs.pictures.keys())))
        else:
            load_schematics(wrds[1])
                    
    elif wrds[0] == 'text':
        Glbs.adding_text_queue.extend(wrds[1:])

    elif 'add' in wrds[0]:
        List = dbase.findMatches('')
        if len(wrds)==1:
            logs.log_info('loaded pictures:  %s'%str(List))
        else:
            for Wrd in wrds[1:]:
                if Wrd in List:
                    Glbs.adding_queue.append(Wrd)
                else:
                    Match = dbase.findMatches(Wrd)
                    if len(Match) == 1:
                        Glbs.adding_queue.extend(Match)
                    else:
                        logs.log_error('add of "%s" failed,. not found or found several: "%s"' % (Wrd,str(Match)))
    elif 'name' in wrds[0]:
        Glbs.paramName='name'
        Glbs.params_queue.extend(wrds[1:])
    elif 'param' in wrds[0]:
        Glbs.paramName=wrds[1]
        Glbs.params_queue.extend(wrds[2:])
    elif 'spice' in wrds[0]:
        Root = Glbs.get_context('root')
        Fname = '%s.cir'%(Root)
        File = open(Fname,'w')
        logs.log_info('writing spice file "%s.cir"'%Root)
        GG = connectivityClass(Glbs,Root)
        GG.dumpSpice(File)
        File.close()
    elif wrds[0] in ['zlib','picture']:
        if len(wrds)==1:
            Fname = '%s.zpic'%(Root)
        elif len(wrds)>=1:
            Fname = os.path.expanduser(Fname)
            Fname = os.path.abspath(Fname)
            ww = Fname.split('/')
            if ww[-1] == Root:
                Fname = Fname + '.zpic'
                ww = Fname.split('/')
            if ww[-1] not in [Root,Root+'.zpic']:
                Fname = Fname + '/'+Root+'.zpic'
        try:
            File = open(Fname,'w')
        except:
            log_error('failed to open zpic file for writing "%s" ' % Fname)
            File = False
        if File:
            pictify.pictify(Glbs,Root,File)

    elif ('dump' in wrds[0])or('verilog' in wrds[0])or('rtl' in wrds[0])or('user' in wrds[0]):
        Rtl = 'rtl' in wrds[0]
        User = 'user' in wrds[0]
        if len(wrds)==1:
            Root = Glbs.get_context('root')
            Fname = '%s.v'%(Root)
            File = open(Fname,'w')
            logs.log_info('writing verilog file "%s.v"'%Root)
            GG = connectivityClass(Glbs,Root)
            GG.dumpVerilog(File,Rtl,User)
            File.close()
        elif len(wrds)==2:
            Fname = wrds[1]
            File = open(Fname,'w')
            Root = Glbs.get_context('root')
            GG = connectivityClass(Glbs,Root)
            GG.dumpVerilog(File,Rtl,User)
            File.close()
        elif len(wrds)==3:
            Fname = wrds[2]
            File = open(Fname,'w')
            if wrds[1]=='*':
                for Name in Glbs.details:
                    GG = connectivityClass(Glbs,Root)
                    GG.dumpVerilog(File,Rtl,User)
            else:
                GG = connectivityClass(Glbs,wrds[1])
                GG.dumpVerilog(File,Rtl,User)
            File.close()

    elif ('sys' == wrds[0]):
        os.system('%s\n'%(' '.join(wrds[1:])))
    elif 'ls' in wrds[0]:
        if len(wrds)>1:
            Dir = wrds[1]
        else:
            Dir = '.'
        if not os.path.exists(Dir):
            logs.log_warning('no such directory "%s"'%Dir)
            return

        LL = os.listdir(Dir)
        L1 = []
        L2 = []
        for Fname in LL:
            if ('.zdraw' in Fname):
                L1.append(Fname)
            elif ('.zpic' in Fname):
                L2.append(Fname)
            elif ('.zlib' in Fname):
                L2.append(Fname)
        for Cell in L1+L2:
            Glbs.listed[Cell] = Dir

        logs.log_info('schematics in "%s"  %s'%(Dir,L1))
        logs.log_info('pictures   in "%s"  %s'%(Dir,L2))
                
    elif (len(wrds)==3)and(wrds[1]=='='):
        Glbs.set_context(wrds[0],makenum(wrds[2]))
    elif(wrds[0]=='variables'):
        for Key in Glbs.contexts:
            print(Key,Glbs.contexts[Key])
    elif 'help' in wrds[0]:
        if len(wrds)==1:
            logs.log_info(helpString.helpString)
        else:
            List = helpString.helpString.split('\n')
            for Str in List:
                if wrds[1] in Str:
                    logs.log_info(Str)
    elif matchesCommand(wrds[0]):
        Comm = matchesCommand(wrds[0])
        wrds[0]=Comm
        use_command_wrds(wrds)
    else:
        logs.log_error('dont know to %s'%wrds)

def load_schematics(newRoot):
    List = list(Glbs.details.keys())
    if newRoot in List:
        Glbs.set_context('root',newRoot) 
        Glbs.graphicsChanged=True
        Glbs.undoStack = []
        Glbs.redoStack = []
    else:
        Fname = figure_out_the_file(newRoot)
        if Fname:
            dbase.load_dbase_file(Fname)
            Glbs.undoStack = []
            Glbs.redoStack = []
        else:
            logs.log_error('file "%s" cant be read'%newRoot)
            return
            

import importlib
def my_importing(Fname):
    sys.path += ['.']
    Orig = Fname
    if (len(Fname)>2)and(Fname[-3:]=='.py'):
        Fname = Fname[:-3]
    if ('/' in Fname):
        wrds2 = Fname.split('/')
        Fname = wrds2[-1]
        Path = '/'.join(wrds2[:-1])
        Path = os.path.abspath(Path)
        sys.path += [Path]

    That = importlib.import_module(Fname)
    print('importing0 "%s"'%Fname)
    That = importlib.import_module(Fname)
    print('importing1 "%s"'%Fname)
    if 'run' in dir(That):
        run = That.run
        That.Glbs = Glbs
        return Fname,run
    else:
        logs.log_error('in imported file "%s" You need to have "run(yada-yada-yada)" function' % (Fname))
        return False,False

from renders import screen2schem
dbase.load_schematics = load_schematics

def on_mouse_press(button, modifiers,xy):
    x,y = xy
    Glbs.Vertical=(x,y)
    Glbs.Msx=x
    Glbs.Msy=y
#    Glbs.graphicsChanged=True
    dbase.use_mousedown(x,y)

def on_key_press(Chr,Ord,xy):
#    if (Chr=='Q'):   # Q key
#        sys.exit()
    if (Chr=='h'):
        logs.log_info(helpString.helpString)
    else:
        dbase.use_keystroke(Chr,Ord,xy)

def on_special_press(Chr,x,y):
    dbase.use_keystroke(Chr,x,y)

def timerFun(Value):
    if (Glbs.finished or Glbs.pleaseExit):
        stopRunning()
        logs.flushLogs()
        sys.exit()
    if Glbs.graphicsChanged:
        on_draw()
#    glutTimerFunc(100,timerFun,333)
    





def printScreen():
    logs.log_warning('print screen - not yet.')


ValidCommandsTxt = ''' add param dump load new delete print save change history help quit exit variables zlib picture include source ls
    verilog spice plot text
'''


ValidCommands = ValidCommandsTxt.split()
ValidCommands.sort()

def matchesCommand(Wrd0):
    res=[]
    for Comm in ValidCommands:
        if startsTheSame(Wrd0,Comm):
            res.append(Comm)
    if len(res)==1:
        return res[0]
    if len(res)>1:
        logs.log_warning('ambigious command %s matches %s'%(Wrd0,res))
    elif len(res)==0:
       logs.log_info('valid cmds: %s'%ValidCommands)

    return False


def startsTheSame(Wrd0,Comm):
    Len = len(Wrd0)
    if Len >len(Comm):
        return False
    Part = Comm[:Len]
    return Part==Wrd0


def endsWith(Fname,With):
    if With not in Fname:
        return False
    ind = Fname.index(With)
    return len(Fname)==(ind+len(With))



main()




