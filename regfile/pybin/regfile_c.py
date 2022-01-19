
import string,os,sys
import logs
HEADER = '''
// auto generated C headers file of MODULE regfile
#ifndef __RF_INTERFACE_RGF_H
    #define __RF_INTERFACE_RGF_H

    #include <inttypes.h>

    typedef struct {
'''

def produce_c_headers(Module,Db):
   Chip = Db['chip']
   Items = Db['items']
   Range = Chip.Addr+4
   Fch = open('%s_cinc.h'%(Module),'w')
   Fch.write(HEADER.replace('MODULE',Module).replace('RF_INTERFACE_RGF',Module.upper()))
   outputStructures(Module,Items,Fch)
   outputFields(Items,Fch)
   Fch.write('\n#endif\n')
   Fch.close()


def outputStructures(Module,Items,Fch):
    RunAddr = 0
    for Item in Items:
        if Item.Kind=='reg':
            if 'description' not in Item.Params: Item.Params['description'] = ''
            Desc = Item.Params['description'].replace('.',' ')
            Name = Item.Name
            Width = Item.Params['width']
            Access = Item.Params['access']
            WW = ''
            Jump = 1
            if Width>32:
                Jump = (int(Width/32)+((Width%32)!=0))
                WW = '[%d]'%Jump
            if 'w' in Access:
                ACC = 'rw'
            else:
                ACC = 'ro'
            Addr = hex(Item.Addr)
            if Item.Addr>RunAddr:
                Empties = int((Item.Addr-RunAddr)/4)+( ((Item.Addr-RunAddr)%4)!=0)
                if Empties<2:
                    Fch.write('    ro uint32_t  %15s;          // gap\n'%('gap'+Addr)) 
                else:
                    Fch.write('    ro uint32_t  %15s;          // gap\n'%('gap%s[%d]'%(Addr,Empties))) 

            NW = '%s%s'%(Name.upper(),WW)
            Fch.write('    %s uint32_t  %-25s;          // ad=%s w=%d acc=%s      %s\n'%(ACC,NW,Addr,Width,Access,Desc)) 
            RunAddr = Item.Addr+(Jump*4)

    Fch.write('} %s_RegDef;\n\n'%Module)

def ensureParam(Item,Param):
    if Param in Item.Params: return
    logs.log_error('#%d: ensureParams item=%s missing=%s   avail=%s'%(Item.Lnum,Item.Name,Param,Item.Params))
    Item.Params[Param] = -1,-1

def outputFields(Items,Fch):
    for Item in Items:
        if Item.Kind=='reg':
            Active = Item.Name
        elif Item.Kind=='field':
            ensureParam(Item,'width')
            ensureParam(Item,'position')
            Fch.write('#define %s_COUNT (%d)\n'%(Item.Name,Item.Params['width']))
            Fch.write('#define %s_OFFSET (%s)\n'%(Item.Name,Item.Params['position'][1]))

