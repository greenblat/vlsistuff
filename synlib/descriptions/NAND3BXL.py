Desc = cellDescClass("NAND3BXL")
Desc.properties["cell_leakage_power"] = "661.254192"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND3BXL"]=Desc
