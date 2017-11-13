Desc = cellDescClass("BUFX16")
Desc.properties["cell_leakage_power"] = "4129.124040"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX16"]=Desc
