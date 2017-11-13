Desc = cellDescClass("RSLATX1")
Desc.properties["cell_leakage_power"] = "1082.604042"
Desc.properties["cell_footprint"] = "rslat"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'R', 'S', 'next']
Desc.add_arc("R","S","hold_falling")
Desc.add_arc("S","R","hold_falling")
Desc.add_arc("S","Q","preset")
Desc.add_arc("R","Q","clear")
Desc.add_arc("S","QN","clear")
Desc.add_arc("R","QN","preset")
Desc.add_param("area",33.264000);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.set_pin_job("S","clock")
Desc.add_pin("S","input")
Desc.set_pin_job("R","clock")
Desc.add_pin("R","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATX1"]=Desc
