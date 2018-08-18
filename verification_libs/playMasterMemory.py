
import veri
import logs
import string

masterRam={}
access=[0]
was_m_rd=0
was_m_rd_data=0
was2_m_rd=0
was2_m_rd_data=0
bytes_written=0
def run():
    global was_m_rd,was_m_rd_data,bytes_written
    global was2_m_rd,was2_m_rd_data

    if  peek('m_local_rd')==1:
        m_local_rd_addr  = peek('m_local_rd_addr')
        if m_local_rd_addr in masterRam:
            Data = masterRam[m_local_rd_addr]
        else:
            Data = string.replace('0xRfReRdRcRbRaR9R8R7R6R5R4R3R2R1R0','R','%x'%(access[0]&0xf))
            access[0] += 1
        force('m_local_rd_addr_ok','1')
        logs.log_info('masterRam read %x -> "%s" %s'%(m_local_rd_addr,'',Data))
    else: 
        force('m_local_rd_addr_ok','0')

    if peek('m_local_wr')==1:
        m_local_wr_addr  = peek('m_local_wr_addr')
        m_local_wr_data = peek('m_local_wr_data')
        m_local_wstrb = peek('m_local_wstrb')
        force('m_local_wr_ok','1')
        bytes_written += logs.countOnes(m_local_wstrb)
        logs.log_info('masterRam write %x <- %x (wstrb=%x) bytes_written=%d '%(m_local_wr_addr,m_local_wr_data,m_local_wstrb,bytes_written))
#        mactive.masterWrite(m_local_wr_addr,m_local_wr_data,m_local_wstrb)
    else:
        force('m_local_wr_ok','0')

    if was_m_rd:
        force('m_local_rd_data_ok',was_m_rd)
        force('m_local_rd_data',was_m_rd_data)
    else:
        force('m_local_rd_data_ok',0)
        force('m_local_rd_data',0)

    was_m_rd = was2_m_rd
    was_m_rd_data = was2_m_rd_data


    was2_m_rd = peek('m_local_rd')
    if peek('m_local_rd')==1:
        was2_m_rd_data = Data



def peek(Sig):
    return logs.peek('tb.%s'%Sig)
def force(Sig,Val):
    veri.force('tb.%s'%Sig,str(Val))

