Desc = cellDescClass("XNOR2X2")
Desc.properties["cell_leakage_power"] = "2696.948460"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2X2"]=Desc
