Desc = cellDescClass("TTLATX4")
Desc.properties["cell_leakage_power"] = "3055.004100"
Desc.properties["cell_footprint"] = "ttlat"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'OE', 'Q', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("OE","Q","three_state_disable")
Desc.add_arc("OE","Q","three_state_enable")
Desc.add_param("area",76.507200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("OE","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("latch")
CellLib["TTLATX4"]=Desc
