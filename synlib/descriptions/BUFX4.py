Desc = cellDescClass("BUFX4")
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "16.632000"
Desc.properties["cell_leakage_power"] = "1060.451514"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX4"]=Desc
