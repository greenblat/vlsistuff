


KCHARS = {}

def negate(Str,Who):
    X = Str.replace('0','x')
    X = X.replace('1','0')
    X = X.replace('x','1')
    KCHARS[Str] = Who
    KCHARS[X]   = Who
    return X

K280_m = '0011110100'
K280_p = negate(K280_m,'K280')


K281_m = '0011111001'
K281_p = negate(K281_m,'K281')

K282_m = '0011110101'
K282_p = negate(K282_m,'K282')

K283_m = '0011110011'
K283_p = negate(K283_m,'K283')

K284_m = '0011110010'
K284_p = negate(K284_m,'K284')

K285_m = '0011111010'
K285_p = negate(K285_m,'K285')

K286_m = '0011110110'
K286_p = negate(K286_m,'K286')

K287_m = '0011111000'
K287_p = negate(K287_m,'K287')

K237_m = '1110101000'
K237_p = negate(K237_m,'K237')

K277_m = '1101101000'
K277_p = negate(K277_m,'K277')

K297_m = '1011101000'
K297_p = negate(K297_m,'K297')

K307_m = '0111101000'
K307_p = negate(K307_m,'K307')

def trans8to10(eight,plus):
    if type(eight) is int:
        eight = ('00000000'+bin(eight)[2:])[-8:]
    B3 = eight[:3]
    B5 = eight[3:]

    B4 = trans3to4(B3,plus)
    B6 = trans5to6(B5,plus)
    return B6+B4

def trans10to8(ten):
    if type(ten) is int:
        ten = ('0000000000'+bin(ten)[2:])[-10:]

    if ten in KCHARS: return KCHARS[ten]

    B6 = ten[:6]
    B4 = ten[6:]

    B3 = trans4to3(B4)
    B5 = trans6to5(B6)
    if (not B3) or (not B5): return False,ten
    return B3+B5


def trans3to4(bits3,plus):
    if (bits3=="000")and plus: return "0100"
    if (bits3=="000")and not plus: return "1011"
    if (bits3=="001"): return "1001"
    if (bits3=="010"): return "0101"
    if (bits3=="011")and plus: return "0011"
    if (bits3=="011")and not plus: return "1100"
    if (bits3=="100")and plus: return "0010"
    if (bits3=="100")and not plus: return "1101"
    if (bits3=="101"): return "1010"
    if (bits3=="110"): return "0110"
    if (bits3=="111")and plus: return "0001"
    if (bits3=="111")and not plus: return "1110"
def trans4to3(bits4):
    if (bits4=="0001"): return "111"
    if (bits4=="0010"): return "100"
    if (bits4=="0011"): return "011"
    if (bits4=="0100"): return "000"
    if (bits4=="0101"): return "010"
    if (bits4=="0110"): return "110"
    if (bits4=="0111"): return "111"
    if (bits4=="1000"): return "111"
    if (bits4=="1001"): return "001"
    if (bits4=="1010"): return "101"
    if (bits4=="1011"): return "000"
    if (bits4=="1100"): return "011"
    if (bits4=="1101"): return "100"
    if (bits4=="1110"): return "111"
    return False
def trans5to6(bits5,plus):
    if (bits5=="00000")and plus: return "100111"
    if (bits5=="00000")and not plus: return "011000"
    if (bits5=="00001")and plus: return "011101"
    if (bits5=="00001")and not plus: return "100010"
    if (bits5=="00010")and plus: return "101101"
    if (bits5=="00010")and not plus: return "010010"
    if (bits5=="00011"): return "110001"
    if (bits5=="00100")and plus: return "110101"
    if (bits5=="00100")and not plus: return "001010"
    if (bits5=="00101"): return "101001"
    if (bits5=="00110"): return "011001"
    if (bits5=="00111")and plus: return "111000"
    if (bits5=="00111")and not plus: return "000111"
    if (bits5=="01000")and plus: return "111001"
    if (bits5=="01000")and not plus: return "000110"
    if (bits5=="01001"): return "100101"
    if (bits5=="01010"): return "010101"
    if (bits5=="01011"): return "110100"
    if (bits5=="01100"): return "001101"
    if (bits5=="01101"): return "101100"
    if (bits5=="01110"): return "011100"
    if (bits5=="01111")and plus: return "010111"
    if (bits5=="01111")and not plus: return "101000"
    if (bits5=="10000")and plus: return "011011"
    if (bits5=="10000")and not plus: return "100100"
    if (bits5=="10001"): return "100011"
    if (bits5=="10010"): return "010011"
    if (bits5=="10011"): return "110010"
    if (bits5=="10100"): return "001011"
    if (bits5=="10101"): return "101010"
    if (bits5=="10110"): return "011010"
    if (bits5=="10111")and plus: return "111010"
    if (bits5=="10111")and not plus: return "000101"
    if (bits5=="11000")and plus: return "110011"
    if (bits5=="11000")and not plus: return "001100"
    if (bits5=="11001"): return "100110"
    if (bits5=="11010"): return "010110"
    if (bits5=="11011")and plus: return "110110"
    if (bits5=="11011")and not plus: return "001001"
    if (bits5=="11100"): return "001110"
    if (bits5=="11101")and plus: return "101110"
    if (bits5=="11101")and not plus: return "010001"
    if (bits5=="11110")and plus: return "011110"
    if (bits5=="11110")and not plus: return "100001"
    if (bits5=="11111")and plus: return "101011"
    if (bits5=="11111")and not plus: return "010100"
def trans6to5(bits6):
    if (bits6=="000101"): return "10111"
    if (bits6=="000110"): return "01000"
    if (bits6=="000111"): return "00111"
    if (bits6=="001001"): return "11011"
    if (bits6=="001010"): return "00100"
    if (bits6=="001011"): return "10100"
    if (bits6=="001100"): return "11000"
    if (bits6=="001101"): return "01100"
    if (bits6=="001110"): return "11100"
    if (bits6=="010001"): return "11101"
    if (bits6=="010010"): return "00010"
    if (bits6=="010011"): return "10010"
    if (bits6=="010100"): return "11111"
    if (bits6=="010101"): return "01010"
    if (bits6=="010110"): return "11010"
    if (bits6=="010111"): return "01111"
    if (bits6=="011000"): return "00000"
    if (bits6=="011001"): return "00110"
    if (bits6=="011010"): return "10110"
    if (bits6=="011011"): return "10000"
    if (bits6=="011100"): return "01110"
    if (bits6=="011101"): return "00001"
    if (bits6=="011110"): return "11110"
    if (bits6=="100001"): return "11110"
    if (bits6=="100010"): return "00001"
    if (bits6=="100011"): return "10001"
    if (bits6=="100100"): return "10000"
    if (bits6=="100101"): return "01001"
    if (bits6=="100110"): return "11001"
    if (bits6=="100111"): return "00000"
    if (bits6=="101000"): return "01111"
    if (bits6=="101001"): return "00101"
    if (bits6=="101010"): return "10101"
    if (bits6=="101011"): return "11111"
    if (bits6=="101100"): return "01101"
    if (bits6=="101101"): return "00010"
    if (bits6=="101110"): return "11101"
    if (bits6=="110001"): return "00011"
    if (bits6=="110010"): return "10011"
    if (bits6=="110011"): return "11000"
    if (bits6=="110100"): return "01011"
    if (bits6=="110101"): return "00100"
    if (bits6=="110110"): return "11011"
    if (bits6=="111000"): return "00111"
    if (bits6=="111001"): return "01000"
    if (bits6=="111010"): return "10111"
    return False

KCHARS = {}
KCHARS[0x1c] = 'K280'
KCHARS[0x3c] = 'K281'
KCHARS[0x5c] = 'K282'
KCHARS[0x7c] = 'K283'
KCHARS[0x9c] = 'K284'
KCHARS[0xbc] = 'K285'
KCHARS[0xdc] = 'K286'
KCHARS[0xfc] = 'K287'

KCHARS[0xf7] = 'K237'
KCHARS[0xfb] = 'K277'
KCHARS[0xfd] = 'K297'
KCHARS[0xfe] = 'K307'

def symbolx(Kchar,Val):
    if (Kchar):
       return KCHARS[Val] 
    return '%02x'%Val
        

def main():
    for ii in range(256):
        PP = trans8to10(ii,True)
        PH = '%03x'%(int(PP,2))
        MM = trans8to10(ii,False)
        MH = '%03x'%(int(MM,2))
        print('%02x pp %s mm %s      pp %s m %s'%(ii,PP,MM,PH,MH))


if __name__ == '__main__': main()



