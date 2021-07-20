Desc = cellDescClass("MX2XL")
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "26.611200"
Desc.properties["cell_leakage_power"] = "1314.350550"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("S0","input")
Desc.add_pin("B","input")
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MX2XL"]=Desc
