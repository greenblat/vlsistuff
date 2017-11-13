Desc = cellDescClass("BENCX4")
Desc.properties["cell_leakage_power"] = "12534.821280"
Desc.properties["cell_footprint"] = "recsel"
Desc.properties["area"] = "202.910400"
Desc.pinOrder = ['A', 'M0', 'M1', 'M2', 'S', 'X2']
Desc.add_arc("M2","A","combi")
Desc.add_arc("M1","A","combi")
Desc.add_arc("M0","A","combi")
Desc.add_arc("M2","S","combi")
Desc.add_arc("M1","S","combi")
Desc.add_arc("M0","S","combi")
Desc.add_arc("M1","X2","combi")
Desc.add_arc("M0","X2","combi")
Desc.add_param("area",202.910400);
Desc.add_pin("A","output")
Desc.add_pin_func("A","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("M1","input")
Desc.add_pin("M0","input")
Desc.add_pin("M2","input")
Desc.add_pin("X2","output")
Desc.add_pin_func("X2","unknown")
CellLib["BENCX4"]=Desc
