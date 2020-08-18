#! /usr/bin/env python3

import os,sys,string
import random

ZLIB = False

def main():
    global OutFileName,Password
    if len(sys.argv)<3:
        print('usage"  encdec [e|d] <filename> [<outfilename>] [<password>]')
        print(' e stands for encoding, "d" is used for decoding')
        print('if password given - the file is encrypted')
        return
    What = sys.argv[1]
    Fname = sys.argv[2]
    if len(sys.argv)>3:
        OutFileName = sys.argv[3]
    else:
        OutFileName=False
    if len(sys.argv)>4:
        Password = sys.argv[4]
        Seed = 1
        for X in Password:
            Y = ord(X)-ord('!')
            Seed = (Seed * 91 + Y) & 0x7fffffff
        random.seed(Seed)
    else:
        Password=False

    if os.path.isdir(Fname):
        print('>>>>>isdir')
        os.system('tar czf /tmp/tmp.tzf %s'%Fname)
        Fname = '/tmp/tmp.tzf'
        wasDir=True
    else:
        print('>>>>>nodir')
        wasDir=False

    if What[0] in 'dD':
        File = open(Fname,'r')
        if not OutFileName:
            OutFileName='decoded.file'
        decode_file(File)
        Str = 'file %s'%OutFileName
        print('str "%s"'%Str)
        Pipe = os.popen(Str)
        What = Pipe.read()
        if 'gzip compressed data' in What:
            os.system('/bin/mv %s aaa.%s'%(OutFileName,OutFileName))
            os.system('tar xzf aaa.%s'%(OutFileName))
        print('what',What)
    else:
        File = open(Fname,'rb')
        if not OutFileName:
            OutFileName='encoded.file'
        encode_file(File)
    if wasDir: 
        os.system('/bin/rm /tmp/tmp.tzf')

import zlib



def encode_file(File):
    Fout = open(OutFileName,'w')
    Zobj = zlib.compressobj(9)
    encline=''
    while 1:
        line = File.read(128)
        if Password:
            line=encrypt_line(line,'a')
        if line=='':
            if ZLIB:
                encline += Zobj.flush()
                encline = encode_in_parts(encline,Fout)
                encoding(Fout,encline,True)
                return
            else:
                encline = encode_in_parts(encline,Fout)
                encoding(Fout,encline,True)
                return
        else:
            if ZLIB:
                encline += Zobj.compress(line)
            else:
                encline +=line
        encline = encode_in_parts(encline,Fout)

def encode_in_parts(encline,Fout):
    while len(encline)>128:
        part = encline[:128]
        encline = encline[128:]
        part=encoding(Fout,part,False)
        encline = part+encline
    return encline

def decode_file(File):
    Fout = open(OutFileName,'w')
    LineNum=0
    Zobj = zlib.decompressobj()
    while 1:
        line = File.readline()
        LineNum += 1
        if line=='':
            res2 = Zobj.flush()
            decoding(Fout,res2,Zobj,LineNum)
#            Fout.write(res2)
            Fout.close()
            return
        decoding(Fout,line,Zobj,LineNum)


Base = ord('!')+1
def encode3(Ch0,Ch1,Ch2):
        X = (ord(Ch0)<<16)+(ord(Ch1)<<8)+ord(Ch2)
        C0 = Base + ((X>>18)&0x3f)
        C1 = Base + ((X>>12)&0x3f)
        C2 = Base + ((X>>6)&0x3f)
        C3 = Base + (X&0x3f)
        return '%s%s%s%s'%(chr(C0),chr(C1),chr(C2),chr(C3))

def encoding(Fout,Chars,Last):
    if (Chars=='')and not Last:
        return
    res = ['!']
    while len(Chars)>=3:
        Add = encode3(Chars[0],Chars[1],Chars[2])
        Chars = Chars[3:]
        res.append(Add)
    if Last and (len(Chars)>0):
        if len(Chars)==1:
            res[0]='{'
            Chars += '00'
        elif len(Chars)==2:
            res[0]='}'
            Chars += '0'
        Add = encode3(Chars[0],Chars[1],Chars[2])
        res.append(Add)
        Chars=''

    str1 = ''.join(res)+'!\n'
    Fout.write(str1)
    if Last:
        Fout.write('!!\n')
        Fout.close()
    return Chars

# line must start with "!" end with "!" and new line char.
# between those it must have divisible by 3 number of chars.
def decoding(Fout,Line,Zobj,Num):
    if len(Line)<3:
        return
    if Line[0]=='!':
        End=0
    elif Line[0]=='{':
        End=1
    elif Line[0]=='}':
        End=2
    else:
        print('wrong format "%s" is not my line. @%d'%(Line,Num))
        return
    if Line[-2]!='!':
        print('wrong format "%s" is not my line. @%d'%(Line,Num))
        return
    Char = Line[1:-2]
    Len= len(Char)
    if (Len & 3)!=0:
        print('wrong format "%s" is not my line. @%d'%(Line,Num))
        sys.exit()
    i = 0 
    res = ''
    while Char!='':
        A,B,C = decode2(Char[0],Char[1],Char[2],Char[3])
        Char = Char[4:]
        res = res + A+B+C
    if ZLIB:
        res2 = Zobj.decompress(res)
    else:
        res2=res
    if End==1:
        res2=res2[:-2]
    elif End==2:
        res2=res2[:-1]
    if Password:
        res2=encrypt_line(res2,'b')
    Fout.write(res2)

def decode2(A,B,C,D):
    A0 = (ord(A)-Base)&0x3f    
    B0 = (ord(B)-Base)&0x3f    
    C0 = (ord(C)-Base)&0x3f    
    D0 = (ord(D)-Base)&0x3f    
    X =  (A0<<18)+(B0<<12)+(C0<<6)+(D0)
    Ch0 = chr((X>>16)&0xff)
    Ch1 = chr((X>>8)&0xff)
    Ch2 = chr(X&0xff)
    return Ch0,Ch1,Ch2        
     
def encrypt_line(line,Txt):
    res=''
    for Chr in line:
        if type(Chr) is int:
            X = chr(Chr ^ random.randint(0,255))
        else:
            X = chr(ord(Chr) ^ random.randint(0,255))
        res += X
    return res


main()
