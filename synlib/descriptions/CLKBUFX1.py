Desc = cellDescClass("CLKBUFX1")
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "465.424218"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX1"]=Desc
