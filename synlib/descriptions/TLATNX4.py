Desc = cellDescClass("TLATNX4")
Desc.properties["cell_leakage_power"] = "2663.067780"
Desc.properties["cell_footprint"] = "tlatn"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_param("area",56.548800);
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
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNX4"]=Desc
