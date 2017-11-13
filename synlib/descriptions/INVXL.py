Desc = cellDescClass("INVXL")
Desc.properties["cell_leakage_power"] = "113.872846"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",6.652800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVXL"]=Desc
