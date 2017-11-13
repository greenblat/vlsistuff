Desc = cellDescClass("RFRDX1")
Desc.properties["cell_leakage_power"] = "135.409968"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcout"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['BRB', 'RB']
Desc.add_arc("RB","BRB","combi")
Desc.set_job("inv") # (!RB)
Desc.add_param("area",16.632000);
Desc.add_pin("BRB","output")
Desc.add_pin_func("BRB","unknown")
Desc.add_pin("RB","input")
CellLib["RFRDX1"]=Desc
