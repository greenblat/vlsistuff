Desc = cellDescClass("AOI2BB1X4")
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "36.590400"
Desc.properties["cell_leakage_power"] = "1964.988720"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A0N","input")
Desc.add_pin("A1N","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI2BB1X4"]=Desc
