Desc = cellDescClass("NAND3BX4")
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["area"] = "36.590400"
Desc.properties["cell_leakage_power"] = "1827.108900"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["NAND3BX4"]=Desc
