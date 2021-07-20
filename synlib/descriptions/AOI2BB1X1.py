Desc = cellDescClass("AOI2BB1X1")
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "16.632000"
Desc.properties["cell_leakage_power"] = "761.882274"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A0N","input")
Desc.add_pin("A1N","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI2BB1X1"]=Desc
