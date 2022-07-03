

import random
from module_class import is_external_dir

def help_main(Env):
    Mod = Env.Current
    fub = fubarizeClass(Mod)
    fub.workOnMod()

class fubarizeClass:
    def __init__(self,Mod,work=True):
        self.TRANS = []
        self.Translation = {}
        self.Mod = Mod
        self.Invented = {}
        if work:
            self.workOnMod()
        

    def workOnMod(self):
         self.makeRenames()
         self.renameDeep(False)
         Fout = open('0.%s.fbr'%self.Mod.Module,'w')
         self.Mod.dump_verilog(Fout)
         Fout.close()
         self.make2Renames()
         self.addAssigns()
         Fout = open('%s.fbr'%self.Mod.Module,'w')
         self.Mod.dump_verilog(Fout)
         Fout.close()

    def addAssigns(self):
         for (Dir,Net,Invent) in self.TRANS:
             if 'output' in Dir:
                 self.Mod.hard_assigns.append((Net,Invent,'',''))
             else:
                 self.Mod.hard_assigns.append((Invent,Net,'',''))

    def renameDeep(self,noFubar = False):
        for ind,(Dst,Src,A,B) in enumerate(self.Mod.hard_assigns):
            Xd = self.renameExpr(Dst,noFubar)
            Xs = self.renameExpr(Src,noFubar)
            self.Mod.hard_assigns[ind] = (Xd,Xs,A,B)
        for ind,Always in enumerate(self.Mod.alwayses):
            Alw = self.renameExpr(Always,noFubar)
            self.Mod.alwayses[ind] = Alw
    
        for ind,Body in enumerate(self.Mod.generates):
            Alw = self.renameExpr(Body,noFubar)
            self.Mod.generates[ind] = Alw
            
            
    def renameExpr(self,Src,noFubar = False):
        if type(Src) is str: 
            if Src in self.Translation: return self.Translation[Src]
            return Src
    
        if type(Src) is int:
            return Src

        if (len(Src)==3)and(Src[0] in ['hex','dig','bin']):
            if noFubar: return Src
            Invent = self.fubarname()
            if Src[0]=='hex':
                Val = int(Src[2],16)
                if Src[1]=='':
                    Src = Val
                else:
                    Src = ['dig',Src[1],str(Val)]
    
            self.Mod.localparams[Invent]=Src
            return Invent
            
    
        if type(Src) is list:
            for ind,X in enumerate(Src):
                Y = self.renameExpr(X,noFubar)
                Src[ind]=Y
            return Src
    
        if type(Src) is tuple:
            LL = list(Src)
            Res = self.renameExpr(LL,noFubar)
            return tuple(Res)
    
    
        print('ERROR rename %s'%str(Src))
        return Src
    
    def make2Renames(self):    
        self.Translation = {}
        Nets = list(self.Mod.nets.keys())
        for Net in Nets:
            Dir,Wid = self.Mod.nets[Net]
            if is_external_dir(Dir):
                Invent = self.fubarname()
                self.Translation[Net] = Invent
                self.Mod.nets[Invent] = 'wire',Wid
                self.TRANS.append((Dir,Net,Invent))
        self.renameDeep()

    
    def makeRenames(self):
        Nets = list(self.Mod.nets.keys())
        for Net in Nets:
            Dir,Wid = self.Mod.nets[Net]
            if not is_external_dir(Dir):
                Invent = self.fubarname()
                self.Translation[Net] = Invent
                self.Mod.nets.pop(Net)
                self.Mod.nets[Invent] = Dir,Wid
#            else:
#                Invent = self.fubarname()
#                self.Translation[Net] = Invent
#                self.Mod.nets[Invent] = 'wire',Wid
#                self.TRANS.append((Dir,Net,Invent))
    
        Prms = list(self.Mod.localparams.keys())
        for Prm in Prms:
            Val =  self.Mod.localparams[Prm]
            Invent = self.fubarname()
            self.Translation[Prm] = Invent
            self.Mod.localparams.pop(Prm)
            self.Mod.localparams[Invent] = Val
            
            
    
    
    
    def fubarname(self):
        X = random.randint(0x10000,0xfffff)
        Y = random.randint(0x10000,0xfffff)
        Res = 'x%xy%x'%(X,Y)
        if Res in self.Invented:
            Res = fubarname(Res)
        self.Invented[Res]=1
        return Res
        
