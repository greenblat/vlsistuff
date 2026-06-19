module riscx_decoder(input [31:0] opcode,input valid,output not_opcode
,output nop_code
,output [31:0] nop_opcode
,output stop_code
,output finish_good_code
,output finish_bad_code
,output load_code
,output store_code
,output call_code
,output return_code
,output branch_code
,output jump_code
,output addi_code
,output subi_code
,output muli_code
,output andi_code
,output ori_code
,output loadi_code
,output loadih_code
,output mul_code
,output add_code
,output sub_code
,output and_code
,output or_code
,output xor_code
,output shiftr_reg_code
,output shiftar_reg_code
,output shiftl_reg_code
,output shiftr_code
,output shiftl_code
,output shiftar_code
,output neg_code
,output move_code
,output loadabs_code
,output storeabs_code
,output sleep_code
,output [19:0] imm_field
,output ext_field
,output [7:0] offset_field
,output [4:0] src_field
,output [4:0] dst_field
,output [2:0] cond_field
,output simple_opcode_flag
,output uses_src_flag
,output simple_branch_flag
,output uses_dst_flag
);
assign nop_code = valid && ((opcode & 32'hffffff00)==32'hfb8b3b00) ;
assign nop_opcode = 32'hfb8b3b00;
assign stop_code = valid && ((opcode & 32'hffffffff)==32'hfb8b3adf) ;
assign finish_good_code = valid && ((opcode & 32'hffffffff)==32'hfb8b3ade) ;
assign finish_bad_code = valid && ((opcode & 32'hffffffff)==32'hfb8b3add) ;
assign load_code = valid && ((opcode & 32'hfff80000)==32'hfb980000) ;
assign store_code = valid && ((opcode & 32'hfff80000)==32'hfb900000) ;
assign call_code = valid && ((opcode & 32'hffff0000)==32'hfb8f0000) ;
assign return_code = valid && ((opcode & 32'hffffffff)==32'hfb8b3adc) ;
assign branch_code = valid && ((opcode & 32'hfffff000)==32'hfb8b7000) ;
assign jump_code = valid && ((opcode & 32'hffff0000)==32'hfb8e0000) ;
assign addi_code = valid && ((opcode & 32'hffff8000)==32'hfb8d8000) ;
assign subi_code = valid && ((opcode & 32'hffff8000)==32'hfb8d0000) ;
assign muli_code = valid && ((opcode & 32'hffff8000)==32'hfb8c8000) ;
assign andi_code = valid && ((opcode & 32'hffff8000)==32'hfb8c0000) ;
assign ori_code = valid && ((opcode & 32'hffff8000)==32'hfb8b8000) ;
assign loadi_code = valid && ((opcode & 32'hfe000000)==32'hfe000000) ;
assign loadih_code = valid && ((opcode & 32'hfe000000)==32'hfc000000) ;
assign mul_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b6c00) ;
assign add_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b6800) ;
assign sub_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b6400) ;
assign and_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b6000) ;
assign or_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b5c00) ;
assign xor_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b5800) ;
assign shiftr_reg_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b5400) ;
assign shiftar_reg_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b5000) ;
assign shiftl_reg_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b4c00) ;
assign shiftr_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b4800) ;
assign shiftl_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b4400) ;
assign shiftar_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b4000) ;
assign neg_code = valid && ((opcode & 32'hffffffe0)==32'hfb8b3ae0) ;
assign move_code = valid && ((opcode & 32'hfffffc00)==32'hfb8b3c00) ;
assign loadabs_code = valid && ((opcode & 32'hffe00000)==32'hfbe00000) ;
assign storeabs_code = valid && ((opcode & 32'hffe00000)==32'hfbc00000) ;
assign sleep_code = valid && ((opcode & 32'hffe00000)==32'hfba00000) ;
assign not_opcode = !(
    nop_code ||stop_code ||finish_good_code ||finish_bad_code ||load_code
     ||store_code ||call_code ||return_code ||branch_code ||jump_code
     ||addi_code ||subi_code ||muli_code ||andi_code ||ori_code ||loadi_code
     ||loadih_code ||mul_code ||add_code ||sub_code ||and_code ||or_code
     ||xor_code ||shiftr_reg_code ||shiftar_reg_code ||shiftl_reg_code
     ||shiftr_code ||shiftl_code ||shiftar_code ||neg_code ||move_code
     ||loadabs_code ||storeabs_code ||sleep_code);
assign imm_field[0] = (opcode[0] && (nop_code||call_code||jump_code))||(opcode[3] && (branch_code))||(opcode[5] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||shiftr_code||shiftl_code||shiftar_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[1] = (opcode[1] && (nop_code||call_code||jump_code))||(opcode[4] && (branch_code))||(opcode[6] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||shiftr_code||shiftl_code||shiftar_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[2] = (opcode[2] && (nop_code||call_code||jump_code))||(opcode[5] && (branch_code))||(opcode[7] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||shiftr_code||shiftl_code||shiftar_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[3] = (opcode[3] && (nop_code||call_code||jump_code))||(opcode[6] && (branch_code))||(opcode[8] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||shiftr_code||shiftl_code||shiftar_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[4] = (opcode[4] && (nop_code||call_code||jump_code))||(opcode[7] && (branch_code))||(opcode[9] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||shiftr_code||shiftl_code||shiftar_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[5] = (opcode[5] && (nop_code||call_code||jump_code))||(opcode[8] && (branch_code))||(opcode[10] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[6] = (opcode[6] && (nop_code||call_code||jump_code))||(opcode[9] && (branch_code))||(opcode[11] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[7] = (opcode[7] && (nop_code||call_code||jump_code))||(opcode[10] && (branch_code))||(opcode[12] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[8] = (opcode[8] && (call_code||jump_code))||(opcode[11] && (branch_code))||(opcode[13] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[9] = (opcode[9] && (call_code||jump_code))||(opcode[14] && (addi_code||subi_code||muli_code||andi_code||ori_code||loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[10] = (opcode[10] && (call_code||jump_code))||(opcode[15] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[11] = (opcode[11] && (call_code||jump_code))||(opcode[16] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[12] = (opcode[12] && (call_code||jump_code))||(opcode[17] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[13] = (opcode[13] && (call_code||jump_code))||(opcode[18] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[14] = (opcode[14] && (call_code||jump_code))||(opcode[19] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[15] = (opcode[15] && (call_code||jump_code))||(opcode[20] && (loadi_code||loadih_code||loadabs_code||storeabs_code||sleep_code));
assign imm_field[16] = opcode[21];
assign imm_field[17] = opcode[22];
assign imm_field[18] = opcode[23];
assign imm_field[19] = opcode[24];
assign ext_field = opcode[18];
assign offset_field[0] = opcode[10];
assign offset_field[1] = opcode[11];
assign offset_field[2] = opcode[12];
assign offset_field[3] = opcode[13];
assign offset_field[4] = opcode[14];
assign offset_field[5] = opcode[15];
assign offset_field[6] = opcode[16];
assign offset_field[7] = opcode[17];
assign src_field[0] = opcode[5];
assign src_field[1] = opcode[6];
assign src_field[2] = opcode[7];
assign src_field[3] = opcode[8];
assign src_field[4] = opcode[9];
assign dst_field[0] = opcode[0];
assign dst_field[1] = opcode[1];
assign dst_field[2] = opcode[2];
assign dst_field[3] = opcode[3];
assign dst_field[4] = opcode[4];
assign cond_field[0] = opcode[0];
assign cond_field[1] = opcode[1];
assign cond_field[2] = opcode[2];
assign simple_opcode_flag = valid && (nop_code ||return_code ||addi_code ||subi_code ||muli_code ||andi_code ||ori_code ||loadi_code ||loadih_code ||mul_code ||add_code ||sub_code ||and_code ||or_code ||xor_code ||shiftr_reg_code ||shiftar_reg_code ||shiftl_reg_code ||shiftr_code ||shiftl_code ||shiftar_code ||neg_code ||move_code);
assign uses_src_flag = valid && (load_code ||store_code ||mul_code ||add_code ||sub_code ||and_code ||or_code ||xor_code ||move_code);
assign simple_branch_flag = valid && (branch_code ||jump_code);
assign uses_dst_flag = valid && (addi_code ||subi_code ||muli_code ||andi_code ||ori_code ||loadi_code ||loadih_code ||shiftr_reg_code ||shiftar_reg_code ||shiftl_reg_code ||shiftr_code ||shiftl_code ||shiftar_code ||neg_code);
endmodule

