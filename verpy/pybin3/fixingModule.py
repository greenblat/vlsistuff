

import types,string
from module_class import support_set,pr_wid,pr_expr

def fixingModule(Mod,Env):
    Defs={}
    for (Dst,Src,_,_) in Mod.hard_assigns:
        Sup0 = support_set(Dst,True)
        Sup1 = support_set(Src,True)
        for Item in Sup0+Sup1:
            if Item not in Mod.parameters:
                useForDefs(Item,Defs)
    for (Body,When,_) in Mod.alwayses:
        Sup0 = support_set(Body,True)
        Sup1 = support_set(When,True)
        for Item in Sup0+Sup1:
            if Item not in Mod.parameters:
                useForDefs(Item,Defs)
    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        for Pin in Obj.conns:
            Sig = Obj.conns[Pin]
            Sup0 = support_set(Sig,True)
            for Item in Sup0:
                if Item not in Mod.parameters:
                    useForDefs(Item,Defs)




    print('>>>',Mod.Module)
    for Net in Defs:
        if Net not in Mod.nets:
            print('net %s is not a net %s'%(Net,Defs[Net]))
            print('wire  %s %s;\n'%(pr_wid(Wid),pr_expr(Net)))
           
        else:
            Dir,Wid = Mod.nets[Net]
            print('net %s here=%s mod=%s %s'%(Net,Defs[Net],Dir,Wid))


def useForDefs(Item,Defs):
    if type(Item) is str:
        if '[' in Item:
            Bus,Hi,Lo = extractBus(Item)
            if Lo<0: Lo=999999
            if Bus in Defs:
                Wh,Wl = Defs[Bus]
                Defs[Bus]=(max(Wh,Hi),min(Wl,Lo))
            else:
                Defs[Bus]=(Hi,Lo)
        elif (Item in Defs):
            pass
        else:
            Defs[Item]=(-1,999999)
    elif type(Item) is list:
        print('list',Item)
    else:
        print('error %s'%(str(Item)))
        

def extractBus(Item):
    X = Item.index('[')
    Bus = Item[:X]
    Rest = Item[X+1:-1]
    ww = Rest.split(':')
    if len(ww)==2:
        Hi = tryInt(ww[0])
        Lo = tryInt(ww[1])
        return Bus,Hi,Lo
    
    if len(ww)==1:
        Ind = tryInt(ww[0])
        return Bus,Ind,Ind

def tryInt(Txt):
    try:
        return eval(Txt)
    except:
        return -1



def orderHardAssigns(Mod,Env):
    HAS = {}
    Ordered=[]
    Ins = []
    Regs = []
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir: Ins.append(Net)
        if 'reg' in Dir: Regs.append(Net)

    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        if Dst!='//':
            Sup0 = support_set(Dst,False)
            Sup1 = support_set(Src,False)
            HAS[ind]=(Sup0,Sup1)

    ReadyList = Ins[:]+Regs[:]
    WorkList = HAS.keys()
    while len(WorkList)!=0:
        pos=0
        while pos<len(WorkList):
            ind = WorkList[pos]
            Dst,Src = HAS[ind]
            if allReady(Src,ReadyList):
                WorkList.pop(pos)
                pos=999999
                ReadyList.extend(Dst)
                Ordered.append(ind)

    
            





