#! /usr/bin/python

import sys
import os
from string import *
import logs

biggest = []
biggest_dir = []
totallest = 0.0
bad_names = ['core']
baddies=[]
filesx = {}
lensx={}
numerousDirs = []

def try_big_dir_10(curdirsize,curdir,numOfLines):
    biggest_dir.append((curdirsize,curdir))
    biggest_dir.sort()
    while (len(biggest_dir)>Number):
        biggest_dir.pop(0)
    numerousDirs.append((numOfLines,curdir))
    numerousDirs.sort()
    while (len(numerousDirs)>Number):
        numerousDirs.pop(0)


def try_big_30(sizex,namex,curdir):
    global biggest
    global totallest
    global baddies
    global filesx,lensx
    totallest = totallest + (1.0*sizex/1000000)
    biggest = biggest+[(sizex,namex,curdir)]
    biggest.sort()
    if (len(biggest)>Number):
        biggest = biggest[-Number:]
    if (namex in bad_names):
        baddies = baddies + [(sizex,namex,curdir)]
    if (namex in filesx):
        filesx[namex] = filesx[namex]+[curdir]
        lensx[namex]=len(filesx[namex])
    else:
        filesx[namex] = [curdir]



def analyze_lines(lines):
    state = 'hunt'
    curdirsize=0.0
    curdir=''
    numOfLines = 0
    for line in lines:
        line = line[:-1]
#        print state,curdirsize,'line %s'%line
        if len(line)<2:
            pass 
        elif (state=='hunt'): 
            if (line[-1]==':'):
                if (curdirsize>0):
                    try_big_dir_10(curdirsize,curdir,numOfLines)
                curdir = line[:-1]
                curdirsize=0.0
                numOfLines = 0

#                print 'in "%s"'%curdir
                state='indir'
            else: 
                wrds= split(line)
                if (wrds[0]=='total'):
                    state = 'work'
                    if (curdirsize>0):
                        try_big_dir_10(curdirsize,curdir,numOfLines)
                    curdirsize=0.0
                    numOfLines = 0
        elif (state=='indir'):
            wrds= split(line)
            if (len(wrds)>1)and(wrds[0]=='total'):
               state='work'
        elif (state=='work'):
            wrds= split(line)
            if (line[-1]==':'):
                if (curdirsize>0):
                    try_big_dir_10(curdirsize,curdir,numOfLines)
                curdir = line[:-1]
                curdirsize=0.0
                numOfLines = 0
#                print 'in "%s"'%curdir
                state='indir'
            elif (len(wrds)<8):
                state='hunt'
            else:
                sizex = int(wrds[4])
                namex = wrds[8]
                if (namex[-1]=='*'):
                    namex=namex[:-1]
                numOfLines += 1
                if (namex!='./')and(namex!='../'):
#                    print 'try file',sizex,namex,curdir    
                    try_big_30(sizex,namex,curdir)
                    curdirsize = 1.0*curdirsize+sizex
            

def main():
    global Number
    argv = sys.argv
    Number=100
    if (len(argv)>2):
        Number = int(argv[2])
    if (len(argv)==1):
        print 'help: correct usage: diskspace <directory_name> [optional: number of report lines]'
        return
    targetdir=argv[1]
    pid = os.getpid()
    fname = '/tmp/'+str(pid)+'.ilia'
    os.system('ls -alFR %s > %s'%(targetdir,fname))
    File = open(fname,'read')
    lines = File.readlines()
    File.close()
    logs.log_info('done collecting %s to %s, total %d lines'%(targetdir,fname,len(lines)))
#    os.system('/bin/rm %s'%(fname))

    analyze_lines(lines)

    if (len(baddies)>0):
        logs.log_info('files having removable names:')
    pos=1
    for (A,B,C) in baddies:
        A=nicer(A)
        logs.log_info('%5d: %12s /bin/rm %s/%s '%(pos,A,C,B))
        pos=pos-1

    logs.log_info('biggest files:')
    pos=len(biggest)
    Total = 0.0
    for (A,B,C) in biggest:
        Total = Total + 1.0*A
        A=nicer(A)
        logs.log_info('%5d: %12s /bin/rm %s/%s '%(pos,A,C,B))
        pos=pos-1
    Total = Total/1000000
    logs.log_info('biggest files take: %d meg of disk space '%int(Total))

    pos=len(numerousDirs)
    for (A,B) in numerousDirs:
        logs.log_info( '%5d: %12s populous dirs  /bin/rm -Rf %s'%(pos,A,B))
        pos=pos-1

    pos=len(biggest_dir)
    Total = 0.0
    for (A,B) in biggest_dir:
        Total = Total + 1.0*A
        A=nicer(A)
        logs.log_info( '%5d: %12s /bin/rm -R %s '%(pos,A,B))
        pos=pos-1

    Total = Total/1000000
    logs.log_info('biggest dirs take: %d meg of disk space'%int(Total))
    logs.log_info('total files searched take %d megs'%(totallest))


#    analyze_common_names()

def analyze_common_names():
    Lens={}
    for Fname in lensx.keys():
        Len = lensx[Fname]
        Lens[Len]=1

    Lens1 = Lens.keys()
    Lens1.sort()
    Lens1.reverse()
    Len1 = len(Lens1)
    Last = min(Len1,50)
    Lens2 = Lens1[0:Last]
    for Len in Lens2:
        for Fname in lensx.keys():
            if (lensx[Fname]==Len):
                Dirs = filesx[Fname]
                print Len,Fname,Dirs[0]







def nicer(A):
    if (A>1000000000):
        A = str(int(A/100000000))+'G'
        A = A[0:-2]+'.'+A[-2:]
    elif (A>1000000):
        A = str(int(A/100000))+'M'
        A = A[0:-2]+'.'+A[-2:]
    elif (A>1000):
        A = str(int(A/100))+'K'
        A = A[0:-2]+'.'+A[-2:]
    else:
        A = str(A)
    return A

main()
