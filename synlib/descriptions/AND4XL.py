Desc = cellDescClass("AND4XL")
Desc.properties["cell_footprint"] = "and4"
Desc.properties["area"] = "19.958400"
Desc.properties["cell_leakage_power"] = "607.591530"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AND4XL"]=Desc
