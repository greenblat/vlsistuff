
import string

def dumpVerilog(Glbs,Root,File):
    global Names,Nodes
    Mod = Glbs.details[Root]
    Names={}
    Params={}
    Nodes={}
    Wnodes={}
    for Key in Mod.params:
        Obj = Mod.params[Key]
        if (Obj.Param=='name')and(Obj.Value!='$inst'):
            Names[Obj.Owner]=Obj.Value
        elif Obj.Owner not in Params:
            Params[Obj.Owner]=[(Obj.Param,Obj.Value)]
        else:
            Params[Obj.Owner].append((Obj.Param,Obj.Value))
    print("NAMES",Names)
    Inps={}
    Outs={}
    Conns={}
    for Inst in Mod.instances:
        Obj = Mod.instances[Inst]
        if Obj.Type=='input':
            if Inst in Names:
                Inps[Names[Inst]]=Inst
            else:
                Inps[Inst]=Inst
                Names[Inst]=Inst
        elif Obj.Type=='output':
            if Inst in Names:
                Outs[Names[Inst]]=Inst
            else:
                Outs[Inst]=Inst
                Names[Inst]=Inst
        elif Obj.Type=='node':
            Nodes[Inst]=[]
                
    for Wire in Mod.wires:
        Wnodes[Wire]=[]
        Obj = Mod.wires[Wire]
        Start = Obj.Start
        End = Obj.End
        if Start in Nodes:
            Wnodes[Wire].append(Start)
            if Wire not in Nodes[Start]:
                Nodes[Start].append(Wire)
        if End in Nodes:
            Wnodes[Wire].append(End)
            if Wire not in Nodes[End]:
                Nodes[End].append(Wire)

    for Wire in Mod.wires:
        Obj = Mod.wires[Wire]
        Start = Obj.Start
        End = Obj.End
        if Start in Names:
            Wname = Names[Start]
            Names[Wire]=Wname
            for Node in Wnodes[Wire]:
                for Wire1 in Nodes[Node]:
                    Names[Wire1]=Wname
        if End in Names:
            Wname = Names[End]
            Names[Wire]=Wname
            for Node in Wnodes[Wire]:
                for Wire1 in Nodes[Node]:
                    Names[Wire1]=Wname
                
    spread_the_joy()
    for Wire in Mod.wires:
        if Wire not in Names:
            Names[Wire]=Wire
            spread_the_joy()

    for Wire in Mod.wires:
        Obj = Mod.wires[Wire]
        Start = Obj.Start
        End = Obj.End

        if Wire in Names:
            Wname=Names[Wire]
        else:
            Wname=Wire
            
        if '.' in Start:
            pp = Start.split('.')
            Pin = pp[1]
            Inst=pp[0]
            if Inst not in Conns:
                Conns[Inst]={}
            Conns[Inst][Pin]=Wname

        if '.' in End:
            pp = End.split('.')
            Pin = pp[1]
            Inst=pp[0]
            if Inst not in Conns:
                Conns[Inst]={}
            Conns[Inst][Pin]=Wname



    File.write('Xmodule %s ('%Mod.Module)
    Pref=' '
    for Inp in Inps:
        File.write('    %sinput %s\n'%(Pref,Inp))
        Pref=','
    for Out in Outs:
        File.write('    %soutput %s\n'%(Pref,Out))
        Pref=','
    File.write(');\n')
    for Inst in Mod.instances:
        Obj = Mod.instances[Inst]
        if Inst in Names:
            Name = Names[Inst]
        else:
            Name = Obj.Inst
        if (Obj.Type not in ['input','output','node'])and('logo' not in Obj.Type):
            if Inst in Params:
                PP = []
                for Prm,Val in Params[Inst]:
                    Val1 = make_legal(Val)
                    Str='.%s(%s)'%(Prm,Val1)
                    if Prm!='name': PP.append(Str)
                ObjParams = '#(%s)'%(','.join(PP))
            else:
                ObjParams='#(%d,%d)'%(Obj.Point)

            File.write('%s %s %s ('%(Obj.Type,ObjParams,Name))
#            print("XXXXXX",Inst,Obj.Type,Conns[Inst])
            if Inst in Conns:
                Pref = ''
                Pins  = Conns[Inst]
                for Pin in Pins:
                    File.write(' %s.%s(%s)\n'%(Pref,Pin,Pins[Pin]))
                    Pref = ','
                 
            File.write(');\n')
    File.write('endmodule\n')


def make_legal(Txt):
    if (Txt[0] in string.letters):
        return Txt

    if Txt[0] in string.digits:
        try:
            x = int(Txt)
            return Txt
        except:
            return '_%s'%Txt
    return Txt

def spread_the_joy():
    dones=1
    while dones:
        dones=0
        for Node in Nodes:
            List = Nodes[Node]
            Name=False
            for Wire in List:
                if Wire in Names:
                    Name=Names[Wire]
            if Name:
                for Wire in List:
                    if Wire not in Names:
                        Names[Wire]=Name
                        dones +=1
