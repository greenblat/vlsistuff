Desc = cellDescClass("RSLATNX2")
Desc.properties["cell_footprint"] = "rslatn"
Desc.properties["area"] = "36.590400"
Desc.properties["cell_leakage_power"] = "1700.400600"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("RN","SN","hold_rising")
Desc.add_arc("SN","RN","hold_rising")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",36.590400);
Desc.set_pin_job("SN","clock")
Desc.add_pin("SN","input")
Desc.set_pin_job("RN","clock")
Desc.add_pin("RN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
CellLib["RSLATNX2"]=Desc
