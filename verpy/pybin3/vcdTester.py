
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

    TB.nets['errors'] = 'integer',0
    TB.nets['wrongs'] = 'integer',0
    TB.nets['warnings'] = 'integer',0
    TB.nets['corrects'] = 'integer',0
    TB.nets['cycles'] = 'integer',0
    TB.nets['clk'] = 'reg',0
    Fout = open('%s.tb' % Mod.Module,'w')
    TB.dump_verilog(Fout,{'style':'new','mergehards':False,'endmodule':False})
    Fout.write(Epilog)
    Fout.close()
    bussesInc(Mod)
    singlesInc(Mod)

def bussesInc(Mod):
    Fout = open('bussed_inouts.py','w')
    Ins,Ous = [],[]
    for Net in Mod.nets:
        Dir,Wid  = Mod.nets[Net]
        if 'input' in Dir:
            Ins.append(Net)
        elif 'output' in Dir:
            Ous.append(Net)
    Ins.sort()
    Ous.sort()

    Fout.write("INS= '''\n")
    for In in Ins:
        Fout.write(' %s\n' % In)
    Fout.write("'''.split()\n\n")

    Fout.write("OUS= '''\n")
    for Ou in Ous:
        Fout.write(' %s\n' % Ou)
    Fout.write("'''.split()\n\n")

    Fout.close()

def singlesInc(Mod):
    Fout = open('singles_inouts.py','w')
    Ins,Ous = [],[]
    for Net in Mod.nets:
        Dir,Wid  = Mod.nets[Net]
        if (type(Wid) is int) and (Wid <= 1):
            Nets = [Net]
        else:
            H,L = Wid
            Nets = []
            for Ind in range(H,L-1,-1):
                Sig = '%s[%s]' % (Net,Ind)
                Nets.append(Sig)


        if 'input' in Dir:
            Ins.extend(Nets)
        elif 'output' in Dir:
            Ous.extend(Nets)
    Ins.sort()
    Ous.sort()

    Fout.write("INS= '''\n")
    for In in Ins:
        Fout.write(' %s\n' % In)
    Fout.write("'''.split()\n\n")

    Fout.write("OUS= '''\n")
    for Ou in Ous:
        Fout.write(' %s\n' % Ou)
    Fout.write("'''.split()\n\n")

    Fout.close()

Epilog = '''

initial begin
    $dumpvars(0,tb);
    wrongs = 0;
    errors = 0;
    corrects = 0;
    warnings = 0;
    cycles = 0;
end
    `include "tester_clk.include"
    `include "tester.include"
    `include "tester_chk.include"



endmodule

'''

