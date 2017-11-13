Desc = cellDescClass("MXI4X1")
Desc.properties["cell_leakage_power"] = "3207.151260"
Desc.properties["cell_footprint"] = "muxi4"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MXI4X1"]=Desc
