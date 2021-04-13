#! /usr/bin/env python3
import os,sys,string

def main():
    os.system('gitspace status > aaa')
    File = open('aaa')
    Lines = File.readlines()
    for Line in Lines:
        if ' M ' in Line:
            Ind = Line.index(' M ')
            End = Line[Ind+2:-1]
            print('gitspace add '+End)
        elif ' D ' in Line: 
            Ind = Line.index(' D ')
            End = Line[Ind+2:-1]
            print('gitspace add '+End)
    print('\n')


if __name__ == '__main__': main()

