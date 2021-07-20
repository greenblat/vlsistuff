Desc = cellDescClass("NOR3BX2")
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["area"] = "26.611200"
Desc.properties["cell_leakage_power"] = "737.846820"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NOR3BX2"]=Desc
