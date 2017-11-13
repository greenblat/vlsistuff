Desc = cellDescClass("TLATRX4")
Desc.properties["cell_leakage_power"] = "1513.070604"
Desc.properties["cell_footprint"] = "tlatr"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATRX4"]=Desc
