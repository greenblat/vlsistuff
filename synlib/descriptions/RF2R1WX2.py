Desc = cellDescClass("RF2R1WX2")
Desc.properties["cell_leakage_power"] = "1800.199080"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcrrw"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['IQ', 'IQN', 'R1B', 'R1W', 'R2B', 'R2W', 'WB', 'WW', 'next']
Desc.add_arc("WW","WB","setup_falling")
Desc.add_arc("WW","WB","hold_falling")
Desc.add_arc("WB","R1B","combi")
Desc.add_arc("WW","R1B","rising_edge")
Desc.add_arc("R1W","R1B","three_state_disable")
Desc.add_arc("R1W","R1B","three_state_enable")
Desc.add_arc("WB","R2B","combi")
Desc.add_arc("WW","R2B","rising_edge")
Desc.add_arc("R2W","R2B","three_state_disable")
Desc.add_arc("R2W","R2B","three_state_enable")
Desc.add_param("area",53.222400);
Desc.add_pin("R1W","input")
Desc.add_pin("WB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("R2B","output")
Desc.add_pin_func("R2B","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_pin_job("WW","clock")
Desc.add_pin("WW","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("R1B","output")
Desc.add_pin_func("R1B","unknown")
Desc.add_pin("R2W","input")
Desc.set_job("latch")
CellLib["RF2R1WX2"]=Desc
