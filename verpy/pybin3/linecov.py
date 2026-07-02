
import module_class
from synthesis0 import expr_width
import logs

DISPLAYS = {}
def help_main(Env):
    Mod = Env.Current
    for ind,(Time,Body,Kind) in enumerate(Mod.alwayses):
        X = work(Body,Mod.Module,Mod)
        Mod.alwayses[ind] = (Time,X,Kind)

    for Dst,_,_,_ in Mod.hard_assigns:
        if (type(Dst) is str) and ( Dst.startswith('panic') or Dst.startswith('dbg_')):
            pass
        else:
            treat_assign(Dst,Mod)



    Fout = open('%s.linev' % Mod.Module,'w')
    Mod.dump_verilog(Fout,{'style':'new','mergehards':False,'endmodule':False})
    Fout.write('`include "covstep_task.h"\n')
    Fout.write('endmodule\n')
    Fout.close()
    Fdisp = open('%s.disp' % Mod.Module,'w')
    for M,S in DISPLAYS:
        Val = DISPLAYS[(M,S)]
        Fdisp.write('%s %s %s\n' % (M,S,Val))
    Fdisp.close()

def treat_assign(Dst,Mod):
    if (type(Dst) is list) and (Dst[0] == 'curly'):
        for Item in Dst[1:]:
            treat_assign(Item,Mod)
        return
    Dstn = module_class.hashit(Dst)
    Dname = Dstn
    for Chr in '[]:':
        Dname = Dname.replace(Chr,'_')
    Obj = Mod.add_inst('tgl_mon','tgl_mon_%s' % Dname)
    Obj.conns['signame'] = '"%s"' % Dstn
    Obj.conns['modul'] = '"%s"' % Mod.Module
    Obj.conns['sigval'] = Dst
    Obj.params['WID'] = expr_width(Dst,Mod)
    DISPLAYS[(Mod.Module,Dstn)] = 999

        
    

def work(Body,Module,Mod):
    if type(Body) is list:
        if Body[0] == 'for':
            return Body
        elif Body[0] == 'case':
            Cond = Body[1]
            LL = []
            for Item in Body[2]:
                X = work(Item[1],Module,Mod)
                LL.append([Item[0],X])
            return ['case',Cond,LL]
        elif Body[0] == 'list':
            for ind,Item in enumerate(Body[1:]):
                A = work(Item,Module,Mod)
                Body[ind+1] = A
            return Body
        elif Body[0] == 'ifelse':
            A = work(Body[2],Module,Mod)
            B = work(Body[3],Module,Mod)
            return ['ifelse',Body[1],A,B]
            
        elif Body[0] == 'if':
            A = work(Body[2],Module,Mod)
            return ['if',Body[1],A]
        elif Body[0] in ['<=','=']:
            Dst = Body[1]
            
            Var = '"%s"' % module_class.hashit(Body[1])
            Run = runningNum(Var)
            BX = ['list',Body[:],['functioncall', 'covstep', ['"%s"' % Module,'%s' % Var,Run]]]
            DISPLAYS[(Module,Var)] = Run
            if (type(Dst) is str) and ( Dst.startswith('panic') or Dst.startswith('dbg_')):
                pass
            else:
                treat_assign(Body[1],Mod)
            return BX
        else:
            logs.log_info('missing LLL %s' % str(Body))
            return Body

    else:
        logs.log_info('missing WWW %s' % str(Body))
        return Body

RUNS = {}
def runningNum(Var):
    if Var not in RUNS:
        RUNS[Var] = 0
        return 0
    RUNS[Var] += 1
    return RUNS[Var]


        
