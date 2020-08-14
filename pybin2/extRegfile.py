#! /usr/bin/env python

import buildDb
import os,sys,string
import logs

NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)

import regfile_busses as busses
def main():
    Fname = sys.argv[1]
    Db = buildDb.readFile(Fname)
    Db.LINES = [ [],[],[],[],[],[],[],[],[],[],[],[]]
    Chip = Db.chip.Params
    prepareBusses(Db) 
    addRamInstance(Db)
    genSpecials(Db)

#    Items = Db.items
#    for Item in Items:
#        print(Item.Params)

    generate(Db)
    generateNewRegfile(Db)

def generateNewRegfile(Db):
    Ind = 0
    while Ind < len(Db.items):
        Item = Db.items[Ind]
        if Item.Kind=='gap':
            Ind += 1
        else: 
            Name = Item.Params['names'][0]
            if Name in Db.makeExternals:
                Was = Item.Params['access']
                Item.Params['access'] = 'external'
                if (Was == 'w1c'):
                    New = buildDb.itemClass(['a','a'])
                    New.Kind = 'reg'
                    New.Params['names'] = [Name+'_clean']
                    New.Params['access'] = 'ro'
                    New.Params['desc'] = 'read.without.clear'
                    New.Params['wid'] = Item.Params['wid']
                    Db.items.insert(Ind,New)
            Ind += 1
    Fout = open('%s_base.regfile'%Db.Module,'w')
    for ind,Item in enumerate([Db.chip]+Db.items):
        Names = Item.Params['names']
        if ind==0:
            Names[0] += '_base'
            if 'axi4lite' in Names: Names.remove('axi4lite')
            if 'apb' in Names: Names.remove('apb')
            if 'ram' not in Names: Names.append('ram')
            Fout.write('%s %s '%(Item.Kind,string.join(Names,' ')))
        Fout.write('%s %s '%(Item.Kind,string.join(Names,' ')))
        for Prm in Item.Params:
            if Prm not in ['names','clk']:
                Fout.write(' %s=%s'%(Prm,Item.Params[Prm]))
        Fout.write('\n')
    Fout.write('end\n')




def addRamInstance(Db):
    Str = string.replace(busses.APBInst,'MODULE',Db.Module+'_base')
    Db.LINES[4].append(Str)
    Db.makeExternals = []
    for Item in Db.items:
        Kind = Item.Kind
        Params = Item.Params
        if Item.Kind!='gap':
            Name = Item.Params['names'][0]
            Wid= getPrm(Item,'width',32)
            Access= getPrm(Item,'access','rw')
        if Item.Kind=='reg':
            if ('clk' in Item.Params)and(Access!='event_counter'):
                Wire = '%s_int'%Name
                Db.LINES[3].append('wire [%s:0] %s;'%(Wid-1,Wire))
            else:
                Wire = Name
            if Access=='ro':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Wire))
            elif Access=='rw':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Wire))
            elif Access=='ro_pulse':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Wire))
                Db.LINES[4].append('    ,.%s_rd_pulse(%s_rd_pulse)'%(Name,Name))
            elif Access=='rw_pulse':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Wire))
                Db.LINES[4].append('    ,.%s_wr_pulse(%s_wr_pulse)'%(Name,Name))
            elif Access=='external':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_wr_pulse(%s_wr_pulse)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_rd_pulse(%s_rd_pulse)'%(Name,Name))
            elif Access=='w1c':
                Db.LINES[4].append('    ,.%s(%s_int)'%(Name,Wire))
                Db.LINES[4].append('    ,.%s_clean(%s_clean)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_wr_pulse(%s_wr_pulse)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_rd_pulse(%s_rd_pulse)'%(Name,Name))
                Db.makeExternals.append(Name)
            elif Access=='event_counter':
                Db.LINES[4].append('    ,.%s(%s)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_wr_pulse(%s_wr_pulse)'%(Name,Name))
                Db.LINES[4].append('    ,.%s_rd_pulse(%s_rd_pulse)'%(Name,Name))
                Db.makeExternals.append(Name)
            else:
                logs.log_info('ERROR! access %s'%Access)
        elif Item.Kind=='ram':
            Db.LINES[4].append('    ,.%s_rdata(%s_rdata)'%(Name,Name))
            Db.LINES[4].append('    ,.%s_addr(%s_addr)'%(Name,Name))
            Db.LINES[4].append('    ,.%s_rd_pulse(%s_rd_pulse)'%(Name,Name))
            Db.LINES[4].append('    ,.%s_wr_pulse(%s_wr_pulse)'%(Name,Name))
        elif Item.Kind=='gap':
            pass
        else:
            logs.log_info('ERROR! kind %s'%Item.Kind)



def prepareBusses(Db):
    if Db.Bus == 'axi4lite':
        Head = busses.AXIHEADER
        Db.LINES[3] = [busses.AXISTRING2]
    elif Db.Bus == 'apb':
        Head = busses.APBHEADER
        Db.LINES[3] = busses.APB2RAM
    elif Db.Bus == 'ram':
        Head = busses.RAMHEADER
    Str = string.replace(Head,'MODULE',Db.Module)
    Db.LINES[0] = [Str]
    Clocks = getClocks(Db)
    for Clk in Clocks: Db.LINES[1].append('    ,input %s'%Clk)

    for Item in Db.items:
        Kind = Item.Kind
        Params = Item.Params
        if Item.Kind!='gap':
            Name = Item.Params['names'][0]
            Wid= getPrm(Item,'width',32)
            Access= getPrm(Item,'access','rw')
        if Item.Kind=='reg':
            if Access=='ro':
                Db.LINES[2].append('    ,input [%s:0] %s'%(Wid-1,Name))
            elif Access=='rw':
                Db.LINES[2].append('    ,output [%s:0] %s'%(Wid-1,Name))
            elif Access=='ro_pulse':
                Db.LINES[2].append('    ,input   [%s:0] %s'%(Wid-1,Name))
                Db.LINES[2].append('    ,output  %s_rd_pulse'%(Name))
            elif Access=='rw_pulse':
                Db.LINES[2].append('    ,output [%s:0] %s'%(Wid-1,Name))
                Db.LINES[2].append('    ,output  %s_wr_pulse'%(Name))
            elif Access=='external':
                Db.LINES[2].append('    ,input [%s:0] %s'%(Wid-1,Name))
                Db.LINES[2].append('    ,output  %s_wr_pulse'%(Name))
                Db.LINES[2].append('    ,output  %s_rd_pulse'%(Name))
            elif Access=='w1c':
                Db.LINES[2].append('    ,input   [%s:0] %s'%(Wid-1,Name))
                Db.LINES[3].append('wire [%s:0] %s_clean;'%(Wid-1,Name))
            elif Access=='event_counter':
                Db.LINES[2].append('    ,input   %s_countup'%(Name))
                Db.LINES[3].append('wire [%s:0] %s;'%(Wid-1,Name))
            else:
                logs.log_info('ERROR! access %s'%Access)
        elif Item.Kind=='ram':
            Line = '    ,input [%d:0] %s_rdata'%(Wid-1,Name)
            Db.LINES[2].append(Line)
            Dep = getPrm(Item,'depth',32)
            Line = '    ,output [%d:0] %s_addr'%(logs.neededBits(Dep-1),Name)
            Db.LINES[2].append(Line)
            Line = '    ,output %s_rd_pulse'%(Name)
            Db.LINES[2].append(Line)
            Line = '    ,output %s_wr_pulse'%(Name)
            Db.LINES[2].append(Line)
        elif Item.Kind=='gap':
            pass









def getClocks(Db):
    Clocks = []
    for Reg in Db.items:
        if 'clk' in Reg.Params:
            Clk = Reg.Params['clk']
            if Clk not in Clocks: Clocks.append(Clk)
    Db.Clocks = Clocks
    return Clocks

def genSpecials(Db):
    for Item in Db.items:
        Kind = Item.Kind
        Params = Item.Params
        if (Item.Kind=='reg'):
            Name = Item.Params['names'][0]
            Wid= getPrm(Item,'width',32)
            Access= getPrm(Item,'access','rw')
            if 'clk' in Params:
                Clk = Params['clk']
                if (Access=='rw'):
                    Str = 'mlbr_rw_async #(.WID(%s)) i_%s (.clk(%s),.rst_n(rst_n),.wr_pulse(%s_wr_pulse)\n'%(Wid,Name,Clk,Name)
                    Str += '    ,.dout(%s),.din(%s_int));'%(Name,Name)
                    Db.LINES[5].append(Str)
                elif (Access=='event_counter'):
                    Str = 'mlbr_event_counter_async #(.WID(%s)) i_%s (.clk(clk),.rst_n(rst_n),.oclk(%s),.rd_pulse(%s_rd_pulse)\n'%(Wid,Name,Clk,Name)
                    Str += '    ,.countup(%s_countup),.dout(%s));'%(Name,Name)
                    Db.LINES[5].append(Str)
                elif (Access=='w1c'):
                    Str = 'mlbr_w1c_async #(.WID(%s)) i_%s (.clk(clk),.rst_n(rst_n),.oclk(%s),.rd_pulse(%s_rd_pulse)\n'%(Wid,Name,Clk,Name)
                    Str += '    ,.wr_pulse(%s_wr_pulse)\n'%(Name)
                    Str += '    ,.rd_clean(%s_clean_rd_pulse)\n'%(Name)
                    Str += '    ,.dout(%s_int),.dclean(%s_clean),.din(%s));'%(Name,Name,Name)
                    Db.LINES[5].append(Str)
                elif (Access=='ro'):
                    Str = 'mlbr_ro_async #(.WID(%s)) i_%s (.clk(%s),.rst_n(rst_n),.rd_pulse(%s_rd_pulse)\n'%(Wid,Name,Clk,Name)
                    Str += '    ,.dout(%s_int),.din(%s));'%(Name,Name)
                    Db.LINES[5].append(Str)
            elif (Access=='w1c'):
                Str = 'mlbr_w1c_sync #(.WID(%s)) i_%s (.clk(clk),.rst_n(rst_n),.rd_pulse(%s_rd_pulse)\n'%(Wid,Name,Name)
                Str += '    ,.wr_pulse(%s_wr_pulse)\n'%(Name)
                Str += '    ,.rd_clean(%s_clean_rd_pulse)\n'%(Name)
                Str += '    ,.dout(%s_int),.dclean(%s_clean),.din(%s));'%(Name,Name,Name)
                Db.LINES[5].append(Str)
            elif (Access=='event_counter'):
                Str = 'mlbr_event_counter_sync #(.WID(%s)) i_%s (.clk(clk),.rst_n(rst_n),.rd_pulse(%s_rd_pulse)\n'%(Wid,Name,Name)
                Str += '    ,.countup(%s_countup),.dout(%s));'%(Name,Name)
                Db.LINES[5].append(Str)

def generate(Db):
    File = open('%s.v'%Db.Module,'w')
    for Line in Db.LINES[0]:
        File.write('%s\n'%Line)

    for Line in Db.LINES[1]:
        File.write('%s\n'%Line)

    for Line in Db.LINES[2]:
        File.write('%s\n'%Line)
    File.write(');\n')
    for Line in Db.LINES[3]:
        File.write('%s\n'%Line)
    for Line in Db.LINES[4]:
        File.write('%s\n'%Line)
    File.write(');\n')
    for Line in Db.LINES[5]:
        File.write('%s\n'%Line)
    File.write('endmodule\n')
    File.close()


def getPrm(Obj,Name,Default):
    if Name in Obj.Params: return Obj.Params[Name]
    return Default

if __name__ == '__main__': main()

