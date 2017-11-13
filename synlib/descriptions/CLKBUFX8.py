Desc = cellDescClass("CLKBUFX8")
Desc.properties["cell_leakage_power"] = "1619.249130"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX8"]=Desc
