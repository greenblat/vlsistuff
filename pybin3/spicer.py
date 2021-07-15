#! /usr/bin/env python3

import sys,os,string

header=''
currentCellName='***'



REPLACEMENTS = { '\<':'[','\>':']' }

def main():
    global Spfile
    global Odir
    doing_cadence=True
    argv = sys.argv
    Fname = argv[1]
    if (len(argv)>2):
        Odir = argv[2]
    else:
        Odir = 'tmpv'
    if (len(argv)>3):
        Style = argv[3]
        if (Style[0]=='c'):
            doing_cadence=True
        else:
            doing_cadence = False
    File = open(Fname,'r')
    Spfile = open('all_trans.com','w')
    os.system('mkdir '+Odir)
    if (doing_cadence):
        print('doing cadence spice')
        cadence_spice(File)
    else:
        print('doing regular spice')
        regular_spice(File,Fname)
    File.close()
    List=[]
    for Mod in Modules:
        Mos = Modules[Mod].moses
        print('CellLib["%s"].mos_count = %s'%(Mod.upper(),Mos))
#        List.append((Modules[Mod].get_total(),Mod))
#        Modules[Mod].recognizeInvs()
#        Modules[Mod].recognizeCmos()
#        Modules[Mod].dumpDraw()
    List.sort()
    List.reverse()
    for Tot,Mod in List:
        print('%10d   %s'%(Tot,Mod))





def regular_spice(File,Fname):
    filter0(File)
    File.close()
    File = open(Fname,'r')
    filter1(File)
    File.close()
    Spfile.close()

def cadence_spice(File):
    lines = scan_file(File)
    print('len %d'%len(lines))
    gather_headers(lines)
    write_verilogs(lines)

Headers = {}

def write_verilogs(lines):
    state='idle'
    for line in lines:
        line = line.lower()
        line = line.replace('(',' ( ')
        line = line.replace(')',' ) ')
        wrds = line.split()
        print('wrds0',wrds[0])
        if (wrds[0] in ['subckt','.subckt']):
            state='cell'
            Cell = wrds[1]
            Modules[Cell]=moduleClass(Cell)
            File = open('%s/%s.v'%(Odir,Cell),'w')
            File.write('module %s ('%(Cell))
            Nobus = []
            Bussed = {}
            for wrd in wrds[2:]:
                if ('=' not in wrd):
                    wrd = useReplacements(wrd)
                    if '[' in wrd:
                        Bus,Ind = parseNet(wrd)
                        if Bus not in Bussed: Bussed[Bus] = []
                        Bussed[Bus].append(Ind)
                    else:
                        Nobus.append(wrd)

            Nobus.sort()

            Pref = ' '
            for wrd in Nobus:
                if ('=' not in wrd):
                    File.write('   %sinout %s\n'%(Pref,wrd))
                    Pref=','

            Keys = list(Bussed.keys())
            Keys.sort()
            for Bus in Keys:
                LLL = Bussed[Bus]
                LLL.sort()
                File.write('   %sinout [%d:%d] %s\n'%(Pref,LLL[-1],LLL[0],Bus))
                Pref=','
            File.write(');\n')
        elif (wrds[0]=='ends'):
            File.write('endmodule\n')
            File.close()
            state='idle'
        else:
            if (state!='idle'):
                print('>>>>',wrds)
                Inst = clean_sig(wrds[0])
                St = wrds.index('(')
                En = wrds.index(')')
                Nets = list(map(useReplacements,wrds[St+1:En]))
                Type = wrds[En+1]
                Modules[Cell].add_son(Type,Inst)
                if (Type in Headers):
                    Pins = Headers[Type]
                    Conns=[]
                    Bussed = {}
                    for i in range(len(Nets)):    
                        if '[' in Pins[i]:
                            Bus,Ind0,Net,Ind1 = parseConn(Pins[i],Nets[i])
                            if Bus not in Bussed: Bussed[Bus] = []
                            Bussed[Bus].append((Ind0,Ind1,Net))
                            
                        else:
                            PN = '.%s(%s)'%(Pins[i],Nets[i])
                            Conns += [PN]

                    File.write('%s %s( %s '%(Type,Inst,', '.join(Conns)))
                    
                    for Bus in Bussed:
                        LL = Bussed[Bus]
                        LL.sort()
                        LL.reverse()
                        Res = []
                        High = LL[0][1]
                        Runbus = LL[0][2]
                        Runind = LL[0][1]
                        for _,Indx,Nbus in LL[1:]:
                            if (Indx == (Runind-1))and(Nbus==Runbus):
                                Runind = Indx
                            elif (Runind==High):
                                if High== -1:
                                    Res.append('%s'%(Runbus))
                                else:
                                    Res.append('%s[%s]'%(Runbus,High))
                                Runbus = Nbus
                                High = Indx 
                                Runind = Indx
                            else:
                                Res.append('%s[%s:%s]'%(Runbus,High,Runind))
                                Runbus = Nbus
                                High = Indx 
                                Runind = Indx
                        if (Runind==High):                                
                            Res.append('%s[%s]'%(Runbus,High))
                        else:
                            Res.append('%s[%s:%s]'%(Runbus,High,Runind))
                                
                        Conns = ','.join(Res)                                
                        if len(Res)==1:
                            File.write('\n    ,.%s(%s)'%(Bus,Conns))
                        else:
                            File.write('\n    ,.%s({%s})'%(Bus,Conns))
                    File.write(');\n')
                else:
                    Params = wrds[En+2:]
                    if Inst[0] in 'Mm':
                        S,G,D,B = Nets
                        if G == '0': G = 'vss'
                        if D == '0': D = 'vss'
                        if S == '0': S = 'vss'

                        if G[0] in '0123456789': G = 'nn'+G
                        if D[0] in '0123456789': D = 'nn'+D
                        if S[0] in '0123456789': S = 'nn'+S

                        Conns = '.s(%s),.g(%s),.d(%s),.b(%s)'%(S,G,D,B)
                        if Type[0] in 'pP':
                            File.write('pmos_tran %s( %s );\n'%(Inst,Conns))
                        elif Type[0] in 'nN':
                            File.write('nmos_tran %s( %s );\n'%(Inst,Conns))
                        else:
                            print('error trans typ is %s %s'%(Inst,Type))
                    else:
                        File.write('%s %s( %s );\n'%(Type,Inst,', '.join(Nets)))



def gather_headers(lines):
    for line in lines:
        line = line.lower()
        wrds = line.split()
        print(wrds[0])
        if (wrds[0]=='subckt'):
            heads=[]
            for wrd in wrds:
                if ('=' not in wrd):
                    wrd = useReplacements(wrd)
                    heads += [wrd]
            Cell = wrds[1]
            Pins = list(map(useReplacements,wrds[2:]))
            Headers[Cell]=Pins    
            print('header of %s == %s'%(Cell,len(Pins)))

def scan_file(File):
    lines = File.readlines()
    i=0
    while i<len(lines):
        line = lines[i]
        line = line[:-1]
        wrds = line.split()
        if (len(wrds)==0):    
            lines.pop(i)
        elif (line[-1]=='\\'):
            line = line[:-1]
            line = line + ' ' + lines[i+1]
            lines[i]=line
            lines.pop(i+1)
        elif (len(line)>2)and(line[0:2]=='//'):
            lines.pop(i)
        else:
            i +=1
    return lines


def filter0(File):
    global header
    holder=''
    header=''
    dones = 0
    guard = 100000
    Ok=1
    state=0
    while (Ok):
        line = File.readline()
        if (len(line)==0):
            break
    
        dones = dones+1
        guard=guard-1
        if (guard==0):
            guard=100000
            print(dones,len(header),len(holder))
        line = line.lower()
        wrds = line.split()
        if (state==0):
            if (len(wrds)>1)and(wrds[0]=='.subckt'):
                header = line[:-1]
                state=1
        elif (state==1):
            if (line[0]=='+'):
                header = header + ' '+line[1:-1]
            else:
                header,prms = remove_params(header)
                use_header(header,prms)
                header=''
                state=2
                holder=line[:-1]
                if (len(wrds)>1)and(wrds[0]=='*.pininfo'):
                    work_on_pininfo(currentCellName,wrds)
                if (len(wrds)>0)and(wrds[0]=='.ends'):
                    state=0
                    holder=''
        elif (state==2):
            if (line[0]=='+'):
                holder = holder + ' '+clean_params(line[1:-1])
            else:
                holder = line[:-1]
                if (len(wrds)>1)and(wrds[0]=='*.pininfo'):
                    work_on_pininfo(currentCellName,wrds)
            if (len(wrds)>0)and(wrds[0]=='.ends'):
                state=0
                holder=''

def remove_params(In):
    wrds = In.split()
    res = ''
    params = []
    for wrd in wrds:
        if ('=' in wrd):
            params.append(wrd)
        else:
            res = res + ' '+wrd
    return res,params



def filter1(File):
    header=''
    holder=''
    dones = 0
    guard = 100000
    Ok=1
    state=0
    while (Ok):
        line = File.readline()
        if (len(line)==0):
            break
    
        dones = dones+1
        guard=guard-1
        if (guard==0):
            guard=100000
            print(dones,len(header),len(holder))
        line = line.lower()
        if (state==0):
            wrds = line.split()
            if (len(wrds)>1)and(wrds[0]=='.subckt'):
                print('opening ',wrds[1])
                header = line[:-1]
                state=1
        elif (state==1):
            if (line[0]=='+'):
                header = header + ' '+line[1:-1]
            else:
                header,prms=remove_params(header)
                push_line(header,prms)
                header=''
                state=2
                holder=line[:-1]
        elif (state==2):
            if (line[0]=='+'):
                holder = holder + ' '+line[1:-1]
            else:
                holder,prms=remove_params(holder)
                push_line(holder,prms)
                holder = line[:-1]
            if (len(line)>4)and(line[0:5]=='.ends'):
                state=0
                push_line(holder,prms)
                holder=''


def clean_sig(word):
    if (len(word)>0)and(word[0]=='\\'):
        word  = word[1:]
    word = word.replace('\\','_')
    word = word.replace('!','')
    for Chr in '/\[].<>$':
        word = word.replace(Chr,'_')
    word = word.replace('__','_')
    if (word=='output'):
        word='out'
    if (len(word)>0)and(word[0] in '0123456789'):
        word = 'sig'+word
    while (len(word)>1)and(word[-1]=='_'):
        word=word[:-1]
    return word



def clean_params(line):
    wrds = line.split()
    res = []
    params = []
    for word in wrds:
        if ('=' not in word):
            res.append(word)
        else:
            params.append(word)
    return ' '.join(res)

filt2_state=0

def use_header(line,prms):
    global Headers,currentCellName
    wrds = line.split()
    if (wrds[0]=='.subckt'):
        Cell = wrds[1]
        currentCellName=Cell
        Pins = []
        for word in wrds[2:]:
            if ('=' not in word):
                Pins = Pins+[word]

        print('opening 281 ',Cell)
        Modules[Cell]=moduleClass(Cell,Pins,prms)

        if (Cell in Headers):
            print('header contention ',Cell,'pins=',Headers[Cell])
        else:
            Headers[Cell]=Pins    
            print('header added ',Cell,len(Pins))
    else:
        print('error!!! use_header got %s'%line)



def push_line(line,prms):
    global Headers
    global filt2_state
    global Vfile
    global Cell
    if (len(line)==0)or(line[0]=='*'):
        return
    wrds = line.split()
    if (len(wrds)==0):
        return
    if ((wrds[0])[0]=='*'):
        return
    wrds2 = wrds
    wrds = []
    for word in wrds2:
        if ('=' not in word):
            wrds = wrds + [clean_sig(word)]
        else:
            wrds = wrds + [word]
    if (filt2_state==0):
        if (wrds[0]=='_subckt'):
            filt2_state=1
            Cell = clean_sig(wrds[1])
            print('opening 328 ',Cell)
            if Cell not in Modules:
                Modules[Cell]=moduleClass(Cell)
            Pins = []
            for word in wrds[2:]:
                if ('=' not in word):
                    Pins = Pins+[clean_sig(word)]
            Vfile = open(Odir+'/'+Cell+'.v','w')
            write_header(Vfile,Cell,Pins)
    elif (filt2_state==1):
        if (wrds[0]=='_ends'):
            Vfile.write('endmodule\n')
            Vfile.close()
            filt2_state=0
        else:
            write_comp(Vfile,wrds)
            Modules[currentCellName].addComp(wrds,prms)
            
        
def write_header(Vfile,Cell,Pins):
    Vfile.write('module '+Cell+' (\n')
    Pref = ' '
    for Pin in Pins:
        Dir = get_dir(Cell,Pin)
        Vfile.write('    '+Pref+Dir+' '+clean_sig(Pin)+'\n')
        Pref=','
    Vfile.write(');\n')

def write_comp(Vfile,wrds):
    wrd0=wrds[0]
    if (wrd0[0]=='x'):
        write_xcomp(Vfile,wrds)
    elif (wrd0[0]=='m'):
        print('<<<<<<<',wrds)
        write_mos(Vfile,wrds)
        Modules[Cell].add_mos()
    elif (wrd0[0]=='r'):
        write_res(Vfile,wrds)
    elif (wrd0[0]=='d'):
        write_diode(Vfile,wrds)
    elif (wrd0[0]=='q'):
        write_bipolar(Vfile,wrds)
    else:
        print('error unknown device ','"'+' '.join(wrds)+'"')

def write_bipolar(Vfile,wrds):
    Inst = wrds[0]
    P1 = wrds[1]
    P2 = wrds[2]
    P3 = wrds[3]
    Type = wrds[4]+'bipolar'
    Vfile.write('%s %s(.p1(%s ),.p2(%s ),.p3(%s ));\n'%(Type,Inst,P1,P2,P3));
    return
def write_diode(Vfile,wrds):
    print('diode disregarded ',wrds)
    Vfile.write('// diode disregarded %s\n'%(str(wrds)));
    return
def write_mos(Vfile,wrds):
    Inst = wrds[0]
    S = wrds[1]
    G = wrds[2]
    D = wrds[3]
    B = wrds[4]
    Type = wrds[5]+'mos_tran'
    Vfile.write('%s %s(.s(%s ),.d(%s ),.g(%s ),.b(%s ));\n'%(Type,Inst,S,D,G,B));

def write_res(Vfile,wrds):
    Inst = wrds[0]
    S = wrds[1]
    D = wrds[2]
    Type = 'res'
    Vfile.write('%s %s(.a(%s ),.b(%s ));\n'%(Type,Inst,S,D));


def write_xcomp(Vfile,wrds):
    Cons = []
    for word in wrds[1:]:
         if ('=' not in word):
            Cons = Cons+[word]
    if (len(Cons)==0):
        return
    Type = Cons[-1]
    Cons = Cons[:-1]
    Inst = clean_sig(wrds[0])
    Modules[Cell].add_son(Type,Inst)
    if (len(Type)>0)and(Type[0] in '0123456789'):
        Type = 'x'+Type
    Type = clean_sig(Type)
    Vfile.write('%s %s (\n'%(Type,Inst)),
    if (len(Cons)>1)and(Cons[-1]=='_'):
        Cons = Cons[:-1]
    if (Type in Headers):
        Pins = Headers[Type]
    else:
        Ind = range(0,len(Cons))
        Pins=[]
        for i in Ind:
            Pins = Pins + ['pin'+str(i)]
    IndP = len(Pins)
    IndC = len(Cons)
    Ind = min(IndP,IndC)
    if (IndC!=IndP):
        print('error type=',Type," lenpins=",IndP," lencons=",IndC," inst=",Inst,Cons)
    Pref=' '
    for I in range(0,Ind):
        Vfile.write('    %s.%s (%s )\n'%(Pref,clean_sig(Pins[I]),Cons[I]))
        Pref=','
    WL = []
    for word in wrds[1:]:
        if ('=' not in word):
             PV = word.split('=')
             if (len(PV)==2)and(PV[0] in ['w','l']):
                WL = WL + [(PV[0],PV[1])]
                    
    Vfile.write(');\n')
    if (len(WL)>0):
        Vfile.write('// spice: %s %s %s '%(Cell,Type,Inst))
        Spfile.write('spice_mos(%s,%s,[(name,%s)'%(Cell,Type,Inst))
        for (P,V) in WL:
            if (V[-1]=='u'):
                V=V[:-1]
            Vfile.write(',(%s,%s)'%(P,V))
            Spfile.write(',(%s,%s)'%(P,V))
        Vfile.write('\n')
        Spfile.write(']).\n')

def work_on_pininfo(currentCellName,wrds):
    for word in wrds:
        wx = word.split(':')
        if (len(wx)==2):
            make_dir(wx[0],wx[1],currentCellName)

dirs = {}
def make_dir(Sig,Dir,Cell):
    global dirs
    Dir = Dir.lower()
    if (Dir=='i'):
        Dir='input'
    elif (Dir=='o'):
        Dir='output'
    elif (Dir=='b'):
        Dir='inout'
    else:
        print('ilia strange dir',Dir)
        Dir='inout'
    dirs[Cell+'|'+clean_sig(Sig)]=Dir
    print('added dir',Cell+'|'+clean_sig(Sig),Dir)

def get_dir(Cell,Sig):
    Key = Cell+'|'+clean_sig(Sig)
    if (Key in dirs):
        return dirs[Key]
    return 'inout'

class instanceClass:
    def __init__(self,Type,Inst,Conns={},Params={}):
        self.Type=Type
        self.Inst=Inst
        self.Conns=Conns
        self.Params=Params
            


def makeParamsDir(Wrds):
    Res={}
    for wrd in Wrds:
        if '=' in wrd:
            ww = wrd.split('=')
            if len(ww)==2:
                Res[ww[0]]=ww[1]
            else:
                print('error! makeParamsDir got "%s"'%wrd)
        else:
            print('error! makeParamsDir got "%s"'%wrd)
    return Res

def normal_name(Txt):
    Net = clean_sig(Txt)
    if Net =='vss': return 'gnd'
    if Net =='vdd': return 'vcc'
    return Net


Modules={}
class moduleClass:
    def __init__(self,Module,Pins=[],Params=[]):
        self.total=-1
        self.name = Module
        self.moses=0
        self.cells=0
        self.sons={}
        self.Pins=Pins
        self.Params=Params
        self.instances={}
        self.wireId = 0

    def addComp(self,wrds,prms):
        if wrds[0][0] =='m':
            Inst = wrds[0]
            S = normal_name(wrds[1])
            G = normal_name(wrds[2])
            D = normal_name(wrds[3])
            B = normal_name(wrds[4])
            Type = wrds[5]+'mos'
            if Type not in self.instances:
                self.instances[Type]={}
            PP = makeParamsDir(prms)
            self.instances[Type][Inst]=instanceClass(Type,Inst,{'i':S,'g':G,'o':D},PP)
        elif wrds[0][0] =='r':
            print('ilia add res ',wrds,prms)
        elif wrds[0][0] =='c':
            print('ilia add cap ',wrds,prms)
        elif wrds[0][0] =='d':
            print('ilia add diode ',wrds,prms)
        elif wrds[0][0] =='q':
            print('ilia add qtran ',wrds,prms)


    def dump(self):
        for Type in self.instances:
            Insts = self.instances[Type]
            for Inst in Insts.keys():
                print(self.name,Type,Inst,Insts[Inst].Conns,Insts[Inst].Params)

    def createNets(self):
        self.Nets={}
        for Type in self.instances:
            Insts = self.instances[Type].keys()
            for Inst in Insts:
                Obj=self.instances[Type][Inst]
                for Pin in Obj.Conns:
                    Sig = Obj.Conns[Pin]
                    if Sig not in self.Nets:
                        self.Nets[Sig]=[(Inst,Pin)]
                    else:
                        self.Nets[Sig].append((Inst,Pin))



    def recognizeInvs(self):
        Pmoses = self.instances['pmos'].keys()
        for Pmos in Pmoses:
            Objp = self.instances['pmos'][Pmos]
            G = Objp.Conns['g']
            if (Objp.Conns['i']=='vcc'):
                II = Objp.Conns['o']
            elif(Objp.Conns['o']=='vcc'):
                II = Objp.Conns['i']
            else:
                II = False
            if II:
                Nmoses = self.instances['nmos'].keys()
                for Nmos in Nmoses:
                    Objn = self.instances['nmos'][Nmos]
                    if (G == Objn.Conns['g']):
                        if (Objn.Conns['i']=='gnd'):
                            JJ = Objn.Conns['o']
                        elif(Objn.Conns['o']=='gnd'):
                            JJ = Objn.Conns['i']
                        else:
                            JJ = False
                        if II==JJ:
                            self.instances['pmos'].pop(Pmos)
                            self.instances['nmos'].pop(Nmos)
                            if 'inv' not in self.instances:
                                self.instances['inv']={}
                            New = '%s_%s'%(Pmos,Nmos)
                            self.instances['inv'][New] = instanceClass('inv',New,{'i1':G,'o1':II},{})

    def recognizeCmos(self):
        Pmoses = self.instances['pmos'].keys()
        for Pmos in Pmoses:
            Objp = self.instances['pmos'][Pmos]
            Gp = Objp.Conns['g']
            IOP = [Objp.Conns['o'],Objp.Conns['i']]
            IOP.sort()
            Nmoses = self.instances['nmos'].keys()
            for Nmos in Nmoses:
                Objn = self.instances['nmos'][Nmos]
                Gn = Objn.Conns['g']
                ION = [Objn.Conns['o'],Objn.Conns['i']]
                ION.sort()
                if (ION==IOP):
                    self.instances['pmos'].pop(Pmos)
                    self.instances['nmos'].pop(Nmos)
                    if 'cmos' not in self.instances:
                        self.instances['cmos']={}
                    New = '%s_%s'%(Pmos,Nmos)
                    self.instances['cmos'][New] = instanceClass('cmos',New,{'c':Gn,'c_b':Gp,'o':ION[0],'i':ION[1]},{})

    def recognizeTinvs(self):
        Pmoses = self.instances['pmos'].keys()
        for Pmos in Pmoses:
            Objp = self.instances['pmos'][Pmos]
            Gp = Objp.Conns['g']
            IOP = [Objp.Conns['o'],Objp.Conns['i']]
            IOP.sort()
            if 'vcc' in IOP:
                if IOP[0]=='vcc': P0 = IOP[1]
                else: P0 = IOP[0]
                if (P0 in self.Nets)and(len(self.Nets[P0])==2):
                    return




        


    def dumpDraw(self):
        self.Fout = open('%s.zdraw'%self.name,'w')
        self.Fout.write('schematic %s\n'%(self.name))
        Nets={}            
        for ind,Pin in enumerate(self.Pins):
            if Pin not in ['vcc','gnd']:
                self.Fout.write('inst inout %s xy=5,%d\n'%(Pin,5+ind*1))
            Nets[Pin]=[Pin]
        X = 7
        Y = 5
        for Type in self.instances:
            if Type=='nmos':
                Pref = 'rot=r90'
            elif Type=='pmos':
                Pref = 'rot=fr270'
            else:
                Pref=''
            Insts = self.instances[Type].keys()
            for Inst in Insts:
                self.Fout.write('inst %s %s xy=%.1f,%.1f %s\n'%(Type,Inst,X,Y,Pref))
                X,Y = nextXY(X,Y)
        for Type in self.instances:
            Insts = self.instances[Type].keys()
            for Inst in Insts:
                Obj=self.instances[Type][Inst]
                for Pin in Obj.Conns:
                    Sig = Obj.Conns[Pin]
                    if Sig not in Nets:
                        Nets[Sig]=['%s.%s'%(Inst,Pin)]
                    else:
                        Nets[Sig].append('%s.%s'%(Inst,Pin))

        X,Y = newlineXY(X,Y)
        VCC=0
        if 'vcc' in Nets:
            LL = Nets['vcc']
            for Con in LL:
                self.Fout.write('inst vcc vcc_%d xy=%.1f,%.1f\n'%(VCC,X,13))
                self.Fout.write('wire wire_%d vcc_%d %s\n'%(self.getWireId(),VCC,Con))
                X,Y = newlineXY(X,Y)
                VCC += 1

        GND=0
        if 'gnd' in Nets:
            LL = Nets['gnd']
            for Con in LL:
                self.Fout.write('inst gnd gnd_%d xy=%.1f,%.1f\n'%(GND,X,2))
                self.Fout.write('wire wire_%d gnd_%d %s\n'%(self.getWireId(),GND,Con))
                X,Y = newlineXY(X,Y)
                GND += 1


            




        X,Y = newlineXY(X,Y)
        for Net in Nets:
            if Net not in ['vcc','gnd']:
                LL = Nets[Net]
                if len(LL)==2:
                    self.Fout.write('wire %s %s %s\n'%(Net,LL[0],LL[1]))
                elif len(LL)>2:
                    if (Net not in self.Pins):
                        self.Fout.write('inst node %s xy=%.1f,%.1f\n'%(Net,X,Y))
                        X,Y = nextXY(X,Y)
                 
                    for Con in LL:
                        self.Fout.write('wire wire_%d %s %s\n'%(self.getWireId(),Net,Con))
                    
        self.Fout.write('end\n')
        self.Fout.close()

    def getWireId(self):
        Id = self.wireId
        self.wireId += 1
        return Id

    def add_mos(self):
        self.moses+=1
    def add_son(self,Type,Inst):
        self.sons[Inst]=Type

    def get_total(self):
        if self.total>=0:
            return self.total
        else:
            return self.count()
    def count(self):
        tot = self.moses
        for Son in self.sons:
            Type = self.sons[Son]
            if Type in Modules:
                tot += Modules[Type].get_total()
            else:
                print('\n|||type %s called from %s is not in modules'%(Type,self.name))

        self.total=tot
        return tot

def nextXY(X,Y):
    Y += 3
    if Y>12:
        X += 3
        Y = 5
    return X,Y

def newlineXY(X,Y):
    X += 5
    Y = 5
    return X,Y


Patterns={}

Patterns['inv'] = '''
    pmos g=Gate S0=vcc S1=Out 
    nmos g=Gate S0=gnd S1=Out 
    add inv i1=Gate o1=Out 
''' 

Patterns['cmos'] = '''
    pmos s0=In s1=Out g=GateN
    nmos s0=In s1=Out g=GateP
    add cmos i1=In o1=Out c=GateN c_b=GateP 
'''

Patterns['tinvA'] = '''
    pmos g=Gate1 S0=vcc S1=Node0 
    node2 Node0 
    pmos g=Gate0 S0=Node0 S1=Out
    nmos g=Gate0 S0=Node1 S1=Out
    node2 Node1 
    nmos g=Gate2 s0=gnd s1=Node1
    add tinv i1=Gate0 o1=Out enp=Gate1 enn=Gate2
''' 

Patterns['tinvB'] = '''
    pmos g=Gate0 S0=vcc S1=Node0 
    node2 Node0 
    pmos g=Gate1 S0=Node0 S1=Out 
    nmos g=Gate2 S0=Node1 S1=Out 
    node2 Node1 
    nmos g=Gate0 S0=gnd S1=Node1 
    add tinv i1=Gate0 o1=Out enp=Gate1 enn=Gate2
''' 

Patterns['nand2'] = '''
    pmos g=Gate0 s0=vcc s1=Out 
    pmos g=Gate1 s0=vcc s1=Out 
    nmos g=Gate1 s0=Node1 s1=Out
    node2 Node1 
    nmos g=Gate0 s0=gnd s1=Node1 
    add nand2 i1=Gate0 i2=Gate1 o1=Out
''' 
    
Patterns['nor2'] = '''
    pmos g=Gate0 s0=vcc s1=Node0 
    pmos g=Gate1 s0=Node0 s1=Out
    node2 Node0 
    nmos g=Gate0 s0=gnd s1=Out 
    nmos g=Gate1 s0=gnd s1=Out 
    add nor2 i1=Gate0 i2=Gate1 o1=Out
'''
    
def prepPattern(Which):
    Pat = Patterns[Which]
    List = Pat.split('\n')
    Seq = []
    for Line in List:
        Pat0 = patternize(Line)
        Seq.append(Pat0)
    return Seq 

def parseConn(Pin,Net):
    A,B = parseNet(Pin)
    C,D = parseNet(Net)
    return A,B,C,D

def parseNet(Pin):
    Pin = Pin.replace('[',' ')
    Pin = Pin.replace(']',' ')
    wrds = Pin.split()
    if len(wrds)==1: return Pin,-1
    if len(wrds)==2: return wrds[0],int(wrds[1])

def useReplacements(Pin):
    for Key in REPLACEMENTS:
        Pin = Pin.replace(Key,REPLACEMENTS[Key])
    return Pin
main()



