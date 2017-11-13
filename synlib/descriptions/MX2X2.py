Desc = cellDescClass("MX2X2")
Desc.properties["cell_leakage_power"] = "2043.111600"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2X2"]=Desc
