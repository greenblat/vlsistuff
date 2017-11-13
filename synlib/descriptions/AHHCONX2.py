Desc = cellDescClass("AHHCONX2")
Desc.properties["cell_leakage_power"] = "2114.534160"
Desc.properties["cell_footprint"] = "ahhcon"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AHHCONX2"]=Desc
