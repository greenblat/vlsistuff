Desc = cellDescClass("CLKINVX1")
Desc.properties["cell_leakage_power"] = "138.122852"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX1"]=Desc
