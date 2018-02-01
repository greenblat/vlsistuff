Desc = cellDescClass("XNOR3X4")
Desc.properties["cell_leakage_power"] = "8438.400180"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",99.792000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XNOR3X4"]=Desc