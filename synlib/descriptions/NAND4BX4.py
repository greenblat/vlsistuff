Desc = cellDescClass("NAND4BX4")
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "59.875200"
Desc.properties["cell_leakage_power"] = "2886.363720"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND4BX4"]=Desc
