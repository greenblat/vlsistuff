Desc = cellDescClass("DFFSX1")
Desc.properties["cell_leakage_power"] = "1846.035360"
Desc.properties["cell_footprint"] = "dffs"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",63.201600);
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
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSX1"]=Desc
