Desc = cellDescClass("AND2X4")
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "16.632000"
Desc.properties["cell_leakage_power"] = "1266.842268"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AND2X4"]=Desc
