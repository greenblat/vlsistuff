Desc = cellDescClass("JKFFSX1")
Desc.properties["cell_leakage_power"] = "1972.515240"
Desc.properties["cell_footprint"] = "jkffs"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSX1"]=Desc
