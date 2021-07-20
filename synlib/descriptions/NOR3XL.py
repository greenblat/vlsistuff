Desc = cellDescClass("NOR3XL")
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "155.351261"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NOR3XL"]=Desc
