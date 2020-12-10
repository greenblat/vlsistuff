
extern "C" long getValue(int path) {
    switch (path) {
        case 0 : return (long) top->rst_n; // rst_n
        case 1 : return (long) top->clk; // clk
        case 2 : return (long) top->a0; // a0
        case 3 : return (long) top->a1; // a1
        case 4 : return (long) top->a2; // a2
        case 5 : return (long) top->a3; // a3
        case 6 : return (long) top->aa; // aa
        case 7 : return (long) top->cycles; // cycles
        case 8 : return (long) top->errors; // errors
        case 9 : return (long) top->wrongs; // wrongs
        case 10 : return (long) top->panics; // panics
        case 11 : return (long) top->corrects; // corrects
        case 12 : return (long) top->marker0; // marker0
        case 13 : return (long) top->marker1; // marker1
        case 14 : return (long) top->marker2; // marker2

        default : {
            printf("error! net=%d is not defined for peek\n",path);
            return -1L;
        }
    }
}


extern "C" int setValue(int path,long val) {
    switch (path) {
    case 0 : {top->rst_n = val;return 0;} // rst_n
    case 1 : {top->clk = val;return 0;} // clk
    case 2 : {top->a0 = val;return 0;} // a0
    case 3 : {top->a1 = val;return 0;} // a1
    case 4 : {top->a2 = val;return 0;} // a2
    case 5 : {top->a3 = val;return 0;} // a3
    case 6 : {top->aa = val;return 0;} // aa
    case 7 : {top->cycles = val;return 0;} // cycles
    case 8 : {top->errors = val;return 0;} // errors
    case 9 : {top->wrongs = val;return 0;} // wrongs
    case 10 : {top->panics = val;return 0;} // panics
    case 11 : {top->corrects = val;return 0;} // corrects
    case 12 : {top->marker0 = val;return 0;} // marker0
    case 13 : {top->marker1 = val;return 0;} // marker1
    case 14 : {top->marker2 = val;return 0;} // marker2

        default : {
            printf("error! net=%d is not defined for force\n",path);
            return -1L;
        }
    }
}
extern "C" int getWid(int path) {
    switch (path) {
        case 0: return 1; // rst_n
        case 1: return 1; // clk
        case 2: return 1; // a0
        case 3: return 1; // a1
        case 4: return 1; // a2
        case 5: return 1; // a3
        case 6: return 4; // aa
        case 7: return 32; // cycles
        case 8: return 32; // errors
        case 9: return 32; // wrongs
        case 10: return 32; // panics
        case 11: return 32; // corrects
        case 12: return 32; // marker0
        case 13: return 32; // marker1
        case 14: return 32; // marker2
        default: return -1;
    }
}
