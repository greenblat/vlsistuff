
import logs

def help_main(Env):
    Mod = Env.Current
    Fout = open('%s.vx'%Mod.Module,'w')
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if (type(Wid) is tuple)or(type(Wid) is list):
            Widx = int(Wid[0])-int(Wid[1])+1
            Fout.write('net %s | width=%d ;\n'%(Net,Widx))
    Inserts,Extracts = [],[]
    for Inst in Mod.insts:
        Type = Mod.insts[Inst].Type
        Obj = Mod.insts[Inst]
        if Type in renames:
            Type0 = renames[Type] 
        else:
            logs.log_error('type %s is not renamed'%Type)
            Type0 = Type.lower() 
        Str = 'inst %s %s '%(Type0,Inst)
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Pin,Dir = pinDir(Pin,Type)

            if type(Sig) is list:
                if Sig[0]=='subbit':
                    New = '%s_%s_'%(Sig[1],Sig[2])
                    DD,_ = Mod.nets[Sig[1]]
                    if (Dir=='<'):
                        if (Sig[1],Sig[2]) not in Extracts:
                            Extracts.append((Sig[1],Sig[2]))
                    elif (Dir=='>'):
                        if (Sig[1],Sig[2]) not in Inserts:
                            Inserts.append((Sig[1],Sig[2]))
                    Sig = New

            Str += '%s%s%s '%(Pin,Dir,Sig)
        Fout.write('%s\n'%Str)
    BUF = 0
    for Dst,Src,_,_ in Mod.hard_assigns:
        if simple(Dst) and simple(Src):
            Fout.write('inst buf bufx%s a<%s o>%s ;\n'%(BUF,Src,Dst))
            BUF += 1
        else:
            print('ddd',Dst)
            print('sss',Src)

    Inserts.sort()
    Extracts.sort()
    for SigInd in Inserts:
        if SigInd in Extracts:
            II = Extracts.index(SigInd)
            Extracts.pop(II)
    for ind,(Sig,Dig) in enumerate(Inserts):
        Fout.write('inst insert insrert%d a<%s_%s_ o>%s | index=%s ;\n'%(ind,Sig,Dig,Sig,Dig))

    for ind,(Sig,Dig) in enumerate(Extracts):
        Fout.write('inst extract extract%d a<%s o>%s_%s_ | index=%s ;\n'%(ind,Sig,Sig,Dig,Dig))


    Fout.close()

def simple(Txt):
    if type(Txt) is int: return True
    if type(Txt) is str: return True
    return False

def pinDir(Pin,Type):
    Pin = renamePin(Type,Pin)
    if Pin in ['o','q']: return Pin,'>'
    return Pin,'<'

def renamePin(Type,Pin):
    if Pin in renames: 
        return renames[Pin]
        
    logs.log_error('type %s pin %s is not translated'%(Type,Pin))

renames = { 'DFF':'dff','A':'a','B':'b','C':'c','Y':'o','CK':'clk','SEL':'sel','Q':'q','D':'d'
    ,'NAND2':'nand2' ,'NAND3':'nand3'
    ,'NOR2':'nor2' ,'NOR3':'nor3'
    ,'AND2':'and2' ,'AND3':'and3'
    ,'OR2':'or2' ,'OR3':'or3'
    ,'XOR2':'xor2' ,'XOR3':'xor3'
    ,'XNOR2':'xnor2' ,'XNOR3':'xnor3'
    ,'MUX2':'mux2' ,'INV':'inv','BUF':'buf'
}


