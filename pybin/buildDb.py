

import os,sys,string
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)


import logs

SYNONYMS = {'wid':'width'}

class dbClass:
    def __init__(self):
        self.items = []
        self.chip = False

def  readFile(Fname):
    File = open(Fname)
    Db = dbClass()
    while True:
        line = File.readline()
        if line=='': return
        if '//' in line: line = line[:line.index('//')]
        if '#' in line: line = line[:line.index('#')]
        wrds = string.split(line)
        if len(wrds)==0:
            pass
        elif (wrds[0]=='end'):
            return Db
        elif (wrds[0]=='chip'):
            Db.chip = itemClass(wrds)
            Names = Db.chip.Params['names']
            Db.Module = Names[0]
            if 'async' in Names:
                Db.Reset = 'async'
            else:
                Db.Reset = 'sync'

            if 'axi4lite' in Names:
                Db.Bus = 'axi4lite'
            elif 'ram' in Names:
                Db.Bus = 'ram'
            elif 'apb' in Names:
                Db.Bus = 'apb'


        else:
            Item = itemClass(wrds)
            Db.items.append(Item)



class itemClass:
    def __init__(self,Wrds):
        self.Kind = Wrds[0]
        self.Params = getParams(Wrds[1:])
        self.Synonyms()
        self.Addr = -1
        self.RAMS = ''
        self.RAMS_WIRES = ''
    def dump(self):
        print('%s : (%d 0x%x) %s'%(self.Kind,self.Addr,self.Addr,self.Params))
    def Synonyms(self):
        for Key in SYNONYMS:
            if Key in self.Params:
                Val = SYNONYMS[Key]
                if Val not in self.Params:
                    self.Params[Val] = self.Params[Key]


def getParams(wrds):
    Res = {}
    Nn = []
    for wrd in wrds:
        if '=' in wrd:
            ww = string.split(wrd,'=')
            try:
                AA = eval(ww[1])
            except:
                AA = ww[1]
            Res[ww[0]] = AA
        else:
            Nn.append(wrd)
    Res['names']=Nn
    return Res 



