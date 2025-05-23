Desc = cellDescClass("NAND2X1")
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "9.979200"
Desc.properties["cell_leakage_power"] = "258.251166"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND2X1"]=Desc
