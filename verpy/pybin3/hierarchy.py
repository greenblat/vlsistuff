



import os,sys
import logs
import db0 
import traceback

'''
make nice drawing out of hiearchy 
'''

Dones = {}
def help_main(Env):
    if Env.Current==None:
        logs.log_err('no module to work on')
        return

    Fout = open('%s.dot' % Env.Current.Module,'w')
    Fout.write('digraph hierarchy {\n')
    Dones[Env.Current.Module]=True
#    scan_deep(Env,Env.Current,Env.Current.Module,Env.Current.Module,Fout)
    Stops = []
    if '-stop' in Env.params:
        Stops = Env.params['-stop']
    Splits = []
    if '-split' in Env.params:
        Splits = Env.params['-split']
    Dones2 = []
    print("STOPS",Stops)
    scan_deep2(Env,Env.Current,6,Dones2,Fout,Stops,Splits)

    Fout.write('}\n')
    Fout.close()
    os.system('dot -Tsvg %s.dot -o %s.svg' % (Env.Current.Module,Env.Current.Module))
    os.system('dot -Tpng %s.dot -o %s.png' % (Env.Current.Module,Env.Current.Module))
    secondRun(Env,Env.Current)
    thirdRun(Env,Env.Current)
    preparePythonHierarch(Env,Env.Current)

def scan_deep2(Env,Mod,Deep,Dones,Fout,Stops,Splits):
    if Deep == 0: return
    if Mod.Module in Stops: return
    if Mod.Module in Dones: return
    Inventory = {}
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if Type in Inventory: 
            Inventory[Type] += 1
        else:
            Inventory[Type] = 1
    LL = list(Inventory.keys())
    LL.sort()
    LL.reverse()
    for Type in LL:
        if Type in Splits:
            Let = logs.incrVar(Type)
            Fout.write('%s  -> %s_%d [label="%s"] ; \n'%(Mod.Module,Type,Let,Inventory[Type]))
        else:
            Fout.write('%s  -> %s [label="%s"] ; \n'%(Mod.Module,Type,Inventory[Type]))
        print("INV %s %s  %s" % (Mod.Module,Type,Inventory[Type]))
    Dones.append(Mod.Module)
    for Type in LL:
        if Type not in Stops:
            Env.try_and_load_module(Type,Env)
            if Type in Env.Modules:
                scan_deep2(Env,Env.Modules[Type],Deep-1,Dones,Fout,Stops,Splits)



def scan_deep(Env,Mod,Ftype,Finst,Fout):
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        Down = '%s_%s'%(Inst,Type)
        Fout.write('%s  -> %s [label="%s"] ; \n'%(Finst,Inst,Type))
        if Down not in Dones:
            Dones[Down]=1
            Env.try_and_load_module(Type,Env)
            if Type in Env.Modules:
                scan_deep(Env,Env.Modules[Type],Type,Inst,Fout)
                
def preparePythonHierarch(Env,Mod):
    Fhier = open('%s_hier.py' % Mod.Module,'w')
    Fhier.write('HIER = {}\n')
    __preparePythonHierarch(Env,Mod,Mod.Module,Fhier)
    Fhier.close()

def __preparePythonHierarch(Env,Mod,Path,Fhier):
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        Pathd = Path + '.' + Inst
        registerPath(Pathd,Inst,Type,Fhier)
        if Type in Env.Modules:
            Down = Env.Modules[Type]
            __preparePythonHierarch(Env,Down,Pathd,Fhier)
            
def registerPath(Pathd,Inst,Type,Fhier):
    Fhier.write('HIER["%s"] = "%s","%s"\n' % (Pathd,Type,Inst))
        


def thirdRun(Env,Mod):
    Queue = [Mod.Module]
    Dones = []
    while Queue!=[]:
        Module = Queue.pop(0)
        Mod = Env.Modules[Module]
        for Inst in Mod.insts:
            Type = Mod.insts[Inst].Type
            if Type in Env.Modules:
                instPins = Mod.insts[Inst].conns.keys()
                typePins = getIOPins(Env.Modules[Type])
                Mut=[]
                for AA in instPins:
                    if AA in typePins:
                        Mut.append(AA)
                for Pin in instPins:
                    if Pin not in Mut:
                        logs.log_error('pin %s is in instance %s %s but not in module'%(Pin,Inst,Type))
                for Pin in typePins:
                    if Pin not in Mut:
                        logs.log_error('pin %s is in module %s but not in  instance %s '%(Pin,Type,Inst))

            if (Type not in Dones)and(Type not in Queue)and(Type in Env.Modules): 
                Queue.append(Type)
        Dones.append(Module)

def getIOPins(Mod):
    IO=[]
    for Net in Mod.nets:
        if 'input' in Mod.nets[Net][0]:
            IO.append(Net)
        elif 'output' in Mod.nets[Net][0]:
            IO.append(Net)
    return IO

def secondRun(Env,Mod):
    Dones=[]
    Fout2 = open('new2.dot','w')
    Fout2.write('digraph hierarchy {\n')
    Queue = [Mod.Module]
    while Queue!=[]:
        Module = Queue.pop(0)
        Mod = Env.Modules[Module]
        This = []
        for Inst in Mod.insts:
            Type = Mod.insts[Inst].Type
            if Type not in This:
                Fout2.write('%s -> %s;\n'%(Mod.Module,Type))
                This.append(Type)
            if (Type not in Dones)and(Type not in Queue)and(Type in Env.Modules): Queue.append(Type)
    Fout2.write('}\n')
    Fout2.close()
    os.system('dot -Tpng new2.dot -o new2.png')



