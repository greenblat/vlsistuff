Desc = cellDescClass("OR3X4")
Desc.properties["cell_leakage_power"] = "2003.126760"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["OR3X4"]=Desc
