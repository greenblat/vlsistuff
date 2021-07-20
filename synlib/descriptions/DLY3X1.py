Desc = cellDescClass("DLY3X1")
Desc.properties["cell_footprint"] = "dly3"
Desc.properties["area"] = "23.284800"
Desc.properties["cell_leakage_power"] = "595.058238"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY3X1"]=Desc
