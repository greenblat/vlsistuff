Desc = cellDescClass("ADDFX4")
Desc.properties["cell_footprint"] = "addf"
Desc.properties["area"] = "76.507200"
Desc.properties["cell_leakage_power"] = "4448.850480"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDFX4"]=Desc
