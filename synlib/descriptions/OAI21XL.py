Desc = cellDescClass("OAI21XL")
Desc.properties["cell_footprint"] = "oai21"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "233.755470"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI21XL"]=Desc
