Desc = cellDescClass("AFHCONX4")
Desc.properties["cell_leakage_power"] = "8363.458980"
Desc.properties["cell_footprint"] = "afhcon"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['A', 'B', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("B","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",86.486400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AFHCONX4"]=Desc
