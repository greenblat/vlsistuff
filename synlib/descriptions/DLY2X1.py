Desc = cellDescClass("DLY2X1")
Desc.properties["cell_leakage_power"] = "625.705884"
Desc.properties["cell_footprint"] = "dly2"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY2X1"]=Desc
