#! /usr/bin/env python3
import os,sys

def main():
    Fname = sys.argv[1]
    os.system('mvlg.py %s all.files' % Fname)
    File = open('all.files')
    Lines = File.readlines()
    Fout = open('all.files.xpr','w')
    for line in Lines:
        Path = line[line.index('trialfpga')+10:-1]
        Str = CODE.replace('FILE',Path)
        Fout.write(Str)
    Fout.close()


CODE ='''
      <File Path="$PPRDIR/../FILE">
        <FileInfo  SFType="SVerilog">
          <Attr Name="UsedIn" Val="synthesis"/>
          <Attr Name="UsedIn" Val="implementation"/>
          <Attr Name="UsedIn" Val="simulation"/>
        </FileInfo>
      </File>
'''

if __name__ == '__main__': main()
