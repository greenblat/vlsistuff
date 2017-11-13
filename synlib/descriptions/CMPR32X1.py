Desc = cellDescClass("CMPR32X1")
Desc.properties["cell_leakage_power"] = "3632.359140"
Desc.properties["cell_footprint"] = "add32"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['A', 'B', 'C', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("C","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("C","CO","combi")
Desc.add_param("area",69.854400);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["CMPR32X1"]=Desc
