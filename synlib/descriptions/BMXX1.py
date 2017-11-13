Desc = cellDescClass("BMXX1")
Desc.properties["cell_leakage_power"] = "3241.851660"
Desc.properties["cell_footprint"] = "recmux"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'M0', 'M1', 'PP', 'S', 'X2']
Desc.add_arc("X2","PP","combi")
Desc.add_arc("M0","PP","combi")
Desc.add_arc("A","PP","combi")
Desc.add_arc("S","PP","combi")
Desc.add_arc("M1","PP","combi")
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("PP","output")
Desc.add_pin_func("PP","unknown")
Desc.add_pin("S","input")
Desc.add_pin("M1","input")
Desc.add_pin("M0","input")
Desc.add_pin("X2","input")
CellLib["BMXX1"]=Desc
