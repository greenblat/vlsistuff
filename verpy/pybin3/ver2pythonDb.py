'''
takes verilog soft gatelevel synthesis results and creates python class ready to be used in ML travels

'''

import logs
import inspect
import json
import yaml

HEADER = '''
class MODClass:
    def __init__(self):
        self.Name = "MOD"
'''

class moduleClass:
    def __init__(self,Name):
        self.Name = Name
        self.netdirs = {}
        self.netwids = {}
        self.wires = {}
        self.insts = {}
        self.bufs = []
        self.libtypes0 = {}
        self.libtypes1 = {}
        self.types0 = {}
        self.types1 = {}

def help_main(Env):
    Mod = Env.Current
    Build = createBuild(Mod)
    dumpPython(Build,Mod)
    dumpYaml(Build,Mod)
    dumpJson(Build,Mod)

def dumpJson(Build,Mod):
    Fout = open('%s.json' % Mod.Module,'w')
    json.dump(Build.__dict__,Fout,indent=4)
    Fout.close()
    return

#     Fout.write('\ntypes0 =')
#     json.dump(Build.types0,Fout,indent=4)
#     Fout.write('\ntypes1 =')
#     json.dump(Build.types1,Fout,indent=4)
#     Fout.write('\nnetwids =')
#     json.dump(Build.netwids,Fout,indent=4)
#     Fout.write('\nnetdirs =')
#     json.dump(Build.netdirs,Fout,indent=4)
#     Fout.write('\ninsts = ')
#     json.dump(Build.insts,Fout,indent=4)
#     Fout.close()

def dumpYaml(Build,Mod):
    Fout = open('%s.yaml' % Mod.Module,'w')
    yaml.dump(Build,Fout)
    Fout.close()

def dumpPython(Build,Mod):
    Fout = open('%s.py' % Mod.Module,'w')
    Fout.write(HEADER.replace('MOD',Mod.Module))

    Fout.write('        self.types0 = {\n')
    Pref = ' '
    for Inst in Build.types0:
        Type =  Build.types0[Inst]
        Fout.write('           %s"%s":"%s"\n' % (Pref,Inst,Type))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.types1 = {\n')
    Pref = ' '
    for Type in Build.types1:
        List =  Build.types1[Type]
        Fout.write('           %s"%s" : %s\n' % (Pref,Type,repr(List)))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.libtypes0 = {\n')
    Pref = ' '
    for Inst in Build.libtypes0:
        Type =  Build.libtypes0[Inst]
        Fout.write('           %s"%s":"%s"\n' % (Pref,Inst,Type))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.libtypes1 = {\n')
    Pref = ' '
    for Type in Build.libtypes1:
        List =  Build.libtypes1[Type]
        Fout.write('           %s"%s" : %s\n' % (Pref,Type,repr(List)))
        Pref = ','
    Fout.write('        }\n')



    Fout.write('        self.netwids = {\n')
    Pref = ' '
    for Net in Build.netwids:
        Wid =  Build.netwids[Net]
        Fout.write('           %s"%s" : %s\n' % (Pref,Net,Wid))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.netdirs = {\n')
    Pref = ' '
    for Net in Build.netdirs:
        Dir =  Build.netdirs[Net]
        Fout.write('           %s"%s" : "%s"\n' % (Pref,Net,Dir))
        Pref = ','
    Fout.write('        }\n')

    Fout.write('        self.wires = {\n')
    Pref = ' '
    for Net in Build.wires:
        Wid =  Build.wires[Net]
        Fout.write('           %s"%s" : "%s"\n' % (Pref,Net,Wid))
        Pref = ','
    Fout.write('        }\n')


    Fout.write('        self.conns = {\n')
    Pref = ' '
    for Inst in Build.insts:
        Conns =  Build.insts[Inst]
        Fout.write('           %s"%s" : %s\n' % (Pref,Inst,repr(Conns)))
        Pref = ','
    Fout.write('        }\n')

    Fout.close()


#    source_code = inspect.getsource(Build)
#    Fout.write(source_code)

def createBuild(Mod):
    Build = moduleClass(Mod.Module)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Width = getWid(Wid)
        if isSynWire(Net):
            Build.wires[Net] = Width
        else:
            Build.netdirs[Net] = Dir
            Build.netwids[Net] = Width
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        if libType(Type):
            Build.libtypes0[Inst] = Type
            if Type  not in Build.libtypes1: Build.libtypes1[Type] = []
            Build.libtypes1[Type].append(Inst)
            Build.insts[Inst] = {}
            for Pin in Mod.insts[Inst].conns:
                Sig = Mod.insts[Inst].conns[Pin]
                Sig1 = Mod.pr_expr(Sig)
                Build.insts[Inst][Pin] = Sig1
        else:
            Build.types0[Inst] = Type
            if Type  not in Build.types1: Build.types1[Type] = []
            Build.types1[Type].append(Inst)
            Build.insts[Inst] = {}
            for Pin in Mod.insts[Inst].conns:
                Sig = Mod.insts[Inst].conns[Pin]
                Sig1 = Mod.pr_expr(Sig)
                Build.insts[Inst][Pin] = Sig1

#        Build.insts[Inst] = Mod.insts[Inst].conns
    return Build


def getWid(Wid):
    if Wid == 0: return 1
    if type(Wid) is int: return Wid
    if type(Wid) is list:
        if len(Wid) == 2:
            if (type(Wid[0]) is int) and (type(Wid[1]) is int):
                return Wid[0]-Wid[1]+1
            try:
                Hi = int(Wid[0])
                Lo = int(Wid[1])
                return Hi-Lo
            except:
                return ('+',Wid[0],1)
    if type(Wid) is tuple:
        if len(Wid) == 2:
            if (type(Wid[0]) is int) and (type(Wid[1]) is int):
                return Wid[0]-Wid[1]+1
            try:
                Hi = int(Wid[0])
                Lo = int(Wid[1])
                return Hi-Lo
            except:
                return ('+',Wid[0],1)


    logs.log_error('getWid got "%s"' % (str(Wid)))

    return 1

def isSynWire(Net):
    if type(Net) is not str: return False
    return  (Net[0] == '_') and (Net[-1] == '_')
        
def libType(Type):
    return Type.startswith('scs130ms_')



