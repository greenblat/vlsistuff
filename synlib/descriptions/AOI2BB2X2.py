Desc = cellDescClass("AOI2BB2X2")
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "29.937600"
Desc.properties["cell_leakage_power"] = "872.321238"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A0N","input")
Desc.add_pin("A1N","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI2BB2X2"]=Desc
