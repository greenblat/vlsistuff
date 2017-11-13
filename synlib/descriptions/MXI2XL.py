Desc = cellDescClass("MXI2XL")
Desc.properties["cell_leakage_power"] = "1149.161742"
Desc.properties["cell_footprint"] = "muxi2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MXI2XL"]=Desc
