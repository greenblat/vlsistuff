Desc = cellDescClass("AFCSHCONX2")
Desc.properties["cell_leakage_power"] = "10285.062480"
Desc.properties["cell_footprint"] = "afcshcon"
Desc.properties["area"] = "169.646400"
Desc.pinOrder = ['A', 'B', 'CI0', 'CI1', 'CO0N', 'CO1N', 'CS', 'S']
Desc.add_arc("CS","S","combi")
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI0","S","combi")
Desc.add_arc("CI1","S","combi")
Desc.add_arc("A","CO0N","combi")
Desc.add_arc("B","CO0N","combi")
Desc.add_arc("CI0","CO0N","combi")
Desc.add_arc("A","CO1N","combi")
Desc.add_arc("B","CO1N","combi")
Desc.add_arc("CI1","CO1N","combi")
Desc.add_param("area",169.646400);
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CO0N","output")
Desc.add_pin_func("CO0N","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CI1","input")
Desc.add_pin("CI0","input")
Desc.add_pin("CO1N","output")
Desc.add_pin_func("CO1N","unknown")
Desc.add_pin("CS","input")
CellLib["AFCSHCONX2"]=Desc
