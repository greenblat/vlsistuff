#! /usr/bin/env python3.10
import os,sys,string
import paramiko
import datetime

def main():
    Fname = sys.argv[1]
    ww = Fname.split('/')
    Dst = ww[-1]
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect('192.168.68.120', username='ilia',password='talnirran')   # ,key_filename='')
    print ("copying")
    sftp = client.open_sftp()
    sftp.put(Fname,'/home/ilia/%s' % (Dst))
    sftp.close()

# fedora:
# ilia@192.168.68.120



if __name__ == '__main__': main()
