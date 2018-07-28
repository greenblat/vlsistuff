#! /usr/bin/python
import os,sys,string,types

class csvPageClass:
    def __init__(self,Fnames,produce_csv_from_xls):
        self.produce_csv_from_xls = produce_csv_from_xls
        self.Db=databaseClass('system')
        self.Board={}
        self.Fnames={}
        self.Translates={}
        for (F,R) in Fnames:
            self.Translates[F]=R
        self.lnum=0
        if type(Fnames)==types.ListType:
            for Fname,Realname in Fnames:
                self.readfile(Fname)
        else:
            self.readfile(Fnames)
        self.Patterns={}

        self.regs={}
        self.fields={}
        self.lastReg=''
        self.runAddr=0
        self.Module='none'

        self.scan2()

    def readlines(self,Fname):
        try:
            File = open(Fname)
        except:
            print 'file %s cannot be opened for reading'%(Fname)
            sys.exit()
        lines = File.readlines()
        dones=1
        while dones:
            dones=0
            i =0
            while i<len(lines):
                line = lines[i]
                line = string.replace(line,chr(13),'')
                lines[i]=line
                Quotes = count_chars(line,'"')
                if (Quotes&1)==1:
                    line += lines[i+1]
                    lines[i]=line
                    lines.pop(i+1)
                    dones=1
                else:
                    i+=1
        return lines



    def readfile(self,Fname):
        lines = self.readlines(Fname)
        lnum0=self.lnum
        pos=0
        while pos<len(lines):
            line=lines[pos]
            line=line[:-1]
            if (len(line)>0)and(ord(line[-1])==13):
                line=line[:-1]
            line = string.lower(line)
            wrds = string.split(line,',')
            wrds = gather_strings(wrds)
            wrds = clean_comments(wrds)
            cnum=0
            maxlen=0
            if '#include' in wrds:
                Incname0 = wrds[wrds.index('#include')+1]
                Incname1 = abspath(self.Translates[Fname],Incname0)
                if not os.path.exists(Incname1):
                    print 'error! cannot open file "%s" expanded as "%s" from "%s" "%s"'%(Incname0,Incname1,Fname,self.Translates[Fname])
                    sys.exit()
                else: 
                    print 'including file "%s" expanded as "%s"'%(Incname0,Incname1)
                CsvName = self.produce_csv_from_xls(Incname1)
                lines2 = self.readlines(CsvName)

                lines = lines[:pos]+lines2+lines[pos+1:]
            else:
                for wrd in wrds:
                    wrd = string.replace(wrd,'\r\n','')
                    maxlen=max(maxlen,len(wrd))
                    self.Board[(self.lnum,cnum)]=wrd
                    cnum +=1
                if (wrds!=[])and(maxlen>0):
                    self.lnum +=1
                pos += 1
        self.Fnames[Fname]=(lnum0,self.lnum)
        return




    def get_fname_by_lnum(self,lnum):
        for Fname in self.Fnames:
            (L,H)=self.Fnames[Fname]
            if (lnum>=L)and(lnum<=H):
                return Fname
            return 'warning! noFileName'



    def scan1self(self,lnum):
            cnum = 0
            state='idle'
            while (lnum,cnum) in self.Board:
                Word = self.Board[(lnum,cnum)]
                if state=='idle':
                    if (len(Word)>1)and(Word[0]=='#'):
                        state='in'
                        Kind=Word[1:]
                        Fields={}
                        Fields[cnum]=Kind
                elif state=='in':
                    if (len(Word)>1)and(Word[0]=='#'):
                        Field=Word[1:]
                        Fields[cnum]=Field

                cnum +=1
            if (state=='in'):
                self.Patterns[Kind]=Fields

    def scan2(self):
        for lnum in range(self.lnum):
            cnum = 0
            Kind = 'none'
            LL = []
            while (lnum,cnum) in self.Board:
                Word = self.Board[(lnum,cnum)]
                Word = Word.strip()
                if (cnum==0)and(len(Word)>0)and(Word[0]=='/'):
                    cnum = 10000
                elif (cnum==0)and(Word==''):
                    Kind = 'empty'
                elif (cnum==0)and(Word=='reg'):
                    Kind = 'reg'
                elif (cnum==0)and(Word=='array'):
                    Kind = 'array'
                elif (cnum==0)and(Word=='ram'):
                    Kind = 'ram'
                elif (cnum==0)and(Word=='module'):
                    Kind = 'module'
                LL.append(Word)
                cnum += 1
            self.useWords(lnum,Kind,LL)

    def useWords(self,lnum,Kind,LL):
        if Kind=='reg':
#            print '>>>>',LL
            Name = LL[1]
            Access = LL[3]
            Width = int(LL[5])
            Desc = LL[8]
            Latch = LL[9]
            if LL[6]=='':
                Def=0
            else:
                Def = LL[6]
            Addr = self.runAddr
            if Width>32:
                X = Width/32
                Y = Width % 32
                if Y!=0: X += 1
                self.runAddr += 4*X
            else:
                self.runAddr += 4
            self.regs[Name]=[Access,Width,Def,Addr,Desc,Latch]
            self.lastReg=Name
            self.fields[self.lastReg]=[]
        elif (Kind=='empty')and(LL[2]!=''):
            Width = int(LL[5])
            Field = LL[2]
            Def = (LL[6])
            Desc = LL[8]
            self.fields[self.lastReg].append([Width,Def,Field,Desc])
        elif (Kind=='module'):
            self.Module = LL[1]
        elif (Kind=='ram'):
            Name = LL[1]
            Width = int(LL[5])
            Am = string.replace(LL[7],'"','')
            Am = string.replace(Am,' ','')
            Amount = int(Am)
            Addr = self.runAddr
            if Width<=32:
                self.runAddr += 4*Amount
            elif Width<=64:
                self.runAddr += 8*Amount
            elif Width<=128:
                self.runAddr += 16*Amount
            self.regs[Name]=['ram',Width,Amount,Addr]
            self.fields[Name]=[]




    def __scan2(self):
        for lnum in range(self.lnum):
            cnum = 0
            state='idle'
            offset = 0
            Kind='none'
            while (lnum,cnum) in self.Board:
                Word = self.Board[(lnum,cnum)]
                Word = Word.strip()
                if (Word!='')and(Word[0]=='#')and(state=='idle'):
                    self.scan1self(lnum)
                    if Word=='#inst':
                        self.Db.Reg = databaseClass('inst')
                        self.Db.Reg.Name=self.Board[(lnum,cnum+1)]
                        Many = self.Board[(lnum,cnum+2)]
                        if Many[0]=='#':
                            Many=Many[1:]
                        self.Db.Reg.params={'many':int(Many)}
                        self.Db.Reg.fields=[]
                        self.Db.regs.append(self.Db.Reg)
                    if Word=='#endinst':
                        self.Db.Reg = databaseClass('endinst')
                        self.Db.regs.append(self.Db.Reg)



                    state='idle'
                    cnum=100000
                elif len(Word)>0:
                    if state=='idle':
                        if Word in self.Patterns:
                            Kind=Word
                            Fields={}
                            Pattern=self.Patterns[Kind]
                            state='in'
                            offset=0
                            for X in Pattern:
                                if Pattern[X]==Word:
                                    offset = X-cnum
                    elif state=='in':
                        if (cnum+offset) in Pattern:
                            Key = Pattern[(cnum+offset)]
                            Key = Key.strip()
                            if Key=='':
                                print 'error! in line %s there are more fields than in pattern %s'%(string.join(self.linetokens(lnum),','),string.join(Pattern,','))
                            Fields[Key]=Word
                cnum +=1
            if (state=='in'):
                self.use_it(Kind,Fields,lnum)
            else:
                ww2 = self.linetokens(lnum,False)
                WW = string.join(ww2,',')
                ww = self.linetokens(lnum,True)
                if len(ww)>0:
                    if (ww[0][0]!='#')and(ww[0][0]!='/'):
                        print 'error! lnum=%d disregarded "%s" len=%d len=%d'%(lnum,WW,len(ww),len(WW))

    def linetokens(self,lnum,Clean=False):
        res=[]
        cnum = 0
        while (lnum,cnum) in self.Board:
            Word = self.Board[(lnum,cnum)]
            if (Word!='')or not Clean:
                res.append(Word)
            cnum +=1
        return res

    def use_it(self,Kind,Fields,lnum):
        if 'name' not in Fields:
           print 'name not in fields ',Fields
           return

        if Kind=='container':
            Name = Fields['name']
            self.Db.Name=Name
            self.Db.instances={}
            self.Db.order=0
            self.Db.params=Fields
            return
    
        if (Kind=='fifo'):
            self.Db.Reg = databaseClass('fifo')
            Name = Fields['name']
            self.Db.Reg.Name=Name
            self.Db.Reg.params=Fields
            self.Db.Reg.fields=[]
            self.Db.regs.append(self.Db.Reg)
            return
        if (Kind=='reg'):
            self.Db.Reg = databaseClass('reg')
            Name = Fields['name']
            self.Db.Reg.Name=Name
            self.Db.Reg.params=Fields
            self.Db.Reg.fields=[]
            self.Db.regs.append(self.Db.Reg)
            return

        if (Kind=='array'):
            self.Db.Reg = databaseClass('array')
            Name = Fields['name']
            self.Db.Reg.Name=Name
            self.Db.Reg.params=Fields
            self.Db.Reg.fields=[]
            self.Db.regs.append(self.Db.Reg)
            return
    
        if (Kind=='ram'):
            self.Db.Reg = databaseClass('ram')
            Name = Fields['name']
            self.Db.Reg.Name=Name
            self.Db.Reg.params=Fields
            self.Db.Reg.fields=[]
            self.Db.regs.append(self.Db.Reg)
            return



        if (Kind=='field'):
            Name = Fields['name']
            self.LastField=Name
            self.Db.Reg.fields.append((Name,Fields))
            return
    
        if (Kind=='enum'):
            Key = (self.Db.Reg.Name,self.LastField)
            if Key not in self.Db.enums:
                self.Db.enums[Key]=[]
            self.Db.enums[Key].append(Fields['name'])
            return
    
        if (Kind=='param'):
            Name = Fields['name']
            self.Db.extparams[Name] = Fields
            return
        

        print 'csvPageClass warning: ',self.Db.state,'kind',Kind,Fields        

        

def abspath(Fname,Relname):
    curpath = os.path.dirname(os.path.abspath(Fname))
    Path = os.path.join(curpath, os.path.expandvars(os.path.expanduser(Relname)))
    return Path




class databaseClass:
    def __init__(self,Kind):
        self.Kind=Kind
        self.Versions=[]
        self.enums={}
        self.rams=[]
        self.regs=[]
        self.Name=''
        self.extparams={}
        self.params={}
        self.instances={}
        self.lastaddr={}
        self.lastlpaddr={}
        self.state='idle'
        self.chk_nets={}
        self.chk_conns={}
        self.chk_params={}
        self.chk_vars={}
        self.filler_name=0

    def dump0(self,Pref=''):
        print Pref,self.Kind,self.Name
        for Inst in self.instances:
            Pos_Base=self.instances[Inst]
            print Pref,'   inst',Pos_Base,Inst
        if self.Kind=='module':
            for Item in self.regs:
                print Pref,Item.Kind,Item.Name,Item.params
                for Field,Params in Item.fields:
                    print Pref,'   field',Field,Params
                    
        





Db = databaseClass('system')


def clean_comments(wrds):
    state='idle'
    res = []
    for wrd in wrds:
        if (state=='idle'):
            if '//' in wrd:
                state='comment'
                res.append('')
            else:
                res.append(wrd)
        else:
            res.append('')
    return res

def gather_strings(wrds):
    res=[]
    curr=''
    state='idle'
    for wrd in wrds:
        if state=='idle':
            if wrd=='':
                res.append(wrd)
            elif wrd[0]=='"':
                if wrd[-1]=='"':
                    res.append(wrd)
                else:
                    state='string'
                    curr=wrd
            else:
                res.append(wrd)
        elif state=='string':
            curr += ' '+wrd
            if wrd[-1]=='"':
                res.append(curr)
                curr=''
                state='idle'
    return res            


def count_chars(Str,Char):
    res=0
    for Chr in Str:
        if Chr==Char:
            res +=1
    return res



def main():
    Fname=sys.argv[1:]
    Board = csvPageClass(Fname)
if __name__ == '__main__':
    main()

