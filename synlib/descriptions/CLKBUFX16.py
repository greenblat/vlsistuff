Desc = cellDescClass("CLKBUFX16")
Desc.properties["cell_leakage_power"] = "5029.443900"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX16"]=Desc
