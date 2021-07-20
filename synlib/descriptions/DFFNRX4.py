Desc = cellDescClass("DFFNRX4")
Desc.properties["cell_footprint"] = "dffnr"
Desc.properties["area"] = "103.118400"
Desc.properties["cell_leakage_power"] = "3214.454220"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",103.118400);
Desc.add_pin("D","input")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
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
CellLib["DFFNRX4"]=Desc
