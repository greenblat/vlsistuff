Desc = cellDescClass("SDFFRHQXL")
Desc.properties["cell_leakage_power"] = "2155.029300"
Desc.properties["cell_footprint"] = "sdffrhq"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFRHQXL"]=Desc
