Desc = cellDescClass("AOI222X2")
Desc.properties["cell_footprint"] = "aoi222"
Desc.properties["area"] = "46.569600"
Desc.properties["cell_leakage_power"] = "822.467358"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("C0","input")
Desc.add_pin("C1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI222X2"]=Desc
