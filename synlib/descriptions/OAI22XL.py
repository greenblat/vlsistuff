Desc = cellDescClass("OAI22XL")
Desc.properties["cell_footprint"] = "oai22"
Desc.properties["area"] = "19.958400"
Desc.properties["cell_leakage_power"] = "246.296052"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI22XL"]=Desc
