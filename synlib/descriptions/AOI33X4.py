Desc = cellDescClass("AOI33X4")
Desc.properties["cell_footprint"] = "aoi33"
Desc.properties["area"] = "36.590400"
Desc.properties["cell_leakage_power"] = "1441.993590"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI33X4"]=Desc
