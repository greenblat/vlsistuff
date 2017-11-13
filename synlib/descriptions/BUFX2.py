Desc = cellDescClass("BUFX2")
Desc.properties["cell_leakage_power"] = "574.299720"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX2"]=Desc
