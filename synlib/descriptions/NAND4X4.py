Desc = cellDescClass("NAND4X4")
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "56.548800"
Desc.properties["cell_leakage_power"] = "2207.337480"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND4X4"]=Desc
