Desc = cellDescClass("SDFFTRXL")
Desc.properties["cell_footprint"] = "sdfftr"
Desc.properties["area"] = "73.180800"
Desc.properties["cell_leakage_power"] = "1891.657800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",73.180800);
Desc.add_pin("SI","input")
Desc.add_pin("SE","input")
Desc.add_pin("D","input")
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("RN","input")
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
CellLib["SDFFTRXL"]=Desc
