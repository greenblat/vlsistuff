Desc = cellDescClass("TLATNRXL")
Desc.properties["cell_leakage_power"] = "829.502694"
Desc.properties["cell_footprint"] = "tlatnr"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNRXL"]=Desc
