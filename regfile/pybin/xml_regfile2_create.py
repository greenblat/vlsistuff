
import logs
import string

Check = '''

#ifndef CHECK
#define CHECK


'''

def createXml(Module,Db):
    Chip = Db['chip']
    Items = Db['regs']
    Range = Chip.Addr+4
    Fout = open('%s/%s.xml'%(Db['dir'],Module),'w')
    Fccc = open('%s/%s.h'%(Db['dir'],Module),'w')
    Fccc.write(Check.replace('CHECK','%s_'%Module.upper()))
    Fccc.write('#define %s_BASEADDR    0x0\n'%(Module.upper()))
    Fvcc = open('%s/%s.vh'%(Db['dir'],Module),'w')
    Fvcc.write('`define %s_BASEADDR    \'h0\n'%(Module.upper()))
    Str = HEADER.replace('NAME',Module)
    Str = Str.replace('LIBRARY','AutoTalksLib')
    Str = Str.replace('BASEADDR','0')
    Str = Str.replace('RANGE','%x'%Range)
    Fout.write(Str)
    BusWidth = Db['chip'].Params['width']
    Pref = ''
    if 'pref' in Db['chip'].Params:
        Pref = Db['chip'].Params['pref']

    for Item in Items:
        Usable=True
        if Item.Kind=='ram':
            Acc = 'ram'
            Amount = Item.Params['depth']
        elif Item.Kind=='gap':
            Usable=False
        elif Item.Kind=='field':
            Usable=False
        elif Item.Kind=='external':
            Usable=False
        else:
            logs.mustKey(Item.Params,'access','#%d:'%Item.Lnum) 
            if 'access' in Item.Params:
                Acc = Item.Params['access']
            Amount = 0
        if Usable: 
            Wid = Item.Params['width']
            Reg = Item.Params['names'][0]
            if 'desc' in Item.Params:
                Item.Params['description'] = Item.Params['desc']
            if 'description' not in Item.Params:
                Desc = 'DESC NOT GIVEN'
                logs.log_warning('#%d: description of %s not given'%(Item.Lnum,Reg))
            else:
                Desc = Item.Params['description']
            if 'reset' not in Item.Params:
                Reset = 0
            else:
                Reset = Item.Params['reset']
            Addr = Item.Addr
    #        Fout.write('item %s %x %s\n'%(Item.Kind,Item.Addr,Item.Params))
            print("ASASAS",Wid,Reg,Addr)
            if Wid<=32:
                print("ASASAS",Wid,Reg,Addr)
                writeItem(Db,Item,Fout,Module,Acc,Addr,Wid,Reset,Desc,Reg,Amount)
            else:
                Acc0 = Acc
                Acc = Acc.replace('_pulse','')
                Run = 0
                while Wid>32:
                    writeItem(Db,Item,Fout,Module,Acc,Addr,32,Reset,Desc,Reg+'_%d'%Run,Amount)
                    Addr += 4
                    Run += 1 
                    Wid -= 32
                writeItem(Db,Item,Fout,Module,Acc,Addr,Wid,Reset,Desc,Reg+'_%d'%Run,Amount)
            Addr = Item.Addr
            Wid = Item.Params['width']
            if (Wid>BusWidth)and(Wid<=(BusWidth*2)):
                BusBytes = int(BusWidth/8)
                Fccc.write('#define %sADDR_%-50s  (%s_BASEADDR+0x%x)\n'%(Pref,Reg.upper()+'_LO',Module.upper(),Addr))
                Fccc.write('#define %sADDR_%-50s  (%s_BASEADDR+0x%x)\n'%(Pref,Reg.upper()+'_HI',Module.upper(),Addr+BusBytes))
                Fvcc.write('`define %sADDR_%-50s  \'h%x\n'%(Pref,Reg.upper()+'_LO',Addr))
                Fvcc.write('`define %sADDR_%-50s  \'h%x\n'%(Pref,Reg.upper()+'_HI',Addr+BusBytes))
            else:
                Fccc.write('#define %sADDR_%-50s  (%s_BASEADDR+0x%x)\n'%(Pref,Reg.upper(),Module.upper(),Addr))
                Fvcc.write('`define %sADDR_%-50s  \'h%x\n'%(Pref,Reg.upper(),Addr))
    Fccc.write('\n\n#endif\n')
    Fccc.close()
    Fout.write(TRAILER)
    Fout.close()



def writable(Acc):
    if 'w' in Acc: return True
    if 'W' in Acc: return True
    if 'dual' in Acc: return True
    return False

def hasFields(Db,Reg):
    return Reg in Db['fields']


def buildFields(Db,Reg):
    List = Db['fields'][Reg]
    Res = ''
    for Item in List:
        Name = Item.Name
        if Name != 'gap':
            _,Offset = Item.Params['position']
            Width =  Item.Params['width']
            Str = FIELD_TEMPLATE.replace('NAME',Item.Name)
            Str = Str.replace('WIDTH',str(Width))
            Str = Str.replace('OFFSET',str(Offset))
            if 'description' in Item.Params:
                Desc = '<ipxact:description>XXX</ipxact:description>'
                Desc = Desc.replace('XXX',Item.Params['description'])
                Str = Str.replace('DESCRIPTION',Desc)
            else:
                Str = Str.replace('DESCRIPTION','')
            if 'reset' in Item.Params:
                Str = Str.replace('RESET',str(Item.Params['reset']))
            else:
                Str = Str.replace('RESET','0')
            Res += Str
    return Res


def writeItem(Db,Item,Fout,Module,Acc,Addr,Wid,Reset,Desc,Reg,Amount=0):
    Reset = str(Reset)
    Desc = str(Desc).replace('.',' ')
    Desc = Desc.replace('"','')
    print("XWWW",Acc,Reg)

    if writable(Acc)and ('pulse' in Acc) and hasFields(Db,Reg) :
        Str = REG_FIELDED_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('VOLATILE','true')
        Str = Str.replace('RESET',Reset)
        Desc = Desc.replace('.',' ')
        Desc = Desc.replace('"','')
        Str = Str.replace('DESCRIPTION',Desc)
        Fields = buildFields(Db,Reg)
        Fields = Fields.replace('VOLATILE','false')
        Fields = Fields.replace('USERLOGIC','false')
        Str = Str.replace('FIELDS',Fields)
        Fout.write(Str)

    elif writable(Acc)and ('pulse' in Acc):
        Str = REG_USER_LOGIC_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('VOLATILE','true')
        Str = Str.replace('RESET',Reset)
        Desc = Desc.replace('.',' ')
        Desc = Desc.replace('"','')
        Str = Str.replace('DESCRIPTION',Desc)
        Fout.write(Str)

    elif writable(Acc) and hasFields(Db,Reg):
        Str = REG_FIELDED_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('RESET',Reset)
        Str = Str.replace('DESCRIPTION','"%s"'%Desc)
        Str = Str.replace('USERLOGIC','false')
        Str = Str.replace('VOLATILE','false')
        Fields = buildFields(Db,Reg)
        Fields = Fields.replace('VOLATILE','false')
        Fields = Fields.replace('USERLOGIC','false')
        Str = Str.replace('FIELDS',Fields)
        Fout.write(Str)
    elif writable(Acc):
        Str = REG_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('RESET',Reset)
        Str = Str.replace('DESCRIPTION','"%s"'%Desc)
        Str = Str.replace('USERLOGIC','false')
        Str = Str.replace('VOLATILE','false')
        Fout.write(Str)
    elif ('ro' in Acc) and hasFields(Db,Reg):
        Str = REG_FIELDED_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('RESET',Reset)
        Str = Str.replace('DESCRIPTION','"%s"'%Desc)
        Str = Str.replace('read-write','read-only')
        Str = Str.replace('USERLOGIC','true')
        Str = Str.replace('VOLATILE','true')
        Fields = buildFields(Db,Reg)
        Fields = Fields.replace('VOLATILE','true')
        Fields = Fields.replace('USERLOGIC','true')
        Str = Str.replace('FIELDS',Fields)
        Fout.write(Str)
    elif 'ro' in Acc:
        Str = REG_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('RESET',Reset)
        Str = Str.replace('DESCRIPTION','"%s"'%Desc)
        Str = Str.replace('read-write','read-only')
        Str = Str.replace('USERLOGIC','true')
        Str = Str.replace('VOLATILE','true')
        Fout.write(Str)

    elif 'external' in Acc:
        Str = REG_USER_LOGIC_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('VOLATILE','true')
        Str = Str.replace('RESET',Reset)
        Str = Str.replace('DESCRIPTION',Desc)
        Fout.write(Str)
    elif 'ram' in Acc:
        Str = ARRAY_TEMPLATE.replace('NAME',Reg)
        Str = Str.replace('ADDRESS','%x'%Addr)
        Str = Str.replace('WIDTH','\'h%x'%Wid)
        Str = Str.replace('AMOUNT','\'h%x'%Amount)
        Str = Str.replace('USERLOGIC','true')
        Str = Str.replace('VOLATILE','true')
        Str = Str.replace('DESCRIPTION',Desc)
        Fout.write(Str)
    else:
        logs.log_error('#%d: acc = %s is not treated for reg %s in %s'%(Item.Lnum,Acc,Reg,Module))





HEADER = '''<?xml version="1.0" encoding="UTF-8"?>

<ipxact:component xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:ipxact="http://www.accellera.org/XMLSchema/IPXACT/1685-2014"
    xsi:schemaLocation="http://www.accellera.org/XMLSchema/IPXACT/1685-2014 http://www.accellera.org/XMLSchema/IPXACT/1685-2014/index.xsd">
    <ipxact:vendor>Autotalks</ipxact:vendor>
    <ipxact:library>LIBRARY</ipxact:library>
    <ipxact:name>NAME</ipxact:name>
    <ipxact:version>0.0</ipxact:version>
    <ipxact:description>Auto Regfiles</ipxact:description>
    <ipxact:memoryMaps>
        <ipxact:memoryMap>
            <ipxact:name>MAP</ipxact:name>
            <ipxact:isPresent>true</ipxact:isPresent>
            <ipxact:addressUnitBits>8</ipxact:addressUnitBits>
            <ipxact:addressBlock>
                <ipxact:name>BLOCK</ipxact:name>
                <ipxact:isPresent>true</ipxact:isPresent>
                <ipxact:baseAddress>'hBASEADDR</ipxact:baseAddress>
                <ipxact:range>'hRANGE</ipxact:range>
                <ipxact:width>32</ipxact:width>
'''

TRAILER = ''' 



            </ipxact:addressBlock>
        </ipxact:memoryMap>
    </ipxact:memoryMaps>


</ipxact:component>
'''



ARRAY_TEMPLATE = '''
               <ipxact:register>
                    <ipxact:name>NAME</ipxact:name>
                    <ipxact:displayName>NAME</ipxact:displayName>
                    <ipxact:description>DESCRIPTION</ipxact:description>
                    <ipxact:isPresent>true</ipxact:isPresent>
                    <ipxact:dim>AMOUNT</ipxact:dim>
                    <ipxact:addressOffset>'hADDRESS</ipxact:addressOffset>
                    <ipxact:size>32</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:displayName>NAME</ipxact:displayName>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>0</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
                        <ipxact:resets> <ipxact:reset> <ipxact:value>RESET</ipxact:value> </ipxact:reset> </ipxact:resets>
                        <ipxact:vendorExtensions>
                            <userLogic>USERLOGIC</userLogic>
                        </ipxact:vendorExtensions>
                    </ipxact:field>
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''


REG_USER_LOGIC_TEMPLATE = '''
                <ipxact:register>
                    <ipxact:name>NAME</ipxact:name>
                    <ipxact:displayName>NAME</ipxact:displayName>
                    <ipxact:description>DESCRIPTION</ipxact:description>
                    <ipxact:isPresent>true</ipxact:isPresent>
                    <ipxact:addressOffset>'hADDRESS</ipxact:addressOffset>
                    <ipxact:size>32</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:displayName>NAME</ipxact:displayName>
                        <ipxact:description>DESCRIPTION</ipxact:description>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>0</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
                        <ipxact:access>read-write</ipxact:access>
                        <ipxact:resets> <ipxact:reset> <ipxact:value>RESET</ipxact:value> </ipxact:reset> </ipxact:resets>
                        <ipxact:vendorExtensions>
                            <userLogic>true</userLogic>
                        </ipxact:vendorExtensions>
                    </ipxact:field>
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''

FIELD_TEMPLATE = '''
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>OFFSET</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
                        <ipxact:resets> <ipxact:reset> <ipxact:value>RESET</ipxact:value> </ipxact:reset> </ipxact:resets>
                        <ipxact:vendorExtensions>
                            <userLogic>USERLOGIC</userLogic>
                        </ipxact:vendorExtensions>
                        DESCRIPTION
                    </ipxact:field>
'''

REG_TEMPLATE = '''
               <ipxact:register>
                    <ipxact:name>NAME</ipxact:name>
                    <ipxact:isPresent>true</ipxact:isPresent>
                    <ipxact:addressOffset>'hADDRESS</ipxact:addressOffset>
                    <ipxact:description>DESCRIPTION</ipxact:description>
                    <ipxact:size>32</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>0</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
                        <ipxact:resets> <ipxact:reset> <ipxact:value>RESET</ipxact:value> </ipxact:reset> </ipxact:resets>
                        <ipxact:vendorExtensions>
                            <userLogic>USERLOGIC</userLogic>
                        </ipxact:vendorExtensions>
                    </ipxact:field>
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''

REG_FIELDED_TEMPLATE = '''
               <ipxact:register>
                    <ipxact:name>NAME</ipxact:name>
                    <ipxact:isPresent>true</ipxact:isPresent>
                    <ipxact:addressOffset>'hADDRESS</ipxact:addressOffset>
                    <ipxact:description>DESCRIPTION</ipxact:description>
                    <ipxact:size>32</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    FIELDS
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''

