#! /usr/bin/env python3
'''
 versionize.py creates versions of directories given at invocation
 it checks if previous latest version is identical to current files,
 if so it skips creating new version.

the versions are numbered in increasing number. they are called .VER<NUM> directories

of -lim <DEPTH> is given, only last <DEPTH> versions are kept and all other deleted.
You can delete versions by yourself.

versionize.py rtl llbin flows -dont -lim 100M -ignore "*.vcd" -m "why it was versionised"

if file ./.versionrc   or ~/.versionrc is present , it can control what not to save in versions.

ignore *.vcd    as example : ignore files named "*.vcd" as so.
limitsize 100M    as example (files bigger than 100M will not be copied).

-dont dont change anything just report
by default versioned files are made readonly.
'''


import os,sys
import datetime
import logs

def main():
    Params = logs.parse_args()
    print(Params)
    Dirnames = Params['fnames']
    if '-lim' in Params:
        db.sizeLimit = int(Params['-lim'][0])
    if '-ignore' in Params:
        db.ignores = Params['-ignore']
    if '-m' in Params:
        db.MMM = Params['-m']
    db.DONT =  '-dont' in Params
    if Dirnames==[]:
        help()
        return
    for Dir in Dirnames:
        workOn(Dir)

def workOn(Dir):
    List = os.listdir(Dir)
    print('LLL',List)
    LatestVer = findLatest(List)
    eligibleFiles = db.goodFiles(List,Dir)
    if LatestVer<0:
        if db.DONT: 
            print('no previous versions for dir=%s and -dont : nothing to do'%(Dir))
            return
        print('creating version %d'%(0))
        copyFiles(eligibleFiles,Dir,0)
    else:
        Diffs,Dfiles = haveDiffFiles(Dir,'.VER%d'%LatestVer,eligibleFiles)
        if db.DONT:
            if Diffs>0:
                print('creating version (with DONT)  %d diffs=%d'%(LatestVer+1,Diffs))
                for Fx in Dfiles:
                    print('      %s'%Fx)
            else:
                print('in dir "%s" no changes. latest version ".VER%s" stays'%(Dir,LatestVer))
        elif Diffs>0:
            print('creating version %d diffs=%d'%(LatestVer+1,Diffs))
            copyFiles(eligibleFiles,Dir,LatestVer+1)
        else:
            print('in dir "%s" no changes. latest version ".VER%s" stays'%(Dir,LatestVer))
        
def copyFiles(List,Dir,Ver):
    Vdir = '%s/.VER%d'%(Dir,Ver)
    os.mkdir(Vdir)
    Freadme = open('%s/README%d'%(Vdir,Ver),'w')
    Date = datetime.date.today()
    DDD = str(Date.day)+'_'+str(Date.month)+'_'+str(Date.year)
    Freadme.write('version created on %s at %s\n'%(DDD,Vdir))
    Freadme.close()
    for Fname in List:
        os.system('/bin/cp %s/%s %s/  ;   chmod -w %s/%s'%(Dir,Fname,Vdir,Vdir,Fname))
    if db.MMM!='':
        Fmmm = open('%s/MMM'%(Vdir),'w')
        Fmmm.write('version remarks:\n%s\n'%(db.MMM))
        Fmmm.close()


def haveDiffFiles(Dir,Vdir,List):
    count=0
    Dfiles = []
    for Fname in List:
        if 'README' not in Fname:
            Vfullname = '%s/%s/%s'%(Dir,Vdir,Fname)
            if not os.path.exists(Vfullname):
                count +=1 
                Dfiles.append(Fname)
            else:
                L1 = os.popen('diff -bBw  %s/%s  %s/%s/%s'%(Dir,Fname,Dir,Vdir,Fname)).readlines()
                if L1!=[]: 
                    Dfiles.append(Fname)
                    count += 1 
    return count,Dfiles

def findLatest(List):
    Max=-1
    for Item in List:
        if 'VER' in Item: 
            print('ITEM',Item,logs.startsWith(Item,'.VER'))
        if logs.startsWith(Item,'.VER'):
            Ind = int(Item[4:])
            Max = max(Ind,Max)
    return Max

class holderClass:
    def __init__(self):
        self.ignores=[]
        self.sizeLimit= 0
        self.MMM = ''
    def goodFiles(self,List,Dir):
        Goods = []
        for Item in List:
            if not logs.startsWith(Item,'.VER'):
                if '.swp' not in  Item:
                    Fullname= '%s/%s'%(Dir,Item)
                    if not os.path.isdir(Fullname):
                        Goods.append(Item)
        return Goods                


db = holderClass()

def help():
    print(__doc__)

main()
