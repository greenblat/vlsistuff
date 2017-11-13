

import os,sys,string,random
import veri

sys.path.append('../vlibs')
import logs
import stilPlayer

cycles=0
def negedge():
    global cycles
    cycles += 1
    veri.force('tb.cycles',str(cycles))
    if (cycles>100000):
        veri.finish()

    stilPlayer.run()



