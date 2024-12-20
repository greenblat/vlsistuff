Desc = cellDescClass("NAND3X4")
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "33.264000"
Desc.properties["cell_leakage_power"] = "1162.603368"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND3X4"]=Desc
