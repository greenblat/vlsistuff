Desc = cellDescClass("INVX12")
Desc.properties["cell_leakage_power"] = "3253.878540"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX12"]=Desc
