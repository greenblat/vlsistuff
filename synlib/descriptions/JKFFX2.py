Desc = cellDescClass("JKFFX2")
Desc.properties["cell_footprint"] = "jkff"
Desc.properties["area"] = "83.160000"
Desc.properties["cell_leakage_power"] = "2383.212780"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.add_pin("J","input")
Desc.add_pin("K","input")
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
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
Desc.set_job("flipflop")
CellLib["JKFFX2"]=Desc
