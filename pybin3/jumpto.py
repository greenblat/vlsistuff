#! /usr/bin/env python3
import os,sys,string

CURRENTS = '''
cd ~/projects/my6809    ::: my 6809 rtl
cd ~/project2           ::: CANFD latest
cd ~/project0           ::: LIN   latest
cd ~/project1           ::: SPMI  latest
cd ~/clients/magic/mlcpu           ::: MLCPU  latest, inside there is vrltb
'''
def main():
    print(CURRENTS)
    

if __name__ == '__main__': main()
