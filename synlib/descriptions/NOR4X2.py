Desc = cellDescClass("NOR4X2")
Desc.properties["cell_leakage_power"] = "538.097256"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NOR4X2"]=Desc
