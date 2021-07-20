Desc = cellDescClass("XOR2X1")
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "26.611200"
Desc.properties["cell_leakage_power"] = "1704.108780"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["XOR2X1"]=Desc
