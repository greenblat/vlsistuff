
FWID = "`WWW"

def help_main(Env):
    Mod = Env.Current
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Wid == 0:
            Mod.nets[Net] = Dir,(FWID,0)    
        elif type(Wid) is tuple:
            if type(Wid[0]) is int:
                Wid2 = ('packed',Wid,(FWID,0))
                Mod.nets[Net] = Dir,Wid2   

            
            
