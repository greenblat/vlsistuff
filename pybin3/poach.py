#! /usr/bin/env python3
import os,sys,string

def main():
    if len(sys.argv)==1:
        print(HelpString)
    Dir = sys.argv[1]
    Dst = '~/poaching'
    Ends = sys.argv[2]
    Ends = Ends.split('.')
    if len(sys.argv)>3:
        Dst = sys.argv[3]
    if not os.path.exists(Dst): os.mkdir(Dst)
    if not os.path.exists('./poached'): 
        os.mkdir('poached')
    else:
        os.system('/bin/rm -R poached')
        os.mkdir('poached')
    travelDeep(Dir,Dst,Ends)

FROM = {}
def travelDeep(Dir,Dst,Ends):
    try:
        List = os.listdir(Dir)
    except:
        print('failed to go into %s'%Dir)
        return
    for Fname in List:
        if endsCorrect(Fname,Ends):
            if not os.path.exists(Dst): mkdir(Dst)
            os.system('/bin/cp %s/%s %s/'%(Dir,Fname,Dst))
            if os.path.exists('poached/%s'%Fname):
                if Fname not in FROM: FROM[Fname] = '?'
                print('>>>>','poached/%s'%Fname,os.path.exists('poached/%s'%Fname))
                print('warning!! overwritining %s by %s/%s'%(FROM[Fname],Dir,Fname))
            else:
                FROM[Fname] = Dir
                FROM[Fname.lower()] = Dir
                FROM[Fname.upper()] = Dir
                print('cp %s/%s'%(Dir,Fname))                
                os.system('/bin/cp %s/%s poached'%(Dir,Fname))
    for Fdir in List:
        if Fdir[0] != '.':
            Full = '%s/%s'%(Dir,Fdir)
            if os.path.isdir(Full):
                NewDst = '%s/%s'%(Dst,Fdir)
                travelDeep(Full,NewDst,Ends)
            

def mkdir(Dst):
    WW = Dst.split('/')
    for II in range(1,1+len(WW)):
        Head = '/'.join(WW[:II])
        if (Head!='') and (not os.path.exists(Head)):
            os.mkdir(Head)


def endsCorrect(Fname,Ends):
    ww = Fname.split('.')
    if len(ww)<2: return False
    Ext = ww[-1]
    return Ext in Ends

    


HelpString = '''
copy all relevant (and only those) files to a new tree

poach.py <FromDir> <Endings> [ <ToDir> ]

default of ToDir is '~/poaching'
Endings is one string punctuted by dots ".v.sv.h.vh"
'''

if __name__ == '__main__': main()
