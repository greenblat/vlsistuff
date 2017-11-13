Desc = cellDescClass("TIEHI")
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "tiehi"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['Y']
Desc.set_job("supply1")
Desc.add_param("area",6.652800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TIEHI"]=Desc
