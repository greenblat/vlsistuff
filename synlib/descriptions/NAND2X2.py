Desc = cellDescClass("NAND2X2")
Desc.properties["cell_leakage_power"] = "525.788172"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2X2"]=Desc
