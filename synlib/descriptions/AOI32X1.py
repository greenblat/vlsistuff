Desc = cellDescClass("AOI32X1")
Desc.properties["cell_footprint"] = "aoi32"
Desc.properties["area"] = "23.284800"
Desc.properties["cell_leakage_power"] = "445.354200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI32X1"]=Desc
