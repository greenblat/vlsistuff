Desc = cellDescClass("TBUFIX2")
Desc.properties["cell_leakage_power"] = "411.636978"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX2"]=Desc
