Desc = cellDescClass("OAI2BB2X4")
Desc.properties["cell_leakage_power"] = "2057.016060"
Desc.properties["cell_footprint"] = "oai2bb2"
Desc.properties["area"] = "49.896000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",49.896000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["OAI2BB2X4"]=Desc
