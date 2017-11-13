Desc = cellDescClass("CLKINVX12")
Desc.properties["cell_leakage_power"] = "4259.856420"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX12"]=Desc
