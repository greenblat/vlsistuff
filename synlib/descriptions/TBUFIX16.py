Desc = cellDescClass("TBUFIX16")
Desc.properties["cell_leakage_power"] = "5367.510360"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX16"]=Desc
