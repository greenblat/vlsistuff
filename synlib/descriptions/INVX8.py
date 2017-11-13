Desc = cellDescClass("INVX8")
Desc.properties["cell_leakage_power"] = "1086.526062"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX8"]=Desc
