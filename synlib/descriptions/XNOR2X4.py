Desc = cellDescClass("XNOR2X4")
Desc.properties["cell_leakage_power"] = "5408.167500"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2X4"]=Desc
