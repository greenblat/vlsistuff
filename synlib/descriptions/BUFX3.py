Desc = cellDescClass("BUFX3")
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "762.792876"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX3"]=Desc
