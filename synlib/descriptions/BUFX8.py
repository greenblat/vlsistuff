Desc = cellDescClass("BUFX8")
Desc.properties["cell_leakage_power"] = "2043.346500"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX8"]=Desc
