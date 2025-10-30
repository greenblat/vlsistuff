

class cellDescClass:
    def __init__(self,Name):
        self.Name = Name
        self.Pins = {}
        self.params = {}
        self.pinsJobs = {}
        self.pinsFunc = {}
        self.Job='combi'
        self.properties = {}
        self.Delays={}
        self.arcs=[]
        self.Outputs = {}

    def add_arc(self,Pin0,Pin1,Kind):
        self.arcs.append((Pin0,Pin1,Kind))
    def is_output(self,Pin):
        if Pin not in self.Pins: return False
        return self.Pins[Pin]=='output'
    def is_input(self,Pin):
        if Pin not in self.Pins: return False
        return self.Pins[Pin]=='input'

    def is_flop(self):
        return self.Job=='flipflop'


    def add_param(self,Param,Val):
        self.params[Param]=Val
    def add_pin(self,Pin,Dir):
        self.Pins[Pin]=Dir
        if Dir == 'output': self.Outputs[Pin] = True
    def add_pin_func(self,Pin,Func):
        self.pinsFunc[Pin]=Func
    def set_pin_job(self,Pin,Job):
        self.pinsJobs[Pin]=Job

    def set_job(self,Job):
        self.Job=Job

    def combi_in(self,Pin):
        if Pin not in self.Pins:
            return False 
        if self.Pins[Pin]!='input':
            return False 
        if Pin in self.pinsJobs:
            return False 
        return True

    def combi_out(self,Pin):
        if Pin not in self.Pins:
            return False 
        if self.Pins[Pin]!='output':
            return False 
        if Pin in self.pinsJobs:
            return False 
        return True
cellLib = {}

Desc = cellDescClass("scs130ms_a2111o_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a2111o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1 || D1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111o_1"]=Desc
Desc = cellDescClass("scs130ms_a2111o_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a2111o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1 || D1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111o_2"]=Desc
Desc = cellDescClass("scs130ms_a2111o_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "a2111o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1 || D1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111o_4"]=Desc
Desc = cellDescClass("scs130ms_a2111oi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a2111oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111oi_1"]=Desc
Desc = cellDescClass("scs130ms_a2111oi_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "a2111oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111oi_2"]=Desc
Desc = cellDescClass("scs130ms_a2111oi_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "a2111oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) && ( ! D1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_a2111oi_4"]=Desc
Desc = cellDescClass("scs130ms_a211o_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a211o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211o_1"]=Desc
Desc = cellDescClass("scs130ms_a211o_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a211o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211o_2"]=Desc
Desc = cellDescClass("scs130ms_a211o_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "a211o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211o_4"]=Desc
Desc = cellDescClass("scs130ms_a211oi_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "a211oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211oi_1"]=Desc
Desc = cellDescClass("scs130ms_a211oi_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a211oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211oi_2"]=Desc
Desc = cellDescClass("scs130ms_a211oi_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "a211oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a211oi_4"]=Desc
Desc = cellDescClass("scs130ms_a21bo_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a21bo"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || ( ! B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21bo_1"]=Desc
Desc = cellDescClass("scs130ms_a21bo_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a21bo"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || ( ! B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21bo_2"]=Desc
Desc = cellDescClass("scs130ms_a21bo_4")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "a21bo"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || ( ! B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21bo_4"]=Desc
Desc = cellDescClass("scs130ms_a21boi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a21boi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && B1N ) || ( ( ! A2 ) && B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21boi_1"]=Desc
Desc = cellDescClass("scs130ms_a21boi_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a21boi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && B1N ) || ( ( ! A2 ) && B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21boi_2"]=Desc
Desc = cellDescClass("scs130ms_a21boi_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "a21boi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && B1N ) || ( ( ! A2 ) && B1N )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_a21boi_4"]=Desc
Desc = cellDescClass("scs130ms_a21o_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a21o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21o_1"]=Desc
Desc = cellDescClass("scs130ms_a21o_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a21o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21o_2"]=Desc
Desc = cellDescClass("scs130ms_a21o_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "a21o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21o_4"]=Desc
Desc = cellDescClass("scs130ms_a21oi_1")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "a21oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",6.393600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21oi_1"]=Desc
Desc = cellDescClass("scs130ms_a21oi_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a21oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21oi_2"]=Desc
Desc = cellDescClass("scs130ms_a21oi_4")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "a21oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a21oi_4"]=Desc
Desc = cellDescClass("scs130ms_a221o_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a221o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 ) || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221o_1"]=Desc
Desc = cellDescClass("scs130ms_a221o_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a221o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 ) || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221o_2"]=Desc
Desc = cellDescClass("scs130ms_a221o_4")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "a221o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",31.968000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 ) || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221o_4"]=Desc
Desc = cellDescClass("scs130ms_a221oi_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a221oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221oi_1"]=Desc
Desc = cellDescClass("scs130ms_a221oi_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "a221oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221oi_2"]=Desc
Desc = cellDescClass("scs130ms_a221oi_4")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "a221oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",35.164800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a221oi_4"]=Desc
Desc = cellDescClass("scs130ms_a222o_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a222o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("C2","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( C1 && C2 ) || ( B1 && B2 ) || ( A1 && A2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
Desc.add_pin("C2","input")
cellLib["scs130ms_a222o_1"]=Desc
Desc = cellDescClass("scs130ms_a222o_2")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "a222o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("C2","X","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( C1 && C2 ) || ( B1 && B2 ) || ( A1 && A2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
Desc.add_pin("C2","input")
cellLib["scs130ms_a222o_2"]=Desc
Desc = cellDescClass("scs130ms_a222oi_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a222oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("C2","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B1 ) && ( ! C2 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C2 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C2 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
Desc.add_pin("C2","input")
cellLib["scs130ms_a222oi_1"]=Desc
Desc = cellDescClass("scs130ms_a222oi_2")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "a222oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("C2","Y","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B1 ) && ( ! C2 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A1 ) && ( ! B2 ) && ( ! C2 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C2 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B2 ) && ( ! C2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
Desc.add_pin("C2","input")
cellLib["scs130ms_a222oi_2"]=Desc
Desc = cellDescClass("scs130ms_a22o_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a22o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22o_1"]=Desc
Desc = cellDescClass("scs130ms_a22o_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a22o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22o_2"]=Desc
Desc = cellDescClass("scs130ms_a22o_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "a22o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( A1 && A2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22o_4"]=Desc
Desc = cellDescClass("scs130ms_a22oi_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "a22oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22oi_1"]=Desc
Desc = cellDescClass("scs130ms_a22oi_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a22oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22oi_2"]=Desc
Desc = cellDescClass("scs130ms_a22oi_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "a22oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a22oi_4"]=Desc
Desc = cellDescClass("scs130ms_a2bb2o_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a2bb2o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( ( ! A1N ) && ( ! A2N ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2o_1"]=Desc
Desc = cellDescClass("scs130ms_a2bb2o_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a2bb2o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( ( ! A1N ) && ( ! A2N ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2o_2"]=Desc
Desc = cellDescClass("scs130ms_a2bb2o_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "a2bb2o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( B1 && B2 ) || ( ( ! A1N ) && ( ! A2N ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2o_4"]=Desc
Desc = cellDescClass("scs130ms_a2bb2oi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a2bb2oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( A1N && ( ! B1 ) ) || ( A1N && ( ! B2 ) ) || ( A2N && ( ! B1 ) ) || ( A2N && ( ! B2 ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2oi_1"]=Desc
Desc = cellDescClass("scs130ms_a2bb2oi_2")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "a2bb2oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( A1N && ( ! B1 ) ) || ( A1N && ( ! B2 ) ) || ( A2N && ( ! B1 ) ) || ( A2N && ( ! B2 ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2oi_2"]=Desc
Desc = cellDescClass("scs130ms_a2bb2oi_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "a2bb2oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( A1N && ( ! B1 ) ) || ( A1N && ( ! B2 ) ) || ( A2N && ( ! B1 ) ) || ( A2N && ( ! B2 ) )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a2bb2oi_4"]=Desc
Desc = cellDescClass("scs130ms_a311o_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a311o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311o_1"]=Desc
Desc = cellDescClass("scs130ms_a311o_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a311o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311o_2"]=Desc
Desc = cellDescClass("scs130ms_a311o_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "a311o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1 || C1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311o_4"]=Desc
Desc = cellDescClass("scs130ms_a311oi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a311oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A3 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311oi_1"]=Desc
Desc = cellDescClass("scs130ms_a311oi_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "a311oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A3 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311oi_2"]=Desc
Desc = cellDescClass("scs130ms_a311oi_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "a311oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A2 ) && ( ! B1 ) && ( ! C1 ) ) || ( ( ! A3 ) && ( ! B1 ) && ( ! C1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_a311oi_4"]=Desc
Desc = cellDescClass("scs130ms_a31o_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a31o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31o_1"]=Desc
Desc = cellDescClass("scs130ms_a31o_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a31o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31o_2"]=Desc
Desc = cellDescClass("scs130ms_a31o_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "a31o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31o_4"]=Desc
Desc = cellDescClass("scs130ms_a31oi_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "a31oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31oi_1"]=Desc
Desc = cellDescClass("scs130ms_a31oi_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a31oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31oi_2"]=Desc
Desc = cellDescClass("scs130ms_a31oi_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "a31oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a31oi_4"]=Desc
Desc = cellDescClass("scs130ms_a32o_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "a32o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || ( B1 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32o_1"]=Desc
Desc = cellDescClass("scs130ms_a32o_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a32o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || ( B1 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32o_2"]=Desc
Desc = cellDescClass("scs130ms_a32o_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "a32o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 ) || ( B1 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32o_4"]=Desc
Desc = cellDescClass("scs130ms_a32oi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a32oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) ) || ( ( ! A3 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32oi_1"]=Desc
Desc = cellDescClass("scs130ms_a32oi_2")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "a32oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) ) || ( ( ! A3 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32oi_2"]=Desc
Desc = cellDescClass("scs130ms_a32oi_4")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "a32oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",35.164800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A1 ) && ( ! B2 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B2 ) ) || ( ( ! A3 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_a32oi_4"]=Desc
Desc = cellDescClass("scs130ms_a41o_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "a41o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 && A4 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41o_1"]=Desc
Desc = cellDescClass("scs130ms_a41o_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "a41o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 && A4 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41o_2"]=Desc
Desc = cellDescClass("scs130ms_a41o_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "a41o"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && A2 && A3 && A4 ) || B1")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41o_4"]=Desc
Desc = cellDescClass("scs130ms_a41oi_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "a41oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A4 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41oi_1"]=Desc
Desc = cellDescClass("scs130ms_a41oi_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "a41oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A4 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41oi_2"]=Desc
Desc = cellDescClass("scs130ms_a41oi_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "a41oi"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! B1 ) ) || ( ( ! A2 ) && ( ! B1 ) ) || ( ( ! A3 ) && ( ! B1 ) ) || ( ( ! A4 ) && ( ! B1 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_a41oi_4"]=Desc
Desc = cellDescClass("scs130ms_and2_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2_1"]=Desc
Desc = cellDescClass("scs130ms_and2_2")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2_2"]=Desc
Desc = cellDescClass("scs130ms_and2_4")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2_4"]=Desc
Desc = cellDescClass("scs130ms_and2b_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "and2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2b_1"]=Desc
Desc = cellDescClass("scs130ms_and2b_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "and2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2b_2"]=Desc
Desc = cellDescClass("scs130ms_and2b_4")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "and2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_and2b_4"]=Desc
Desc = cellDescClass("scs130ms_and3_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3_1"]=Desc
Desc = cellDescClass("scs130ms_and3_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3_2"]=Desc
Desc = cellDescClass("scs130ms_and3_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3_4"]=Desc
Desc = cellDescClass("scs130ms_and3b_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "and3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3b_1"]=Desc
Desc = cellDescClass("scs130ms_and3b_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "and3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3b_2"]=Desc
Desc = cellDescClass("scs130ms_and3b_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "and3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_and3b_4"]=Desc
Desc = cellDescClass("scs130ms_and4_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C && D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4_1"]=Desc
Desc = cellDescClass("scs130ms_and4_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C && D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4_2"]=Desc
Desc = cellDescClass("scs130ms_and4_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A && B && C && D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4_4"]=Desc
Desc = cellDescClass("scs130ms_and4b_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "and4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4b_1"]=Desc
Desc = cellDescClass("scs130ms_and4b_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "and4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4b_2"]=Desc
Desc = cellDescClass("scs130ms_and4b_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "and4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && B && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4b_4"]=Desc
Desc = cellDescClass("scs130ms_and4bb_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "and4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && ( ! BN ) && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4bb_1"]=Desc
Desc = cellDescClass("scs130ms_and4bb_2")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "and4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && ( ! BN ) && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4bb_2"]=Desc
Desc = cellDescClass("scs130ms_and4bb_4")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "and4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'X']
Desc.add_arc("AN","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",30.369600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ! AN ) && ( ! BN ) && C && D")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_and4bb_4"]=Desc
Desc = cellDescClass("scs130ms_buf_1")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",6.393600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_buf_1"]=Desc
Desc = cellDescClass("scs130ms_buf_16")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",35.164800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_buf_16"]=Desc
Desc = cellDescClass("scs130ms_buf_2")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",7.992000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_buf_2"]=Desc
Desc = cellDescClass("scs130ms_buf_4")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_buf_4"]=Desc
Desc = cellDescClass("scs130ms_buf_8")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_buf_8"]=Desc
Desc = cellDescClass("scs130ms_bufbuf_16")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",43.156800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_bufbuf_16"]=Desc
Desc = cellDescClass("scs130ms_bufbuf_8")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_bufbuf_8"]=Desc
Desc = cellDescClass("scs130ms_bufinv_16")
Desc.properties["area"] = "39.960000"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",39.960000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_bufinv_16"]=Desc
Desc = cellDescClass("scs130ms_bufinv_8")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_bufinv_8"]=Desc
Desc = cellDescClass("scs130ms_clkbuf_1")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",6.393600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkbuf_1"]=Desc
Desc = cellDescClass("scs130ms_clkbuf_16")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",31.968000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkbuf_16"]=Desc
Desc = cellDescClass("scs130ms_clkbuf_2")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",6.393600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkbuf_2"]=Desc
Desc = cellDescClass("scs130ms_clkbuf_4")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",9.590400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkbuf_4"]=Desc
Desc = cellDescClass("scs130ms_clkbuf_8")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",17.582400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkbuf_8"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv3sd1_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv3sd1_1"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv3sd2_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv3sd2_1"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv3sd3_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv3sd3_1"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv5sd1_1")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv5sd1_1"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv5sd2_1")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv5sd2_1"]=Desc
Desc = cellDescClass("scs130ms_clkdlyinv5sd3_1")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "clkdlyinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkdlyinv5sd3_1"]=Desc
Desc = cellDescClass("scs130ms_clkinv_1")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",4.795200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkinv_1"]=Desc
Desc = cellDescClass("scs130ms_clkinv_16")
Desc.properties["area"] = "38.361600"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",38.361600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkinv_16"]=Desc
Desc = cellDescClass("scs130ms_clkinv_2")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",6.393600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkinv_2"]=Desc
Desc = cellDescClass("scs130ms_clkinv_4")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkinv_4"]=Desc
Desc = cellDescClass("scs130ms_clkinv_8")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_clkinv_8"]=Desc
Desc = cellDescClass("scs130ms_conb_1")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "conb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['HI', 'LO']
Desc.set_job("buf") # 1
Desc.set_job("buf") # 0
Desc.add_param("area",4.795200);
Desc.add_pin("HI","output")
Desc.add_pin_func("HI","1")
Desc.add_pin("LO","output")
Desc.add_pin_func("LO","0")
cellLib["scs130ms_conb_1"]=Desc
Desc = cellDescClass("scs130ms_decap_4")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "decap"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = []
Desc.add_param("area",6.393600);
cellLib["scs130ms_decap_4"]=Desc
Desc = cellDescClass("scs130ms_decap_8")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "decap"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = []
Desc.add_param("area",12.787200);
cellLib["scs130ms_decap_8"]=Desc
Desc = cellDescClass("scs130ms_dfbbn_1")
Desc.properties["area"] = "44.755200"
Desc.properties["cell_footprint"] = "dfbbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SETB', 'next']
Desc.add_arc("CLKN","SETB","recovery_falling")
Desc.add_arc("CLKN","SETB","removal_falling")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLKN","QN","falling_edge")
Desc.add_param("area",44.755200);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "D","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_dfbbn_1"]=Desc
Desc = cellDescClass("scs130ms_dfbbn_2")
Desc.properties["area"] = "47.952000"
Desc.properties["cell_footprint"] = "dfbbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SETB', 'next']
Desc.add_arc("CLKN","SETB","recovery_falling")
Desc.add_arc("CLKN","SETB","removal_falling")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLKN","QN","falling_edge")
Desc.add_param("area",47.952000);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "D","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_dfbbn_2"]=Desc
Desc = cellDescClass("scs130ms_dfbbp_1")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "dfbbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SETB', 'next']
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",43.156800);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_dfbbp_1"]=Desc
Desc = cellDescClass("scs130ms_dfrbp_1")
Desc.properties["area"] = "38.361600"
Desc.properties["cell_footprint"] = "dfrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",38.361600);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrbp_1"]=Desc
Desc = cellDescClass("scs130ms_dfrbp_2")
Desc.properties["area"] = "46.353600"
Desc.properties["cell_footprint"] = "dfrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",46.353600);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrbp_2"]=Desc
Desc = cellDescClass("scs130ms_dfrtn_1")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "dfrtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_param("area",36.763200);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrtn_1"]=Desc
Desc = cellDescClass("scs130ms_dfrtp_1")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "dfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",36.763200);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrtp_1"]=Desc
Desc = cellDescClass("scs130ms_dfrtp_2")
Desc.properties["area"] = "38.361600"
Desc.properties["cell_footprint"] = "dfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",38.361600);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrtp_2"]=Desc
Desc = cellDescClass("scs130ms_dfrtp_4")
Desc.properties["area"] = "44.755200"
Desc.properties["cell_footprint"] = "dfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",44.755200);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","clear": "!RESETB" }
cellLib["scs130ms_dfrtp_4"]=Desc
Desc = cellDescClass("scs130ms_dfsbp_1")
Desc.properties["area"] = "39.960000"
Desc.properties["cell_footprint"] = "dfsbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",39.960000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","preset": "!SETB" }
cellLib["scs130ms_dfsbp_1"]=Desc
Desc = cellDescClass("scs130ms_dfsbp_2")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "dfsbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",43.156800);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","preset": "!SETB" }
cellLib["scs130ms_dfsbp_2"]=Desc
Desc = cellDescClass("scs130ms_dfstp_1")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "dfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",36.763200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","preset": "!SETB" }
cellLib["scs130ms_dfstp_1"]=Desc
Desc = cellDescClass("scs130ms_dfstp_2")
Desc.properties["area"] = "39.960000"
Desc.properties["cell_footprint"] = "dfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",39.960000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","preset": "!SETB" }
cellLib["scs130ms_dfstp_2"]=Desc
Desc = cellDescClass("scs130ms_dfstp_4")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "dfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",43.156800);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D","preset": "!SETB" }
cellLib["scs130ms_dfstp_4"]=Desc
Desc = cellDescClass("scs130ms_dfxbp_1")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "dfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",31.968000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D" }
cellLib["scs130ms_dfxbp_1"]=Desc
Desc = cellDescClass("scs130ms_dfxbp_2")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "dfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",36.763200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D" }
cellLib["scs130ms_dfxbp_2"]=Desc
Desc = cellDescClass("scs130ms_dfxtp_1")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",27.172800);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D" }
cellLib["scs130ms_dfxtp_1"]=Desc
Desc = cellDescClass("scs130ms_dfxtp_2")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "dfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",28.771200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D" }
cellLib["scs130ms_dfxtp_2"]=Desc
Desc = cellDescClass("scs130ms_dfxtp_4")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "dfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_param("area",31.968000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "D" }
cellLib["scs130ms_dfxtp_4"]=Desc
Desc = cellDescClass("scs130ms_dlclkp_1")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "dlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_param("area",22.377600);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.set_job("statetable")
# (['CLK GATE', 'm0'], '" L L : - : L ,\\              L H : - : H ,\\              H - : - : N "')
cellLib["scs130ms_dlclkp_1"]=Desc
Desc = cellDescClass("scs130ms_dlclkp_2")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "dlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_param("area",25.574400);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.set_job("statetable")
# (['CLK GATE', 'm0'], '" L L : - : L ,\\              L H : - : H ,\\              H - : - : N "')
cellLib["scs130ms_dlclkp_2"]=Desc
Desc = cellDescClass("scs130ms_dlclkp_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "dlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_param("area",28.771200);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.set_job("statetable")
# (['CLK GATE', 'm0'], '" L L : - : L ,\\              L H : - : H ,\\              H - : - : N "')
cellLib["scs130ms_dlclkp_4"]=Desc
Desc = cellDescClass("scs130ms_dlrbn_1")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "dlrbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("GATEN","RESETB","recovery_rising")
Desc.add_arc("GATEN","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATEN","QN","falling_edge")
Desc.add_param("area",28.771200);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrbn_1"]=Desc
Desc = cellDescClass("scs130ms_dlrbn_2")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "dlrbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("GATEN","RESETB","recovery_rising")
Desc.add_arc("GATEN","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATEN","QN","falling_edge")
Desc.add_param("area",30.369600);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrbn_2"]=Desc
Desc = cellDescClass("scs130ms_dlrbp_1")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dlrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("GATE","RESETB","recovery_falling")
Desc.add_arc("GATE","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATE","QN","rising_edge")
Desc.add_param("area",27.172800);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrbp_1"]=Desc
Desc = cellDescClass("scs130ms_dlrbp_2")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "dlrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'next']
Desc.add_arc("GATE","RESETB","recovery_falling")
Desc.add_arc("GATE","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATE","QN","rising_edge")
Desc.add_param("area",30.369600);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrbp_2"]=Desc
Desc = cellDescClass("scs130ms_dlrtn_1")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "dlrtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATEN","RESETB","recovery_rising")
Desc.add_arc("GATEN","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",23.976000);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtn_1"]=Desc
Desc = cellDescClass("scs130ms_dlrtn_2")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dlrtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATEN","RESETB","recovery_rising")
Desc.add_arc("GATEN","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",27.172800);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtn_2"]=Desc
Desc = cellDescClass("scs130ms_dlrtn_4")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "dlrtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATEN","RESETB","recovery_rising")
Desc.add_arc("GATEN","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",31.968000);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtn_4"]=Desc
Desc = cellDescClass("scs130ms_dlrtp_1")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "dlrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATE","RESETB","recovery_falling")
Desc.add_arc("GATE","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_param("area",22.377600);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtp_1"]=Desc
Desc = cellDescClass("scs130ms_dlrtp_2")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "dlrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATE","RESETB","recovery_falling")
Desc.add_arc("GATE","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_param("area",23.976000);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtp_2"]=Desc
Desc = cellDescClass("scs130ms_dlrtp_4")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "dlrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'RESETB', 'next']
Desc.add_arc("GATE","RESETB","recovery_falling")
Desc.add_arc("GATE","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_param("area",30.369600);
Desc.add_pin("RESETB","input")
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D","clear": "!RESETB" }
cellLib["scs130ms_dlrtp_4"]=Desc
Desc = cellDescClass("scs130ms_dlxbn_1")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dlxbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATEN","QN","falling_edge")
Desc.add_param("area",27.172800);
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D" }
cellLib["scs130ms_dlxbn_1"]=Desc
Desc = cellDescClass("scs130ms_dlxbn_2")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "dlxbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATEN","QN","falling_edge")
Desc.add_param("area",30.369600);
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D" }
cellLib["scs130ms_dlxbn_2"]=Desc
Desc = cellDescClass("scs130ms_dlxbp_1")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dlxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GATE","QN","rising_edge")
Desc.add_param("area",27.172800);
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D" }
cellLib["scs130ms_dlxbp_1"]=Desc
Desc = cellDescClass("scs130ms_dlxtn_1")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "dlxtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",22.377600);
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D" }
cellLib["scs130ms_dlxtn_1"]=Desc
Desc = cellDescClass("scs130ms_dlxtn_2")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "dlxtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",23.976000);
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D" }
cellLib["scs130ms_dlxtn_2"]=Desc
Desc = cellDescClass("scs130ms_dlxtn_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "dlxtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATEN', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("GATEN","D","setup_rising")
Desc.add_arc("GATEN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATEN","Q","falling_edge")
Desc.add_param("area",27.172800);
Desc.add_pin("D","input")
Desc.set_pin_job("GATEN","clock")
Desc.add_pin("GATEN","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "!GATEN","data_in": "D" }
cellLib["scs130ms_dlxtn_4"]=Desc
Desc = cellDescClass("scs130ms_dlxtp_1")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "dlxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['D', 'GATE', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("GATE","D","setup_falling")
Desc.add_arc("GATE","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GATE","Q","rising_edge")
Desc.add_param("area",25.574400);
Desc.add_pin("D","input")
Desc.set_pin_job("GATE","clock")
Desc.add_pin("GATE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("latch")
Desc.function = { "regs":"IQ IQN" ,"enable": "GATE","data_in": "D" }
cellLib["scs130ms_dlxtp_1"]=Desc
Desc = cellDescClass("scs130ms_dlygate4sd1_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "dlygate4sd"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlygate4sd1_1"]=Desc
Desc = cellDescClass("scs130ms_dlygate4sd2_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "dlygate4sd"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlygate4sd2_1"]=Desc
Desc = cellDescClass("scs130ms_dlygate4sd3_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "dlygate4sd"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlygate4sd3_1"]=Desc
Desc = cellDescClass("scs130ms_dlymetal6s2s_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "delay"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlymetal6s2s_1"]=Desc
Desc = cellDescClass("scs130ms_dlymetal6s4s_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "delay"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlymetal6s4s_1"]=Desc
Desc = cellDescClass("scs130ms_dlymetal6s6s_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "delay"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'X']
Desc.add_arc("A","X","combi")
Desc.set_job("buf") # (A)
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A")
Desc.add_pin("A","input")
cellLib["scs130ms_dlymetal6s6s_1"]=Desc
Desc = cellDescClass("scs130ms_ebufn_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "ebufn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",12.787200);
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","A")
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
cellLib["scs130ms_ebufn_1"]=Desc
Desc = cellDescClass("scs130ms_ebufn_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "ebufn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",14.385600);
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","A")
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
cellLib["scs130ms_ebufn_2"]=Desc
Desc = cellDescClass("scs130ms_ebufn_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "ebufn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",19.180800);
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","A")
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
cellLib["scs130ms_ebufn_4"]=Desc
Desc = cellDescClass("scs130ms_ebufn_8")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "ebufn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",35.164800);
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","A")
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
cellLib["scs130ms_ebufn_8"]=Desc
Desc = cellDescClass("scs130ms_edfxbp_1")
Desc.properties["area"] = "47.952000"
Desc.properties["cell_footprint"] = "edfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_param("area",47.952000);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE) | (IQ&!DE)" }
cellLib["scs130ms_edfxbp_1"]=Desc
Desc = cellDescClass("scs130ms_edfxtp_1")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "edfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_param("area",43.156800);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE) | (IQ&!DE)" }
cellLib["scs130ms_edfxtp_1"]=Desc
Desc = cellDescClass("scs130ms_einvn_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "einvn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",7.992000);
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvn_1"]=Desc
Desc = cellDescClass("scs130ms_einvn_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "einvn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",11.188800);
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvn_2"]=Desc
Desc = cellDescClass("scs130ms_einvn_4")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "einvn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",17.582400);
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvn_4"]=Desc
Desc = cellDescClass("scs130ms_einvn_8")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "einvn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TEB', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TEB","Z","three_state_enable")
Desc.add_arc("TEB","Z","three_state_disable")
Desc.add_param("area",30.369600);
Desc.add_pin("A","input")
Desc.add_pin("TEB","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvn_8"]=Desc
Desc = cellDescClass("scs130ms_einvp_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "einvp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TE', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TE","Z","three_state_enable")
Desc.add_arc("TE","Z","three_state_disable")
Desc.add_param("area",7.992000);
Desc.add_pin("A","input")
Desc.add_pin("TE","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvp_1"]=Desc
Desc = cellDescClass("scs130ms_einvp_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "einvp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TE', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TE","Z","three_state_enable")
Desc.add_arc("TE","Z","three_state_disable")
Desc.add_param("area",11.188800);
Desc.add_pin("A","input")
Desc.add_pin("TE","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvp_2"]=Desc
Desc = cellDescClass("scs130ms_einvp_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "einvp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TE', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TE","Z","three_state_enable")
Desc.add_arc("TE","Z","three_state_disable")
Desc.add_param("area",19.180800);
Desc.add_pin("A","input")
Desc.add_pin("TE","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvp_4"]=Desc
Desc = cellDescClass("scs130ms_einvp_8")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "einvp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'TE', 'Z']
Desc.add_arc("A","Z","combi")
Desc.add_arc("TE","Z","three_state_enable")
Desc.add_arc("TE","Z","three_state_disable")
Desc.add_param("area",30.369600);
Desc.add_pin("A","input")
Desc.add_pin("TE","input")
Desc.add_pin("Z","output")
Desc.add_pin_func("Z","! A")
cellLib["scs130ms_einvp_8"]=Desc
Desc = cellDescClass("scs130ms_fa_1")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "fa"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CIN', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CIN","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CIN","SUM","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CIN ) || ( B && CIN )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CIN ) ) || ( ( ! A ) && B && ( ! CIN ) ) || ( ( ! A ) && ( ! B ) && CIN ) || ( A && B && CIN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CIN","input")
cellLib["scs130ms_fa_1"]=Desc
Desc = cellDescClass("scs130ms_fa_2")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "fa"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CIN', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CIN","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CIN","SUM","combi")
Desc.add_param("area",30.369600);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CIN ) || ( B && CIN )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CIN ) ) || ( ( ! A ) && B && ( ! CIN ) ) || ( ( ! A ) && ( ! B ) && CIN ) || ( A && B && CIN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CIN","input")
cellLib["scs130ms_fa_2"]=Desc
Desc = cellDescClass("scs130ms_fa_4")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "fa"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CIN', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CIN","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CIN","SUM","combi")
Desc.add_param("area",36.763200);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CIN ) || ( B && CIN )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CIN ) ) || ( ( ! A ) && B && ( ! CIN ) ) || ( ( ! A ) && ( ! B ) && CIN ) || ( A && B && CIN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CIN","input")
cellLib["scs130ms_fa_4"]=Desc
Desc = cellDescClass("scs130ms_fah_1")
Desc.properties["area"] = "46.353600"
Desc.properties["cell_footprint"] = "fah"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CI', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CI","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CI","SUM","combi")
Desc.add_param("area",46.353600);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CI ) || ( B && CI )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CI ) ) || ( ( ! A ) && B && ( ! CI ) ) || ( ( ! A ) && ( ! B ) && CI ) || ( A && B && CI )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
cellLib["scs130ms_fah_1"]=Desc
Desc = cellDescClass("scs130ms_fah_2")
Desc.properties["area"] = "47.952000"
Desc.properties["cell_footprint"] = "fah"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CI', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CI","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CI","SUM","combi")
Desc.add_param("area",47.952000);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CI ) || ( B && CI )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CI ) ) || ( ( ! A ) && B && ( ! CI ) ) || ( ( ! A ) && ( ! B ) && CI ) || ( A && B && CI )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
cellLib["scs130ms_fah_2"]=Desc
Desc = cellDescClass("scs130ms_fah_4")
Desc.properties["area"] = "51.148800"
Desc.properties["cell_footprint"] = "fah"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CI', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CI","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CI","SUM","combi")
Desc.add_param("area",51.148800);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && B ) || ( A && CI ) || ( B && CI )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CI ) ) || ( ( ! A ) && B && ( ! CI ) ) || ( ( ! A ) && ( ! B ) && CI ) || ( A && B && CI )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
cellLib["scs130ms_fah_4"]=Desc
Desc = cellDescClass("scs130ms_fahcin_1")
Desc.properties["area"] = "43.156800"
Desc.properties["cell_footprint"] = "fahcin"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CIN', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("CIN","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CIN","SUM","combi")
Desc.add_param("area",43.156800);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","( A && ( ! CIN ) ) || ( A && B ) || ( B && ( ! CIN ) )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( ( ! A ) && ( ! B ) && ( ! CIN ) ) || ( A && B && ( ! CIN ) ) || ( A && ( ! B ) && CIN ) || ( ( ! A ) && B && CIN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CIN","input")
cellLib["scs130ms_fahcin_1"]=Desc
Desc = cellDescClass("scs130ms_fahcon_1")
Desc.properties["area"] = "38.361600"
Desc.properties["cell_footprint"] = "fahcon"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CI', 'COUTN', 'SUM']
Desc.add_arc("A","COUTN","combi")
Desc.add_arc("B","COUTN","combi")
Desc.add_arc("CI","COUTN","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_arc("CI","SUM","combi")
Desc.add_param("area",38.361600);
Desc.add_pin("COUTN","output")
Desc.add_pin_func("COUTN","( ( ! A ) && ( ! CI ) ) || ( ( ! A ) && ( ! B ) ) || ( ( ! B ) && ( ! CI ) )")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) && ( ! CI ) ) || ( ( ! A ) && B && ( ! CI ) ) || ( ( ! A ) && ( ! B ) && CI ) || ( A && B && CI )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CI","input")
cellLib["scs130ms_fahcon_1"]=Desc
Desc = cellDescClass("scs130ms_ha_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "ha"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","A && B")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_ha_1"]=Desc
Desc = cellDescClass("scs130ms_ha_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "ha"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","A && B")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_ha_2"]=Desc
Desc = cellDescClass("scs130ms_ha_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "ha"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'COUT', 'SUM']
Desc.add_arc("A","COUT","combi")
Desc.add_arc("B","COUT","combi")
Desc.add_arc("A","SUM","combi")
Desc.add_arc("B","SUM","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("COUT","output")
Desc.add_pin_func("COUT","A && B")
Desc.add_pin("SUM","output")
Desc.add_pin_func("SUM","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_ha_4"]=Desc
Desc = cellDescClass("scs130ms_inv_1")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",4.795200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_inv_1"]=Desc
Desc = cellDescClass("scs130ms_inv_16")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_inv_16"]=Desc
Desc = cellDescClass("scs130ms_inv_2")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",4.795200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_inv_2"]=Desc
Desc = cellDescClass("scs130ms_inv_4")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_inv_4"]=Desc
Desc = cellDescClass("scs130ms_inv_8")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","! A")
Desc.add_pin("A","input")
cellLib["scs130ms_inv_8"]=Desc
Desc = cellDescClass("scs130ms_maj3_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "maj3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && B ) || ( A && C ) || ( B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_maj3_1"]=Desc
Desc = cellDescClass("scs130ms_maj3_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "maj3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && B ) || ( A && C ) || ( B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_maj3_2"]=Desc
Desc = cellDescClass("scs130ms_maj3_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "maj3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && B ) || ( A && C ) || ( B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_maj3_4"]=Desc
Desc = cellDescClass("scs130ms_mux2_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("S","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S ) ) || ( A1 && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2_1"]=Desc
Desc = cellDescClass("scs130ms_mux2_2")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("S","X","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S ) ) || ( A1 && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2_2"]=Desc
Desc = cellDescClass("scs130ms_mux2_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("S","X","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S ) ) || ( A1 && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2_4"]=Desc
Desc = cellDescClass("scs130ms_mux2i_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "mux2i"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("S","Y","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A0 ) && ( ! S ) ) || ( ( ! A1 ) && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2i_1"]=Desc
Desc = cellDescClass("scs130ms_mux2i_2")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "mux2i"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("S","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A0 ) && ( ! S ) ) || ( ( ! A1 ) && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2i_2"]=Desc
Desc = cellDescClass("scs130ms_mux2i_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "mux2i"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'S', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("S","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A0 ) && ( ! S ) ) || ( ( ! A1 ) && S )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("S","input")
cellLib["scs130ms_mux2i_4"]=Desc
Desc = cellDescClass("scs130ms_mux4_1")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'A2', 'A3', 'S0', 'S1', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("S0","X","combi")
Desc.add_arc("S1","X","combi")
Desc.add_param("area",31.968000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S0 ) && ( ! S1 ) ) || ( A1 && S0 && ( ! S1 ) ) || ( A2 && ( ! S0 ) && S1 ) || ( A3 && S0 && S1 )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("S0","input")
Desc.add_pin("S1","input")
cellLib["scs130ms_mux4_1"]=Desc
Desc = cellDescClass("scs130ms_mux4_2")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'A2', 'A3', 'S0', 'S1', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("S0","X","combi")
Desc.add_arc("S1","X","combi")
Desc.add_param("area",35.164800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S0 ) && ( ! S1 ) ) || ( A1 && S0 && ( ! S1 ) ) || ( A2 && ( ! S0 ) && S1 ) || ( A3 && S0 && S1 )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("S0","input")
Desc.add_pin("S1","input")
cellLib["scs130ms_mux4_2"]=Desc
Desc = cellDescClass("scs130ms_mux4_4")
Desc.properties["area"] = "55.944000"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A0', 'A1', 'A2', 'A3', 'S0', 'S1', 'X']
Desc.add_arc("A0","X","combi")
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("S0","X","combi")
Desc.add_arc("S1","X","combi")
Desc.add_param("area",55.944000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A0 && ( ! S0 ) && ( ! S1 ) ) || ( A1 && S0 && ( ! S1 ) ) || ( A2 && ( ! S0 ) && S1 ) || ( A3 && S0 && S1 )")
Desc.add_pin("A0","input")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("S0","input")
Desc.add_pin("S1","input")
cellLib["scs130ms_mux4_4"]=Desc
Desc = cellDescClass("scs130ms_nand2_1")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",4.795200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2_1"]=Desc
Desc = cellDescClass("scs130ms_nand2_2")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2_2"]=Desc
Desc = cellDescClass("scs130ms_nand2_4")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2_4"]=Desc
Desc = cellDescClass("scs130ms_nand2_8")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2_8"]=Desc
Desc = cellDescClass("scs130ms_nand2b_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2b_1"]=Desc
Desc = cellDescClass("scs130ms_nand2b_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2b_2"]=Desc
Desc = cellDescClass("scs130ms_nand2b_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nand2b_4"]=Desc
Desc = cellDescClass("scs130ms_nand3_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3_1"]=Desc
Desc = cellDescClass("scs130ms_nand3_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3_2"]=Desc
Desc = cellDescClass("scs130ms_nand3_4")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3_4"]=Desc
Desc = cellDescClass("scs130ms_nand3b_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3b_1"]=Desc
Desc = cellDescClass("scs130ms_nand3b_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3b_2"]=Desc
Desc = cellDescClass("scs130ms_nand3b_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nand3b_4"]=Desc
Desc = cellDescClass("scs130ms_nand4_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4_1"]=Desc
Desc = cellDescClass("scs130ms_nand4_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4_2"]=Desc
Desc = cellDescClass("scs130ms_nand4_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4_4"]=Desc
Desc = cellDescClass("scs130ms_nand4b_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4b_1"]=Desc
Desc = cellDescClass("scs130ms_nand4b_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4b_2"]=Desc
Desc = cellDescClass("scs130ms_nand4b_4")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",30.369600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || ( ! B ) || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4b_4"]=Desc
Desc = cellDescClass("scs130ms_nand4bb_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || BN || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4bb_1"]=Desc
Desc = cellDescClass("scs130ms_nand4bb_2")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || BN || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4bb_2"]=Desc
Desc = cellDescClass("scs130ms_nand4bb_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","AN || BN || ( ! C ) || ( ! D )")
Desc.add_pin("AN","input")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nand4bb_4"]=Desc
Desc = cellDescClass("scs130ms_nor2_1")
Desc.properties["area"] = "4.795200"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",4.795200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nor2_1"]=Desc
Desc = cellDescClass("scs130ms_nor2_2")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nor2_2"]=Desc
Desc = cellDescClass("scs130ms_nor2_4")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nor2_4"]=Desc
Desc = cellDescClass("scs130ms_nor2_8")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_nor2_8"]=Desc
Desc = cellDescClass("scs130ms_nor2b_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && BN")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_nor2b_1"]=Desc
Desc = cellDescClass("scs130ms_nor2b_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && BN")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_nor2b_2"]=Desc
Desc = cellDescClass("scs130ms_nor2b_4")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && BN")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_nor2b_4"]=Desc
Desc = cellDescClass("scs130ms_nor3_1")
Desc.properties["area"] = "6.393600"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",6.393600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nor3_1"]=Desc
Desc = cellDescClass("scs130ms_nor3_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nor3_2"]=Desc
Desc = cellDescClass("scs130ms_nor3_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_nor3_4"]=Desc
Desc = cellDescClass("scs130ms_nor3b_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_nor3b_1"]=Desc
Desc = cellDescClass("scs130ms_nor3b_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_nor3b_2"]=Desc
Desc = cellDescClass("scs130ms_nor3b_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_nor3b_4"]=Desc
Desc = cellDescClass("scs130ms_nor4_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nor4_1"]=Desc
Desc = cellDescClass("scs130ms_nor4_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nor4_2"]=Desc
Desc = cellDescClass("scs130ms_nor4_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && ( ! D )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_nor4_4"]=Desc
Desc = cellDescClass("scs130ms_nor4b_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4b_1"]=Desc
Desc = cellDescClass("scs130ms_nor4b_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4b_2"]=Desc
Desc = cellDescClass("scs130ms_nor4b_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && ( ! C ) && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4b_4"]=Desc
Desc = cellDescClass("scs130ms_nor4bb_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4bb_1"]=Desc
Desc = cellDescClass("scs130ms_nor4bb_2")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4bb_2"]=Desc
Desc = cellDescClass("scs130ms_nor4bb_4")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("CN","Y","combi")
Desc.add_arc("DN","Y","combi")
Desc.add_param("area",36.763200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ! A ) && ( ! B ) && CN && DN")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_nor4bb_4"]=Desc
Desc = cellDescClass("scs130ms_o2111a_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o2111a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 && D1 ) || ( A2 && B1 && C1 && D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111a_1"]=Desc
Desc = cellDescClass("scs130ms_o2111a_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o2111a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 && D1 ) || ( A2 && B1 && C1 && D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111a_2"]=Desc
Desc = cellDescClass("scs130ms_o2111a_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "o2111a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_arc("D1","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 && D1 ) || ( A2 && B1 && C1 && D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111a_4"]=Desc
Desc = cellDescClass("scs130ms_o2111ai_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o2111ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 ) || ( ! D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111ai_1"]=Desc
Desc = cellDescClass("scs130ms_o2111ai_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o2111ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 ) || ( ! D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111ai_2"]=Desc
Desc = cellDescClass("scs130ms_o2111ai_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "o2111ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'D1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_arc("D1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 ) || ( ! D1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
Desc.add_pin("D1","input")
cellLib["scs130ms_o2111ai_4"]=Desc
Desc = cellDescClass("scs130ms_o211a_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o211a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211a_1"]=Desc
Desc = cellDescClass("scs130ms_o211a_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o211a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211a_2"]=Desc
Desc = cellDescClass("scs130ms_o211a_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "o211a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211a_4"]=Desc
Desc = cellDescClass("scs130ms_o211ai_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "o211ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211ai_1"]=Desc
Desc = cellDescClass("scs130ms_o211ai_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o211ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211ai_2"]=Desc
Desc = cellDescClass("scs130ms_o211ai_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "o211ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o211ai_4"]=Desc
Desc = cellDescClass("scs130ms_o21a_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "o21a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21a_1"]=Desc
Desc = cellDescClass("scs130ms_o21a_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o21a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21a_2"]=Desc
Desc = cellDescClass("scs130ms_o21a_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o21a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21a_4"]=Desc
Desc = cellDescClass("scs130ms_o21ai_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "o21ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21ai_1"]=Desc
Desc = cellDescClass("scs130ms_o21ai_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o21ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21ai_2"]=Desc
Desc = cellDescClass("scs130ms_o21ai_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o21ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o21ai_4"]=Desc
Desc = cellDescClass("scs130ms_o21ba_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o21ba"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && ( ! B1N ) ) || ( A2 && ( ! B1N ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21ba_1"]=Desc
Desc = cellDescClass("scs130ms_o21ba_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o21ba"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && ( ! B1N ) ) || ( A2 && ( ! B1N ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21ba_2"]=Desc
Desc = cellDescClass("scs130ms_o21ba_4")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "o21ba"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1N","X","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && ( ! B1N ) ) || ( A2 && ( ! B1N ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21ba_4"]=Desc
Desc = cellDescClass("scs130ms_o21bai_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "o21bai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || B1N")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21bai_1"]=Desc
Desc = cellDescClass("scs130ms_o21bai_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o21bai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || B1N")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21bai_2"]=Desc
Desc = cellDescClass("scs130ms_o21bai_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "o21bai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1N', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1N","Y","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) ) || B1N")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1N","input")
cellLib["scs130ms_o21bai_4"]=Desc
Desc = cellDescClass("scs130ms_o221a_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o221a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A1 && B2 && C1 ) || ( A2 && B2 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221a_1"]=Desc
Desc = cellDescClass("scs130ms_o221a_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o221a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A1 && B2 && C1 ) || ( A2 && B2 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221a_2"]=Desc
Desc = cellDescClass("scs130ms_o221a_4")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "o221a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",25.574400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A1 && B2 && C1 ) || ( A2 && B2 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221a_4"]=Desc
Desc = cellDescClass("scs130ms_o221ai_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o221ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221ai_1"]=Desc
Desc = cellDescClass("scs130ms_o221ai_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o221ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221ai_2"]=Desc
Desc = cellDescClass("scs130ms_o221ai_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "o221ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o221ai_4"]=Desc
Desc = cellDescClass("scs130ms_o22a_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o22a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A1 && B2 ) || ( A2 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22a_1"]=Desc
Desc = cellDescClass("scs130ms_o22a_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o22a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A1 && B2 ) || ( A2 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22a_2"]=Desc
Desc = cellDescClass("scs130ms_o22a_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "o22a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A1 && B2 ) || ( A2 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22a_4"]=Desc
Desc = cellDescClass("scs130ms_o22ai_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "o22ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22ai_1"]=Desc
Desc = cellDescClass("scs130ms_o22ai_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o22ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22ai_2"]=Desc
Desc = cellDescClass("scs130ms_o22ai_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "o22ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( ( ! A1 ) && ( ! A2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o22ai_4"]=Desc
Desc = cellDescClass("scs130ms_o2bb2a_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o2bb2a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A1N ) && B1 ) || ( ( ! A2N ) && B1 ) || ( ( ! A1N ) && B2 ) || ( ( ! A2N ) && B2 )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2a_1"]=Desc
Desc = cellDescClass("scs130ms_o2bb2a_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o2bb2a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A1N ) && B1 ) || ( ( ! A2N ) && B1 ) || ( ( ! A1N ) && B2 ) || ( ( ! A2N ) && B2 )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2a_2"]=Desc
Desc = cellDescClass("scs130ms_o2bb2a_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "o2bb2a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'X']
Desc.add_arc("A1N","X","combi")
Desc.add_arc("A2N","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A1N ) && B1 ) || ( ( ! A2N ) && B1 ) || ( ( ! A1N ) && B2 ) || ( ( ! A2N ) && B2 )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2a_4"]=Desc
Desc = cellDescClass("scs130ms_o2bb2ai_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o2bb2ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( A1N && A2N )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2ai_1"]=Desc
Desc = cellDescClass("scs130ms_o2bb2ai_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o2bb2ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( A1N && A2N )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2ai_2"]=Desc
Desc = cellDescClass("scs130ms_o2bb2ai_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "o2bb2ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1N', 'A2N', 'B1', 'B2', 'Y']
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("A2N","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! B1 ) && ( ! B2 ) ) || ( A1N && A2N )")
Desc.add_pin("A1N","input")
Desc.add_pin("A2N","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o2bb2ai_4"]=Desc
Desc = cellDescClass("scs130ms_o311a_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o311a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A3 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311a_1"]=Desc
Desc = cellDescClass("scs130ms_o311a_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o311a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A3 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311a_2"]=Desc
Desc = cellDescClass("scs130ms_o311a_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "o311a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("C1","X","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 && C1 ) || ( A2 && B1 && C1 ) || ( A3 && B1 && C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311a_4"]=Desc
Desc = cellDescClass("scs130ms_o311ai_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o311ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311ai_1"]=Desc
Desc = cellDescClass("scs130ms_o311ai_2")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "o311ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311ai_2"]=Desc
Desc = cellDescClass("scs130ms_o311ai_4")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "o311ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'C1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",36.763200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 ) || ( ! C1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("C1","input")
cellLib["scs130ms_o311ai_4"]=Desc
Desc = cellDescClass("scs130ms_o31a_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o31a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31a_1"]=Desc
Desc = cellDescClass("scs130ms_o31a_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o31a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31a_2"]=Desc
Desc = cellDescClass("scs130ms_o31a_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "o31a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31a_4"]=Desc
Desc = cellDescClass("scs130ms_o31ai_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "o31ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31ai_1"]=Desc
Desc = cellDescClass("scs130ms_o31ai_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o31ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31ai_2"]=Desc
Desc = cellDescClass("scs130ms_o31ai_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "o31ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o31ai_4"]=Desc
Desc = cellDescClass("scs130ms_o32a_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "o32a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A1 && B2 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A2 && B2 ) || ( A3 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32a_1"]=Desc
Desc = cellDescClass("scs130ms_o32a_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o32a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A1 && B2 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A2 && B2 ) || ( A3 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32a_2"]=Desc
Desc = cellDescClass("scs130ms_o32a_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "o32a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_arc("B2","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A1 && B2 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A2 && B2 ) || ( A3 && B2 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32a_4"]=Desc
Desc = cellDescClass("scs130ms_o32ai_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o32ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ( ! B1 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32ai_1"]=Desc
Desc = cellDescClass("scs130ms_o32ai_2")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "o32ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ( ! B1 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32ai_2"]=Desc
Desc = cellDescClass("scs130ms_o32ai_4")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "o32ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'B1', 'B2', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",36.763200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) ) || ( ( ! B1 ) && ( ! B2 ) )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
cellLib["scs130ms_o32ai_4"]=Desc
Desc = cellDescClass("scs130ms_o41a_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "o41a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A4 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41a_1"]=Desc
Desc = cellDescClass("scs130ms_o41a_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "o41a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A4 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41a_2"]=Desc
Desc = cellDescClass("scs130ms_o41a_4")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "o41a"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'X']
Desc.add_arc("A1","X","combi")
Desc.add_arc("A2","X","combi")
Desc.add_arc("A3","X","combi")
Desc.add_arc("A4","X","combi")
Desc.add_arc("B1","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A1 && B1 ) || ( A2 && B1 ) || ( A3 && B1 ) || ( A4 && B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41a_4"]=Desc
Desc = cellDescClass("scs130ms_o41ai_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "o41ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) && ( ! A4 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41ai_1"]=Desc
Desc = cellDescClass("scs130ms_o41ai_2")
Desc.properties["area"] = "20.779200"
Desc.properties["cell_footprint"] = "o41ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",20.779200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) && ( ! A4 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41ai_2"]=Desc
Desc = cellDescClass("scs130ms_o41ai_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "o41ai"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A1', 'A2', 'A3', 'A4', 'B1', 'Y']
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("A3","Y","combi")
Desc.add_arc("A4","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A1 ) && ( ! A2 ) && ( ! A3 ) && ( ! A4 ) ) || ( ! B1 )")
Desc.add_pin("A1","input")
Desc.add_pin("A2","input")
Desc.add_pin("A3","input")
Desc.add_pin("A4","input")
Desc.add_pin("B1","input")
cellLib["scs130ms_o41ai_4"]=Desc
Desc = cellDescClass("scs130ms_or2_1")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_or2_1"]=Desc
Desc = cellDescClass("scs130ms_or2_2")
Desc.properties["area"] = "7.992000"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",7.992000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_or2_2"]=Desc
Desc = cellDescClass("scs130ms_or2_4")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_or2_4"]=Desc
Desc = cellDescClass("scs130ms_or2b_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "or2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || ( ! BN )")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_or2b_1"]=Desc
Desc = cellDescClass("scs130ms_or2b_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "or2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || ( ! BN )")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_or2b_2"]=Desc
Desc = cellDescClass("scs130ms_or2b_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "or2b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'BN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("BN","X","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || ( ! BN )")
Desc.add_pin("A","input")
Desc.add_pin("BN","input")
cellLib["scs130ms_or2b_4"]=Desc
Desc = cellDescClass("scs130ms_or3_1")
Desc.properties["area"] = "9.590400"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",9.590400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_or3_1"]=Desc
Desc = cellDescClass("scs130ms_or3_2")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_or3_2"]=Desc
Desc = cellDescClass("scs130ms_or3_4")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_or3_4"]=Desc
Desc = cellDescClass("scs130ms_or3b_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "or3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_or3b_1"]=Desc
Desc = cellDescClass("scs130ms_or3b_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "or3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_or3b_2"]=Desc
Desc = cellDescClass("scs130ms_or3b_4")
Desc.properties["area"] = "19.180800"
Desc.properties["cell_footprint"] = "or3b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_param("area",19.180800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
cellLib["scs130ms_or3b_4"]=Desc
Desc = cellDescClass("scs130ms_or4_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_or4_1"]=Desc
Desc = cellDescClass("scs130ms_or4_2")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_or4_2"]=Desc
Desc = cellDescClass("scs130ms_or4_4")
Desc.properties["area"] = "22.377600"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("D","X","combi")
Desc.add_param("area",22.377600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || D")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
cellLib["scs130ms_or4_4"]=Desc
Desc = cellDescClass("scs130ms_or4b_1")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "or4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4b_1"]=Desc
Desc = cellDescClass("scs130ms_or4b_2")
Desc.properties["area"] = "14.385600"
Desc.properties["cell_footprint"] = "or4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",14.385600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4b_2"]=Desc
Desc = cellDescClass("scs130ms_or4b_4")
Desc.properties["area"] = "23.976000"
Desc.properties["cell_footprint"] = "or4b"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",23.976000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || C || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4b_4"]=Desc
Desc = cellDescClass("scs130ms_or4bb_1")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "or4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN ) || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4bb_1"]=Desc
Desc = cellDescClass("scs130ms_or4bb_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "or4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN ) || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4bb_2"]=Desc
Desc = cellDescClass("scs130ms_or4bb_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "or4bb"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'CN', 'DN', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("CN","X","combi")
Desc.add_arc("DN","X","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","A || B || ( ! CN ) || ( ! DN )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("CN","input")
Desc.add_pin("DN","input")
cellLib["scs130ms_or4bb_4"]=Desc
Desc = cellDescClass("scs130ms_sdfbbn_1")
Desc.properties["area"] = "55.944000"
Desc.properties["cell_footprint"] = "sdfbbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLKN","SETB","recovery_falling")
Desc.add_arc("CLKN","SETB","removal_falling")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("CLKN","SCD","setup_falling")
Desc.add_arc("CLKN","SCD","hold_falling")
Desc.add_arc("CLKN","SCE","setup_falling")
Desc.add_arc("CLKN","SCE","hold_falling")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLKN","QN","falling_edge")
Desc.add_param("area",55.944000);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_sdfbbn_1"]=Desc
Desc = cellDescClass("scs130ms_sdfbbn_2")
Desc.properties["area"] = "60.739200"
Desc.properties["cell_footprint"] = "sdfbbn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLKN","SETB","recovery_falling")
Desc.add_arc("CLKN","SETB","removal_falling")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("CLKN","SCD","setup_falling")
Desc.add_arc("CLKN","SCD","hold_falling")
Desc.add_arc("CLKN","SCE","setup_falling")
Desc.add_arc("CLKN","SCE","hold_falling")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLKN","QN","falling_edge")
Desc.add_param("area",60.739200);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_sdfbbn_2"]=Desc
Desc = cellDescClass("scs130ms_sdfbbp_1")
Desc.properties["area"] = "52.747200"
Desc.properties["cell_footprint"] = "sdfbbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_param("area",52.747200);
Desc.add_pin("SETB","input")
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB","preset": "!SETB","clear_preset_var1": "H","clear_preset_var2": "L" }
cellLib["scs130ms_sdfbbp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfrbp_1")
Desc.properties["area"] = "46.353600"
Desc.properties["cell_footprint"] = "sdfrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",46.353600);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrbp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfrbp_2")
Desc.properties["area"] = "49.550400"
Desc.properties["cell_footprint"] = "sdfrbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("RESETB","QN","preset")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",49.550400);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrbp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfrtn_1")
Desc.properties["area"] = "46.353600"
Desc.properties["cell_footprint"] = "sdfrtn"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLKN', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLKN","RESETB","recovery_falling")
Desc.add_arc("CLKN","RESETB","removal_falling")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLKN","D","setup_falling")
Desc.add_arc("CLKN","D","hold_falling")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLKN","Q","falling_edge")
Desc.add_arc("CLKN","SCD","setup_falling")
Desc.add_arc("CLKN","SCD","hold_falling")
Desc.add_arc("CLKN","SCE","setup_falling")
Desc.add_arc("CLKN","SCE","hold_falling")
Desc.add_param("area",46.353600);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLKN","clock")
Desc.add_pin("CLKN","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "!CLKN","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrtn_1"]=Desc
Desc = cellDescClass("scs130ms_sdfrtp_1")
Desc.properties["area"] = "44.755200"
Desc.properties["cell_footprint"] = "sdfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",44.755200);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrtp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfrtp_2")
Desc.properties["area"] = "47.952000"
Desc.properties["cell_footprint"] = "sdfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",47.952000);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrtp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfrtp_4")
Desc.properties["area"] = "49.550400"
Desc.properties["cell_footprint"] = "sdfrtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'RESETB', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","RESETB","recovery_rising")
Desc.add_arc("CLK","RESETB","removal_rising")
Desc.add_arc("RESETB","RESETB","min_pulse_width")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("RESETB","Q","clear")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",49.550400);
Desc.add_pin("RESETB","input")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","clear": "!RESETB" }
cellLib["scs130ms_sdfrtp_4"]=Desc
Desc = cellDescClass("scs130ms_sdfsbp_1")
Desc.properties["area"] = "47.952000"
Desc.properties["cell_footprint"] = "sdfsbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",47.952000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","preset": "!SETB" }
cellLib["scs130ms_sdfsbp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfsbp_2")
Desc.properties["area"] = "59.140800"
Desc.properties["cell_footprint"] = "sdfsbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("SETB","QN","clear")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",59.140800);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","preset": "!SETB" }
cellLib["scs130ms_sdfsbp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfstp_1")
Desc.properties["area"] = "46.353600"
Desc.properties["cell_footprint"] = "sdfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",46.353600);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","preset": "!SETB" }
cellLib["scs130ms_sdfstp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfstp_2")
Desc.properties["area"] = "49.550400"
Desc.properties["cell_footprint"] = "sdfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",49.550400);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","preset": "!SETB" }
cellLib["scs130ms_sdfstp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfstp_4")
Desc.properties["area"] = "52.747200"
Desc.properties["cell_footprint"] = "sdfstp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'SETB', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("SETB","Q","preset")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SETB","recovery_rising")
Desc.add_arc("CLK","SETB","removal_rising")
Desc.add_arc("SETB","SETB","min_pulse_width")
Desc.add_param("area",52.747200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SETB","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)","preset": "!SETB" }
cellLib["scs130ms_sdfstp_4"]=Desc
Desc = cellDescClass("scs130ms_sdfxbp_1")
Desc.properties["area"] = "41.558400"
Desc.properties["cell_footprint"] = "sdfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",41.558400);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sdfxbp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfxbp_2")
Desc.properties["area"] = "44.755200"
Desc.properties["cell_footprint"] = "sdfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",44.755200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sdfxbp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfxtp_1")
Desc.properties["area"] = "36.763200"
Desc.properties["cell_footprint"] = "sdfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",36.763200);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sdfxtp_1"]=Desc
Desc = cellDescClass("scs130ms_sdfxtp_2")
Desc.properties["area"] = "39.960000"
Desc.properties["cell_footprint"] = "sdfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",39.960000);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sdfxtp_2"]=Desc
Desc = cellDescClass("scs130ms_sdfxtp_4")
Desc.properties["area"] = "41.558400"
Desc.properties["cell_footprint"] = "sdfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",41.558400);
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("SCD","input")
Desc.add_pin("SCE","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sdfxtp_4"]=Desc
Desc = cellDescClass("scs130ms_sdlclkp_1")
Desc.properties["area"] = "25.574400"
Desc.properties["cell_footprint"] = "sdlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge_precontrol"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'SCE', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",25.574400);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.add_pin("SCE","input")
Desc.set_job("statetable")
# (['CLK GATE SCE', 'm0'], '" L L L : - : L ,\\              L L H : - : H ,\\              L H L : - : H ,\\              L H H : - : H ,\\              H - - : - : N "')
cellLib["scs130ms_sdlclkp_1"]=Desc
Desc = cellDescClass("scs130ms_sdlclkp_2")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "sdlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge_precontrol"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'SCE', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",27.172800);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.add_pin("SCE","input")
Desc.set_job("statetable")
# (['CLK GATE SCE', 'm0'], '" L L L : - : L ,\\              L L H : - : H ,\\              L H L : - : H ,\\              L H H : - : H ,\\              H - - : - : N "')
cellLib["scs130ms_sdlclkp_2"]=Desc
Desc = cellDescClass("scs130ms_sdlclkp_4")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "sdlclkp"
Desc.properties["clock_gating_integrated_cell"] = "latch_posedge_precontrol"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['CLK', 'GATE', 'GCLK', 'SCE', 'm0']
Desc.add_arc("CLK","GCLK","combi")
Desc.add_arc("CLK","GATE","setup_rising")
Desc.add_arc("CLK","GATE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_param("area",31.968000);
Desc.add_pin("GCLK","output")
Desc.add_pin_func("GCLK","unknown")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("GATE","input")
Desc.add_pin("SCE","input")
Desc.set_job("statetable")
# (['CLK GATE SCE', 'm0'], '" L L L : - : L ,\\              L L H : - : H ,\\              L H L : - : H ,\\              L H H : - : H ,\\              H - - : - : N "')
cellLib["scs130ms_sdlclkp_4"]=Desc
Desc = cellDescClass("scs130ms_sedfxbp_1")
Desc.properties["area"] = "54.345600"
Desc.properties["cell_footprint"] = "sedfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_param("area",54.345600);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SCD","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE&!SCE) | (IQ&!DE&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sedfxbp_1"]=Desc
Desc = cellDescClass("scs130ms_sedfxbp_2")
Desc.properties["area"] = "57.542400"
Desc.properties["cell_footprint"] = "sedfxbp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'QN', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","QN","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_param("area",57.542400);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","IQN")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SCD","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE&!SCE) | (IQ&!DE&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sedfxbp_2"]=Desc
Desc = cellDescClass("scs130ms_sedfxtp_1")
Desc.properties["area"] = "51.148800"
Desc.properties["cell_footprint"] = "sedfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_param("area",51.148800);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SCD","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE&!SCE) | (IQ&!DE&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sedfxtp_1"]=Desc
Desc = cellDescClass("scs130ms_sedfxtp_2")
Desc.properties["area"] = "54.345600"
Desc.properties["cell_footprint"] = "sedfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_param("area",54.345600);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SCD","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE&!SCE) | (IQ&!DE&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sedfxtp_2"]=Desc
Desc = cellDescClass("scs130ms_sedfxtp_4")
Desc.properties["area"] = "55.944000"
Desc.properties["cell_footprint"] = "sedfxtp"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.properties["driver_waveform_rise"] = "ramp"
Desc.properties["driver_waveform_fall"] = "ramp"
Desc.pinOrder = ['CLK', 'D', 'DE', 'IQ', 'IQN', 'Q', 'SCD', 'SCE', 'next']
Desc.add_arc("CLK","Q","rising_edge")
Desc.add_arc("CLK","D","setup_rising")
Desc.add_arc("CLK","D","hold_rising")
Desc.add_arc("CLK","DE","setup_rising")
Desc.add_arc("CLK","DE","hold_rising")
Desc.add_arc("CLK","SCE","setup_rising")
Desc.add_arc("CLK","SCE","hold_rising")
Desc.add_arc("CLK","SCD","setup_rising")
Desc.add_arc("CLK","SCD","hold_rising")
Desc.add_param("area",55.944000);
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","IQ")
Desc.set_pin_job("CLK","clock")
Desc.add_pin("CLK","input")
Desc.add_pin("D","input")
Desc.add_pin("DE","input")
Desc.add_pin("SCE","input")
Desc.add_pin("SCD","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.set_job("flipflop")
Desc.function = { "regs":"IQ IQN" ,"clocked_on": "CLK","next_state": "(D&DE&!SCE) | (IQ&!DE&!SCE) | (SCD&SCE)" }
cellLib["scs130ms_sedfxtp_4"]=Desc
Desc = cellDescClass("scs130ms_xnor2_1")
Desc.properties["area"] = "11.188800"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",11.188800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A ) && ( ! B ) ) || ( A && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xnor2_1"]=Desc
Desc = cellDescClass("scs130ms_xnor2_2")
Desc.properties["area"] = "17.582400"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",17.582400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A ) && ( ! B ) ) || ( A && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xnor2_2"]=Desc
Desc = cellDescClass("scs130ms_xnor2_4")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",30.369600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","( ( ! A ) && ( ! B ) ) || ( A && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xnor2_4"]=Desc
Desc = cellDescClass("scs130ms_xnor3_1")
Desc.properties["area"] = "27.172800"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",27.172800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A ) && ( ! B ) && ( ! C ) ) || ( A && B && ( ! C ) ) || ( A && ( ! B ) && C ) || ( ( ! A ) && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xnor3_1"]=Desc
Desc = cellDescClass("scs130ms_xnor3_2")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A ) && ( ! B ) && ( ! C ) ) || ( A && B && ( ! C ) ) || ( A && ( ! B ) && C ) || ( ( ! A ) && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xnor3_2"]=Desc
Desc = cellDescClass("scs130ms_xnor3_4")
Desc.properties["area"] = "33.566400"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",33.566400);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( ( ! A ) && ( ! B ) && ( ! C ) ) || ( A && B && ( ! C ) ) || ( A && ( ! B ) && C ) || ( ( ! A ) && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xnor3_4"]=Desc
Desc = cellDescClass("scs130ms_xor2_1")
Desc.properties["area"] = "12.787200"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",12.787200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xor2_1"]=Desc
Desc = cellDescClass("scs130ms_xor2_2")
Desc.properties["area"] = "15.984000"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",15.984000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xor2_2"]=Desc
Desc = cellDescClass("scs130ms_xor2_4")
Desc.properties["area"] = "28.771200"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_param("area",28.771200);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) ) || ( ( ! A ) && B )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
cellLib["scs130ms_xor2_4"]=Desc
Desc = cellDescClass("scs130ms_xor3_1")
Desc.properties["area"] = "30.369600"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",30.369600);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) && ( ! C ) ) || ( ( ! A ) && B && ( ! C ) ) || ( ( ! A ) && ( ! B ) && C ) || ( A && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xor3_1"]=Desc
Desc = cellDescClass("scs130ms_xor3_2")
Desc.properties["area"] = "31.968000"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",31.968000);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) && ( ! C ) ) || ( ( ! A ) && B && ( ! C ) ) || ( ( ! A ) && ( ! B ) && C ) || ( A && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xor3_2"]=Desc
Desc = cellDescClass("scs130ms_xor3_4")
Desc.properties["area"] = "35.164800"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["cell_leakage_power"] = "0.00"
Desc.pinOrder = ['A', 'B', 'C', 'X']
Desc.add_arc("A","X","combi")
Desc.add_arc("B","X","combi")
Desc.add_arc("C","X","combi")
Desc.add_param("area",35.164800);
Desc.add_pin("X","output")
Desc.add_pin_func("X","( A && ( ! B ) && ( ! C ) ) || ( ( ! A ) && B && ( ! C ) ) || ( ( ! A ) && ( ! B ) && C ) || ( A && B && C )")
Desc.add_pin("A","input")
Desc.add_pin("B","input")
Desc.add_pin("C","input")
cellLib["scs130ms_xor3_4"]=Desc
