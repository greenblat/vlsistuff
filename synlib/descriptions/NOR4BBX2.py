Desc = cellDescClass("NOR4BBX2")
Desc.properties["cell_leakage_power"] = "1026.713232"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BBX2"]=Desc
