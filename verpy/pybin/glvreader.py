#! /usr/bin/python


import os,sys,string
from  module_class import module_class

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    glv_readfile(File)
    print Db.used
    print Db.Insts
    Fout=open('dddd','w')
    Db.Current.dump_verilog(Fout)

def glv_readfile(File):
    lnum=0
    while 1:
        lnum+=1
        line = File.readline()
        if line=='':
            return Db.Modules
        wrds = string.split(line)
        if len(wrds)==4:
            use_wrds(wrds)
        if ((lnum%100000)==0): print 'wrds %d %s %s'%(lnum,wrds,Db.state)

class Db_class:
    def __init__(self):
        self.state='idle'
        self.used=0
        self.Module=None
        self.Modules={}
        self.Stack=[]
        self.Curly=['curly']
        self.Insts=0
        self.right_assign=''

Db=Db_class()


def debug():
    try:
        return str(Db.Current.nets)
    except:
        return '..'


def use_wrds(wrds):
    Db.used+=1
    Key=(Db.state,wrds[1])
    if wrds[0]=='EOL':
       pass    
    elif Key in Table:
        (Nstate,Actions)=Table[Key]
#        print 'state=%s wrds="%s" next=%s actions=%s curly=%s   %s'%(Db.state,wrds,Nstate,Actions,Db.Curly,debug())
        for Action in Actions:
            if Action!='none':
#                Str = '%s(%s,%s,%s,%s)'%(Action,wrds[0],wrds[1],wrds[2],wrds[3])
                Str = '%s(wrds)'%(Action)
                eval(Str)
        if Nstate=='pop':
            pop_state()
        else:
            Db.state=Nstate
    else:
        print 'error! state=%s lex=%s wrds=%s'%(Db.state,wrds[1],wrds)
        sys.exit()

def set_left_assign(wrds):
    if Db.WidthH and Db.WidthL:
        Db.assign=['subbus',Db.assign,Db.WidthH,Db.WidthL]
    elif Db.WidthH:
        Db.assign=['subbit',Db.assign,Db.WidthH]

    Db.WidthH=None
    Db.WidthL=None
    
def start_assign(wrds):
    Db.WidthH=None
    Db.WidthL=None



def remember_assign(wrds):
    Db.right_assign=wrds[0]
    Db.WidthH=None
    Db.WidthL=None

def set_assign0(wrds):
    Db.assign=wrds[0]
def set_assign1(wrds):
    Db.assign=Db.Curly
    Db.state='assign1'

def set_right_assign(wrds):
    if Db.WidthH and Db.WidthL:
        Db.right_assign=['subbus',Db.right_assign,Db.WidthH,Db.WidthL]
    elif Db.WidthH:
        Db.right_assign=['subbit',Db.right_assign,Db.WidthH]
    Db.Current.add_hard_assign(Db.assign,Db.right_assign)

def set_module(wrds):
    Db.Module=wrds[0]
    Db.Current = module_class(Db.Module)
    Db.Modules[Db.Module]=Db.Current
def set_input(wrds):
    Db.Dir='input'
    Db.WidthH=None
    Db.WidthL=None
def set_wire(wrds):
    Db.Dir='wire'
    Db.WidthH=None
    Db.WidthL=None
def set_inout(wrds):
    Db.Dir='inout'
    Db.WidthH=None
    Db.WidthL=None
def set_output(wrds):
    Db.Dir='output'
    Db.WidthH=None
    Db.WidthL=None
def set_header(wrds):
    Name=wrds[0]
    add_net(Name,Db.Dir,Db.WidthH,Db.WidthL)

def push(wrds):
    Db.Stack.append(Db.state)
def pop_state():
    Db.state = Db.Stack.pop(-1)
def set_state_conn3(wrds):
    Db.state='conn3'
def set_state_assign3(wrds):
    Db.state='assign3'

def add_width_h(wrds):
    Db.WidthH=wrds[0]
def add_width_l(wrds):
    Db.WidthL=wrds[0]

def set_type(wrds):
    Db.Type=wrds[0]
def set_inst(wrds):
    Db.Inst=wrds[0]
    Db.Insts+=1
    Db.Current.add_inst(Db.Type,Db.Inst)
def set_pin(wrds):
    Db.Pin=wrds[0]
    Db.WidthH=None
    Db.WidthL=None
    Db.Curly=['curly']
def set_conn0(wrds):
    Db.Conn=wrds[0]
def set_conn_none(wrds):
    Db.Conn=None
def add_curly(wrds):
    Db.Curly.append(wrds[0])

def check_curly_bus0(wrds):
    if Db.WidthL!=None:
        Was=Db.Curly[-1]
        New = ['subbus',Was,(int(Db.WidthH),int(Db.WidthL))]
        Db.Curly[-1]=New
    elif Db.WidthH!=None:
        Was=Db.Curly[-1]
        New = ['subbit',Was,int(Db.WidthH)]
        Db.Curly[-1]=New
    Db.WidthH=None
    Db.WidthL=None
def check_curly_bus(wrds):
    check_curly_bus0(wrds)
    Db.right_assign=Db.Curly[:]
#    Db.Curly=['curly']

def finish_conn_empty(wrds):
    Db.Current.add_conn(Db.Inst,Db.Pin,None)
def finish_conn(wrds):
    if Db.Curly!=['curly']:
        Conn = Db.Curly
    elif Db.WidthL:
        Conn = ['subbus',Db.Conn,[Db.WidthH,Db.WidthL]]
    elif Db.WidthH:
        Conn = ['subbit',Db.Conn,Db.WidthH]
    else:
        Conn = Db.Conn
    Db.Current.add_conn(Db.Inst,Db.Pin,Conn)

def add_wire_assign(wrds):
    Db.Current.add_hard_assign(Db.current_wire,wrds[0])

def add_wire(wrds):
    Db.current_wire = wrds[0]
    add_net(wrds[0],Db.Dir,Db.WidthH,Db.WidthL)



def add_net(Name,Dir,WidthH,WidthL):
    if WidthH:
        Wid=(WidthH,WidthL)
    else:
        Wid=0
    Db.Current.add_sig(Name,Dir,Wid)


    

Table={}
TableStr = '''
idle     module      module1 none
module1  token       module2 set_module
module2  ;           body0 none
module2  (           header0 none
header0  )           header3 set_input
header0  input       header1 set_input
header0  output      header1 set_output
header0  inout       header1 set_inout
header0  token       theader1 none
header1  token       header2 set_header
header1  [           width0  push
header2  ,           header0  none
header2  )           header3  none
header3  ;           body0  none
theader1 ,           theader2 none
theader1 )           header3 none
theader2 token       theader1 none
body0    input       wire0   set_input
body0    output      wire0   set_output
body0    inout       wire0   set_inout
body0    wire        wire0   set_wire
body0    endmodule   idle   none
wire0    [           width0 push
wire0    token       wire1 add_wire
wire1    ,           wire0 none
wire1    =           wire2 none
wire1    ;           body0 none
wire2    ubin        wire3 add_wire_assign
wire3    ;           body0 none
width0   token       width1 add_width_h
width0   number      width1 add_width_h
width0   -           width0 add_width_h
width1   :           width2 none
width1   ]           pop none
width2   token       width3 add_width_l
width2   number      width3 add_width_l
width2   -           width2 add_width_l
width3   ]           pop none
body0    token       inst0 set_type
inst0    token       inst1 set_inst
inst1    ;           body0 none
inst1    (           inst2 none
inst2    .           conn0 none
inst2    )           inst4 none
conn0    token       conn1 set_pin
conn1    (           conn2 none
conn2    token       conn3 set_conn0
conn2    bin         conn3 set_conn0
conn2    ubin        conn3 set_conn0
conn2    hex         conn3 set_conn0
conn2    uhex        conn3 set_conn0
conn2    dig         conn3 set_conn0
conn2    )           inst3 finish_conn_empty
conn2    {           curly0 set_state_conn3 push
conn3    )           inst3 finish_conn
conn3    [           width0 push
inst3    ,           inst2 none
inst3    )           inst4 none
inst4    ;           body0 none
curly0   token       curly1 add_curly
curly0   ubin         curly1 add_curly
curly0   bin         curly1 add_curly
curly0   hex         curly1 add_curly
curly0   uhex        curly1 add_curly
curly0   dig         curly1 add_curly
curly0   }           pop check_curly_bus
curly1   ,           curly0 check_curly_bus0
curly1   }           pop check_curly_bus
curly1   [           width0 push

body0    assign      assign0 start_assign
assign0  #           assign0_dly none
assign0  {           curly0 set_assign1 push
assign0_dly  number  assign0 none
assign0  token       assign1 set_assign0
assign1  [           width0  push
assign1  =           assign2  set_left_assign
assign2  bin         assign3  remember_assign
assign2  ubin        assign3  remember_assign
assign2  dig         assign3  remember_assign
assign2  uhex        assign3  remember_assign
assign2  hex         assign3  remember_assign
assign2  token       assign3  remember_assign
assign2  {           curly0   set_state_assign3 push
assign3  [           width0   push
assign3  ;           body0    set_right_assign

'''
TableLines = string.split(TableStr,'\n')
for Line in TableLines:
    ww = string.split(Line)
    if len(ww)>=4:
        Key = (ww[0],ww[1])
        Table[Key]=(ww[2],ww[3:])




if __name__ == '__main__':
    main()



