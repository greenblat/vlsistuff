Desc = cellDescClass("AOI22X4")
Desc.properties["cell_leakage_power"] = "1337.200812"
Desc.properties["cell_footprint"] = "aoi22"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI22X4"]=Desc
