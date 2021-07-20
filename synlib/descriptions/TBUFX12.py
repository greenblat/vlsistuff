Desc = cellDescClass("TBUFX12")
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "49.896000"
Desc.properties["cell_leakage_power"] = "4022.952480"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",49.896000);
Desc.add_pin("A","input")
Desc.add_pin("OE","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TBUFX12"]=Desc
