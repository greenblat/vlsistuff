Desc = cellDescClass("DFFSRHQX4")
Desc.properties["cell_leakage_power"] = "5687.491140"
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "153.014400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",153.014400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
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
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFSRHQX4"]=Desc
