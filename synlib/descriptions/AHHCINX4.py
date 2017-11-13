Desc = cellDescClass("AHHCINX4")
Desc.properties["cell_leakage_power"] = "2275.656120"
Desc.properties["cell_footprint"] = "ahhcin"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AHHCINX4"]=Desc
