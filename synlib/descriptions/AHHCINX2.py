Desc = cellDescClass("AHHCINX2")
Desc.properties["cell_leakage_power"] = "2082.335040"
Desc.properties["cell_footprint"] = "ahhcin"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AHHCINX2"]=Desc
