Desc = cellDescClass("TLATX4")
Desc.properties["cell_leakage_power"] = "1622.523960"
Desc.properties["cell_footprint"] = "tlat"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATX4"]=Desc
