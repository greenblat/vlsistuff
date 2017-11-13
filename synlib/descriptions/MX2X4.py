Desc = cellDescClass("MX2X4")
Desc.properties["cell_leakage_power"] = "2486.865240"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2X4"]=Desc
