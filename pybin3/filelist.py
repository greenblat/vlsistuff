#! /usr/bin/env python3

import os,sys

def main():
    Flist = sys.argv[1]
    File = open(Flist)
    Lines = File.readlines()
    File.close()

    Fout = open('starting.tcl','w')
    Fout.write(HEADER)

    for line in Lines:
        wrds = line.split()
        if (len(wrds) == 1) and os.path.exists(wrds[0]):
            Fout.write('add_files -norecurse {%s}\n' % wrds[0])            
            Fout.write('set_property file_type SystemVerilog [get_files %s]\n' % wrds[0])
    Fout.write(TRAILER)
    Fout.close()


TRAILER = '''
update_compile_order -fileset sources_1
launch_runs synth_1 -jobs 4
wait_on_run synth_1
'''

            
HEADER = '''
'''

main()


