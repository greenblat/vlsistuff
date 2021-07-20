Desc = cellDescClass("DLY1X1")
Desc.properties["cell_footprint"] = "dly1"
Desc.properties["area"] = "19.958400"
Desc.properties["cell_leakage_power"] = "896.314086"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY1X1"]=Desc
