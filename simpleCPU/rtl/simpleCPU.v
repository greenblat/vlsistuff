
module simpleCPU ( input clk, input rst_n
    ,input irq
    ,output reg mem_rd
    ,output reg mem_wr
    ,output reg mem_fetch
    ,output reg running
    ,output reg [31:0] mem_addr
    ,output reg [31:0] mem_wdata
    ,input  [31:0] mem_rdata
    ,input mem_ready
    ,input [15:0] irq_addr
    ,output stop_code
    ,output reg [15:0] PC
    ,output [7:0] nop_result
    ,output finish_good
    ,output finish_bad
    ,output reg sleeping
    ,output external_access
); 

reg [6:0] flags;
reg [31:0] [31:0] regf;
wire [31:0] nop_opcode;
wire asleep_code;


wire afinish_good_code,afinish_bad_code;
assign finish_good = afinish_good_code;
assign finish_bad = afinish_bad_code;
wire anop_code;
wire asubi_code;
wire [19:0] aimm_field;
assign nop_result = anop_code ? aimm_field[7:0] : 0;


wire aload_code;
wire astore_code;
wire acall_code;
wire areturn_code;
wire abranch_code;
wire ajump_code;
wire aaddi_code;
wire amuli_code;
wire aandi_code;
wire aori_code;
wire aloadi_code;
wire aloadih_code;
wire amul_code;
wire aadd_code;
wire asub_code;
wire aand_code;
wire aor_code;
wire ashiftr_reg_code;
wire ashiftar_reg_code;
wire ashiftl_reg_code;
wire ashiftr_code;
wire ashiftl_code;
wire ashiftar_code;
wire aneg_code;
wire amove_code;
wire aloadabs_code;
wire astoreabs_code;
wire astop_code;
assign stop_code = astop_code;


reg [3:0] state;
wire bad_opcode = (state==3) && !(
       aload_code || astore_code || acall_code || areturn_code
    || abranch_code || ajump_code || aaddi_code || amuli_code
    || aandi_code || aori_code || aloadi_code || aloadih_code
    || amul_code || aadd_code || asub_code || aand_code || aor_code
    || ashiftr_reg_code || ashiftar_reg_code || ashiftl_reg_code
    || ashiftr_code || ashiftl_code || ashiftar_code || aneg_code
    || amove_code || aloadabs_code || astoreabs_code || astop_code || anop_code
    || asubi_code || afinish_good_code || afinish_bad_code 
    || asleep_code
);


wire [7:0] aoffset_field;
wire [4:0] asrc_field;
wire [4:0] adst_field;
wire [2:0] acond_field;
reg [4:0] [15:0] stack;
reg [4:0] keep_reg;
reg [31:0] opcode;
reg [4:0] sdepth;

wire dbg_branch_taken = abranch_code && flags[acond_field];
wire dbg_branch_not_taken = abranch_code && !flags[acond_field];

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        state <= 0;
        PC <= 0;
        keep_reg <= 0;
        mem_rd <= 0;
        mem_fetch <= 0;
        mem_wr <= 0;
        mem_addr <= 0;
        mem_wdata <= 0;
        state <= 0;
        running <= 0;
        sdepth <= 0;
        stack <= 80'hffffffff_ffffffff_ffff;
    end else begin
        if (bad_opcode) begin
            mem_rd <= 0;
            mem_wr <= 0;
            mem_fetch <= 0;
            state <= 0;
            running <= 0;
        end else if (state==0) begin
            if (irq) begin
                state <= 1;
                PC <= irq_addr;
            end
            mem_rd <= 0;
            mem_wr <= 0;
            mem_fetch <= 0;
        end else if (state==1) begin
            mem_addr <= PC;
            mem_rd <= 1;
            mem_wr <= 0;
            mem_fetch <= 1;
            state <= 2;
            running <= 1;
        end else if (state == 2) begin
            if (mem_ready) begin
                opcode <= mem_rdata;
                mem_rd <= 0;
                mem_fetch <= 0;
                state <= 15;
            end
        end else if (state == 15) begin
            opcode <= mem_rdata;
            state <= 3;
        end else if (state == 14) begin
            if (!sleeping) state <= 1;
        end else if (state == 3) begin
            if (astop_code || afinish_good_code || afinish_bad_code) begin
                state <= 0;
                PC <= 0;
                mem_addr <= 0;
                mem_rd <= 0;
                mem_wr <= 0;
                running <= 0;
            end else if (asleep_code) begin
                state <= 14;
                PC <= PC + 4;
            end else if (anop_code) begin
                state <= 1;
                PC <= PC + 4;
            end else if (ajump_code) begin
                PC <= aimm_field[15:0]; 
                state <= 1;
            end else if (abranch_code) begin
                PC <= PC+ (flags[acond_field] ? {{7{aimm_field[8]}},aimm_field[8:0]} : 4); 
                state <= 1;
            end else if (acall_code) begin
                PC <= aimm_field[15:0]; 
                stack[0] <= PC+4;
                stack[1] <= stack[0];
                stack[2] <= stack[1];
                stack[3] <= stack[2];
                stack[4] <= stack[3];
                state <= 1;
                sdepth <= sdepth +1;
            end else if (areturn_code) begin
                PC <= stack[0];
                stack[4] <= 0;
                stack[3] <= stack[4];
                stack[2] <= stack[3];
                stack[1] <= stack[2];
                stack[0] <= stack[1];
                sdepth <= sdepth -1;
                state <= 1;
            end else if (astore_code) begin
                PC <= PC+4; 
                mem_wr <= 1;
                mem_addr <= regf[adst_field]+aoffset_field[7:0];
                mem_wdata <= regf[asrc_field];
                state <= 4;
            end else if (astoreabs_code) begin
                PC <= PC+4; 
                mem_wr <= 1;
                mem_addr <= aimm_field[15:0];
                mem_wdata <= regf[adst_field];
                state <= 4;
            end else if (aload_code) begin
                PC <= PC+4; 
                mem_rd <= 1;
                mem_addr <= regf[asrc_field]+aoffset_field[7:0];
                mem_wdata <= 0;
                keep_reg <= adst_field;
                state <= 5;
            end else if (aloadabs_code) begin
                PC <= PC+4; 
                mem_rd <= 1;
                mem_addr <= aimm_field[15:0];
                mem_wdata <= 0;
                keep_reg <= adst_field;
                state <= 5;

            end else if (aloadi_code) begin
                PC <= PC+4; 
                state <= 1;
                regf[adst_field] <= aimm_field[19:0];
            end else if (aloadih_code) begin
                PC <= PC+4; 
                state <= 1;
                regf[adst_field] <= (regf[adst_field]&32'h00000fff) |   {aimm_field[19:0],12'b0};
            end else if (aadd_code) begin
                regf[adst_field] <= regf[adst_field]  + regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aaddi_code) begin
                regf[adst_field] <= regf[adst_field]  + aimm_field[9:0]; 
                PC <= PC+4; 
                state <= 1;
            end else if (asub_code) begin
                regf[adst_field] <= regf[adst_field]  - regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (asubi_code) begin
                regf[adst_field] <= regf[adst_field]  - aimm_field[9:0]; 
                PC <= PC+4; 
                state <= 1;
            end else if (amul_code) begin
                regf[adst_field] <= regf[adst_field]  * regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (amuli_code) begin
                regf[adst_field] <= regf[adst_field]  * aimm_field[9:0]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aand_code) begin
                regf[adst_field] <= regf[adst_field]  & regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aor_code) begin
                regf[adst_field] <= regf[adst_field]  | regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aandi_code) begin
                regf[adst_field] <= regf[adst_field]  & aimm_field[9:0]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aori_code) begin
                regf[adst_field] <= regf[adst_field]  | aimm_field[9:0]; 
                PC <= PC+4; 
                state <= 1;
            end else if (aneg_code) begin
                regf[adst_field] <= -regf[adst_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (amove_code) begin
                regf[adst_field] <= regf[asrc_field]; 
                PC <= PC+4; 
                state <= 1;
            end else if (ashiftr_reg_code) begin
                regf[adst_field] <= regf[adst_field]  >>  regf[asrc_field & 5'b11111]; 
                PC <= PC+4; 
                state <= 1;
            end else if (ashiftl_reg_code) begin
                regf[adst_field] <= regf[adst_field]  <<  regf[asrc_field & 5'b11111]; 
                PC <= PC+4; 
                state <= 1;
            end else if (ashiftr_code) begin
                regf[adst_field] <= regf[adst_field] >> aimm_field[4:0];  
                PC <= PC+4; 
                state <= 1;
            end else if (ashiftl_code) begin
                regf[adst_field] <= regf[adst_field] << aimm_field[4:0];  
                PC <= PC+4; 
                state <= 1;
            end
        end else if (state == 4) begin
            if (mem_ready) begin mem_wr <= 0; state <= 1; end
        end else if (state == 5) begin
            if (mem_ready) begin
                regf[keep_reg] <= mem_rdata;
                state <= 6;
            end
        end else if (state == 6) begin
            state <= 7;
        end else if (state == 7) begin
             mem_addr <= 0;
             regf[keep_reg] <= mem_rdata;
             state <= 1;
        end
    end
end



wire pvalida = (state == 3)|| (state==4) || (state==5) || (state==6) || (state == 7); 
wire [31:0] popcoda  = opcode; 
wire asimple_opcode_flag;
wire auses_src_flag;
wire asimple_branch_flag;
wire auses_dst_flag;
wire aext_field;



riscx_decoder ariscx_decoder (.valid(pvalida),.opcode(popcoda)
    ,.nop_opcode(nop_opcode)
   ,.nop_code(anop_code)
   ,.stop_code(astop_code)
   ,.load_code(aload_code)
   ,.store_code(astore_code)
   ,.call_code(acall_code)
   ,.return_code(areturn_code)
   ,.branch_code(abranch_code)
   ,.jump_code(ajump_code)
   ,.addi_code(aaddi_code)
   ,.muli_code(amuli_code)
   ,.andi_code(aandi_code)
   ,.ori_code(aori_code)
   ,.loadi_code(aloadi_code)
   ,.loadih_code(aloadih_code)
   ,.mul_code(amul_code)
   ,.add_code(aadd_code)
   ,.sub_code(asub_code)
   ,.and_code(aand_code)
   ,.or_code(aor_code)
   ,.shiftr_reg_code(ashiftr_reg_code)
   ,.shiftar_reg_code(ashiftar_reg_code)
   ,.shiftl_reg_code(ashiftl_reg_code)
   ,.shiftr_code(ashiftr_code)
   ,.shiftl_code(ashiftl_code)
   ,.shiftar_code(ashiftar_code)
   ,.neg_code(aneg_code)
   ,.move_code(amove_code)
   ,.loadabs_code(aloadabs_code)
   ,.storeabs_code(astoreabs_code)
   ,.offset_field(aoffset_field)
   ,.src_field(asrc_field)
   ,.dst_field(adst_field)
   ,.imm_field(aimm_field)
   ,.cond_field(acond_field)
   ,.simple_opcode_flag(asimple_opcode_flag)
   ,.uses_src_flag(auses_src_flag)
   ,.simple_branch_flag(asimple_branch_flag)
   ,.uses_dst_flag(auses_dst_flag)
   ,.finish_good_code(afinish_good_code)
   ,.finish_bad_code(afinish_bad_code)
   ,.subi_code(asubi_code)
   ,.sleep_code(asleep_code)
   ,.ext_field(aext_field)
);

assign external_access = aext_field && (aload_code||astore_code);

reg [31:0] sleeping_count;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        sleeping <= 0;
    end else begin
        if (sleeping_count>0) begin
            sleeping <= 1;
            sleeping_count <= sleeping_count -1;
        end else if (asleep_code) begin
            sleeping_count <=  regf[adst_field]+aimm_field[15:0];
            sleeping <= 1;
        end else begin
            sleeping <= 0;
        end
    end
end





wire [31:0] result0 = regf[adst_field] - regf[asrc_field];
always @(posedge clk) begin
    flags[0] <= 1;
    if (asub_code) begin
        flags[1] <= (result0==0);
        flags[2] <= (result0!=0);
        flags[3] <= (result0[31]);
        flags[4] <= (!result0[31]) && (result0 != 0); 
        flags[5] <=  (result0[31])  || (result0 == 0);
        flags[6] <= (!result0[31]);
    end
end



wire [31:0] dbg_src =  regf[asrc_field];
wire [31:0] dbg0 = regf[0];
wire [31:0] dbg1 = regf[1];
wire [31:0] dbg2 = regf[2];
wire [31:0] dbg3 = regf[3];
wire [31:0] dbg4 = regf[4];
wire [31:0] dbg5 = regf[5];
wire [31:0] dbg6 = regf[6];
wire [31:0] dbg7 = regf[7];
wire [31:0] dbg28 = regf[28];
wire [31:0] dbg29 = regf[29];
wire [31:0] dbg30 = regf[30];
wire [31:0] dbg31 = regf[31];

endmodule




