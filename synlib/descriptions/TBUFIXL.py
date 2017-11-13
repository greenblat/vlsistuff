Desc = cellDescClass("TBUFIXL")
Desc.properties["cell_leakage_power"] = "252.730692"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIXL"]=Desc
