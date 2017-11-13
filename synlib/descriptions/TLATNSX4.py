Desc = cellDescClass("TLATNSX4")
Desc.properties["cell_leakage_power"] = "1597.280310"
Desc.properties["cell_footprint"] = "tlatns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSX4"]=Desc
