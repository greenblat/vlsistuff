Desc = cellDescClass("DFFNXL")
Desc.properties["cell_leakage_power"] = "1452.142728"
Desc.properties["cell_footprint"] = "dffn"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",56.548800);
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
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNXL"]=Desc
