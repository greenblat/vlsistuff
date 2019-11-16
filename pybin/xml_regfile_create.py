
import logs
import string

def createXml(FFF,Addrs,Csv,Reset,lastAddress):
    LL = []
    for Reg in Csv.regs:
        ST = Csv.regs[Reg]
        LL.append((int(ST[3]),Reg))
    LL.sort()
    Range  = lastAddress+4
    Fout = open('%s.xml'%Csv.Module,'w')
    Str = string.replace(HEADER,'NAME',Csv.Module)
    Str = string.replace(Str,'LIBRARY','AutoTalksLib')
    Str = string.replace(Str,'BASEADDR','0')
    Str = string.replace(Str,'RANGE','%x'%Range)
    Fout.write(Str)
    LL = []
    for Reg in Csv.regs:
        ST = Csv.regs[Reg]
        LL.append((int(ST[3]),Reg))
    LL.sort()
    for Addr,Reg in LL:
        ST = Csv.regs[Reg]
        Wid = int(ST[1])
        Acc = ST[0]

        if writable(Acc)and ('pulse' in Acc):
            Str = string.replace(REG_USER_LOGIC_TEMPLATE,'NAME',Reg)
            Str = string.replace(Str,'ADDRESS','%x'%Addr)
            Str = string.replace(Str,'WIDTH','\'h%x'%Wid)
            Str = string.replace(Str,'VOLATILE','true')
            Desc = string.replace(ST[4],'.',' ')
            Desc = string.replace(Desc,'"','')
            Str = string.replace(Str,'DESCRIPTION',Desc)
            Fout.write(Str)
        elif writable(Acc):
            Str = string.replace(REG_TEMPLATE,'NAME',Reg)
            Str = string.replace(Str,'ADDRESS','%x'%Addr)
            Str = string.replace(Str,'WIDTH','\'h%x'%Wid)
            Desc = string.replace(ST[4],'.',' ')
            Desc = string.replace(Desc,'"','')
            Str = string.replace(Str,'DESCRIPTION','"%s"'%Desc)
            Str = string.replace(Str,'USERLOGIC','false')
            Str = string.replace(Str,'VOLATILE','false')
            Fout.write(Str)
        elif 'ro' in Acc:
            Str = string.replace(REG_TEMPLATE,'NAME',Reg)
            Str = string.replace(Str,'ADDRESS','%x'%Addr)
            Str = string.replace(Str,'WIDTH','\'h%x'%Wid)
            Desc = string.replace(ST[4],'.',' ')
            Desc = string.replace(Desc,'"','')
            Str = string.replace(Str,'DESCRIPTION','"%s"'%Desc)
            Str = string.replace(Str,'read-write','read-only')
            Str = string.replace(Str,'USERLOGIC','true')
            Str = string.replace(Str,'VOLATILE','true')
            Fout.write(Str)

        elif 'external' in Acc:
            Str = string.replace(REG_USER_LOGIC_TEMPLATE,'NAME',Reg)
            Str = string.replace(Str,'ADDRESS','%x'%Addr)
            Str = string.replace(Str,'WIDTH','\'h%x'%Wid)
            Str = string.replace(Str,'VOLATILE','true')
            Desc = string.replace(ST[4],'.',' ')
            Desc = string.replace(Desc,'"','')
            Str = string.replace(Str,'DESCRIPTION',Desc)
            Fout.write(Str)
        elif 'ram' in Acc:
            Str = string.replace(ARRAY_TEMPLATE,'NAME',Reg)
            Str = string.replace(Str,'ADDRESS','%x'%Addr)
            Str = string.replace(Str,'WIDTH','\'h%x'%Wid)
            Str = string.replace(Str,'AMOUNT','\'h%x'%ST[2])
            Str = string.replace(Str,'USERLOGIC','true')
            Str = string.replace(Str,'VOLATILE','true')
#            Desc = string.replace(ST[4],'.',' ')
            Desc = str(ST)
            Str = string.replace(Str,'DESCRIPTION',Desc)
            Fout.write(Str)
        else:
            logs.log_error('acc = %s is not treated for reg %s in %s'%(Acc,Reg,Csv.Module))


    Fout.write(TRAILER)
    Fout.close()

def writable(Acc):
    if 'w' in Acc: return True 
    if 'W' in Acc: return True 
    return False



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
                    <ipxact:size>WIDTH</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:displayName>NAME</ipxact:displayName>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>0</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
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
                    <ipxact:size>WIDTH</ipxact:size>
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
                        <ipxact:vendorExtensions>
                            <userLogic>true</userLogic>
                        </ipxact:vendorExtensions>
                    </ipxact:field>
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''

REG_TEMPLATE = '''
               <ipxact:register>
                    <ipxact:name>NAME</ipxact:name>
                    <ipxact:isPresent>true</ipxact:isPresent>
                    <ipxact:addressOffset>'hADDRESS</ipxact:addressOffset>
                    <ipxact:description>DESCRIPTION</ipxact:description>
                    <ipxact:size>WIDTH</ipxact:size>
                    <ipxact:volatile>VOLATILE</ipxact:volatile>
                    <ipxact:access>read-write</ipxact:access>
                    <ipxact:field>
                        <ipxact:name>NAME</ipxact:name>
                        <ipxact:isPresent>true</ipxact:isPresent>
                        <ipxact:bitOffset>0</ipxact:bitOffset>
                        <ipxact:bitWidth>WIDTH</ipxact:bitWidth>
                        <ipxact:volatile>VOLATILE</ipxact:volatile>
                        <ipxact:vendorExtensions>
                            <userLogic>USERLOGIC</userLogic>
                        </ipxact:vendorExtensions>
                    </ipxact:field>
                    <ipxact:vendorExtensions>
                    </ipxact:vendorExtensions>
                </ipxact:register>
'''


