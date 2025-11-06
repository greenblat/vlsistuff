
TEXT = '''
read_liberty -lib /Users/iliagreenblat/clients/yosys_libs/scs130ms_tt_1.80v_25C.lib
read_verilog -sv gutted/CELL.v

# read_verilog  blackboxes/xl_rgf_ram.blkbox
read_verilog  blackboxes/blkbox.blkbox
BLACKBOXES

hierarchy -check -top  CELL



proc; opt; fsm; opt; memory; opt
opt_merge;
opt_expr;
check;
opt -full;
opt_clean;
techmap; opt

dfflibmap -liberty /Users/iliagreenblat/clients/yosys_libs/scs130ms_tt_1.80v_25C.lib
abc -liberty  /Users/iliagreenblat/clients/yosys_libs/scs130ms_tt_1.80v_25C.lib
hilomap -locell TIELO Y -hicell TIEHI Y
opt_merge;
opt_expr -full;
clean
opt_clean -purge
write_verilog -noattr  glv0/CELL.v
'''

def help_main(Env):
    for Module in Env.Modules:
        Mod = Env.Modules[Module]
        Types = []
        for Inst in Mod.insts:
            Type = Mod.insts[Inst].Type
            if Type not in Types: Types.append(Type)
    
        Types.sort()
        Txt = TEXT.replace('CELL',Mod.Module)
        LL = ''
        for Type in Types:
            LL += 'read_verilog  blackboxes/%s.blkbox\n' % Type
    
        Txt = Txt.replace('BLACKBOXES',LL)
        print(Txt)
        Fout = open('incs/%s.inc' % Mod.Module,'w')
        Fout.write(Txt)
        Fout.close()

