Desc = cellDescClass("OR2X1")
Desc.properties["cell_leakage_power"] = "741.994506"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["OR2X1"]=Desc
