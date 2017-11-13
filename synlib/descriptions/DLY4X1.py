Desc = cellDescClass("DLY4X1")
Desc.properties["cell_leakage_power"] = "587.077956"
Desc.properties["cell_footprint"] = "dly4"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY4X1"]=Desc
