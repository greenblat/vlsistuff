Desc = cellDescClass("TBUFIX20")
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "83.160000"
Desc.properties["cell_leakage_power"] = "6694.808760"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("OE","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TBUFIX20"]=Desc
