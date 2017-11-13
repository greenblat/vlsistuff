Desc = cellDescClass("CLKBUFX20")
Desc.properties["cell_leakage_power"] = "6339.486060"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX20"]=Desc
