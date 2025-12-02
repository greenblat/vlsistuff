#! /usr/bin/env python3


import os,sys

# sys.path.append('/Users/iliagreenblat/vlsistuff/verpy/pybin3')

def main():
    Mod = module_class.module_class('allegro')
    Dir = sys.argv[1]
    readPSTXPRT(Dir,Mod)
    readPSTCHIP(Dir,Mod)
    readPSTXNET(Dir,Mod)

    File = open('allegro.v','w')
    for Key in MAP:
        File.write('// MAP %s = %s\n' % (Key,MAP[Key]))
    for Key in Primitives:
        File.write('// PRIMS %s = %s\n' % (Key,Primitives[Key]))
    cleanInstanceNames(Mod)
    Mod.dump_verilog(File)
    File.close()

def cleanInstanceNames(Mod):
    Insts = list(Mod.insts.keys())
    cleaned = 0
    for Inst in Insts:
        Obj = Mod.insts[Inst]
        if '(' in Obj.Type:
            Obj.Type = removeBrackets(Obj.Type)
            Mod.insts[Inst] = Obj
            cleaned += 1
            
        if '(' in Inst:
            New = removeBrackets(Inst)
            Obj = Mod.insts.pop(Inst)
            Obj.Type = removeBrackets(Obj.Type)
            Mod.insts[New] = Obj
            cleaned += 1



    print("CLEANED",cleaned)    
def removeBrackets(Inst):
    if '(' not in Inst: return Inst
    St = Inst.index('(')
    if ')' in Inst:
        En = Inst.index(')')
        New = Inst[:St]+Inst[En+1:]
        return New
    
    New = Inst[:St]
    return New

def readPSTCHIP(Dir,Mod):
    File = open(Dir+'/pstchip.dat')
    Lines = File.readlines()
    File.close()
    workOnLinesCHIP(Lines,Mod)

def readPSTXPRT(Dir,Mod):
    File = open(Dir+'/pstxprt.dat')
    Lines = File.readlines()
    File.close()
    workOnLinesXPRT(Lines,Mod)

def readPSTXNET(Dir,Mod):
    File = open(Dir+'/pstxnet.dat')
    Lines = File.readlines()
    File.close()
    workOnLinesXNET(Lines,Mod)

import module_class
state = ['idle','idle','idle']
def workOnLinesXNET(Lines,Mod):
    for Line in Lines:
        Line = Line.replace("'",' ')
        wrds = Line.split()
        if state[0] == 'idle':
            if (len(wrds)>0) and (wrds[0] == 'NET_NAME'):
                state[0] = 'net_name' 
        elif state[0] == 'net_name':
            Net = wrds[0]
            if Net[0] in '0123456789': Net = '_'+Net
            state[0] = 'nodes'
            Mod.add_net(Net,'wire',1)
        elif state[0] == 'nodes':
            if wrds[0] == 'NODE_NAME':
                Inst = wrds[1]
                if Inst not in Mod.insts:
                    if Inst in MAP:
                        Typex = MAP[Inst]
                    else:
                        Typex = Inst
                    Mod.add_inst(Typex,Inst)
                Pin = wrds[2]
                Type,Pin = findPin(Inst,Pin)
                if Pin[0] in '0123456789': Pin = '_'+Pin
#                if Inst == 'SW16':
#                    print("SW16 ",Pin,wrds[2],Type)
                Mod.add_conn(Inst,Pin,Net)
            elif wrds[0] == 'NET_NAME':
                state[0] = 'net_name' 
                
def findPin(Inst,Pin):
    if Inst in MAP:
        Type = MAP[Inst]
    else:
        Type = Inst
    if Type in Primitives:
        Name,Pins = Primitives[Type]
#        if Inst == 'SW16':
#            print("BEF %s %s %s %s" % (Type,Pin,Name,Pins))
        for Str,Num,Use in Pins:
            if Num == Pin:
                Pin = Str
                Pin = Pin.replace('-','_')
#                if Inst == 'SW16':
#                    print("AFT",Pin,Name,"   >",Str,Num,Use)
                return Name,Pin
    Pin = Pin.replace('-','_')
    return Type,Pin

chip_st = 'idle'
Primitives = {}
def workOnLinesCHIP(Lines,Mod):
    global chip_st
    Name = '?'
    Primitive = '?'
    Number = '?'
    Pins = []
    for Line in Lines:
        Line = Line.replace("'",' ')
        Line = Line.replace(";",' ')
        Line = Line.replace("=",' ')
        Line = Line.replace("(",' ')
        Line = Line.replace(")",' ')
        wrds = Line.split()
        if wrds==[]:
            pass
        elif chip_st == 'idle':
            if wrds[0] == 'primitive':
                Primitive = wrds[1]
                chip_st = 'pins0'
                Pins = []
        elif chip_st == 'pins0':
            if wrds[0] == 'pin':
                chip_st = 'pins1'
            elif wrds[0] == 'body':
                chip_st = 'body0'
        elif chip_st == 'pins1':
            if wrds[-1] == ':':
                Pin =  wrds[0]
                chip_st = 'pins2'
            elif wrds[0] == 'end_pin':
                chip_st = 'body'
        elif chip_st == 'pins2':
            if wrds[0] == 'PIN_NUMBER':
                Number = wrds[1]
                chip_st = 'pins3'
        elif chip_st == 'pins3':
            if wrds[0] == 'PINUSE':
                Use = wrds[1]
                chip_st = 'pins1'
                Pins.append((Pin,Number,Use))
            elif wrds[0] == 'end_pin':
                chip_st = 'body'
        elif chip_st == 'body':
            if (wrds[0] == 'body'):
                chip_st = 'body0'
        elif chip_st == 'body0':
            if wrds[0] == 'PART_NAME':
                Name = wrds[1]
            elif (wrds[0] == 'end_body'):
                chip_st = 'after'
        elif (chip_st == 'after'):
            if wrds[0] == 'end_primitive':
                chip_st = 'idle'
                Primitives[Primitive] = (Name,Pins)
#        if wrds!=[]:
#            print("CHIP %s %s %s  %s" % (chip_st,Primitive,Name,Pins))

xprt_st = 'idle'
MAP = {}
def workOnLinesXPRT(Lines,Mod):
    global xprt_st
    for Line in Lines:
        Line = Line.replace("'",' ')
        Line = Line.replace(";",' ')
        Line = Line.replace(":",' ')
        Line = Line.replace("=",' ')
        wrds = Line.split()
        if wrds==[]:
            pass
        elif xprt_st == 'idle':
            if wrds[0] == 'PART_NAME':
                xprt_st = 'part_name'
        elif xprt_st == 'part_name':
            Inst = wrds[0]
            Type = wrds[1]
            xprt_st = 'idle'
            MAP[Inst] = Type
            
main()







