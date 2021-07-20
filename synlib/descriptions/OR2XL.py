Desc = cellDescClass("OR2XL")
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "720.320526"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OR2XL"]=Desc
