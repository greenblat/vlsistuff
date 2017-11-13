Desc = cellDescClass("ADDHX2")
Desc.properties["cell_leakage_power"] = "5042.266200"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHX2"]=Desc
