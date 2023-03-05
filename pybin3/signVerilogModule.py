#! /usr/bin/env python3
import os,sys,string
import datetime

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Lines = File.readlines()

    Date = datetime.date.today()
    Time = datetime.datetime.now()
    HourDate = str('%02d' % Time.hour)+str('%02d' % Date.day)+str('%02d' % Date.month)+str(Date.year)[2:]




    Signs = {}
    ind = 0
    while ind <len(Lines):
        line = Lines[ind]
        ll = line.replace('#',' ')
        ll = ll.replace('(',' ')
        wrds = ll.split()
        if wrds==[]:
            pass
        elif wrds[0] == 'module':
            Module = wrds[1]
        elif wrds[0] == 'endmodule':
            Module = 'None'
        elif (len(wrds)>=4) and (wrds[0] == 'wire') and (wrds[1] == '[63:0]') and (wrds[2] == 'sign_version'):
            Signs[Module] = ind,wrds[4][4:]
            Lines.pop(ind)
        ind += 1
    Signature = 0            
    sign_version = 'wire [63:0] '
    for ind,line in enumerate(Lines):
        Signature = computeIt(Signature,line)
        ll = line.replace('#',' ')
        ll = ll.replace('(',' ')
        wrds = ll.split()
        if 'sign_version' in line: sign_version = 'assign '
        if wrds==[]:
            pass
        elif wrds[0] == 'module':
            Module = wrds[1]
        elif wrds[0] == 'endmodule':
            if Module in Signs:
                _,Was = Signs[Module]
                Int = int(Was,16)
                Sign = Int>>32
                if Sign != Signature:
                    New = "%s sign_version = 64'h%08x%s ;\nendmodule\n" % (sign_version,Signature,HourDate)
                    Lines[ind] = New
                    

            else:
                New = "%s sign_version = 64'h%08x%s ;\nendmodule\n" % (sign_version,Signature,HourDate)
                Lines[ind] = New
            Signature = 0            
    
    for line in Lines:
        print(line[:-1])


def okchar(Chr):
    if Chr in ['\n','\t',' ']: return False
    return True


def computeIt(Signin,line):
    X = map(ord,filter(okchar,list(line)))
    Mid = sum(X)
    return Signin + Mid


if __name__ == '__main__': main()
