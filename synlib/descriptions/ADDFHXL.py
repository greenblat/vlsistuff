Desc = cellDescClass("ADDFHXL")
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "73.180800"
Desc.properties["cell_leakage_power"] = "3398.980320"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",73.180800);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDFHXL"]=Desc
