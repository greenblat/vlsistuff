Desc = cellDescClass("SDFFSHQX2")
Desc.properties["cell_footprint"] = "sdffshq"
Desc.properties["area"] = "93.139200"
Desc.properties["cell_leakage_power"] = "3345.045660"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",93.139200);
Desc.add_pin("SI","input")
Desc.add_pin("SE","input")
Desc.add_pin("D","input")
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("SN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSHQX2"]=Desc
