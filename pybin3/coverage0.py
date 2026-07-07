#! /usr/bin/env python3

import os,sys

# 40645 TGL tb.peripheral0.dataport5.p4_periph_slot_scheduler.tgl_mon_channel_number   p4_periph_slot_scheduler     cha  nnel_number 0xf

#      14243 ALWLINECOV p4_periph_slot_scheduler num_active_channels          0   

# 3 TGLC tb.peripheral0.p4_periph_top_sm.tgl_mon_cds_change p4_periph_top_sm  cds_change 2
# 17611 ALWC tb.peripheral1.p4_periph_lc_control.covstep p4_periph_lc_control lc_inactivity_cnt 11 

ALWS = {}
ASSIGNS = {}

DISPS = '/Users/iliagreenblat/project4/linecov'

def main():
    for Fname in sys.argv[1:]:
        if os.path.isdir(Fname):
            Files = os.listdir(Fname)
            for File in Files:
                if File.endswith('.log'):
                    oneFile('%s/%s' % (Fname,File))
        else:
            print("FNAME",Fname)
            oneFile(Fname)
    conclusions()
    

def oneFile(Fname):
    print('work %s' % Fname)
    File = open(Fname)
    Lines = File.readlines()
    File.close()
    for Line in Lines:
        if 'ALWC ' in Line:
            ww = Line.split()
            Module = ww[1]
            Bus = ww[2] 
            Mask = int(ww[3],2)
            if (Module,Bus) not in ALWS: ALWS[(Module,Bus)] = 0
            ALWS[(Module,Bus)] |= Mask

        if 'TGLC ' in Line:
            ww = Line.split()
            Module = ww[1]
            Bus = ww[2] 
            Changes = int(ww[3])
            Key = (Module,Bus) 
            if Key not in ASSIGNS: ASSIGNS[Key] = 0
            ASSIGNS[Key] += Changes


        if 'ALW ' in Line:
            ww = Line.split()
            Module = ww[2]
            Bus = ww[3] 
            Where = int(ww[4])
            if (Module,Bus) not in ALWS: ALWS[(Module,Bus)] = 0
            ALWS[(Module,Bus)] |= (1<<Where)

        if 'TGL ' in Line:
            ww = Line.split()
            Module = ww[2]
            Bus = ww[3] 
            Key = (Module,Bus) 
            if Key not in ASSIGNS: ASSIGNS[Key] = 0
            ASSIGNS[Key] += 1

def conclusions():
    Frep = open('coverage.report','w')
    for (Module,_) in ALWS:
        loadDisp(Module)

    Goods = 0
    Total = 0
    for (M,B) in ALWS:
        if (M in LOADED_ALW) and (B in LOADED_ALW[M]):
            Max = LOADED_ALW[M][B]
            Now = bin(ALWS[(M,B)])[2:]
            Total += len(Max)
            Goods += Now.count('1')
            Now,Missed,Covered = extractMissed(Max,Now)
            if Max==Now:
                Frep.write("ALWS: %20s  %20s     %s COVERED!\n" % (M,B,Now))
            else:
                Frep.write("ALWS: %20s  %20s    covered=%s  missed=%s\n" % (M,B,Now,Missed))
            for MM in Missed:
                Frep.write("ALWS: missing  %s  %s  %s\n" % (M,B,MM))
            for MM in Covered:
                Frep.write("ALWS: covered  %s  %s  %s\n" % (M,B,MM))
        else:
            Frep.write("ALWS error %s %s missing from base dspl\n" % (M,B))
            print("ALWS ERROR %s %s missing from base dspl\n" % (M,B))
    if Total==0:
        Ratio = 0
    else:
        Ratio =  (Goods*100/Total)
    Frep.write('ALWS:  caught %d out of %d (%.2f%%)\n' % (Goods,Total,Ratio))
    print('ALWS:  caught %d out of %d (%.2f%%)\n' % (Goods,Total,Ratio))
    print('__________________________________________')
    Total = 0
    PresentModules = []
    for (M,B) in ASSIGNS:
        Frep.write("TGLS: %20s  %20s     %d\n" % (M,B,ASSIGNS[(M,B)]))
        Total += 1
        if M not in PresentModules: PresentModules.append(M)
    Missing = 0
    Covered = 0
    for Module in LOADED_TGL:
        All = LOADED_TGL[Module]
        for Bus in All:
            if (Module,Bus) not in ASSIGNS:
                Frep.write("TGLS: missing %s %s\n" % (Module,Bus))
                Missing += 1
            else:
                Frep.write("TGLS: covered %s %s\n" % (Module,Bus))
                Covered += 1
    Frep.write("TGLS: missing/total %d/%d  =  %.1f\n" % (Missing,len(All),(Missing*100/len(All))))
    print("TGLS: missing/total %d/%d  =  %.1f\n" % (Missing,Missing+Covered,(Missing*100/(Missing+Covered))))
    Frep.close()


LOADED_ALW = {}
LOADED_TGL = {}

def loadDisp(Module):
    if Module in LOADED_ALW: return
    Fname = '%s/%s.disp' % (DISPS,Module)
    Fname1 = '%s.disp' % (Module)
    if os.path.exists(Fname):
        File = open(Fname)
        Lines = File.readlines()
        File.close()
    elif os.path.exists(Fname1):
        File = open(Fname1)
        Lines = File.readlines()
        File.close()
    else:
        print('no disp %s' % Fname)
        return
    Here = {}
    LOADED_ALW[Module] = Here
    LOADED_TGL[Module] = []
    for line in Lines:
        line = line.replace('"','')
        ww = line.split()
        Num = int(ww[2])
        Sig = ww[1]
        if Num<999:
            Here[Sig] = bin((1<<(Num+1))-1)[2:]
        else:
            LOADED_TGL[Module].append(Sig)
            
            

def extractMissed(Max,Now):
    while len(Now)<len(Max):
        Now = '0'+Now
    Missed = []
    Covered = []
    for ii in range(len(Now)-1,-1,-1):
        if Now[ii] == '0':
            Missed.append(len(Now)-1-ii)
        else:
            Covered.append(len(Now)-1-ii)
    return Now,Missed,Covered
        



main()



