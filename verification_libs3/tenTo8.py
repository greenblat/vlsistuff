

# 011100 1000
# 28     8
# elif (six==28): five = 0b01000; valid6= 1;
# elif (four==8): three = 0b000; valid4= 0;

def tenTo8(tenbits):

    four = tenbits & 0xf
    six  = (tenbits >>4) & 0x3f
    valid5,five = runFive(six)
    valid3,three = runFour(four)
    valid = valid5 and valid3
    eightbits = (three<<5)|five
    return valid,eightbits


def runFive(six):
    if (six==0): five = 0b00000; valid6= 0; 
    elif (six==1): five = 0b00000; valid6= 0; 
    elif (six==2): five = 0b00000; valid6= 0; 
    elif (six==3): five = 0b00000; valid6= 0; 
    elif (six==4): five = 0b00000; valid6= 0; 
    elif (six==5): five = 0b11001; valid6= 1; 
    elif (six==6): five = 0b10111; valid6= 1; 
    elif (six==7): five = 0b10110; valid6= 1; 
    elif (six==8): five = 0b00000; valid6= 0; 
    elif (six==9): five = 0b11011; valid6= 1; 
    elif (six==10): five = 0b10101; valid6= 1; 
    elif (six==11): five = 0b01101; valid6= 1; 
    elif (six==12): five = 0b11010; valid6= 1; 
    elif (six==13): five = 0b00011; valid6= 1; 
    elif (six==14): five = 0b01001; valid6= 1; 
    elif (six==15): five = 0b00000; valid6= 0; 
    elif (six==16): five = 0b00000; valid6= 0; 
    elif (six==17): five = 0b11101; valid6= 1; 
    elif (six==18): five = 0b10100; valid6= 1; 
    elif (six==19): five = 0b01011; valid6= 1; 
    elif (six==20): five = 0b11111; valid6= 1; 
    elif (six==21): five = 0b00001; valid6= 1; 
    elif (six==22): five = 0b10001; valid6= 1; 
    elif (six==23): five = 0b11000; valid6= 1; 
    elif (six==24): five = 0b10010; valid6= 1; 
    elif (six==25): five = 0b00110; valid6= 1; 
    elif (six==26): five = 0b01111; valid6= 1; 
    elif (six==27): five = 0b11100; valid6= 1; 
    elif (six==28): five = 0b01000; valid6= 1; 
    elif (six==29): five = 0b10011; valid6= 1; 
    elif (six==30): five = 0b11110; valid6= 1; 
    elif (six==31): five = 0b00000; valid6= 0; 
    elif (six==32): five = 0b00000; valid6= 0; 
    elif (six==33): five = 0b11110; valid6= 1; 
    elif (six==34): five = 0b10011; valid6= 1; 
    elif (six==35): five = 0b01010; valid6= 1; 
    elif (six==36): five = 0b11100; valid6= 1; 
    elif (six==37): five = 0b00000; valid6= 1; 
    elif (six==38): five = 0b10000; valid6= 1; 
    elif (six==39): five = 0b10010; valid6= 1; 
    elif (six==40): five = 0b11000; valid6= 1; 
    elif (six==41): five = 0b00101; valid6= 1; 
    elif (six==42): five = 0b01110; valid6= 1; 
    elif (six==43): five = 0b11111; valid6= 1; 
    elif (six==44): five = 0b00111; valid6= 1; 
    elif (six==45): five = 0b10100; valid6= 1; 
    elif (six==46): five = 0b11101; valid6= 1; 
    elif (six==47): five = 0b00000; valid6= 0; 
    elif (six==48): five = 0b00000; valid6= 0; 
    elif (six==49): five = 0b00100; valid6= 1; 
    elif (six==50): five = 0b01100; valid6= 1; 
    elif (six==51): five = 0b11010; valid6= 1; 
    elif (six==52): five = 0b00010; valid6= 1; 
    elif (six==53): five = 0b10101; valid6= 1; 
    elif (six==54): five = 0b11011; valid6= 1; 
    elif (six==55): five = 0b00000; valid6= 0; 
    elif (six==56): five = 0b10110; valid6= 1; 
    elif (six==57): five = 0b10111; valid6= 1; 
    elif (six==58): five = 0b11001; valid6= 1; 
    elif (six==59): five = 0b00000; valid6= 0; 
    elif (six==60): five = 0b00000; valid6= 0; 
    elif (six==61): five = 0b00000; valid6= 0; 
    elif (six==62): five = 0b00000; valid6= 0; 
    elif (six==63): five = 0b00000; valid6= 0; 
    return valid6,six

def runFour(four):
    if (four==0): three = 0b000;   valid4= 0; 
    elif (four==1): three = 0b111; valid4= 1; 
    elif (four==2): three = 0b110; valid4= 1; 
    elif (four==3): three = 0b101; valid4= 1; 
    elif (four==4): three = 0b100; valid4= 1; 
    elif (four==5): three = 0b000; valid4= 1; 
    elif (four==6): three = 0b001; valid4= 1; 
    elif (four==7): three = 0b000; valid4= 0; 
    elif (four==8): three = 0b000; valid4= 0; 
    elif (four==9): three = 0b010; valid4= 1; 
    elif (four==10): three = 0b011; valid4= 1; 
    elif (four==11): three = 0b100; valid4= 1; 
    elif (four==12): three = 0b101; valid4= 1; 
    elif (four==13): three = 0b110; valid4= 1; 
    elif (four==14): three = 0b111; valid4= 1; 
    elif (four==15): three = 0b000; valid4= 0; 
    return valid4,three




