Desc = cellDescClass("BUFX12")
Desc.properties["cell_leakage_power"] = "3123.936720"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX12"]=Desc
