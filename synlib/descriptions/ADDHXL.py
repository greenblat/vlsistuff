Desc = cellDescClass("ADDHXL")
Desc.properties["cell_leakage_power"] = "1423.696824"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHXL"]=Desc
