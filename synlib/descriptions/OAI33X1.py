Desc = cellDescClass("OAI33X1")
Desc.properties["cell_leakage_power"] = "404.249940"
Desc.properties["cell_footprint"] = "oai33"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI33X1"]=Desc
