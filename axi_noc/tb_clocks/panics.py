
import logs
import veri
def monitorStuff(Net):
    Val = logs.peek(Net)
    if Val!=0:
        logs.log_error('PANIC activated on %s %s'%(Net,veri.peek(Net)))
        return 1
    return 0


def monitorStuffs():
    panics=0
    panics += monitorStuff("tb.dut.axi_clock0.ar_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock0.ar_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock0.aw_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock0.aw_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock0.b_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock0.b_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock0.r_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock0.r_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock0.w_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock0.w_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock1.ar_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock1.ar_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock1.aw_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock1.aw_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock1.b_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock1.b_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock1.r_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock1.r_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.axi_clock1.w_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.axi_clock1.w_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.panic_r_fifo")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.panic_ar_fifo")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.panic_w_fifo")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.panic_order_fifo")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.panic_b_fifo")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.panic_aw_fifo")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_in")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_out")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_underflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_overflow")
    panics += monitorStuff("tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_underflow")

    veri.force('tb.Panics',str(panics))
def snapshot():
    logs.log_info("SNP %x  tb.dut.axi_clock0.ar_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock0.ar_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.ar_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock0.ar_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.aw_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock0.aw_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.aw_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock0.aw_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.b_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock0.b_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.b_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock0.b_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.r_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock0.r_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.r_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock0.r_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.w_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock0.w_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock0.w_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock0.w_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.ar_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock1.ar_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.ar_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock1.ar_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.aw_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock1.aw_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.aw_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock1.aw_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.b_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock1.b_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.b_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock1.b_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.r_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock1.r_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.r_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock1.r_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.w_fifo.panic_overflow" % logs.peek("tb.dut.axi_clock1.w_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.axi_clock1.w_fifo.panic_underflow" % logs.peek("tb.dut.axi_clock1.w_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.panic_r_fifo" % logs.peek("tb.dut.split0.axi_rd_4_splitter.panic_r_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.panic_ar_fifo" % logs.peek("tb.dut.split0.axi_rd_4_splitter.panic_ar_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_in" % logs.peek("tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_out" % logs.peek("tb.dut.split0.axi_rd_4_splitter.a_r_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_overflow" % logs.peek("tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_underflow" % logs.peek("tb.dut.split0.axi_rd_4_splitter.ar_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_in" % logs.peek("tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_out" % logs.peek("tb.dut.split0.axi_rd_4_splitter.b_r_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_in" % logs.peek("tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_out" % logs.peek("tb.dut.split0.axi_rd_4_splitter.c_r_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_in" % logs.peek("tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_out" % logs.peek("tb.dut.split0.axi_rd_4_splitter.d_r_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_in" % logs.peek("tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_out" % logs.peek("tb.dut.split0.axi_rd_4_splitter.r_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.panic_w_fifo" % logs.peek("tb.dut.split0.axi_wr_4_splitter.panic_w_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.panic_order_fifo" % logs.peek("tb.dut.split0.axi_wr_4_splitter.panic_order_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.panic_b_fifo" % logs.peek("tb.dut.split0.axi_wr_4_splitter.panic_b_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.panic_aw_fifo" % logs.peek("tb.dut.split0.axi_wr_4_splitter.panic_aw_fifo"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_overflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_underflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.aw_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_overflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_underflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.b_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_in" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_out" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_a_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_in" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_out" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_b_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_in" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_out" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_c_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_in" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_in"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_out" % logs.peek("tb.dut.split0.axi_wr_4_splitter.back_bid_d_fifo.panic_out"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_overflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_underflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.order_fifo.panic_underflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_overflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_overflow"))
    logs.log_info("SNP %x  tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_underflow" % logs.peek("tb.dut.split0.axi_wr_4_splitter.w_fifo.panic_underflow"))