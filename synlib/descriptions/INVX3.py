Desc = cellDescClass("INVX3")
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "13.305600"
Desc.properties["cell_leakage_power"] = "371.352762"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX3"]=Desc
