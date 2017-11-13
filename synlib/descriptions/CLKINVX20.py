Desc = cellDescClass("CLKINVX20")
Desc.properties["cell_leakage_power"] = "7065.610560"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",96.465600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX20"]=Desc
