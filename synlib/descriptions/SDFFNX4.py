Desc = cellDescClass("SDFFNX4")
Desc.properties["cell_leakage_power"] = "3717.700740"
Desc.properties["cell_footprint"] = "sdffn"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",93.139200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNX4"]=Desc
