


Ciifs={}

def writeCiif(Name,X,Y,Pixel):
    if Name not in Ciifs:
        Ciifs[Name]=open('%s.ciif'%Name,'w')
        Ciifs[Name].write('//pixelWidth=640\n')
        Ciifs[Name].write('//pixelHeight=640\n')

    File = Ciifs[Name]
    File.write('(0 %d %d ) %x\n'%(Y,X,Pixel))


def closeAll():
    for Fname in Ciifs.keys():
        File = Ciifs[Fname]
        File.close()



