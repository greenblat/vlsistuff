Desc = cellDescClass("AOI2BB2X1")
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "23.284800"
Desc.properties["cell_leakage_power"] = "740.950902"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A0N","input")
Desc.add_pin("A1N","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI2BB2X1"]=Desc
