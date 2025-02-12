#! /usr/bin/env python3
import os,sys,string
import importlib

def main():
    Dir = sys.argv[1]
    List = os.listdir(Dir)
    Hiername = sys.argv[2]
    Prefix = sys.argv[3]
    Cut = '-cut' in sys.argv
    xx = Hiername.split('/')
    From = '/'.join(xx[:-1])
    sys.path.append(From)
    That = importlib.import_module(xx[-1][:-3])
    HIER = That.HIER
    Fout = open('holder/tb_mon.v','w')
    Fmvlg = open('holder/tb_mon.mvlg','w')
    Fmvlg.write('tb_mon.v\n')
    Fout.write('module tb_mon;\n')
    Fout.write('initial $dumpvars(0,tb_mon);\n')
    for Fname in List:
        if Fname.endswith('_friend.v'):
            Module = Fname[:-9]
            Path,Inst = getPathInst(Module,HIER)
            if not Path: 
                Path,Inst = '',Module
            if Cut and ('.' in Path):
                Ind = Path.index('.')
                Path = Path[Ind+1:]
             
            if Path == '':
                Path = Prefix
            else:
                Path = Prefix + '.' + Path
            Fout.write('%s_friend %s (\n' % (Module,Inst))
            Fmvlg.write('%s_friend.v\n' % (Module))
            Fcon = open('holder/%s.list' % Module)
            Big = Fcon.read()
            Fcon.close()
            Nets = Big.split()
            Pref = ' '
            for Net in Nets:
                Fout.write('    %s.%s(%s.%s)\n' % (Pref,Net,Path,Net))
                Pref = ','
            Fout.write(');\n')

    Fout.write('endmodule\n')
    Fout.close()
    Fmvlg.close()

def getPathInst(Module,HIER):
    for Path in HIER:
        Type,Inst= HIER[Path]
        if Type == Module: return Path,Inst
    return False,False

if __name__ == '__main__': main()
