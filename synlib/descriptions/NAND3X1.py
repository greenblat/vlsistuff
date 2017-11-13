Desc = cellDescClass("NAND3X1")
Desc.properties["cell_leakage_power"] = "420.378498"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NAND3X1"]=Desc
