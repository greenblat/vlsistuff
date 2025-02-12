#! /usr/bin/env python3.10
import os,sys
import time
import keyboard
def main():
    Fname = sys.argv[1]
    File = open(Fname)
    Lines = File.readlines()
    File.close()
    print("SWITCH TO OTHER WINDOW")
    for ii in range(5,-1,-1):
        print("%d secs" % ii)
        time.sleep(1)
    for Line in Lines:
        keyboard.write(Line)


if __name__ == '__main__': main()
