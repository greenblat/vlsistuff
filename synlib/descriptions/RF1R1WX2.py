Desc = cellDescClass("RF1R1WX2")
Desc.properties["cell_leakage_power"] = "1118.088198"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcrw"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['IQ', 'IQN', 'RB', 'RW', 'RWN', 'WB', 'WW', 'next']
Desc.add_arc("WW","WB","setup_falling")
Desc.add_arc("WW","WB","hold_falling")
Desc.add_arc("WW","RB","rising_edge")
Desc.add_arc("WB","RB","combi")
Desc.add_arc("RW","RB","three_state_disable")
Desc.add_arc("RW","RB","three_state_enable")
Desc.add_arc("RWN","RB","three_state_disable")
Desc.add_arc("RWN","RB","three_state_enable")
Desc.add_param("area",33.264000);
Desc.add_pin("RW","input")
Desc.add_pin("WB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("RWN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_pin_job("WW","clock")
Desc.add_pin("WW","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RB","output")
Desc.add_pin_func("RB","unknown")
Desc.set_job("latch")
CellLib["RF1R1WX2"]=Desc
