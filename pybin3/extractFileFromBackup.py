#! /usr/bin/env python3
import os,sys,string

def main():
#    print("extractFileFromBackup.py  TGZname filename")
    Tgz = sys.argv[1]
    Fname = sys.argv[1]
    Tgza = os.path.abspath(Tgz)

    os.system('cd /tmp ; mkdir xyz; cd xyz; tar xzf %s' % Tgza)
    os.system('cd /tmp/xyz ; find /tmp/xyz -name %s > /tmp/xyz/aaa' % Fname)
    os.system('echo FIND; cat /tmp/xyz/aaa')
    os.system('cd /tmp/xyz ; find /tmp/xyz -name %s ' % Fname)
    File = open('/tmp/xyz/aaa')
    Lines = File.readlines()
    File.close()
    print('lines',Lines)
    os.system('/bin/rm -R /tmp/xyz')



if __name__ == '__main__': main()
