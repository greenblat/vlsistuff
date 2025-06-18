
# gather all inputs / outputs to single clock and data. for fpga ecal runs.

CLKS = 'CLK clk'.split()
RSTS = 'BReset rst_n'.split()
import module_class
def help_main(Env):
    Mod = Env.Current
    ins,ous = 0,0
    Mod.computeParams(4)
    Wrap = module_class.module_class('fpga_wrap')
    Wrap.nets['clk'] = ('input',1)
    Wrap.nets['rst_n'] = ('input',1)
    Wrap.nets['scanin'] = ('input',1)
    Wrap.nets['din'] = ('input',1)
    Wrap.nets['dout'] = ('output',1)
    Obj = Wrap.add_inst(Mod.Module,Mod.Module)
    Run = 0
    Din = 'din'
    Dout = 'sr%s' % Run
    for Net in Mod.nets:
        if Net in CLKS:
            Obj.conns[Net] = 'clk'
        elif Net in RSTS:
            Obj.conns[Net] = 'rst_n'
        else:            
            Dir,Wid = Mod.nets[Net]
            Len = getWid(Wid,Mod)
            if 'input' in Dir:
                In = Wrap.add_inst_conns('dffin','dffin%d' % Run,[ ('clk','clk'),('scanin','scanin'),('din',Din),('dout',Dout),('qout',Net)])
                Wrap.add_inst_param('dffin%d' % Run,'WID',Len)
                Run += 1
                Din = Dout
                Dout = 'sr%s' % Run
                Obj.conns[Net] = Net
                Wrap.nets[Net] = 'wire',Wid
            elif 'output' in Dir:
                In = Wrap.add_inst_conns('dffout','dffout%d' % Run,[  ('clk','clk'),('scanin','scanin'),('din',Din),('dout',Dout),('qin',Net)])
                Wrap.add_inst_param('dffout%d' % Run,'WID',Len)
                Run += 1
                Din = Dout
                Dout = 'sr%s' % Run
                Obj.conns[Net] = Net
                Wrap.nets[Net] = 'wire',Wid
    Wrap.hard_assigns.append(('dout',Din,'',''))
    Fout = open('fpga_wrap.v','w')
    Wrap.dump_verilog(Fout)
    Fout.write(HELPERS)
    Fout.close()




def getWid(Wid,Mod):
    if type(Wid) is int:
        Val = max(Wid,1)
        return Val
    if type(Wid) is tuple:
        H,L = Wid
        HH = module_class.pr_expr(H)
        HI = eval(HH,Mod.parameters,Mod.localparams)
        LL = module_class.pr_expr(L)
        LO = eval(LL,Mod.parameters,Mod.localparams)
        return HI-LO+1
    print("BADWID %s" % str(Wid))
    return 1



    
HELPERS = '''
module dffin #(parameter WID=1) ( input clk, input scanin, input din, output reg dout, output [WID-1:0] qout);
reg [WID-1:0] sr;
always @(posedge clk) begin
    if (scanin) begin
        {dout,sr} <= {sr,din};
    end
end
assign qout = sr;
endmodule

module dffout #(parameter WID=1) ( input clk, input scanin, input din, output reg dout, input [WID-1:0] qin);
reg [WID-1:0] sr;
always @(posedge clk) begin
    if (scanin) begin
        {dout,sr} <= {sr,din};
    end else begin
        sr <= qin;
    end
end
endmodule

'''



