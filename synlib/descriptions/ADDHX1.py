Desc = cellDescClass("ADDHX1")
Desc.properties["cell_leakage_power"] = "2576.298960"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHX1"]=Desc
