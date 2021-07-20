Desc = cellDescClass("NOR2BX1")
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "485.221590"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NOR2BX1"]=Desc
