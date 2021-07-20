Desc = cellDescClass("AFCSHCINX2")
Desc.properties["cell_footprint"] = "afcshcin"
Desc.properties["area"] = "166.320000"
Desc.properties["cell_leakage_power"] = "9757.810800"
Desc.pinOrder = ['A', 'B', 'CI0N', 'CI1N', 'CO0', 'CO1', 'CS', 'S']
Desc.add_arc("CS","S","combi")
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI0N","S","combi")
Desc.add_arc("CI1N","S","combi")
Desc.add_arc("A","CO0","combi")
Desc.add_arc("B","CO0","combi")
Desc.add_arc("CI0N","CO0","combi")
Desc.add_arc("A","CO1","combi")
Desc.add_arc("B","CO1","combi")
Desc.add_arc("CI1N","CO1","combi")
Desc.add_param("area",166.320000);
Desc.add_pin("CS","input")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI0N","input")
Desc.add_pin("CI1N","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO0","output")
Desc.add_pin_func("CO0","unknown")
Desc.add_pin("CO1","output")
Desc.add_pin_func("CO1","unknown")
CellLib["AFCSHCINX2"]=Desc
