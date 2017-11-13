Desc = cellDescClass("INVX16")
Desc.properties["cell_leakage_power"] = "4272.416280"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX16"]=Desc
