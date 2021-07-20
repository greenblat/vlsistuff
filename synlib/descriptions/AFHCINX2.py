Desc = cellDescClass("AFHCINX2")
Desc.properties["cell_footprint"] = "afhcin"
Desc.properties["area"] = "83.160000"
Desc.properties["cell_leakage_power"] = "6586.184520"
Desc.pinOrder = ['A', 'B', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CIN","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["AFHCINX2"]=Desc
