Desc = cellDescClass("CLKINVX16")
Desc.properties["cell_leakage_power"] = "5531.901480"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX16"]=Desc
