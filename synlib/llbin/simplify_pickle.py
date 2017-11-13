#! /usr/bin/python

import os,sys,string
import pickle

def main():
    Fname = sys.argv[1]

    if len(sys.argv)>2:
        Fnameout = sys.argv[2]
    else:
        printIt('before',dataBase)
        Fnameout=False
    simplify(Fname,Fnameout)

def simplify(Fname,Fnameout):    
    File = open(Fname)
    dataBase = pickle.load(File)
    File.close()

    Lib = {}
    for Key in dataBase:
        List = dataBase[Key]
        if len(List)==1:
            Lib[Key]=List[0]


    Used = {}

    dones = 1
    while (dones>0):
        dones=0
        Keys = dataBase.keys()
        for Key in Keys:
            List = dataBase[Key]
            if (len(List)==1)and(List[0] in dataBase):
                dataBase[Key] = dataBase[List[0]]
                dones += 1
            else:
                for ind,Item in enumerate(List):
                    if Item in Lib:
                        List[ind]=Lib[Item]
                        Used[Item]=True
                        dones += 1
         
    print 'removed %d items'%len(Used.keys())
    for Key in Used:
        dataBase.pop(Key)

    checkDataBase("aa",dataBase)
    Keys = dataBase.keys()
    Used = {}
    Ok=True
    round=0
    while Ok:
        Ok=False
        round += 1
        for Key in Keys:
            List = dataBase[Key]
            if List!=[]:
                Key0 = List[0]
                if (len(List)>=2)and(Key[0]==Key0[0]):
                    LL = dataBase[Key0]
                    New = LL + List[1:]
                    dataBase[Key]=New
                    Used[Key0]=True
                    Ok=True

    for Key in Used:
        dataBase.pop(Key)

    checkDataBase("bb",dataBase)
    print 'removed %d items'%len(Used.keys())

    if Fnameout:
        Outf = open(Fnameout,'w')
        pickle.dump(dataBase,Outf)
        Outf.close()
    else:
        printIt('final',dataBase)


def checkDataBase(Why,dataBase):
    Used = {}
    for Key in dataBase:
        List = dataBase[Key]
        for Item in List:
            if len(Item)==2:
                if Item not in dataBase:
                    print '%s: in key=%s item=%s of list=%s is not in the database'%(Why,Key,Item,List)
            Used[Item]=True
    for Key in dataBase:
        if Key not in Used:
            print '%s: key=%s is not used in database'%(Why,str(Key))

def printIt(Why,dataBase):
    for Key in dataBase:
        print Why,Key,dataBase[Key]


if __name__ == '__main__':
    main()




