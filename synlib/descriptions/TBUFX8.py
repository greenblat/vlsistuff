Desc = cellDescClass("TBUFX8")
Desc.properties["cell_leakage_power"] = "2558.827260"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX8"]=Desc
