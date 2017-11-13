Desc = cellDescClass("CMPR42X1")
Desc.properties["cell_leakage_power"] = "5452.116480"
Desc.properties["cell_footprint"] = "add42"
Desc.properties["area"] = "113.097600"
Desc.pinOrder = ['A', 'B', 'C', 'CO', 'D', 'ICI', 'ICO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("C","S","combi")
Desc.add_arc("D","S","combi")
Desc.add_arc("ICI","S","combi")
Desc.add_arc("A","ICO","combi")
Desc.add_arc("B","ICO","combi")
Desc.add_arc("C","ICO","combi")
Desc.add_arc("D","CO","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("C","CO","combi")
Desc.add_arc("ICI","CO","combi")
Desc.add_param("area",113.097600);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("ICO","output")
Desc.add_pin_func("ICO","unknown")
Desc.add_pin("D","input")
Desc.add_pin("ICI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["CMPR42X1"]=Desc
