Desc = cellDescClass("OAI31X1")
Desc.properties["cell_leakage_power"] = "332.236242"
Desc.properties["cell_footprint"] = "oai31"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI31X1"]=Desc
