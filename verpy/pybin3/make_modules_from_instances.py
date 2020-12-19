

import rtl_width
import module_class

def help_main(Env):
    Mod = Env.Current
    Dumped = []
    Fout = open('extracted_modules.v','w')
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Type = Obj.Type
        if Type not in Dumped:
            Dumped.append(Type)
            Fout.write('module %s'%Type)
            Params = list(Obj.params.keys())
            if Params!=[]:
                Fout.write(' #(\n')
                Pref = ' '
                for Prm in Params:
                    Val = Obj.params[Prm]
                    Fout.write('   %sparameter %s=%s\n'%(Pref,Prm,Val))
                    Pref = ','
            
                Fout.write(')(\n')
            else:
                Fout.write('(\n')

            Pref = ' '
            for Pin in Obj.conns:
                Con = Obj.conns[Pin]
                Wid = rtl_width.get_width(Con,Mod)
                Fout.write('   %sinout %s %s\n'%(Pref,module_class.pr_wid(Wid),Pin))
                Pref = ','
            Fout.write(');\n')
            Fout.write('\n\n\n\nendmodule\n\n')
    Fout.close()
