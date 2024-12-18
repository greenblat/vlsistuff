#! /usr/bin/env python3
import os,sys,string

def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Lines = File.readlines()
    Open = False
    for line in Lines:
        if ('>>>>>>>' in line) and line.startswith('>>>>>>>'):
            if Open: Open.close()
            ww = line.split()
            ww2 = ww[1].split('/')
            if not os.path.exists('./%s' % ww2[0]): os.mkdir(ww2[0])
            Open = open(ww[1],'w')

        elif Open:
            Open.write(line)

    if Open: Open.close()
        




if __name__ == '__main__': main()
