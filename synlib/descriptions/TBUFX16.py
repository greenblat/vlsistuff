Desc = cellDescClass("TBUFX16")
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "56.548800"
Desc.properties["cell_leakage_power"] = "5071.021200"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("OE","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TBUFX16"]=Desc
