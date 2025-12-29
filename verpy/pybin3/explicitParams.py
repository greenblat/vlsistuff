
def clog2(Prm):
    Res = len(bin(Prm))-2
    print("PPP",Prm,Res)
    return Res

import os,sys
import module_class
GenerateList = []
def help_main(Env):
    Mod = Env.Current
    if '-params' in Env.params:
        LL = Env.params['-params']
        for Txt in LL:
            WW = Txt.split()
            while WW != []:
                Prm = WW.pop(0)
                Val = WW.pop(0)
                Mod.parameters[Prm] = Val

    Changed = False
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        New = []
        for Param in Obj.params:
            Val = Obj.params[Param]
            Sval = module_class.pr_expr(Val)
            Val2 = eval(Sval,Mod.parameters,Mod.localparams)
            New.append((Param,Val2))
        New.sort()
        if New!=[]:
            GenerateList.append( ( Obj.Type,New))
            NewType = Obj.Type
            for (P,V) in New:
                NewType +=  '_%s_%s' % (P,V)
            Obj.Type = NewType
            Obj.params = {}
            Changed = True
    Modified = explicitName(Mod)
    if Changed or (Modified != Mod.Module):
        if not os.path.exists('paramed'):
            os.mkdir('paramed')
        Mod.Module = Modified
        Fout = open('paramed/%s.v' % Modified,'w')
        Mod.dump_verilog(Fout)
        Fout.close()

        for Module,Prms in GenerateList:
            Cmd1 = Cmd.replace('MOD',Module)
            Res = ''
            for P,V in Prms:
                Res += ' %s %s' % (P,V)
            Cmd2 = Cmd1.replace('PARAMS',Res)
            print(Cmd2)
                

    
Cmd = 'pyver.py rtl/MOD.v -do explicitParams -params "PARAMS"'

def explicitName(Mod):
    New = []
    for Param in Mod.parameters:
        Val = Mod.parameters[Param]
        if Param != '__builtins__':
            Val2 = Mod.compute_int(Val)
#            Sval = module_class.pr_expr(Val)
#            Sval = Sval.replace('$clog2','clog2')
#            Mod.localparams['clog2'] = clog2
#            print("SVAL",Sval)
#            Val2 = eval(Sval,Mod.parameters,Mod.localparams)
            New.append((Param,Val2))

    if New == []: return Mod.Module
    NewType = Mod.Module
    for (P,V) in New:
        NewType +=  '_%s_%s' % (P,V)
    return NewType
        
    
