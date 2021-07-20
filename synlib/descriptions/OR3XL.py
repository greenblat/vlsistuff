Desc = cellDescClass("OR3XL")
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "16.632000"
Desc.properties["cell_leakage_power"] = "1068.089166"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OR3XL"]=Desc
