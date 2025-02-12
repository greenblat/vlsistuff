#! /usr/bin/env python3
import os,sys

FNAME = '/users/iliagreenblat/HOURS/JOBS'
def main():
    if len(sys.argv) == 1:
        report2()
    elif (sys.argv[1] in ['dropped','done','finished']):
        Which = sys.argv[2]
        markFinished(Which)
    elif (sys.argv[1] in ['edit','ed','e','edi']):
        editIt()

def editIt():
    os.system('vi %s' % FNAME)

def report():
    File = open(FNAME)
    Lines = File.readlines()
    ind = 0
    for Line in Lines:
        wrds = Line.split()
        if len(wrds)>=4:
            if '@finished' not in wrds:
                if '@done' not in wrds:
                    if '@dropped' not in wrds:
                        if '@suspended' not in wrds:
                            print("%3d: %20s %8s %8s |    %s" % (ind,wrds[0],wrds[1],wrds[2],' '.join(wrds[3:])))
                            ind += 1
    File.close()

def report2():
    Db = fillDb();
    Pris = {1:[],2:[],3:[],4:[],5:[]}
    for Rec in Db:
        Pri = Rec.priority
        if not Rec.done:
            Pris[Pri].append(Rec)
        
    for Pri in [1,2,3,4,5]:
        for Rec in Pris[Pri]:
            X = Rec.pp()
            print('%d: %s' % (Pri,X))



def fillDb():
    Db = []
    File = open(FNAME)
    Lines = File.readlines()
    File.close()
    for Line in Lines:
        wrds = Line.split()
        if len(wrds)>=4:
            LL = lineClass(Line)
            Db.append(LL)
        
    return Db 


class lineClass:
    def __init__(self,line):
        self.done = False
        self.priority = 1
        self.company = ''
        self.startDate = '0'
        self.txt = ''
        self.parse(line)

    def parse(self,line):
        wrds = line.split()
        self.done = ('@dropped' in wrds) or ('@done' in wrds) or ('@finished' in wrds) or ('@suspended' in wrds)
        if getParam('@pri',wrds): self.priority = getParam('@pri',wrds)
        self.company = wrds[0]
        self.startDate = wrds[1]
        for wrd in wrds[3:]:
            if wrd[0] != '@':
                self.txt += ' '+wrd
    def pp(self):
        if self.done: return False
        Line = '%-16s %10s:   %s' % (self.company,self.startDate,self.txt)
        return Line

def getParam(Param,wrds):
    for wrd in wrds:
        if wrd.startswith(Param):
            if '=' in wrd:
                ww = wrd.split('=')
                if ww[1][0] in '0123456789': return int(ww[1])
                return ww[1]
            else:
                return wrd
    return False


def markFinished(Which):
    return


if __name__ == '__main__': main()
