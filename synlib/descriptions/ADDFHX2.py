Desc = cellDescClass("ADDFHX2")
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "113.097600"
Desc.properties["cell_leakage_power"] = "7522.904160"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",113.097600);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDFHX2"]=Desc
