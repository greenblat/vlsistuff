Desc = cellDescClass("NAND2BX2")
Desc.properties["cell_leakage_power"] = "829.342476"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND2BX2"]=Desc
