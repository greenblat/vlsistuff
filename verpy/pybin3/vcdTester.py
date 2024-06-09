
import module_class
def help_main(Env):
    Mod = Env.Current

    TB  = module_class.module_class('tb')
    Obj = TB.add_inst(Mod.Module,'dut')
    for Net in Mod.nets:
        Dir,Wid  = Mod.nets[Net]
        if 'input' in Dir:
            TB.nets[Net] = 'reg',Wid
            Obj.conns[Net] = Net
        elif 'output' in Dir:
            TB.nets[Net] = 'wire',Wid
            Obj.conns[Net] = Net

    Fout = open('%s.tb' % Mod.Module,'w')
    TB.dump_verilog(Fout,{'style':'new','mergehards':False,'endmodule':False})
    Fout.write(Epilog)
    Fout.close()

Epilog = '''

initial begin
    $dumpvars(0,tb);
end
`include "tester.include"

endmodule

'''

