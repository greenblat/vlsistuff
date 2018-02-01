Desc = cellDescClass("NAND4XL")
Desc.properties["cell_leakage_power"] = "434.784834"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NAND4XL"]=Desc