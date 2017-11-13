Desc = cellDescClass("DFFHQX4")
Desc.properties["cell_leakage_power"] = "3632.190660"
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "73.180800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",73.180800);
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
Desc.set_job("flipflop")
CellLib["DFFHQX4"]=Desc
