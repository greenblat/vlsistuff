Desc = cellDescClass("RFRDX4")
Desc.properties["cell_leakage_power"] = "531.211446"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcout"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['BRB', 'RB']
Desc.add_arc("RB","BRB","combi")
Desc.set_job("inv") # (!RB)
Desc.add_param("area",19.958400);
Desc.add_pin("BRB","output")
Desc.add_pin_func("BRB","unknown")
Desc.add_pin("RB","input")
CellLib["RFRDX4"]=Desc
