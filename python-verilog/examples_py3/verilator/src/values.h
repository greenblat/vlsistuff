
char VVV[50000];
char *getValue(char *path) {
// clk 0 0
     if (strcmp(path,"clk")==0) { sprintf(VVV,"%01x",top->clk); return VVV;}
// rst_n 0 0
     if (strcmp(path,"rst_n")==0) { sprintf(VVV,"%01x",top->rst_n); return VVV;}
// rxd 0 0
     if (strcmp(path,"rxd")==0) { sprintf(VVV,"%01x",top->rxd); return VVV;}
// txd 0 0
     if (strcmp(path,"txd")==0) { sprintf(VVV,"%01x",top->txd); return VVV;}
// baudrate 16 (15, 0)
     if (strcmp(path,"baudrate")==0) { sprintf(VVV,"%04x",top->baudrate); return VVV;}
// fractional 8 (7, 0)
     if (strcmp(path,"fractional")==0) { sprintf(VVV,"%02x",top->fractional); return VVV;}
// txcount 16 (15, 0)
     if (strcmp(path,"txcount")==0) { sprintf(VVV,"%04x",top->txcount); return VVV;}
// softreset 0 0
     if (strcmp(path,"softreset")==0) { sprintf(VVV,"%01x",top->softreset); return VVV;}
// tx_empty 0 0
     if (strcmp(path,"tx_empty")==0) { sprintf(VVV,"%01x",top->tx_empty); return VVV;}
// write_tx 0 0
     if (strcmp(path,"write_tx")==0) { sprintf(VVV,"%01x",top->write_tx); return VVV;}
// control 8 (7, 0)
     if (strcmp(path,"control")==0) { sprintf(VVV,"%02x",top->control); return VVV;}
// rxdata 8 (7, 0)
     if (strcmp(path,"rxdata")==0) { sprintf(VVV,"%02x",top->rxdata); return VVV;}
// txdata 8 (7, 0)
     if (strcmp(path,"txdata")==0) { sprintf(VVV,"%02x",top->txdata); return VVV;}
// result 32 (31, 0)
     if (strcmp(path,"result")==0) { sprintf(VVV,"%08x",top->result); return VVV;}
// vldout 0 0
     if (strcmp(path,"vldout")==0) { sprintf(VVV,"%01x",top->vldout); return VVV;}
// status 8 (7, 0)
     if (strcmp(path,"status")==0) { sprintf(VVV,"%02x",top->status); return VVV;}
// rx_valid 0 0
     if (strcmp(path,"rx_valid")==0) { sprintf(VVV,"%01x",top->rx_valid); return VVV;}
// dst 8 (7, 0)
     if (strcmp(path,"dst")==0) { sprintf(VVV,"%02x",top->dst); return VVV;}
// letA 8 (7, 0)
     if (strcmp(path,"letA")==0) { sprintf(VVV,"%02x",top->letA); return VVV;}
// letB 8 (7, 0)
     if (strcmp(path,"letB")==0) { sprintf(VVV,"%02x",top->letB); return VVV;}
// letC 8 (7, 0)
     if (strcmp(path,"letC")==0) { sprintf(VVV,"%02x",top->letC); return VVV;}
// letD 8 (7, 0)
     if (strcmp(path,"letD")==0) { sprintf(VVV,"%02x",top->letD); return VVV;}
// letE 8 (7, 0)
     if (strcmp(path,"letE")==0) { sprintf(VVV,"%02x",top->letE); return VVV;}
// letF 8 (7, 0)
     if (strcmp(path,"letF")==0) { sprintf(VVV,"%02x",top->letF); return VVV;}
// letG 8 (7, 0)
     if (strcmp(path,"letG")==0) { sprintf(VVV,"%02x",top->letG); return VVV;}
// letH 8 (7, 0)
     if (strcmp(path,"letH")==0) { sprintf(VVV,"%02x",top->letH); return VVV;}
// letI 8 (7, 0)
     if (strcmp(path,"letI")==0) { sprintf(VVV,"%02x",top->letI); return VVV;}
// letJ 8 (7, 0)
     if (strcmp(path,"letJ")==0) { sprintf(VVV,"%02x",top->letJ); return VVV;}
// letK 8 (7, 0)
     if (strcmp(path,"letK")==0) { sprintf(VVV,"%02x",top->letK); return VVV;}
// letL 8 (7, 0)
     if (strcmp(path,"letL")==0) { sprintf(VVV,"%02x",top->letL); return VVV;}
// letM 8 (7, 0)
     if (strcmp(path,"letM")==0) { sprintf(VVV,"%02x",top->letM); return VVV;}
// letN 8 (7, 0)
     if (strcmp(path,"letN")==0) { sprintf(VVV,"%02x",top->letN); return VVV;}
// letO 8 (7, 0)
     if (strcmp(path,"letO")==0) { sprintf(VVV,"%02x",top->letO); return VVV;}
// letP 8 (7, 0)
     if (strcmp(path,"letP")==0) { sprintf(VVV,"%02x",top->letP); return VVV;}
// letQ 8 (7, 0)
     if (strcmp(path,"letQ")==0) { sprintf(VVV,"%02x",top->letQ); return VVV;}
// letR 8 (7, 0)
     if (strcmp(path,"letR")==0) { sprintf(VVV,"%02x",top->letR); return VVV;}
// letS 8 (7, 0)
     if (strcmp(path,"letS")==0) { sprintf(VVV,"%02x",top->letS); return VVV;}
// letT 8 (7, 0)
     if (strcmp(path,"letT")==0) { sprintf(VVV,"%02x",top->letT); return VVV;}
// letU 8 (7, 0)
     if (strcmp(path,"letU")==0) { sprintf(VVV,"%02x",top->letU); return VVV;}
// letV 8 (7, 0)
     if (strcmp(path,"letV")==0) { sprintf(VVV,"%02x",top->letV); return VVV;}
// letW 8 (7, 0)
     if (strcmp(path,"letW")==0) { sprintf(VVV,"%02x",top->letW); return VVV;}
// letX 8 (7, 0)
     if (strcmp(path,"letX")==0) { sprintf(VVV,"%02x",top->letX); return VVV;}
// letY 8 (7, 0)
     if (strcmp(path,"letY")==0) { sprintf(VVV,"%02x",top->letY); return VVV;}
// letZ 8 (7, 0)
     if (strcmp(path,"letZ")==0) { sprintf(VVV,"%02x",top->letZ); return VVV;}
// letCR 8 (7, 0)
     if (strcmp(path,"letCR")==0) { sprintf(VVV,"%02x",top->letCR); return VVV;}
// let0 8 (7, 0)
     if (strcmp(path,"let0")==0) { sprintf(VVV,"%02x",top->let0); return VVV;}
// let1 8 (7, 0)
     if (strcmp(path,"let1")==0) { sprintf(VVV,"%02x",top->let1); return VVV;}
// let2 8 (7, 0)
     if (strcmp(path,"let2")==0) { sprintf(VVV,"%02x",top->let2); return VVV;}
// let3 8 (7, 0)
     if (strcmp(path,"let3")==0) { sprintf(VVV,"%02x",top->let3); return VVV;}
// let4 8 (7, 0)
     if (strcmp(path,"let4")==0) { sprintf(VVV,"%02x",top->let4); return VVV;}
// let5 8 (7, 0)
     if (strcmp(path,"let5")==0) { sprintf(VVV,"%02x",top->let5); return VVV;}
// let6 8 (7, 0)
     if (strcmp(path,"let6")==0) { sprintf(VVV,"%02x",top->let6); return VVV;}
// let7 8 (7, 0)
     if (strcmp(path,"let7")==0) { sprintf(VVV,"%02x",top->let7); return VVV;}
// let8 8 (7, 0)
     if (strcmp(path,"let8")==0) { sprintf(VVV,"%02x",top->let8); return VVV;}
// let9 8 (7, 0)
     if (strcmp(path,"let9")==0) { sprintf(VVV,"%02x",top->let9); return VVV;}
// reads 4 (3, 0)
     if (strcmp(path,"reads")==0) { sprintf(VVV,"%01x",top->reads); return VVV;}
// writes 0 0
     if (strcmp(path,"writes")==0) { sprintf(VVV,"%01x",top->writes); return VVV;}
// count 16 (15, 0)
     if (strcmp(path,"count")==0) { sprintf(VVV,"%04x",top->count); return VVV;}
// frees 16 (15, 0)
     if (strcmp(path,"frees")==0) { sprintf(VVV,"%04x",top->frees); return VVV;}
// dout 80 (['-', ['*', 10, 8], 1], 0)
     if (strcmp(path,"dout")==0) { sprintf(VVV,"%020x%08x%08x",top->dout[2],top->dout[1],top->dout[0]); return VVV;}
// taken 0 0
     if (strcmp(path,"taken")==0) { sprintf(VVV,"%01x",top->taken); return VVV;}
// wr_baudrate 0 0
     if (strcmp(path,"wr_baudrate")==0) { sprintf(VVV,"%01x",top->wr_baudrate); return VVV;}
// wr_fractional 0 0
     if (strcmp(path,"wr_fractional")==0) { sprintf(VVV,"%01x",top->wr_fractional); return VVV;}
// wr_reg 0 0
     if (strcmp(path,"wr_reg")==0) { sprintf(VVV,"%01x",top->wr_reg); return VVV;}
// rd_reg 0 0
     if (strcmp(path,"rd_reg")==0) { sprintf(VVV,"%01x",top->rd_reg); return VVV;}
// work 0 0
     if (strcmp(path,"work")==0) { sprintf(VVV,"%01x",top->work); return VVV;}
// pop 0 0
     if (strcmp(path,"pop")==0) { sprintf(VVV,"%01x",top->pop); return VVV;}
// clean 0 0
     if (strcmp(path,"clean")==0) { sprintf(VVV,"%01x",top->clean); return VVV;}
// reg0 32 (31, 0)
     if (strcmp(path,"reg0")==0) { sprintf(VVV,"%08x",top->reg0); return VVV;}
// reg1 32 (31, 0)
     if (strcmp(path,"reg1")==0) { sprintf(VVV,"%08x",top->reg1); return VVV;}
// reg2 32 (31, 0)
     if (strcmp(path,"reg2")==0) { sprintf(VVV,"%08x",top->reg2); return VVV;}
// reg3 32 (31, 0)
     if (strcmp(path,"reg3")==0) { sprintf(VVV,"%08x",top->reg3); return VVV;}
// reg4 32 (31, 0)
     if (strcmp(path,"reg4")==0) { sprintf(VVV,"%08x",top->reg4); return VVV;}
// reg5 32 (31, 0)
     if (strcmp(path,"reg5")==0) { sprintf(VVV,"%08x",top->reg5); return VVV;}
// reg6 32 (31, 0)
     if (strcmp(path,"reg6")==0) { sprintf(VVV,"%08x",top->reg6); return VVV;}
// reg7 32 (31, 0)
     if (strcmp(path,"reg7")==0) { sprintf(VVV,"%08x",top->reg7); return VVV;}
// fvalue 32 (31, 0)
     if (strcmp(path,"fvalue")==0) { sprintf(VVV,"%08x",top->fvalue); return VVV;}
// AA 8 (7, 0)
     if (strcmp(path,"AA")==0) { sprintf(VVV,"%02x",top->AA); return VVV;}
// BB 8 (7, 0)
     if (strcmp(path,"BB")==0) { sprintf(VVV,"%02x",top->BB); return VVV;}
// CC 8 (7, 0)
     if (strcmp(path,"CC")==0) { sprintf(VVV,"%02x",top->CC); return VVV;}
// oper 4 (3, 0)
     if (strcmp(path,"oper")==0) { sprintf(VVV,"%01x",top->oper); return VVV;}
// sel0 8 (7, 0)
     if (strcmp(path,"sel0")==0) { sprintf(VVV,"%02x",top->sel0); return VVV;}
// sel1 8 (7, 0)
     if (strcmp(path,"sel1")==0) { sprintf(VVV,"%02x",top->sel1); return VVV;}
// dst_wire 8 (7, 0)
     if (strcmp(path,"dst_wire")==0) { sprintf(VVV,"%02x",top->dst_wire); return VVV;}
// src0 32 (31, 0)
     if (strcmp(path,"src0")==0) { sprintf(VVV,"%08x",top->src0); return VVV;}
// src1 32 (31, 0)
     if (strcmp(path,"src1")==0) { sprintf(VVV,"%08x",top->src1); return VVV;}
// resultout 64 (['-', ['*', 8, 8], 1], 0)
     if (strcmp(path,"resultout")==0) { sprintf(VVV,"%016lx",top->resultout); return VVV;}
// txfrees 16 (15, 0)
     if (strcmp(path,"txfrees")==0) { sprintf(VVV,"%04x",top->txfrees); return VVV;}
// txtaken 0 0
     if (strcmp(path,"txtaken")==0) { sprintf(VVV,"%01x",top->txtaken); return VVV;}
// selected_reg 32 (31, 0)
     if (strcmp(path,"selected_reg")==0) { sprintf(VVV,"%08x",top->selected_reg); return VVV;}
// selected_hex 64 (63, 0)
     if (strcmp(path,"selected_hex")==0) { sprintf(VVV,"%016lx",top->selected_hex); return VVV;}
// txwrites 4 (3, 0)
     if (strcmp(path,"txwrites")==0) { sprintf(VVV,"%01x",top->txwrites); return VVV;}
// cycles 32 (31, 0)
     if (strcmp(path,"cycles")==0) { sprintf(VVV,"%08x",top->cycles); return VVV;}
// errors 32 (31, 0)
     if (strcmp(path,"errors")==0) { sprintf(VVV,"%08x",top->errors); return VVV;}
// wrongs 32 (31, 0)
     if (strcmp(path,"wrongs")==0) { sprintf(VVV,"%08x",top->wrongs); return VVV;}
// panics 32 (31, 0)
     if (strcmp(path,"panics")==0) { sprintf(VVV,"%08x",top->panics); return VVV;}
// corrects 32 (31, 0)
     if (strcmp(path,"corrects")==0) { sprintf(VVV,"%08x",top->corrects); return VVV;}
// marker0 32 (31, 0)
     if (strcmp(path,"marker0")==0) { sprintf(VVV,"%08x",top->marker0); return VVV;}
// marker1 32 (31, 0)
     if (strcmp(path,"marker1")==0) { sprintf(VVV,"%08x",top->marker1); return VVV;}
// marker2 32 (31, 0)
     if (strcmp(path,"marker2")==0) { sprintf(VVV,"%08x",top->marker2); return VVV;}

    printf("error! net=%s is not defined for peek\n",path);
    sprintf(VVV,"%s","-1"); return VVV;
}

char tmp[9];
void copy8_old(char *Str,int Pos) {
    int pos = Pos*8;
    for (int ii=0;ii<8;ii++) tmp[ii]=Str[pos+ii];
    tmp[8]=0;
}
void copy8(char *Str,int Pos) {
    int Len = strlen(Str)-1;
    int ii = 7;
    int fr; 
    for (ii=7;(ii>=0);ii--) {
        fr = Len-(Pos*8)-7+ii;
        if (fr>=0) tmp[ii]=Str[fr];
        else tmp[ii]='0';
    }   
    tmp[8]=0;
}





void setValue(char *path,char *val) {
    if (strcmp(path,"clk")==0) {top->clk = strtol(val,NULL,16);return;}
    if (strcmp(path,"rst_n")==0) {top->rst_n = strtol(val,NULL,16);return;}
    if (strcmp(path,"rxd")==0) {top->rxd = strtol(val,NULL,16);return;}
    if (strcmp(path,"txd")==0) {top->txd = strtol(val,NULL,16);return;}
    if (strcmp(path,"baudrate")==0) {top->baudrate = strtol(val,NULL,16);return;}
    if (strcmp(path,"fractional")==0) {top->fractional = strtol(val,NULL,16);return;}
    if (strcmp(path,"txcount")==0) {top->txcount = strtol(val,NULL,16);return;}
    if (strcmp(path,"softreset")==0) {top->softreset = strtol(val,NULL,16);return;}
    if (strcmp(path,"tx_empty")==0) {top->tx_empty = strtol(val,NULL,16);return;}
    if (strcmp(path,"write_tx")==0) {top->write_tx = strtol(val,NULL,16);return;}
    if (strcmp(path,"control")==0) {top->control = strtol(val,NULL,16);return;}
    if (strcmp(path,"rxdata")==0) {top->rxdata = strtol(val,NULL,16);return;}
    if (strcmp(path,"txdata")==0) {top->txdata = strtol(val,NULL,16);return;}
    if (strcmp(path,"result")==0) {top->result = strtol(val,NULL,16);return;}
    if (strcmp(path,"vldout")==0) {top->vldout = strtol(val,NULL,16);return;}
    if (strcmp(path,"status")==0) {top->status = strtol(val,NULL,16);return;}
    if (strcmp(path,"rx_valid")==0) {top->rx_valid = strtol(val,NULL,16);return;}
    if (strcmp(path,"dst")==0) {top->dst = strtol(val,NULL,16);return;}
    if (strcmp(path,"letA")==0) {top->letA = strtol(val,NULL,16);return;}
    if (strcmp(path,"letB")==0) {top->letB = strtol(val,NULL,16);return;}
    if (strcmp(path,"letC")==0) {top->letC = strtol(val,NULL,16);return;}
    if (strcmp(path,"letD")==0) {top->letD = strtol(val,NULL,16);return;}
    if (strcmp(path,"letE")==0) {top->letE = strtol(val,NULL,16);return;}
    if (strcmp(path,"letF")==0) {top->letF = strtol(val,NULL,16);return;}
    if (strcmp(path,"letG")==0) {top->letG = strtol(val,NULL,16);return;}
    if (strcmp(path,"letH")==0) {top->letH = strtol(val,NULL,16);return;}
    if (strcmp(path,"letI")==0) {top->letI = strtol(val,NULL,16);return;}
    if (strcmp(path,"letJ")==0) {top->letJ = strtol(val,NULL,16);return;}
    if (strcmp(path,"letK")==0) {top->letK = strtol(val,NULL,16);return;}
    if (strcmp(path,"letL")==0) {top->letL = strtol(val,NULL,16);return;}
    if (strcmp(path,"letM")==0) {top->letM = strtol(val,NULL,16);return;}
    if (strcmp(path,"letN")==0) {top->letN = strtol(val,NULL,16);return;}
    if (strcmp(path,"letO")==0) {top->letO = strtol(val,NULL,16);return;}
    if (strcmp(path,"letP")==0) {top->letP = strtol(val,NULL,16);return;}
    if (strcmp(path,"letQ")==0) {top->letQ = strtol(val,NULL,16);return;}
    if (strcmp(path,"letR")==0) {top->letR = strtol(val,NULL,16);return;}
    if (strcmp(path,"letS")==0) {top->letS = strtol(val,NULL,16);return;}
    if (strcmp(path,"letT")==0) {top->letT = strtol(val,NULL,16);return;}
    if (strcmp(path,"letU")==0) {top->letU = strtol(val,NULL,16);return;}
    if (strcmp(path,"letV")==0) {top->letV = strtol(val,NULL,16);return;}
    if (strcmp(path,"letW")==0) {top->letW = strtol(val,NULL,16);return;}
    if (strcmp(path,"letX")==0) {top->letX = strtol(val,NULL,16);return;}
    if (strcmp(path,"letY")==0) {top->letY = strtol(val,NULL,16);return;}
    if (strcmp(path,"letZ")==0) {top->letZ = strtol(val,NULL,16);return;}
    if (strcmp(path,"letCR")==0) {top->letCR = strtol(val,NULL,16);return;}
    if (strcmp(path,"let0")==0) {top->let0 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let1")==0) {top->let1 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let2")==0) {top->let2 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let3")==0) {top->let3 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let4")==0) {top->let4 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let5")==0) {top->let5 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let6")==0) {top->let6 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let7")==0) {top->let7 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let8")==0) {top->let8 = strtol(val,NULL,16);return;}
    if (strcmp(path,"let9")==0) {top->let9 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reads")==0) {top->reads = strtol(val,NULL,16);return;}
    if (strcmp(path,"writes")==0) {top->writes = strtol(val,NULL,16);return;}
    if (strcmp(path,"count")==0) {top->count = strtol(val,NULL,16);return;}
    if (strcmp(path,"frees")==0) {top->frees = strtol(val,NULL,16);return;}
    if (strcmp(path,"dout")==0) {
        copy8(val,2); top->dout[2] = strtol(tmp,NULL,16);
        copy8(val,1); top->dout[1] = strtol(tmp,NULL,16);
        copy8(val,0); top->dout[0] = strtol(tmp,NULL,16);
        return; }
    if (strcmp(path,"taken")==0) {top->taken = strtol(val,NULL,16);return;}
    if (strcmp(path,"wr_baudrate")==0) {top->wr_baudrate = strtol(val,NULL,16);return;}
    if (strcmp(path,"wr_fractional")==0) {top->wr_fractional = strtol(val,NULL,16);return;}
    if (strcmp(path,"wr_reg")==0) {top->wr_reg = strtol(val,NULL,16);return;}
    if (strcmp(path,"rd_reg")==0) {top->rd_reg = strtol(val,NULL,16);return;}
    if (strcmp(path,"work")==0) {top->work = strtol(val,NULL,16);return;}
    if (strcmp(path,"pop")==0) {top->pop = strtol(val,NULL,16);return;}
    if (strcmp(path,"clean")==0) {top->clean = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg0")==0) {top->reg0 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg1")==0) {top->reg1 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg2")==0) {top->reg2 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg3")==0) {top->reg3 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg4")==0) {top->reg4 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg5")==0) {top->reg5 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg6")==0) {top->reg6 = strtol(val,NULL,16);return;}
    if (strcmp(path,"reg7")==0) {top->reg7 = strtol(val,NULL,16);return;}
    if (strcmp(path,"fvalue")==0) {top->fvalue = strtol(val,NULL,16);return;}
    if (strcmp(path,"AA")==0) {top->AA = strtol(val,NULL,16);return;}
    if (strcmp(path,"BB")==0) {top->BB = strtol(val,NULL,16);return;}
    if (strcmp(path,"CC")==0) {top->CC = strtol(val,NULL,16);return;}
    if (strcmp(path,"oper")==0) {top->oper = strtol(val,NULL,16);return;}
    if (strcmp(path,"sel0")==0) {top->sel0 = strtol(val,NULL,16);return;}
    if (strcmp(path,"sel1")==0) {top->sel1 = strtol(val,NULL,16);return;}
    if (strcmp(path,"dst_wire")==0) {top->dst_wire = strtol(val,NULL,16);return;}
    if (strcmp(path,"src0")==0) {top->src0 = strtol(val,NULL,16);return;}
    if (strcmp(path,"src1")==0) {top->src1 = strtol(val,NULL,16);return;}
    if (strcmp(path,"resultout")==0) {top->resultout = strtol(val,NULL,16);return;}
    if (strcmp(path,"txfrees")==0) {top->txfrees = strtol(val,NULL,16);return;}
    if (strcmp(path,"txtaken")==0) {top->txtaken = strtol(val,NULL,16);return;}
    if (strcmp(path,"selected_reg")==0) {top->selected_reg = strtol(val,NULL,16);return;}
    if (strcmp(path,"selected_hex")==0) {top->selected_hex = strtol(val,NULL,16);return;}
    if (strcmp(path,"txwrites")==0) {top->txwrites = strtol(val,NULL,16);return;}
    if (strcmp(path,"cycles")==0) {top->cycles = strtol(val,NULL,16);return;}
    if (strcmp(path,"errors")==0) {top->errors = strtol(val,NULL,16);return;}
    if (strcmp(path,"wrongs")==0) {top->wrongs = strtol(val,NULL,16);return;}
    if (strcmp(path,"panics")==0) {top->panics = strtol(val,NULL,16);return;}
    if (strcmp(path,"corrects")==0) {top->corrects = strtol(val,NULL,16);return;}
    if (strcmp(path,"marker0")==0) {top->marker0 = strtol(val,NULL,16);return;}
    if (strcmp(path,"marker1")==0) {top->marker1 = strtol(val,NULL,16);return;}
    if (strcmp(path,"marker2")==0) {top->marker2 = strtol(val,NULL,16);return;}

    printf("error! net=%s is not defined for force\n",path);
    return;
}
char *getWid(char *path) {
    if (strcmp(path,"clk")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"rst_n")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"rxd")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"txd")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"baudrate")==0) { strcpy(VVV,"16"); return VVV;}
    if (strcmp(path,"fractional")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"txcount")==0) { strcpy(VVV,"16"); return VVV;}
    if (strcmp(path,"softreset")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"tx_empty")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"write_tx")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"control")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"rxdata")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"txdata")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"result")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"vldout")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"status")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"rx_valid")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"dst")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letA")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letB")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letC")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letD")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letE")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letF")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letG")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letH")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letI")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letJ")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letK")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letL")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letM")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letN")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letO")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letP")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letQ")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letR")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letS")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letT")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letU")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letV")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letW")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letX")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letY")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letZ")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"letCR")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let0")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let1")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let2")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let3")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let4")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let5")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let6")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let7")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let8")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"let9")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"reads")==0) { strcpy(VVV,"4"); return VVV;}
    if (strcmp(path,"writes")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"count")==0) { strcpy(VVV,"16"); return VVV;}
    if (strcmp(path,"frees")==0) { strcpy(VVV,"16"); return VVV;}
    if (strcmp(path,"dout")==0) { strcpy(VVV,"80"); return VVV;}
    if (strcmp(path,"taken")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"wr_baudrate")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"wr_fractional")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"wr_reg")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"rd_reg")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"work")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"pop")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"clean")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"reg0")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg1")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg2")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg3")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg4")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg5")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg6")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"reg7")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"fvalue")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"AA")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"BB")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"CC")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"oper")==0) { strcpy(VVV,"4"); return VVV;}
    if (strcmp(path,"sel0")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"sel1")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"dst_wire")==0) { strcpy(VVV,"8"); return VVV;}
    if (strcmp(path,"src0")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"src1")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"resultout")==0) { strcpy(VVV,"64"); return VVV;}
    if (strcmp(path,"txfrees")==0) { strcpy(VVV,"16"); return VVV;}
    if (strcmp(path,"txtaken")==0) { strcpy(VVV,"0"); return VVV;}
    if (strcmp(path,"selected_reg")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"selected_hex")==0) { strcpy(VVV,"64"); return VVV;}
    if (strcmp(path,"txwrites")==0) { strcpy(VVV,"4"); return VVV;}
    if (strcmp(path,"cycles")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"errors")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"wrongs")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"panics")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"corrects")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"marker0")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"marker1")==0) { strcpy(VVV,"32"); return VVV;}
    if (strcmp(path,"marker2")==0) { strcpy(VVV,"32"); return VVV;}
    strcpy(VVV,"-1"); return VVV;
}
