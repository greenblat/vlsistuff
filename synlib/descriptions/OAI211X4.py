Desc = cellDescClass("OAI211X4")
Desc.properties["cell_leakage_power"] = "1414.646694"
Desc.properties["cell_footprint"] = "oai211"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI211X4"]=Desc
