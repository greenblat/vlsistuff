Desc = cellDescClass("OAI222X4")
Desc.properties["cell_leakage_power"] = "1456.193214"
Desc.properties["cell_footprint"] = "oai222"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["OAI222X4"]=Desc
