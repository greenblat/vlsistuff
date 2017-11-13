Desc = cellDescClass("JKFFRX2")
Desc.properties["cell_leakage_power"] = "2372.812380"
Desc.properties["cell_footprint"] = "jkffr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
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
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFRX2"]=Desc
