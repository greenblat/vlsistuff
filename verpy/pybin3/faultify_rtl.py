
## make fault ready rtl version.

import logs
from rtl_width import get_width,get_width2
import dump_instance

def help_main(Env):
    Mod = Env.Current
    Mod.Orig = Mod.Module
    for Inst in Mod.insts:
        Mod.insts[Inst].Type = 'Flt_'+Mod.insts[Inst].Type
    Mod.Treated = {}
    for ind,(Dst,Src,A,B) in enumerate(Mod.hard_assigns):
        Dst2 = renameDst(Dst,Mod,'wire')
        Mod.hard_assigns[ind] = (Dst2,Src,A,B)
        
    for ind,(Always,Body,Kind) in enumerate(Mod.alwayses):
        Body = scan_body(Body,Mod)
        Mod.alwayses[ind] = (Always,Body,Kind)

    for ind,Gen in enumerate(Mod.generates):
        if Gen[0] == 'for':
            Body = scan_body(Gen[4],Mod)
            Gen[4] = Body

    Mod.Module = 'Flt_'+Mod.Module
    Fout = open('%s.v'%Mod.Module,'w')
    Mod.dump_verilog(Fout)
    Fout.close()
    makeFltTb(Mod)


def scan_body(Body,Mod):
    if type(Body) is list:
        if Body[0] == 'list':
            for ind,Item in enumerate(Body[1:]):
                Item2 = scan_body(Item,Mod)
                Body[ind+1] = Item2
            return Body    
        if Body[0] == 'ifelse':
            Yes2 = scan_body(Body[2],Mod)
            No2 = scan_body(Body[3],Mod)
            return ['ifelse',Body[1],Yes2,No2]
        if Body[0] == 'if':
            Yes2 = scan_body(Body[2],Mod)
            return ['if',Body[1],Yes2]
        if Body[0] == '<=':
            Dst2 = renameDst(Body[1],Mod,'reg')
            return ['<=',Dst2,Body[2]]
        if Body[0] == '=':
            Dst2 = renameDst(Body[1],Mod,'reg')
            return ['=',Dst2,Body[2]]
        if Body[0] in ['case','casex','casez']:
            Body2 = [Body[0],Body[1],[]]
            for Item in Body[2]:
                Label = Item[0]
                Item2 = scan_body(Item[1],Mod)
                Body2[2].append([[Label],Item2])
            return Body2
        if Body[0] in ['for']:
            Body2 = scan_body(Body[4],Mod)
            return Body[:4]+[Body2]
        if Body[0] in ['#','wait']:
            return Body
        if Body[0] ==  'instance':
            Body[1] = 'Flt_'+Body[1]
            print('BBB',Body[4])
            return Body
    logs.log_error('failed scan_body on %s'%str(Body))
    return Body

def busWidth(Net,Mod):
    if type(Net) is str:    
        if Net in Mod.nets:
            _,Wid = Mod.nets[Net]
            if Wid==0: return 1
            if (type(Wid) is tuple)or(type(Wid) is list):
                if len(Wid)==2:
                    WW = selectWid(Wid)
                    return WW
                if len(Wid)==3:
                    if Wid[0] in ('packed','double'):
                        WW0 = selectWid(Wid[1])
                        WW1 = selectWid(Wid[2])
                        return ('*',WW0,WW1)
        
            logs.log_error('busWidth of %s failed on %s type=%s len=%s'%(Net,Wid,type(Wid),len(Wid)))
            return 1

    logs.log_error('busWidth of %s failed'%str(Net))
    return 1

def selectWid(Wid):
    if Wid[0] in [0,'0']: return ('+',1,Wid[1])
    if Wid[1] in [0,'0']: return ('+',1,Wid[0])
    logs.log_error('selectWid of failed'%str(Wid))
    return 1
    


def renameDst(Dst,Mod,Kind='wire'):
    if type(Dst) is str:
        Dst2 = 'Flt_'+Dst
        if Dst not in Mod.Treated:
            Mod.Treated[Dst] = True
            if Kind == 'wire':
                Dir,Wid = Mod.nets[Dst]
                Mod.nets[Dst2] = 'wire',Wid
            elif (Kind == 'reg'):
                Dir,Wid = Mod.nets[Dst]
                Mod.nets[Dst2] = 'reg',Wid
                Dir = Dir.replace('reg','')
                if Dir=='':
                    Mod.nets[Dst] = 'wire',Wid
                else:
                    Mod.nets[Dst] = Dir,Wid
    
            Mod.add_inst_conns('faultifizer','faultify_%s'%Dst,[('inx',Dst2),('outx',Dst)])
            Mod.add_inst_param('faultify_%s'%Dst,'WID',busWidth(Dst,Mod))
        return Dst2

    if (Kind=='reg') and (type(Dst) is list):
        if Dst[0] == 'subbus':
            Dst2 = ['subbus','Flt_'+Dst[1],Dst[2]]
            renameDst(Dst[1],Mod,Kind)
            return Dst2
        if Dst[0] == 'subbit':
            Dst2 = ['subbit','Flt_'+Dst[1],Dst[2]]
            renameDst(Dst[1],Mod,Kind)
            return Dst2
        if Dst[0] == 'curly':
            Dst2 = ['curly']
            for Item in Dst[1:]:
                Item2 = renameDst(Item,Mod,Kind)
                Dst2.append(Item2)
            return Dst2

    if (Kind=='wire') and (type(Dst) is list):
        if Dst[0] == 'subbus':
#            Dst2 = ['subbus','Flt_'+Dst[1],Dst[2]]
            Dst2 = 'Flt_'+Dst[1]+'_%d_%d'%(Dst[2][0],Dst[2][1])
            Wid =  get_width(Dst,Mod)
            Mod.nets[Dst2] = 'wire',(Wid-1,0)
            Mod.add_inst_conns('faultifizer','faultify_%s'%Dst2,[('inx',Dst2),('outx',Dst)])
            Mod.add_inst_param('faultify_%s'%Dst2,'WID',Wid)
            return Dst2
        if Dst[0] == 'subbit':
#            Dst2 = ['subbit','Flt_'+Dst[1],Dst[2]]
            Dst2 = 'Flt_'+Dst[1]+'_%d'%(Dst[2])
            Mod.nets[Dst2] = 'wire',0
            Mod.add_inst_conns('faultifizer','faultify_%s'%Dst2,[('inx',Dst2),('outx',Dst)])
            Mod.add_inst_param('faultify_%s'%Dst2,'WID',1)
            return Dst2
        if Dst[0] == 'curly':
            Dst2 = ['curly']
            for Item in Dst[1:]:
                Item2 = renameDst(Item,Mod,Kind)
                Dst2.append(Item2)
            return Dst2
                
    logs.log_error('renameDst of %s failed'%str(Dst))
    return Dst

String1 = """

always begin
    clk=0;
    #10;
    clk=1;
    #3;
    $python("negedge()");
    #7;
end
reg makeStuckList;
initial begin
    $dumpvars(0,tb);
    makeStuckList = 0;
"""

def makeFltTb(Mod):
    Fout = open('flt_%s_tb.v'%Mod.Orig,'w')
    Fout.write(TBHEADER)
    
    instance(Mod,Fout)

    Fout.write('endmodule\n')
    Fout.close()
    
def instance(Mod,Fout):
    Sigs = list(Mod.nets.keys())
    Sigs.sort()
    Inps = ''
    Outs = []
    Regs = ''
    Inst0 = ''
    Cons0 = '%s %s (\n'%(Mod.Orig,Mod.Orig)
    Cons1 = '%s %s (\n'%(Mod.Module,Mod.Module)
    Pref = ' '
    for Sig in Sigs:
        DirHL = Mod.nets[Sig]
        Dir1 = DirHL[0]
        if ('input' in Dir1):
            Fout.write('reg %s %s;\n'%(dump_instance.wids(DirHL[1]),Sig))
            Regs +='    %s = 0;\n'%(Sig)
            Cons0 += '    %s.%s(%s)\n'%(Pref,Sig,Sig)
            Cons1 += '    %s.%s(%s)\n'%(Pref,Sig,Sig)
            Pref = ','
        elif ('output' in Dir1):
            Fout.write('wire %s %s,flt_%s;\n'%(dump_instance.wids(DirHL[1]),Sig,Sig))
            Outs.append(Sig)
            Cons0 += '    %s.%s(%s)\n'%(Pref,Sig,Sig)
            Cons1 += '    %s.%s(flt_%s)\n'%(Pref,Sig,Sig)
            Pref = ','

    Cons0 += ');\n'
    Cons1 += ');\n'
    Fout.write(Cons0)
    Fout.write(Cons1)
    Res = []
    for Sig in Outs:
        X = '(%s != flt_%s)'%(Sig,Sig)
        Res.append(X)
    Str = '\n    ||'.join(Res)
    Fout.write('wire cought_fault = %s;\n'%Str)
    Fout.write(String1)
    Fout.write(Regs)
    Fout.write('end\n')

        


TBHEADER = '''
module tb;
reg [31:0] cycles;   initial cycles=0;
reg [31:0] errors;   initial errors=0;
reg [31:0] wrongs;   initial wrongs=0;
reg [31:0] corrects; initial corrects=0;
reg [31:0] marker;   initial marker=0;
reg [39:0] ain;
reg [31:0] discovered,notdiscovered;
reg checkX; initial checkX=0;

initial discovered = 0;
initial notdiscovered = 0;
'''



