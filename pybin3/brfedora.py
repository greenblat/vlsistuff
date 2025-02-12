#! /usr/bin/env python3.10

import os,sys,string

FNAME = sys.argv[1]
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect('192.168.68.120', username='ilia',password='talnirran')   # ,key_filename='')

#Setup sftp connection and transmit this script
print ("copying")

sftp = client.open_sftp()
ww = FNAME.split('/')
sftp.get('/home/ilia/%s' % FNAME, ww[-1])

sftp.close()



