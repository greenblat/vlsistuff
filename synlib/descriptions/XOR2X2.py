Desc = cellDescClass("XOR2X2")
Desc.properties["cell_leakage_power"] = "2882.649060"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XOR2X2"]=Desc
