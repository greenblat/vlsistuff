Desc = cellDescClass("AHHCONX4")
Desc.properties["cell_footprint"] = "ahhcon"
Desc.properties["area"] = "43.243200"
Desc.properties["cell_leakage_power"] = "2461.991760"
Desc.pinOrder = ['A', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AHHCONX4"]=Desc
