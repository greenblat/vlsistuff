Desc = cellDescClass("DFFNSX2")
Desc.properties["cell_leakage_power"] = "2104.752600"
Desc.properties["cell_footprint"] = "dffns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
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
CellLib["DFFNSX2"]=Desc
