#! /usr/bin/env python3
import os,sys,string
import datetime
import zlib

AsideDir = 'aside_tmp'

def main():
    for Fname in sys.argv[1:]:
        work(Fname)


def work(Fname):
    File = open(Fname)
    Lines = File.readlines()
    File.close()
    Abs = os.path.abspath(Fname)
#    print(Abs)

    Date = datetime.date.today()
    Time = datetime.datetime.now()
    HourDate = str('%02d' % Time.hour)+str('%02d' % Date.day)+str('%02d' % Date.month)+str(Date.year)[2:]
    HourDate = str('%02d' % Date.day)+str('%02d' % Date.month)+str(Date.year)[2:]

    Changed = False


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
            ind -= 1
        elif (len(wrds)>=3) and (wrds[0] == 'assign') and (wrds[1] == 'sign_version'):
            Signs[Module] = ind,wrds[3][4:]
            Lines.pop(ind)
            ind -= 1
        elif ('FROMFILE' in line):
            Lines.pop(ind)
            ind -= 1
        ind += 1
    Signature = 0            
    sign_version = 'wire [63:0] '
    Adler = zlib.adler32(b'Ilia G',1)
    for ind,line in enumerate(Lines):
        Was = Signature
        Signature,Adler = computeIt(Signature,Adler,line)
#        print("MODULE %s %08x %08x %08x  line=%s" % (Module,Was,Signature,Adler,line[:-1]))
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
#                print("SIGN %s %08x %08x  %s" % (Module,Signature,Adler,Signs))
                _,Was = Signs[Module]
                Int = int(Was,16)
                Sign = Int>>32
                Now = '%05x%05x' % (Adler & 0xfffff,Signature & 0xfffff)
                WasS = Was[:10]
                if (Now != WasS):
                    print("%s now=%s <> was=%s" % (Module,Now,WasS))
                    New = "%s sign_version = 64'h%s%s ;\nendmodule\n// FROMFILE %05x %05x %s :: %s\n\n" % (sign_version,Now,HourDate,Adler & 0xfffff,Signature & 0xfffff,HourDate,Abs)
                    Changed = True
                else:
                    New = "%s sign_version = 64'h%s ;\nendmodule\n" % (sign_version,Was)
                Lines[ind] = New
            else:
                New = "%s sign_version = 64'h%08x%s ;\nendmodule\n" % (sign_version,Signature,HourDate)
                Lines[ind] = New
                Changed = True
            Signature = 0            
    if Changed: 
        print("CHANGED %s" % (Module))
    else:
        return False
    if not os.path.exists(AsideDir): os.mkdir(AsideDir)
    os.system('/bin/cp  %s %s/%s.v ' % (Fname,AsideDir,Module))
    Fout = open(Fname,'w')
    for line in Lines:
        Fout.write(line)
    Fout.close()
    return HourDate

def okchar(Chr):
    if Chr in ['\n','\t',' ']: return False
    return True


def computeIt(Signin,Adler,line):
    X = map(ord,filter(okchar,list(line)))
    Mid = sum(X)
    Y = map(ord,filter(okchar,list(line)))
    Adl = zlib.adler32(bytes(list(Y)),Adler)
#    print("%d XXXXXXX %08x %08x %s   %s  ||%s" % (Mid,Adler,Adl,list(X),line,list(Y)))
    return (Signin + Mid), Adl


if __name__ == '__main__': main()
