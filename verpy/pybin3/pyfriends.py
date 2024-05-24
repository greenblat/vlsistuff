


import logs


def help_main(Env):
    Mod = Env.Current
    Name = Mod.Module
    Name = Name.replace('_friend','')

#    Flist = open('holder/%s.list' % Name)
#    List = (Flist.read()).split()
    Fout = open('class_%s.py' % Name,'w')
    Fout.write('import logs\n')
    Fout.write('from friendly_lib import *\n')
    Fout.write('class class_%s(logs.driverClass):\n' % Name)
    Fout.write('    def __init__(self,Path):\n')
    Fout.write('        logs.driverClass.__init__(self,Path,[])\n')
    Fout.write('        self.Insts = []\n')
    Fout.write('        self.Nets = {}\n')
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        Conns = {}
        for Prm in Obj.params:
            Val = str(Obj.params[Prm])
            Conns[Prm] = Val.replace('"','')
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sig = Mod.pr_expr(Sig)
            Sig = Sig.replace('&&','and')
            Sig = Sig.replace('||','or')
            Sig = Sig.replace('!','not')
            Sig = Sig.replace('not=','!=')
            Conns[Pin] = Sig.replace('"','')
            
        Fout.write('        self.Insts.append(("%s",class_%s(%s)))\n' % (Inst,Obj.Type,Conns))
    for Dst,Src,_,_ in Mod.hard_assigns:
        if type(Src) is str:
            Conns = {'din':Src,'dout':Dst}
            Fout.write('        self.Insts.append(("copy",class_copy(%s)))\n' % (Conns))
        else:
            logs.log_error('HARD_ASSIGN %s %s' % (Dst,Src))


    Fout.write('    def run(self):\n')
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if Dir == 'input':
            Fout.write('        self.Nets["%s"] = self.peek("%s")\n' % (Net,Net))
        
#    Fout.write('        for Inst,Obj in self.Insts:\n')
#    Fout.write('            Obj.run(Inst,self.Nets)\n')
    Fout.write(FINAL)
    Fout.close()

FINAL='''
        for Inst,Obj in self.Insts:
            if ('dout' in Obj.conns) and (Inst != 'copy'):
                Obj.run(Inst,self.Nets)
        for Inst,Obj in self.Insts:
            if (Inst == 'copy'):
                Obj.run(Inst,self.Nets)
        for Inst,Obj in self.Insts:
            if ('dout' not in Obj.conns):
                Obj.run(Inst,self.Nets)
'''


