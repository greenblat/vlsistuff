Desc = cellDescClass("AFHCONX2")
Desc.properties["cell_footprint"] = "afhcon"
Desc.properties["area"] = "79.833600"
Desc.properties["cell_leakage_power"] = "6426.297000"
Desc.pinOrder = ['A', 'B', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("B","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AFHCONX2"]=Desc
