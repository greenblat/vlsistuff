#! /usr/bin/env python3

# turn csv to instances
# to prepare csv you may use something like this: 
#  pyver.py rtl/sw_scheduler.v rtl/sw_send10.v rtl/sw_bytedrive.v -do prepareCsv -do clean
import os,sys

Insts = {}
# sw_scheduler,driving,o,1,driving
def main():
    Fname = sys.argv[1]
    Csv = open(Fname)
    Lines = Csv.readlines()
    Csv.close()

    for line in Lines:
        line = line[:-1]
        wrds = line.split(',')
        Module,Net,Dir,Wid,Conn = wrds
        if Module != 'module':
            if Module not in Insts: Insts[Module] = []
            Insts[Module].append( (Net,Wid,Conn) )
    Nets = {}
    for Inst in Insts:
        for (Net,Wid,Conn) in Insts[Inst]:
            if Net not in Nets:
                Nets[Net] = Wid
            elif (Wid != Nets[Net]):
                print('discrepancy %s %s %s' % (Net,Wid,Nets[Net],Inst))
    Fout = open('xcons.vx','w')
    for Net in Nets:
        Wid = int(Nets[Net])
        if Wid>1:
            Fout.write('wire [%s:0] %s;\n' % (Wid-1,Net))
        else:
            Fout.write('wire %s;\n' % (Net))

    for Inst in Insts:
        Fout.write('%s %s (\n' % (Inst,Inst))
        Pref = ' '
        for (Net,Wid,Conn) in Insts[Inst]:
            Fout.write('    %s.%s(%s)\n' % (Pref,Net,Conn))
            Pref = ','
        Fout.write(');\n')

    Fout.close()
        
            


if __name__ == '__main__': main()
