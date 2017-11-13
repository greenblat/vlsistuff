Desc = cellDescClass("XOR3X2")
Desc.properties["cell_leakage_power"] = "4534.880580"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XOR3X2"]=Desc
