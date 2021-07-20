Desc = cellDescClass("BUFX20")
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "53.222400"
Desc.properties["cell_leakage_power"] = "5112.567720"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",53.222400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX20"]=Desc
