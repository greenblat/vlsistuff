



def dumpUser(self,Mod,File):
    File.write('module %s user format\n' % Mod.Module)
    for Inp in self.Inps:
        Rinp = reworkPort(Inp)
        File.write('    input %s\n'%(Rinp))
    for Out in self.Outs:
        Rout = reworkPort(Out)
        File.write('    output %s\n'%(Rout))
    for Out in self.Inouts:
        Rout = reworkPort(Out)
        File.write('    inout %s\n'%(Rout))

    for Inst in Mod.instances:
        dumpInstance(Inst,Mod.instances[Inst],self,Mod,File)

    for DstSrc in self.hard_assigns:
        Dst = DstSrc[0]
        Src = DstSrc[1]
        File.write('assign %s = %s;\n' % (Dst,Src))
    File.write('endmodule\n')
    File.close()


def reworkPort(Port):
    return Port


NONISSUES = ['vcc','gnd','antenna','input','output','inout','node','logo']

def dumpInstance(Inst,Obj,self,Mod,File):
    if Inst in self.Names:
        Name = self.Names[Inst]
    else:
        Name = Obj.Inst
    if (Obj.Type not in NONISSUES)and('logo' not in Obj.Type)and('ilia' not in Obj.Type):
        if Inst in self.Params:
            PP = []
            for Prm,Val in self.Params[Inst]:
                Str='.%s(%s)'%(Prm,Val)
                if Prm!='name': PP.append(Str)
            ObjParams = '#(%s)'%(','.join(PP))
        else:
            ObjParams= ''
        File.write('%s %s %s ('%(Obj.Type,ObjParams,Name))
        if Inst in self.Conns:
            Pref = ''
            Pins  = self.Conns[Inst]
            for Pin in Pins:
                File.write(' %s.%s(%s)\n'%(Pref,Pin,Pins[Pin]))
                Pref = ','

        File.write(');\n')


