Desc = cellDescClass("NAND2X4")
Desc.properties["cell_leakage_power"] = "916.074684"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2X4"]=Desc
