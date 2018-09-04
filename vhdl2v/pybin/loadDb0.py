#! /usr/bin/python

import os,sys,string
import pickle
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)

import logs

info = logs.log_info

def main():
    File = open('db0.pickle')
    Adb = pickle.load(File)
    rounds0(Adb)
    rounds1(Adb)
    removes0(Adb)
    reportAdb(Adb)
    reportLinks(Adb)

def removes0(Adb):
    for Key in Adb:
        List = Adb[Key]
        if (len(List[-1])==4):
            if List[-1][0]=='Semicolon':
                Adb[Key] = List[:-1]

def rounds0(Adb):
    while True:
        Bef = len(Adb.keys())
        oneRound0(Adb)
        Aft = len(Adb.keys())
        info('bef=%d aft=%d'%(Bef,Aft))
        if Aft==Bef: return

    
def oneRound0(Adb):
    F0,F4 = findEnds(Adb)
#    info('f0 %d   f4 %d all %d'%(len(F0),len(F4.keys()),len(Adb.keys())))
    useF0_F4(Adb,F0,F4)
#    info('f0 %d   f4 %d all %d'%(len(F0),len(F4.keys()),len(Adb.keys())))
    return Adb

    return

def rounds1(Adb):
    while True:
        Bef = len(Adb.keys())
        doTwos(Adb)
        Aft = len(Adb.keys())
        info('rounds1 bef=%d aft=%d'%(Bef,Aft))
        if Aft==Bef: return

def findOnes(Adb):
    F2 = {}
    for Key in Adb.keys():
        Val = Adb[Key]
        if (len(Val)==1)and(len(Val[0])==2):
            F2[Val[0]] = Key
    return F2

def doTwos(Adb):
    F2 = findOnes(Adb)
    Del = []
    for Key in Adb.keys():
        if Key in F2:
            Val = Adb[Key]
            if (len(Val)>1):
                Bef = F2[Key]
                Adb[Bef]=Val
                Del.append(Key)
                info('key=%s bef=%s val=%s'%(Key,Bef,Val))
    for Bef in Del:
        Adb.pop(Bef)
        


def reportLinks(Adb):
    Root = ('design_file',1)
    scanDeep(Root,Adb,[])

def scanDeep(Root,Adb,Bef):
    if Root in Adb:
        List = Adb[Root]
        for Item in List:
            if (len(Item)==2)and(Item in Adb):
                scanDeep(Item,Adb,Bef+[Item])
            elif (len(Item)==4)and(Item[0] not in Adb):
                logs.log_info('>>>>> %s   %s'%(str(Bef),Item))
                


def reportAdb(Adb):
    for Key in Adb.keys():
        Val = str(Adb[Key])
        if len(Val)>150: Val = Val[:150]
        info('report %s   %s '%(Key,Val))

def useF0_F4(Adb,F0,F4):
    for Key in F0:
        Adb.pop(Key)
    for Key in F4:
        Adb.pop(Key)

    for Key in Adb:
        Old = Adb[Key]
        New = simplify0(Old,F0,F4)
        if New!=Old:
            Adb[Key]=New


def simplify0(Old,F0,F4):
    New = Old[:]
    for Key in F0:
        if Key in New:
            Ind = New.index(Key)
            New.pop(Ind)
    for Key in F4:
        if Key in New:
            Ind = New.index(Key)
            New[Ind]=F4[Key]
    return New



def findEnds(Adb):
    F4 = {}
    F0 = []
    for Key in Adb.keys():
        Val = Adb[Key]
        if (len(Val)==1)and(len(Val[0])==4):
            F4[Key] = Val[0]
        if (Val==[]):
            F0.append(Key)
    return F0,F4            





main()

