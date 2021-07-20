Desc = cellDescClass("AND2X2")
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "661.537530"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AND2X2"]=Desc
