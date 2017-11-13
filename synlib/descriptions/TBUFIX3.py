Desc = cellDescClass("TBUFIX3")
Desc.properties["cell_leakage_power"] = "1358.974746"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX3"]=Desc
