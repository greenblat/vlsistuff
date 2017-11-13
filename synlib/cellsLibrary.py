

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
global CellLib
CellLib = {}

Desc = cellDescClass("ADDFHX1")
Desc.properties["cell_leakage_power"] = "4104.182520"
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFHX1"]=Desc
Desc = cellDescClass("ADDFHX2")
Desc.properties["cell_leakage_power"] = "7522.904160"
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "113.097600"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",113.097600);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFHX2"]=Desc
Desc = cellDescClass("ADDFHX4")
Desc.properties["cell_leakage_power"] = "8036.730900"
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",116.424000);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFHX4"]=Desc
Desc = cellDescClass("ADDFHXL")
Desc.properties["cell_leakage_power"] = "3398.980320"
Desc.properties["cell_footprint"] = "addfh"
Desc.properties["area"] = "73.180800"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",73.180800);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFHXL"]=Desc
Desc = cellDescClass("ADDFX1")
Desc.properties["cell_leakage_power"] = "3632.359140"
Desc.properties["cell_footprint"] = "addf"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",69.854400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFX1"]=Desc
Desc = cellDescClass("ADDFX2")
Desc.properties["cell_leakage_power"] = "3917.386800"
Desc.properties["cell_footprint"] = "addf"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",69.854400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFX2"]=Desc
Desc = cellDescClass("ADDFX4")
Desc.properties["cell_leakage_power"] = "4448.850480"
Desc.properties["cell_footprint"] = "addf"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFX4"]=Desc
Desc = cellDescClass("ADDFXL")
Desc.properties["cell_leakage_power"] = "3632.360760"
Desc.properties["cell_footprint"] = "addf"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['A', 'B', 'CI', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CI","CO","combi")
Desc.add_param("area",69.854400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["ADDFXL"]=Desc
Desc = cellDescClass("ADDHX1")
Desc.properties["cell_leakage_power"] = "2576.298960"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHX1"]=Desc
Desc = cellDescClass("ADDHX2")
Desc.properties["cell_leakage_power"] = "5042.266200"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHX2"]=Desc
Desc = cellDescClass("ADDHX4")
Desc.properties["cell_leakage_power"] = "9768.360240"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",93.139200);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHX4"]=Desc
Desc = cellDescClass("ADDHXL")
Desc.properties["cell_leakage_power"] = "1423.696824"
Desc.properties["cell_footprint"] = "addh"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["ADDHXL"]=Desc
Desc = cellDescClass("AFCSHCINX2")
Desc.properties["cell_leakage_power"] = "9757.810800"
Desc.properties["cell_footprint"] = "afcshcin"
Desc.properties["area"] = "166.320000"
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
Desc.add_pin("A","input")
Desc.add_pin("CO0","output")
Desc.add_pin_func("CO0","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO1","output")
Desc.add_pin_func("CO1","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CS","input")
Desc.add_pin("CI1N","input")
Desc.add_pin("CI0N","input")
CellLib["AFCSHCINX2"]=Desc
Desc = cellDescClass("AFCSHCINX4")
Desc.properties["cell_leakage_power"] = "12758.548140"
Desc.properties["cell_footprint"] = "afcshcin"
Desc.properties["area"] = "192.931200"
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
Desc.add_param("area",192.931200);
Desc.add_pin("A","input")
Desc.add_pin("CO0","output")
Desc.add_pin_func("CO0","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO1","output")
Desc.add_pin_func("CO1","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CS","input")
Desc.add_pin("CI1N","input")
Desc.add_pin("CI0N","input")
CellLib["AFCSHCINX4"]=Desc
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
Desc = cellDescClass("AFCSHCONX4")
Desc.properties["cell_leakage_power"] = "14090.486220"
Desc.properties["cell_footprint"] = "afcshcon"
Desc.properties["area"] = "196.257600"
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
Desc.add_param("area",196.257600);
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
CellLib["AFCSHCONX4"]=Desc
Desc = cellDescClass("AFHCINX2")
Desc.properties["cell_leakage_power"] = "6586.184520"
Desc.properties["cell_footprint"] = "afhcin"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['A', 'B', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AFHCINX2"]=Desc
Desc = cellDescClass("AFHCINX4")
Desc.properties["cell_leakage_power"] = "8735.406120"
Desc.properties["cell_footprint"] = "afhcin"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['A', 'B', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",93.139200);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AFHCINX4"]=Desc
Desc = cellDescClass("AFHCONX2")
Desc.properties["cell_leakage_power"] = "6426.297000"
Desc.properties["cell_footprint"] = "afhcon"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['A', 'B', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("B","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AFHCONX2"]=Desc
Desc = cellDescClass("AFHCONX4")
Desc.properties["cell_leakage_power"] = "8363.458980"
Desc.properties["cell_footprint"] = "afhcon"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['A', 'B', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("B","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",86.486400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("B","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AFHCONX4"]=Desc
Desc = cellDescClass("AHHCINX2")
Desc.properties["cell_leakage_power"] = "2082.335040"
Desc.properties["cell_footprint"] = "ahhcin"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AHHCINX2"]=Desc
Desc = cellDescClass("AHHCINX4")
Desc.properties["cell_leakage_power"] = "2275.656120"
Desc.properties["cell_footprint"] = "ahhcin"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A', 'CIN', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CIN","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("CIN","CO","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("CIN","input")
CellLib["AHHCINX4"]=Desc
Desc = cellDescClass("AHHCONX2")
Desc.properties["cell_leakage_power"] = "2114.534160"
Desc.properties["cell_footprint"] = "ahhcon"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'CI', 'CON', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("CI","S","combi")
Desc.add_arc("A","CON","combi")
Desc.add_arc("CI","CON","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("CI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CON","output")
Desc.add_pin_func("CON","unknown")
CellLib["AHHCONX2"]=Desc
Desc = cellDescClass("AHHCONX4")
Desc.properties["cell_leakage_power"] = "2461.991760"
Desc.properties["cell_footprint"] = "ahhcon"
Desc.properties["area"] = "43.243200"
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
Desc = cellDescClass("AND2X1")
Desc.properties["cell_leakage_power"] = "539.275644"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["AND2X1"]=Desc
Desc = cellDescClass("AND2X2")
Desc.properties["cell_leakage_power"] = "661.537530"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["AND2X2"]=Desc
Desc = cellDescClass("AND2X4")
Desc.properties["cell_leakage_power"] = "1266.842268"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["AND2X4"]=Desc
Desc = cellDescClass("AND2XL")
Desc.properties["cell_leakage_power"] = "520.521228"
Desc.properties["cell_footprint"] = "and2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["AND2XL"]=Desc
Desc = cellDescClass("AND3X1")
Desc.properties["cell_leakage_power"] = "540.094392"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["AND3X1"]=Desc
Desc = cellDescClass("AND3X2")
Desc.properties["cell_leakage_power"] = "854.236692"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["AND3X2"]=Desc
Desc = cellDescClass("AND3X4")
Desc.properties["cell_leakage_power"] = "1434.826386"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["AND3X4"]=Desc
Desc = cellDescClass("AND3XL")
Desc.properties["cell_leakage_power"] = "526.488012"
Desc.properties["cell_footprint"] = "and3"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["AND3XL"]=Desc
Desc = cellDescClass("AND4X1")
Desc.properties["cell_leakage_power"] = "606.385278"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["AND4X1"]=Desc
Desc = cellDescClass("AND4X2")
Desc.properties["cell_leakage_power"] = "982.482858"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["AND4X2"]=Desc
Desc = cellDescClass("AND4X4")
Desc.properties["cell_leakage_power"] = "1836.255420"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["AND4X4"]=Desc
Desc = cellDescClass("AND4XL")
Desc.properties["cell_leakage_power"] = "607.591530"
Desc.properties["cell_footprint"] = "and4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["AND4XL"]=Desc
Desc = cellDescClass("AOI211X1")
Desc.properties["cell_leakage_power"] = "381.307338"
Desc.properties["cell_footprint"] = "aoi211"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI211X1"]=Desc
Desc = cellDescClass("AOI211X2")
Desc.properties["cell_leakage_power"] = "732.564486"
Desc.properties["cell_footprint"] = "aoi211"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI211X2"]=Desc
Desc = cellDescClass("AOI211X4")
Desc.properties["cell_leakage_power"] = "1335.085740"
Desc.properties["cell_footprint"] = "aoi211"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI211X4"]=Desc
Desc = cellDescClass("AOI211XL")
Desc.properties["cell_leakage_power"] = "275.382504"
Desc.properties["cell_footprint"] = "aoi211"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI211XL"]=Desc
Desc = cellDescClass("AOI21X1")
Desc.properties["cell_leakage_power"] = "296.979858"
Desc.properties["cell_footprint"] = "aoi21"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI21X1"]=Desc
Desc = cellDescClass("AOI21X2")
Desc.properties["cell_leakage_power"] = "580.491036"
Desc.properties["cell_footprint"] = "aoi21"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI21X2"]=Desc
Desc = cellDescClass("AOI21X4")
Desc.properties["cell_leakage_power"] = "1254.852324"
Desc.properties["cell_footprint"] = "aoi21"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI21X4"]=Desc
Desc = cellDescClass("AOI21XL")
Desc.properties["cell_leakage_power"] = "246.891402"
Desc.properties["cell_footprint"] = "aoi21"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI21XL"]=Desc
Desc = cellDescClass("AOI221X1")
Desc.properties["cell_leakage_power"] = "395.946792"
Desc.properties["cell_footprint"] = "aoi221"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["AOI221X1"]=Desc
Desc = cellDescClass("AOI221X2")
Desc.properties["cell_leakage_power"] = "775.806660"
Desc.properties["cell_footprint"] = "aoi221"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["AOI221X2"]=Desc
Desc = cellDescClass("AOI221X4")
Desc.properties["cell_leakage_power"] = "1344.986370"
Desc.properties["cell_footprint"] = "aoi221"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["AOI221X4"]=Desc
Desc = cellDescClass("AOI221XL")
Desc.properties["cell_leakage_power"] = "313.752528"
Desc.properties["cell_footprint"] = "aoi221"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["AOI221XL"]=Desc
Desc = cellDescClass("AOI222X1")
Desc.properties["cell_leakage_power"] = "419.233482"
Desc.properties["cell_footprint"] = "aoi222"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["AOI222X1"]=Desc
Desc = cellDescClass("AOI222X2")
Desc.properties["cell_leakage_power"] = "822.467358"
Desc.properties["cell_footprint"] = "aoi222"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["AOI222X2"]=Desc
Desc = cellDescClass("AOI222X4")
Desc.properties["cell_leakage_power"] = "1381.973562"
Desc.properties["cell_footprint"] = "aoi222"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["AOI222X4"]=Desc
Desc = cellDescClass("AOI222XL")
Desc.properties["cell_leakage_power"] = "333.204678"
Desc.properties["cell_footprint"] = "aoi222"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["AOI222XL"]=Desc
Desc = cellDescClass("AOI22X1")
Desc.properties["cell_leakage_power"] = "320.389182"
Desc.properties["cell_footprint"] = "aoi22"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI22X1"]=Desc
Desc = cellDescClass("AOI22X2")
Desc.properties["cell_leakage_power"] = "624.589542"
Desc.properties["cell_footprint"] = "aoi22"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI22X2"]=Desc
Desc = cellDescClass("AOI22X4")
Desc.properties["cell_leakage_power"] = "1337.200812"
Desc.properties["cell_footprint"] = "aoi22"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI22X4"]=Desc
Desc = cellDescClass("AOI22XL")
Desc.properties["cell_leakage_power"] = "273.136698"
Desc.properties["cell_footprint"] = "aoi22"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI22XL"]=Desc
Desc = cellDescClass("AOI2BB1X1")
Desc.properties["cell_leakage_power"] = "761.882274"
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["AOI2BB1X1"]=Desc
Desc = cellDescClass("AOI2BB1X2")
Desc.properties["cell_leakage_power"] = "873.050238"
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["AOI2BB1X2"]=Desc
Desc = cellDescClass("AOI2BB1X4")
Desc.properties["cell_leakage_power"] = "1964.988720"
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["AOI2BB1X4"]=Desc
Desc = cellDescClass("AOI2BB1XL")
Desc.properties["cell_leakage_power"] = "731.477142"
Desc.properties["cell_footprint"] = "aoi2bb1"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["AOI2BB1XL"]=Desc
Desc = cellDescClass("AOI2BB2X1")
Desc.properties["cell_leakage_power"] = "740.950902"
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["AOI2BB2X1"]=Desc
Desc = cellDescClass("AOI2BB2X2")
Desc.properties["cell_leakage_power"] = "872.321238"
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["AOI2BB2X2"]=Desc
Desc = cellDescClass("AOI2BB2X4")
Desc.properties["cell_leakage_power"] = "1784.613060"
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "49.896000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",49.896000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["AOI2BB2X4"]=Desc
Desc = cellDescClass("AOI2BB2XL")
Desc.properties["cell_leakage_power"] = "709.103160"
Desc.properties["cell_footprint"] = "aoi2bb2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["AOI2BB2XL"]=Desc
Desc = cellDescClass("AOI31X1")
Desc.properties["cell_leakage_power"] = "419.419134"
Desc.properties["cell_footprint"] = "aoi31"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI31X1"]=Desc
Desc = cellDescClass("AOI31X2")
Desc.properties["cell_leakage_power"] = "839.367036"
Desc.properties["cell_footprint"] = "aoi31"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI31X2"]=Desc
Desc = cellDescClass("AOI31X4")
Desc.properties["cell_leakage_power"] = "1396.936044"
Desc.properties["cell_footprint"] = "aoi31"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI31X4"]=Desc
Desc = cellDescClass("AOI31XL")
Desc.properties["cell_leakage_power"] = "337.425912"
Desc.properties["cell_footprint"] = "aoi31"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI31XL"]=Desc
Desc = cellDescClass("AOI32X1")
Desc.properties["cell_leakage_power"] = "445.354200"
Desc.properties["cell_footprint"] = "aoi32"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI32X1"]=Desc
Desc = cellDescClass("AOI32X2")
Desc.properties["cell_leakage_power"] = "888.949242"
Desc.properties["cell_footprint"] = "aoi32"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI32X2"]=Desc
Desc = cellDescClass("AOI32X4")
Desc.properties["cell_leakage_power"] = "1415.676042"
Desc.properties["cell_footprint"] = "aoi32"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI32X4"]=Desc
Desc = cellDescClass("AOI32XL")
Desc.properties["cell_leakage_power"] = "357.465474"
Desc.properties["cell_footprint"] = "aoi32"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI32XL"]=Desc
Desc = cellDescClass("AOI33X1")
Desc.properties["cell_leakage_power"] = "471.705930"
Desc.properties["cell_footprint"] = "aoi33"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI33X1"]=Desc
Desc = cellDescClass("AOI33X2")
Desc.properties["cell_leakage_power"] = "932.252166"
Desc.properties["cell_footprint"] = "aoi33"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",43.243200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI33X2"]=Desc
Desc = cellDescClass("AOI33X4")
Desc.properties["cell_leakage_power"] = "1441.993590"
Desc.properties["cell_footprint"] = "aoi33"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI33X4"]=Desc
Desc = cellDescClass("AOI33XL")
Desc.properties["cell_leakage_power"] = "378.159840"
Desc.properties["cell_footprint"] = "aoi33"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["AOI33XL"]=Desc
Desc = cellDescClass("BENCX1")
Desc.properties["cell_leakage_power"] = "4067.868600"
Desc.properties["cell_footprint"] = "recsel"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['A', 'M0', 'M1', 'M2', 'S', 'X2']
Desc.add_arc("M2","A","combi")
Desc.add_arc("M1","A","combi")
Desc.add_arc("M0","A","combi")
Desc.add_arc("M2","S","combi")
Desc.add_arc("M1","S","combi")
Desc.add_arc("M0","S","combi")
Desc.add_arc("M1","X2","combi")
Desc.add_arc("M0","X2","combi")
Desc.add_param("area",103.118400);
Desc.add_pin("A","output")
Desc.add_pin_func("A","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("M1","input")
Desc.add_pin("M0","input")
Desc.add_pin("M2","input")
Desc.add_pin("X2","output")
Desc.add_pin_func("X2","unknown")
CellLib["BENCX1"]=Desc
Desc = cellDescClass("BENCX2")
Desc.properties["cell_leakage_power"] = "6959.257560"
Desc.properties["cell_footprint"] = "recsel"
Desc.properties["area"] = "136.382400"
Desc.pinOrder = ['A', 'M0', 'M1', 'M2', 'S', 'X2']
Desc.add_arc("M2","A","combi")
Desc.add_arc("M1","A","combi")
Desc.add_arc("M0","A","combi")
Desc.add_arc("M2","S","combi")
Desc.add_arc("M1","S","combi")
Desc.add_arc("M0","S","combi")
Desc.add_arc("M1","X2","combi")
Desc.add_arc("M0","X2","combi")
Desc.add_param("area",136.382400);
Desc.add_pin("A","output")
Desc.add_pin_func("A","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("M1","input")
Desc.add_pin("M0","input")
Desc.add_pin("M2","input")
Desc.add_pin("X2","output")
Desc.add_pin_func("X2","unknown")
CellLib["BENCX2"]=Desc
Desc = cellDescClass("BENCX4")
Desc.properties["cell_leakage_power"] = "12534.821280"
Desc.properties["cell_footprint"] = "recsel"
Desc.properties["area"] = "202.910400"
Desc.pinOrder = ['A', 'M0', 'M1', 'M2', 'S', 'X2']
Desc.add_arc("M2","A","combi")
Desc.add_arc("M1","A","combi")
Desc.add_arc("M0","A","combi")
Desc.add_arc("M2","S","combi")
Desc.add_arc("M1","S","combi")
Desc.add_arc("M0","S","combi")
Desc.add_arc("M1","X2","combi")
Desc.add_arc("M0","X2","combi")
Desc.add_param("area",202.910400);
Desc.add_pin("A","output")
Desc.add_pin_func("A","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("M1","input")
Desc.add_pin("M0","input")
Desc.add_pin("M2","input")
Desc.add_pin("X2","output")
Desc.add_pin_func("X2","unknown")
CellLib["BENCX4"]=Desc
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
Desc = cellDescClass("BUFX1")
Desc.properties["cell_leakage_power"] = "458.348220"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX1"]=Desc
Desc = cellDescClass("BUFX12")
Desc.properties["cell_leakage_power"] = "3123.936720"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX12"]=Desc
Desc = cellDescClass("BUFX16")
Desc.properties["cell_leakage_power"] = "4129.124040"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX16"]=Desc
Desc = cellDescClass("BUFX2")
Desc.properties["cell_leakage_power"] = "574.299720"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX2"]=Desc
Desc = cellDescClass("BUFX20")
Desc.properties["cell_leakage_power"] = "5112.567720"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",53.222400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX20"]=Desc
Desc = cellDescClass("BUFX3")
Desc.properties["cell_leakage_power"] = "762.792876"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX3"]=Desc
Desc = cellDescClass("BUFX4")
Desc.properties["cell_leakage_power"] = "1060.451514"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX4"]=Desc
Desc = cellDescClass("BUFX8")
Desc.properties["cell_leakage_power"] = "2043.346500"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFX8"]=Desc
Desc = cellDescClass("BUFXL")
Desc.properties["cell_leakage_power"] = "436.766094"
Desc.properties["cell_footprint"] = "buf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["BUFXL"]=Desc
Desc = cellDescClass("CLKBUFX1")
Desc.properties["cell_leakage_power"] = "465.424218"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX1"]=Desc
Desc = cellDescClass("CLKBUFX12")
Desc.properties["cell_leakage_power"] = "3912.419880"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",53.222400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX12"]=Desc
Desc = cellDescClass("CLKBUFX16")
Desc.properties["cell_leakage_power"] = "5029.443900"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX16"]=Desc
Desc = cellDescClass("CLKBUFX2")
Desc.properties["cell_leakage_power"] = "596.237436"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX2"]=Desc
Desc = cellDescClass("CLKBUFX20")
Desc.properties["cell_leakage_power"] = "6339.486060"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX20"]=Desc
Desc = cellDescClass("CLKBUFX3")
Desc.properties["cell_leakage_power"] = "653.191290"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX3"]=Desc
Desc = cellDescClass("CLKBUFX4")
Desc.properties["cell_leakage_power"] = "823.813092"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX4"]=Desc
Desc = cellDescClass("CLKBUFX8")
Desc.properties["cell_leakage_power"] = "1619.249130"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFX8"]=Desc
Desc = cellDescClass("CLKBUFXL")
Desc.properties["cell_leakage_power"] = "467.033202"
Desc.properties["cell_footprint"] = "clkbuf"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKBUFXL"]=Desc
Desc = cellDescClass("CLKINVX1")
Desc.properties["cell_leakage_power"] = "138.122852"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX1"]=Desc
Desc = cellDescClass("CLKINVX12")
Desc.properties["cell_leakage_power"] = "4259.856420"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX12"]=Desc
Desc = cellDescClass("CLKINVX16")
Desc.properties["cell_leakage_power"] = "5531.901480"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX16"]=Desc
Desc = cellDescClass("CLKINVX2")
Desc.properties["cell_leakage_power"] = "258.205482"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX2"]=Desc
Desc = cellDescClass("CLKINVX20")
Desc.properties["cell_leakage_power"] = "7065.610560"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",96.465600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX20"]=Desc
Desc = cellDescClass("CLKINVX3")
Desc.properties["cell_leakage_power"] = "360.740142"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX3"]=Desc
Desc = cellDescClass("CLKINVX4")
Desc.properties["cell_leakage_power"] = "530.466894"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX4"]=Desc
Desc = cellDescClass("CLKINVX8")
Desc.properties["cell_leakage_power"] = "1086.528816"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVX8"]=Desc
Desc = cellDescClass("CLKINVXL")
Desc.properties["cell_leakage_power"] = "123.041187"
Desc.properties["cell_footprint"] = "clkinv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["CLKINVXL"]=Desc
Desc = cellDescClass("CMPR22X1")
Desc.properties["cell_leakage_power"] = "2576.297340"
Desc.properties["cell_footprint"] = "add22"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'B', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["CMPR22X1"]=Desc
Desc = cellDescClass("CMPR32X1")
Desc.properties["cell_leakage_power"] = "3632.359140"
Desc.properties["cell_footprint"] = "add32"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['A', 'B', 'C', 'CO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("C","S","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("C","CO","combi")
Desc.add_param("area",69.854400);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
CellLib["CMPR32X1"]=Desc
Desc = cellDescClass("CMPR42X1")
Desc.properties["cell_leakage_power"] = "5452.116480"
Desc.properties["cell_footprint"] = "add42"
Desc.properties["area"] = "113.097600"
Desc.pinOrder = ['A', 'B', 'C', 'CO', 'D', 'ICI', 'ICO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("C","S","combi")
Desc.add_arc("D","S","combi")
Desc.add_arc("ICI","S","combi")
Desc.add_arc("A","ICO","combi")
Desc.add_arc("B","ICO","combi")
Desc.add_arc("C","ICO","combi")
Desc.add_arc("D","CO","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("C","CO","combi")
Desc.add_arc("ICI","CO","combi")
Desc.add_param("area",113.097600);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("ICO","output")
Desc.add_pin_func("ICO","unknown")
Desc.add_pin("D","input")
Desc.add_pin("ICI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["CMPR42X1"]=Desc
Desc = cellDescClass("CMPR42X2")
Desc.properties["cell_leakage_power"] = "9437.337540"
Desc.properties["cell_footprint"] = "add42"
Desc.properties["area"] = "133.056000"
Desc.pinOrder = ['A', 'B', 'C', 'CO', 'D', 'ICI', 'ICO', 'S']
Desc.add_arc("A","S","combi")
Desc.add_arc("B","S","combi")
Desc.add_arc("C","S","combi")
Desc.add_arc("D","S","combi")
Desc.add_arc("ICI","S","combi")
Desc.add_arc("A","ICO","combi")
Desc.add_arc("B","ICO","combi")
Desc.add_arc("C","ICO","combi")
Desc.add_arc("D","CO","combi")
Desc.add_arc("A","CO","combi")
Desc.add_arc("B","CO","combi")
Desc.add_arc("C","CO","combi")
Desc.add_arc("ICI","CO","combi")
Desc.add_param("area",133.056000);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("ICO","output")
Desc.add_pin_func("ICO","unknown")
Desc.add_pin("D","input")
Desc.add_pin("ICI","input")
Desc.add_pin("S","output")
Desc.add_pin_func("S","unknown")
Desc.add_pin("CO","output")
Desc.add_pin_func("CO","unknown")
CellLib["CMPR42X2"]=Desc
Desc = cellDescClass("DFFHQX1")
Desc.properties["cell_leakage_power"] = "1876.612860"
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",53.222400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("flipflop")
CellLib["DFFHQX1"]=Desc
Desc = cellDescClass("DFFHQX2")
Desc.properties["cell_leakage_power"] = "2493.222120"
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("flipflop")
CellLib["DFFHQX2"]=Desc
Desc = cellDescClass("DFFHQX4")
Desc.properties["cell_leakage_power"] = "3632.190660"
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "73.180800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",73.180800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("flipflop")
CellLib["DFFHQX4"]=Desc
Desc = cellDescClass("DFFHQXL")
Desc.properties["cell_leakage_power"] = "1774.373040"
Desc.properties["cell_footprint"] = "dffhq"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",53.222400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("flipflop")
CellLib["DFFHQXL"]=Desc
Desc = cellDescClass("DFFNRX1")
Desc.properties["cell_leakage_power"] = "1916.605800"
Desc.properties["cell_footprint"] = "dffnr"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",76.507200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNRX1"]=Desc
Desc = cellDescClass("DFFNRX2")
Desc.properties["cell_leakage_power"] = "2410.318620"
Desc.properties["cell_footprint"] = "dffnr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNRX2"]=Desc
Desc = cellDescClass("DFFNRX4")
Desc.properties["cell_leakage_power"] = "3214.454220"
Desc.properties["cell_footprint"] = "dffnr"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",103.118400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNRX4"]=Desc
Desc = cellDescClass("DFFNRXL")
Desc.properties["cell_leakage_power"] = "1922.552820"
Desc.properties["cell_footprint"] = "dffnr"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",79.833600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNRXL"]=Desc
Desc = cellDescClass("DFFNSRX1")
Desc.properties["cell_leakage_power"] = "1986.000120"
Desc.properties["cell_footprint"] = "dffnsr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",83.160000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSRX1"]=Desc
Desc = cellDescClass("DFFNSRX2")
Desc.properties["cell_leakage_power"] = "2389.932540"
Desc.properties["cell_footprint"] = "dffnsr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSRX2"]=Desc
Desc = cellDescClass("DFFNSRX4")
Desc.properties["cell_leakage_power"] = "3723.759540"
Desc.properties["cell_footprint"] = "dffnsr"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",116.424000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSRX4"]=Desc
Desc = cellDescClass("DFFNSRXL")
Desc.properties["cell_leakage_power"] = "1950.316380"
Desc.properties["cell_footprint"] = "dffnsr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSRXL"]=Desc
Desc = cellDescClass("DFFNSX1")
Desc.properties["cell_leakage_power"] = "1833.582420"
Desc.properties["cell_footprint"] = "dffns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSX1"]=Desc
Desc = cellDescClass("DFFNSX2")
Desc.properties["cell_leakage_power"] = "2104.752600"
Desc.properties["cell_footprint"] = "dffns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSX2"]=Desc
Desc = cellDescClass("DFFNSX4")
Desc.properties["cell_leakage_power"] = "3170.048400"
Desc.properties["cell_footprint"] = "dffns"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",96.465600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSX4"]=Desc
Desc = cellDescClass("DFFNSXL")
Desc.properties["cell_leakage_power"] = "1802.689020"
Desc.properties["cell_footprint"] = "dffns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNSXL"]=Desc
Desc = cellDescClass("DFFNX1")
Desc.properties["cell_leakage_power"] = "1555.901784"
Desc.properties["cell_footprint"] = "dffn"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNX1"]=Desc
Desc = cellDescClass("DFFNX2")
Desc.properties["cell_leakage_power"] = "2057.618700"
Desc.properties["cell_footprint"] = "dffn"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNX2"]=Desc
Desc = cellDescClass("DFFNX4")
Desc.properties["cell_leakage_power"] = "3266.393040"
Desc.properties["cell_footprint"] = "dffn"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",79.833600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNX4"]=Desc
Desc = cellDescClass("DFFNXL")
Desc.properties["cell_leakage_power"] = "1452.142728"
Desc.properties["cell_footprint"] = "dffn"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFNXL"]=Desc
Desc = cellDescClass("DFFRHQX1")
Desc.properties["cell_leakage_power"] = "2220.697620"
Desc.properties["cell_footprint"] = "dffrhq"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFRHQX1"]=Desc
Desc = cellDescClass("DFFRHQX2")
Desc.properties["cell_leakage_power"] = "3206.041560"
Desc.properties["cell_footprint"] = "dffrhq"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFRHQX2"]=Desc
Desc = cellDescClass("DFFRHQX4")
Desc.properties["cell_leakage_power"] = "5170.090680"
Desc.properties["cell_footprint"] = "dffrhq"
Desc.properties["area"] = "106.444800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",106.444800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFRHQX4"]=Desc
Desc = cellDescClass("DFFRHQXL")
Desc.properties["cell_leakage_power"] = "1883.005380"
Desc.properties["cell_footprint"] = "dffrhq"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFRHQXL"]=Desc
Desc = cellDescClass("DFFRX1")
Desc.properties["cell_leakage_power"] = "1819.812420"
Desc.properties["cell_footprint"] = "dffr"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",76.507200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFRX1"]=Desc
Desc = cellDescClass("DFFRX2")
Desc.properties["cell_leakage_power"] = "2371.087080"
Desc.properties["cell_footprint"] = "dffr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFRX2"]=Desc
Desc = cellDescClass("DFFRX4")
Desc.properties["cell_leakage_power"] = "3233.145780"
Desc.properties["cell_footprint"] = "dffr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFRX4"]=Desc
Desc = cellDescClass("DFFRXL")
Desc.properties["cell_leakage_power"] = "1850.527620"
Desc.properties["cell_footprint"] = "dffr"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",76.507200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFRXL"]=Desc
Desc = cellDescClass("DFFSHQX1")
Desc.properties["cell_leakage_power"] = "2078.477820"
Desc.properties["cell_footprint"] = "dffshq"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_job("flipflop")
CellLib["DFFSHQX1"]=Desc
Desc = cellDescClass("DFFSHQX2")
Desc.properties["cell_leakage_power"] = "2889.807840"
Desc.properties["cell_footprint"] = "dffshq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_job("flipflop")
CellLib["DFFSHQX2"]=Desc
Desc = cellDescClass("DFFSHQX4")
Desc.properties["cell_leakage_power"] = "4585.141080"
Desc.properties["cell_footprint"] = "dffshq"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_job("flipflop")
CellLib["DFFSHQX4"]=Desc
Desc = cellDescClass("DFFSHQXL")
Desc.properties["cell_leakage_power"] = "1861.465860"
Desc.properties["cell_footprint"] = "dffshq"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_job("flipflop")
CellLib["DFFSHQXL"]=Desc
Desc = cellDescClass("DFFSRHQX1")
Desc.properties["cell_leakage_power"] = "2257.032600"
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFSRHQX1"]=Desc
Desc = cellDescClass("DFFSRHQX2")
Desc.properties["cell_leakage_power"] = "3350.231280"
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "113.097600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",113.097600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFSRHQX2"]=Desc
Desc = cellDescClass("DFFSRHQX4")
Desc.properties["cell_leakage_power"] = "5687.491140"
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "153.014400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",153.014400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFSRHQX4"]=Desc
Desc = cellDescClass("DFFSRHQXL")
Desc.properties["cell_leakage_power"] = "1965.000060"
Desc.properties["cell_footprint"] = "dffsrhq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.set_job("flipflop")
CellLib["DFFSRHQXL"]=Desc
Desc = cellDescClass("DFFSRX1")
Desc.properties["cell_leakage_power"] = "1951.494120"
Desc.properties["cell_footprint"] = "dffsr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSRX1"]=Desc
Desc = cellDescClass("DFFSRX2")
Desc.properties["cell_leakage_power"] = "2354.190480"
Desc.properties["cell_footprint"] = "dffsr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSRX2"]=Desc
Desc = cellDescClass("DFFSRX4")
Desc.properties["cell_leakage_power"] = "3770.422020"
Desc.properties["cell_footprint"] = "dffsr"
Desc.properties["area"] = "119.750400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",119.750400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSRX4"]=Desc
Desc = cellDescClass("DFFSRXL")
Desc.properties["cell_leakage_power"] = "1945.790100"
Desc.properties["cell_footprint"] = "dffsr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSRXL"]=Desc
Desc = cellDescClass("DFFSX1")
Desc.properties["cell_leakage_power"] = "1846.035360"
Desc.properties["cell_footprint"] = "dffs"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",63.201600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSX1"]=Desc
Desc = cellDescClass("DFFSX2")
Desc.properties["cell_leakage_power"] = "2113.926660"
Desc.properties["cell_footprint"] = "dffs"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSX2"]=Desc
Desc = cellDescClass("DFFSX4")
Desc.properties["cell_leakage_power"] = "3155.074740"
Desc.properties["cell_footprint"] = "dffs"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSX4"]=Desc
Desc = cellDescClass("DFFSXL")
Desc.properties["cell_leakage_power"] = "1850.226300"
Desc.properties["cell_footprint"] = "dffs"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",63.201600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFSXL"]=Desc
Desc = cellDescClass("DFFTRX1")
Desc.properties["cell_leakage_power"] = "1530.324900"
Desc.properties["cell_footprint"] = "dfftr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFTRX1"]=Desc
Desc = cellDescClass("DFFTRX2")
Desc.properties["cell_leakage_power"] = "2119.839660"
Desc.properties["cell_footprint"] = "dfftr"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFTRX2"]=Desc
Desc = cellDescClass("DFFTRX4")
Desc.properties["cell_leakage_power"] = "3438.048240"
Desc.properties["cell_footprint"] = "dfftr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFTRX4"]=Desc
Desc = cellDescClass("DFFTRXL")
Desc.properties["cell_leakage_power"] = "1466.282736"
Desc.properties["cell_footprint"] = "dfftr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFTRXL"]=Desc
Desc = cellDescClass("DFFX1")
Desc.properties["cell_leakage_power"] = "1504.893654"
Desc.properties["cell_footprint"] = "dff"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFX1"]=Desc
Desc = cellDescClass("DFFX2")
Desc.properties["cell_leakage_power"] = "2079.014040"
Desc.properties["cell_footprint"] = "dff"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFX2"]=Desc
Desc = cellDescClass("DFFX4")
Desc.properties["cell_leakage_power"] = "3400.759080"
Desc.properties["cell_footprint"] = "dff"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFX4"]=Desc
Desc = cellDescClass("DFFXL")
Desc.properties["cell_leakage_power"] = "1443.571308"
Desc.properties["cell_footprint"] = "dff"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["DFFXL"]=Desc
Desc = cellDescClass("DLY1X1")
Desc.properties["cell_leakage_power"] = "896.314086"
Desc.properties["cell_footprint"] = "dly1"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY1X1"]=Desc
Desc = cellDescClass("DLY2X1")
Desc.properties["cell_leakage_power"] = "625.705884"
Desc.properties["cell_footprint"] = "dly2"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY2X1"]=Desc
Desc = cellDescClass("DLY3X1")
Desc.properties["cell_leakage_power"] = "595.058238"
Desc.properties["cell_footprint"] = "dly3"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY3X1"]=Desc
Desc = cellDescClass("DLY4X1")
Desc.properties["cell_leakage_power"] = "587.077956"
Desc.properties["cell_footprint"] = "dly4"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("buf") # A
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["DLY4X1"]=Desc
Desc = cellDescClass("EDFFTRX1")
Desc.properties["cell_leakage_power"] = "1838.643300"
Desc.properties["cell_footprint"] = "edfftr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFTRX1"]=Desc
Desc = cellDescClass("EDFFTRX2")
Desc.properties["cell_leakage_power"] = "2329.294320"
Desc.properties["cell_footprint"] = "edfftr"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",89.812800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFTRX2"]=Desc
Desc = cellDescClass("EDFFTRX4")
Desc.properties["cell_leakage_power"] = "3907.632780"
Desc.properties["cell_footprint"] = "edfftr"
Desc.properties["area"] = "106.444800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",106.444800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFTRX4"]=Desc
Desc = cellDescClass("EDFFTRXL")
Desc.properties["cell_leakage_power"] = "1816.536780"
Desc.properties["cell_footprint"] = "edfftr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFTRXL"]=Desc
Desc = cellDescClass("EDFFX1")
Desc.properties["cell_leakage_power"] = "1813.105620"
Desc.properties["cell_footprint"] = "edff"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",76.507200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFX1"]=Desc
Desc = cellDescClass("EDFFX2")
Desc.properties["cell_leakage_power"] = "2306.199600"
Desc.properties["cell_footprint"] = "edff"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",89.812800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFX2"]=Desc
Desc = cellDescClass("EDFFX4")
Desc.properties["cell_leakage_power"] = "3762.027180"
Desc.properties["cell_footprint"] = "edff"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",103.118400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFX4"]=Desc
Desc = cellDescClass("EDFFXL")
Desc.properties["cell_leakage_power"] = "1762.140420"
Desc.properties["cell_footprint"] = "edff"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",76.507200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["EDFFXL"]=Desc
Desc = cellDescClass("HOLDX1")
Desc.properties["cell_leakage_power"] = "409.093578"
Desc.properties["cell_footprint"] = "hold"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['Y']
Desc.add_param("area",13.305600);
CellLib["HOLDX1"]=Desc
Desc = cellDescClass("INVX1")
Desc.properties["cell_leakage_power"] = "135.455522"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",6.652800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX1"]=Desc
Desc = cellDescClass("INVX12")
Desc.properties["cell_leakage_power"] = "3253.878540"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX12"]=Desc
Desc = cellDescClass("INVX16")
Desc.properties["cell_leakage_power"] = "4272.416280"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX16"]=Desc
Desc = cellDescClass("INVX2")
Desc.properties["cell_leakage_power"] = "258.205806"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX2"]=Desc
Desc = cellDescClass("INVX20")
Desc.properties["cell_leakage_power"] = "5295.627720"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX20"]=Desc
Desc = cellDescClass("INVX3")
Desc.properties["cell_leakage_power"] = "371.352762"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX3"]=Desc
Desc = cellDescClass("INVX4")
Desc.properties["cell_leakage_power"] = "517.703238"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX4"]=Desc
Desc = cellDescClass("INVX8")
Desc.properties["cell_leakage_power"] = "1086.526062"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVX8"]=Desc
Desc = cellDescClass("INVXL")
Desc.properties["cell_leakage_power"] = "113.872846"
Desc.properties["cell_footprint"] = "inv"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['A', 'Y']
Desc.add_arc("A","Y","combi")
Desc.set_job("inv") # (!A)
Desc.add_param("area",6.652800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["INVXL"]=Desc
Desc = cellDescClass("JKFFRX1")
Desc.properties["cell_leakage_power"] = "2003.549580"
Desc.properties["cell_footprint"] = "jkffr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFRX1"]=Desc
Desc = cellDescClass("JKFFRX2")
Desc.properties["cell_leakage_power"] = "2372.812380"
Desc.properties["cell_footprint"] = "jkffr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFRX2"]=Desc
Desc = cellDescClass("JKFFRX4")
Desc.properties["cell_leakage_power"] = "3684.254220"
Desc.properties["cell_footprint"] = "jkffr"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",116.424000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFRX4"]=Desc
Desc = cellDescClass("JKFFRXL")
Desc.properties["cell_leakage_power"] = "2029.166640"
Desc.properties["cell_footprint"] = "jkffr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFRXL"]=Desc
Desc = cellDescClass("JKFFSRX1")
Desc.properties["cell_leakage_power"] = "2099.751660"
Desc.properties["cell_footprint"] = "jkffsr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSRX1"]=Desc
Desc = cellDescClass("JKFFSRX2")
Desc.properties["cell_leakage_power"] = "2534.502960"
Desc.properties["cell_footprint"] = "jkffsr"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",103.118400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSRX2"]=Desc
Desc = cellDescClass("JKFFSRX4")
Desc.properties["cell_leakage_power"] = "2956.117680"
Desc.properties["cell_footprint"] = "jkffsr"
Desc.properties["area"] = "109.771200"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",109.771200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSRX4"]=Desc
Desc = cellDescClass("JKFFSRXL")
Desc.properties["cell_leakage_power"] = "2122.937100"
Desc.properties["cell_footprint"] = "jkffsr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSRXL"]=Desc
Desc = cellDescClass("JKFFSX1")
Desc.properties["cell_leakage_power"] = "1972.515240"
Desc.properties["cell_footprint"] = "jkffs"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSX1"]=Desc
Desc = cellDescClass("JKFFSX2")
Desc.properties["cell_leakage_power"] = "2294.503200"
Desc.properties["cell_footprint"] = "jkffs"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",89.812800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSX2"]=Desc
Desc = cellDescClass("JKFFSX4")
Desc.properties["cell_leakage_power"] = "3429.697140"
Desc.properties["cell_footprint"] = "jkffs"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",103.118400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSX4"]=Desc
Desc = cellDescClass("JKFFSXL")
Desc.properties["cell_leakage_power"] = "2002.851360"
Desc.properties["cell_footprint"] = "jkffs"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFSXL"]=Desc
Desc = cellDescClass("JKFFX1")
Desc.properties["cell_leakage_power"] = "1765.903680"
Desc.properties["cell_footprint"] = "jkff"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFX1"]=Desc
Desc = cellDescClass("JKFFX2")
Desc.properties["cell_leakage_power"] = "2383.212780"
Desc.properties["cell_footprint"] = "jkff"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFX2"]=Desc
Desc = cellDescClass("JKFFX4")
Desc.properties["cell_leakage_power"] = "3857.299380"
Desc.properties["cell_footprint"] = "jkff"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFX4"]=Desc
Desc = cellDescClass("JKFFXL")
Desc.properties["cell_leakage_power"] = "1660.987620"
Desc.properties["cell_footprint"] = "jkff"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'IQ', 'IQN', 'J', 'K', 'Q', 'QN', 'next']
Desc.add_arc("CK","J","setup_rising")
Desc.add_arc("CK","J","hold_rising")
Desc.add_arc("CK","K","setup_rising")
Desc.add_arc("CK","K","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("K","input")
Desc.add_pin("J","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["JKFFXL"]=Desc
Desc = cellDescClass("MX2X1")
Desc.properties["cell_leakage_power"] = "1306.587834"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2X1"]=Desc
Desc = cellDescClass("MX2X2")
Desc.properties["cell_leakage_power"] = "2043.111600"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2X2"]=Desc
Desc = cellDescClass("MX2X4")
Desc.properties["cell_leakage_power"] = "2486.865240"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2X4"]=Desc
Desc = cellDescClass("MX2XL")
Desc.properties["cell_leakage_power"] = "1314.350550"
Desc.properties["cell_footprint"] = "mux2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MX2XL"]=Desc
Desc = cellDescClass("MX4X1")
Desc.properties["cell_leakage_power"] = "3414.893580"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",66.528000);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MX4X1"]=Desc
Desc = cellDescClass("MX4X2")
Desc.properties["cell_leakage_power"] = "5627.551140"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MX4X2"]=Desc
Desc = cellDescClass("MX4X4")
Desc.properties["cell_leakage_power"] = "5894.951580"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MX4X4"]=Desc
Desc = cellDescClass("MX4XL")
Desc.properties["cell_leakage_power"] = "2896.712280"
Desc.properties["cell_footprint"] = "mux4"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",66.528000);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MX4XL"]=Desc
Desc = cellDescClass("MXI2X1")
Desc.properties["cell_leakage_power"] = "1276.906518"
Desc.properties["cell_footprint"] = "muxi2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MXI2X1"]=Desc
Desc = cellDescClass("MXI2X2")
Desc.properties["cell_leakage_power"] = "1861.498260"
Desc.properties["cell_footprint"] = "muxi2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MXI2X2"]=Desc
Desc = cellDescClass("MXI2X4")
Desc.properties["cell_leakage_power"] = "3767.207940"
Desc.properties["cell_footprint"] = "muxi2"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MXI2X4"]=Desc
Desc = cellDescClass("MXI2XL")
Desc.properties["cell_leakage_power"] = "1149.161742"
Desc.properties["cell_footprint"] = "muxi2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'S0', 'Y']
Desc.add_arc("S0","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("S0","input")
CellLib["MXI2XL"]=Desc
Desc = cellDescClass("MXI4X1")
Desc.properties["cell_leakage_power"] = "3207.151260"
Desc.properties["cell_footprint"] = "muxi4"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MXI4X1"]=Desc
Desc = cellDescClass("MXI4X2")
Desc.properties["cell_leakage_power"] = "4592.764800"
Desc.properties["cell_footprint"] = "muxi4"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",79.833600);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MXI4X2"]=Desc
Desc = cellDescClass("MXI4X4")
Desc.properties["cell_leakage_power"] = "5699.817720"
Desc.properties["cell_footprint"] = "muxi4"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MXI4X4"]=Desc
Desc = cellDescClass("MXI4XL")
Desc.properties["cell_leakage_power"] = "3325.320540"
Desc.properties["cell_footprint"] = "muxi4"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'S0', 'S1', 'Y']
Desc.add_arc("S1","Y","combi")
Desc.add_arc("S0","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("A","Y","combi")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("S1","input")
Desc.add_pin("S0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["MXI4XL"]=Desc
Desc = cellDescClass("NAND2BX1")
Desc.properties["cell_leakage_power"] = "581.326470"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND2BX1"]=Desc
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
Desc = cellDescClass("NAND2BX4")
Desc.properties["cell_leakage_power"] = "1517.224446"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND2BX4"]=Desc
Desc = cellDescClass("NAND2BXL")
Desc.properties["cell_leakage_power"] = "540.512676"
Desc.properties["cell_footprint"] = "nand2b"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND2BXL"]=Desc
Desc = cellDescClass("NAND2X1")
Desc.properties["cell_leakage_power"] = "258.251166"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2X1"]=Desc
Desc = cellDescClass("NAND2X2")
Desc.properties["cell_leakage_power"] = "525.788172"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2X2"]=Desc
Desc = cellDescClass("NAND2X4")
Desc.properties["cell_leakage_power"] = "916.074684"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2X4"]=Desc
Desc = cellDescClass("NAND2XL")
Desc.properties["cell_leakage_power"] = "217.392336"
Desc.properties["cell_footprint"] = "nand2"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NAND2XL"]=Desc
Desc = cellDescClass("NAND3BX1")
Desc.properties["cell_leakage_power"] = "749.331000"
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
CellLib["NAND3BX1"]=Desc
Desc = cellDescClass("NAND3BX2")
Desc.properties["cell_leakage_power"] = "1169.494686"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND3BX2"]=Desc
Desc = cellDescClass("NAND3BX4")
Desc.properties["cell_leakage_power"] = "1827.108900"
Desc.properties["cell_footprint"] = "nand3b"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NAND3BX4"]=Desc
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
Desc = cellDescClass("NAND3X1")
Desc.properties["cell_leakage_power"] = "420.378498"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NAND3X1"]=Desc
Desc = cellDescClass("NAND3X2")
Desc.properties["cell_leakage_power"] = "836.630208"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NAND3X2"]=Desc
Desc = cellDescClass("NAND3X4")
Desc.properties["cell_leakage_power"] = "1162.603368"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NAND3X4"]=Desc
Desc = cellDescClass("NAND3XL")
Desc.properties["cell_leakage_power"] = "337.208670"
Desc.properties["cell_footprint"] = "nand3"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NAND3XL"]=Desc
Desc = cellDescClass("NAND4BBX1")
Desc.properties["cell_leakage_power"] = "1181.488194"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BBX1"]=Desc
Desc = cellDescClass("NAND4BBX2")
Desc.properties["cell_leakage_power"] = "1791.890100"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BBX2"]=Desc
Desc = cellDescClass("NAND4BBX4")
Desc.properties["cell_leakage_power"] = "3481.180740"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",63.201600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BBX4"]=Desc
Desc = cellDescClass("NAND4BBXL")
Desc.properties["cell_leakage_power"] = "1081.070388"
Desc.properties["cell_footprint"] = "nand4bb"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BBXL"]=Desc
Desc = cellDescClass("NAND4BX1")
Desc.properties["cell_leakage_power"] = "858.367530"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BX1"]=Desc
Desc = cellDescClass("NAND4BX2")
Desc.properties["cell_leakage_power"] = "1447.778610"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BX2"]=Desc
Desc = cellDescClass("NAND4BX4")
Desc.properties["cell_leakage_power"] = "2886.363720"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BX4"]=Desc
Desc = cellDescClass("NAND4BXL")
Desc.properties["cell_leakage_power"] = "757.905174"
Desc.properties["cell_footprint"] = "nand4b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NAND4BXL"]=Desc
Desc = cellDescClass("NAND4X1")
Desc.properties["cell_leakage_power"] = "535.247676"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NAND4X1"]=Desc
Desc = cellDescClass("NAND4X2")
Desc.properties["cell_leakage_power"] = "1103.665500"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NAND4X2"]=Desc
Desc = cellDescClass("NAND4X4")
Desc.properties["cell_leakage_power"] = "2207.337480"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NAND4X4"]=Desc
Desc = cellDescClass("NAND4XL")
Desc.properties["cell_leakage_power"] = "434.784834"
Desc.properties["cell_footprint"] = "nand4"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NAND4XL"]=Desc
Desc = cellDescClass("NOR2BX1")
Desc.properties["cell_leakage_power"] = "485.221590"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR2BX1"]=Desc
Desc = cellDescClass("NOR2BX2")
Desc.properties["cell_leakage_power"] = "631.210644"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR2BX2"]=Desc
Desc = cellDescClass("NOR2BX4")
Desc.properties["cell_leakage_power"] = "1328.275422"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR2BX4"]=Desc
Desc = cellDescClass("NOR2BXL")
Desc.properties["cell_leakage_power"] = "452.954754"
Desc.properties["cell_footprint"] = "nor2b"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['AN', 'B', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR2BXL"]=Desc
Desc = cellDescClass("NOR2X1")
Desc.properties["cell_leakage_power"] = "162.099954"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NOR2X1"]=Desc
Desc = cellDescClass("NOR2X2")
Desc.properties["cell_leakage_power"] = "309.605814"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NOR2X2"]=Desc
Desc = cellDescClass("NOR2X4")
Desc.properties["cell_leakage_power"] = "687.945474"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NOR2X4"]=Desc
Desc = cellDescClass("NOR2XL")
Desc.properties["cell_leakage_power"] = "129.834317"
Desc.properties["cell_footprint"] = "nor2"
Desc.properties["area"] = "9.979200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",9.979200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["NOR2XL"]=Desc
Desc = cellDescClass("NOR3BX1")
Desc.properties["cell_leakage_power"] = "517.384908"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR3BX1"]=Desc
Desc = cellDescClass("NOR3BX2")
Desc.properties["cell_leakage_power"] = "737.846820"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR3BX2"]=Desc
Desc = cellDescClass("NOR3BX4")
Desc.properties["cell_leakage_power"] = "1330.441038"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR3BX4"]=Desc
Desc = cellDescClass("NOR3BXL")
Desc.properties["cell_leakage_power"] = "471.227868"
Desc.properties["cell_footprint"] = "nor3b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'C', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("AN","input")
CellLib["NOR3BXL"]=Desc
Desc = cellDescClass("NOR3X1")
Desc.properties["cell_leakage_power"] = "209.454984"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NOR3X1"]=Desc
Desc = cellDescClass("NOR3X2")
Desc.properties["cell_leakage_power"] = "404.694792"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NOR3X2"]=Desc
Desc = cellDescClass("NOR3X4")
Desc.properties["cell_leakage_power"] = "684.984600"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NOR3X4"]=Desc
Desc = cellDescClass("NOR3XL")
Desc.properties["cell_leakage_power"] = "155.351261"
Desc.properties["cell_footprint"] = "nor3"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["NOR3XL"]=Desc
Desc = cellDescClass("NOR4BBX1")
Desc.properties["cell_leakage_power"] = "663.505506"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BBX1"]=Desc
Desc = cellDescClass("NOR4BBX2")
Desc.properties["cell_leakage_power"] = "1026.713232"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BBX2"]=Desc
Desc = cellDescClass("NOR4BBX4")
Desc.properties["cell_leakage_power"] = "1763.258220"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",66.528000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BBX4"]=Desc
Desc = cellDescClass("NOR4BBXL")
Desc.properties["cell_leakage_power"] = "579.727854"
Desc.properties["cell_footprint"] = "nor4bb"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['AN', 'BN', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("BN","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("BN","input")
Desc.add_pin("C","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BBXL"]=Desc
Desc = cellDescClass("NOR4BX1")
Desc.properties["cell_leakage_power"] = "531.199944"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BX1"]=Desc
Desc = cellDescClass("NOR4BX2")
Desc.properties["cell_leakage_power"] = "875.586186"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BX2"]=Desc
Desc = cellDescClass("NOR4BX4")
Desc.properties["cell_leakage_power"] = "1488.550446"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BX4"]=Desc
Desc = cellDescClass("NOR4BXL")
Desc.properties["cell_leakage_power"] = "481.544676"
Desc.properties["cell_footprint"] = "nor4b"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['AN', 'B', 'C', 'D', 'Y']
Desc.add_arc("AN","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
Desc.add_pin("AN","input")
CellLib["NOR4BXL"]=Desc
Desc = cellDescClass("NOR4X1")
Desc.properties["cell_leakage_power"] = "280.786014"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NOR4X1"]=Desc
Desc = cellDescClass("NOR4X2")
Desc.properties["cell_leakage_power"] = "538.097256"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NOR4X2"]=Desc
Desc = cellDescClass("NOR4X4")
Desc.properties["cell_leakage_power"] = "919.260090"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NOR4X4"]=Desc
Desc = cellDescClass("NOR4XL")
Desc.properties["cell_leakage_power"] = "189.908226"
Desc.properties["cell_footprint"] = "nor4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["NOR4XL"]=Desc
Desc = cellDescClass("OAI211X1")
Desc.properties["cell_leakage_power"] = "421.390674"
Desc.properties["cell_footprint"] = "oai211"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI211X1"]=Desc
Desc = cellDescClass("OAI211X2")
Desc.properties["cell_leakage_power"] = "829.431414"
Desc.properties["cell_footprint"] = "oai211"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI211X2"]=Desc
Desc = cellDescClass("OAI211X4")
Desc.properties["cell_leakage_power"] = "1414.646694"
Desc.properties["cell_footprint"] = "oai211"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI211X4"]=Desc
Desc = cellDescClass("OAI211XL")
Desc.properties["cell_leakage_power"] = "347.220594"
Desc.properties["cell_footprint"] = "oai211"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("C0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI211XL"]=Desc
Desc = cellDescClass("OAI21X1")
Desc.properties["cell_leakage_power"] = "285.251220"
Desc.properties["cell_footprint"] = "oai21"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI21X1"]=Desc
Desc = cellDescClass("OAI21X2")
Desc.properties["cell_leakage_power"] = "582.395508"
Desc.properties["cell_footprint"] = "oai21"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI21X2"]=Desc
Desc = cellDescClass("OAI21X4")
Desc.properties["cell_leakage_power"] = "1153.130580"
Desc.properties["cell_footprint"] = "oai21"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI21X4"]=Desc
Desc = cellDescClass("OAI21XL")
Desc.properties["cell_leakage_power"] = "233.755470"
Desc.properties["cell_footprint"] = "oai21"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI21XL"]=Desc
Desc = cellDescClass("OAI221X1")
Desc.properties["cell_leakage_power"] = "441.924498"
Desc.properties["cell_footprint"] = "oai221"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["OAI221X1"]=Desc
Desc = cellDescClass("OAI221X2")
Desc.properties["cell_leakage_power"] = "871.964514"
Desc.properties["cell_footprint"] = "oai221"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",43.243200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["OAI221X2"]=Desc
Desc = cellDescClass("OAI221X4")
Desc.properties["cell_leakage_power"] = "1377.606690"
Desc.properties["cell_footprint"] = "oai221"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["OAI221X4"]=Desc
Desc = cellDescClass("OAI221XL")
Desc.properties["cell_leakage_power"] = "359.760528"
Desc.properties["cell_footprint"] = "oai221"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C0","input")
CellLib["OAI221XL"]=Desc
Desc = cellDescClass("OAI222X1")
Desc.properties["cell_leakage_power"] = "467.902008"
Desc.properties["cell_footprint"] = "oai222"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["OAI222X1"]=Desc
Desc = cellDescClass("OAI222X2")
Desc.properties["cell_leakage_power"] = "917.914518"
Desc.properties["cell_footprint"] = "oai222"
Desc.properties["area"] = "49.896000"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",49.896000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["OAI222X2"]=Desc
Desc = cellDescClass("OAI222X4")
Desc.properties["cell_leakage_power"] = "1456.193214"
Desc.properties["cell_footprint"] = "oai222"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",39.916800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["OAI222X4"]=Desc
Desc = cellDescClass("OAI222XL")
Desc.properties["cell_leakage_power"] = "374.100282"
Desc.properties["cell_footprint"] = "oai222"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("C0","Y","combi")
Desc.add_arc("C1","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C1","input")
Desc.add_pin("C0","input")
CellLib["OAI222XL"]=Desc
Desc = cellDescClass("OAI22X1")
Desc.properties["cell_leakage_power"] = "306.879354"
Desc.properties["cell_footprint"] = "oai22"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI22X1"]=Desc
Desc = cellDescClass("OAI22X2")
Desc.properties["cell_leakage_power"] = "628.805916"
Desc.properties["cell_footprint"] = "oai22"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI22X2"]=Desc
Desc = cellDescClass("OAI22X4")
Desc.properties["cell_leakage_power"] = "1366.234128"
Desc.properties["cell_footprint"] = "oai22"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",46.569600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI22X4"]=Desc
Desc = cellDescClass("OAI22XL")
Desc.properties["cell_leakage_power"] = "246.296052"
Desc.properties["cell_footprint"] = "oai22"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI22XL"]=Desc
Desc = cellDescClass("OAI2BB1X1")
Desc.properties["cell_leakage_power"] = "602.114472"
Desc.properties["cell_footprint"] = "oai2bb1"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["OAI2BB1X1"]=Desc
Desc = cellDescClass("OAI2BB1X2")
Desc.properties["cell_leakage_power"] = "1000.915866"
Desc.properties["cell_footprint"] = "oai2bb1"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["OAI2BB1X2"]=Desc
Desc = cellDescClass("OAI2BB1X4")
Desc.properties["cell_leakage_power"] = "1862.454060"
Desc.properties["cell_footprint"] = "oai2bb1"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["OAI2BB1X4"]=Desc
Desc = cellDescClass("OAI2BB1XL")
Desc.properties["cell_leakage_power"] = "561.300516"
Desc.properties["cell_footprint"] = "oai2bb1"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
CellLib["OAI2BB1XL"]=Desc
Desc = cellDescClass("OAI2BB2X1")
Desc.properties["cell_leakage_power"] = "629.159724"
Desc.properties["cell_footprint"] = "oai2bb2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["OAI2BB2X1"]=Desc
Desc = cellDescClass("OAI2BB2X2")
Desc.properties["cell_leakage_power"] = "1047.585960"
Desc.properties["cell_footprint"] = "oai2bb2"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["OAI2BB2X2"]=Desc
Desc = cellDescClass("OAI2BB2X4")
Desc.properties["cell_leakage_power"] = "2057.016060"
Desc.properties["cell_footprint"] = "oai2bb2"
Desc.properties["area"] = "49.896000"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",49.896000);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["OAI2BB2X4"]=Desc
Desc = cellDescClass("OAI2BB2XL")
Desc.properties["cell_leakage_power"] = "577.663326"
Desc.properties["cell_footprint"] = "oai2bb2"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0N', 'A1N', 'B0', 'B1', 'Y']
Desc.add_arc("A0N","Y","combi")
Desc.add_arc("A1N","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B0","input")
Desc.add_pin("A1N","input")
Desc.add_pin("A0N","input")
Desc.add_pin("B1","input")
CellLib["OAI2BB2XL"]=Desc
Desc = cellDescClass("OAI31X1")
Desc.properties["cell_leakage_power"] = "332.236242"
Desc.properties["cell_footprint"] = "oai31"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI31X1"]=Desc
Desc = cellDescClass("OAI31X2")
Desc.properties["cell_leakage_power"] = "659.801376"
Desc.properties["cell_footprint"] = "oai31"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI31X2"]=Desc
Desc = cellDescClass("OAI31X4")
Desc.properties["cell_leakage_power"] = "1322.263764"
Desc.properties["cell_footprint"] = "oai31"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI31X4"]=Desc
Desc = cellDescClass("OAI31XL")
Desc.properties["cell_leakage_power"] = "258.545682"
Desc.properties["cell_footprint"] = "oai31"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI31XL"]=Desc
Desc = cellDescClass("OAI32X1")
Desc.properties["cell_leakage_power"] = "356.225202"
Desc.properties["cell_footprint"] = "oai32"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI32X1"]=Desc
Desc = cellDescClass("OAI32X2")
Desc.properties["cell_leakage_power"] = "710.657712"
Desc.properties["cell_footprint"] = "oai32"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI32X2"]=Desc
Desc = cellDescClass("OAI32X4")
Desc.properties["cell_leakage_power"] = "1323.586332"
Desc.properties["cell_footprint"] = "oai32"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI32X4"]=Desc
Desc = cellDescClass("OAI32XL")
Desc.properties["cell_leakage_power"] = "273.115314"
Desc.properties["cell_footprint"] = "oai32"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_param("area",23.284800);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI32XL"]=Desc
Desc = cellDescClass("OAI33X1")
Desc.properties["cell_leakage_power"] = "404.249940"
Desc.properties["cell_footprint"] = "oai33"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI33X1"]=Desc
Desc = cellDescClass("OAI33X2")
Desc.properties["cell_leakage_power"] = "802.102824"
Desc.properties["cell_footprint"] = "oai33"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",43.243200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI33X2"]=Desc
Desc = cellDescClass("OAI33X4")
Desc.properties["cell_leakage_power"] = "1387.803456"
Desc.properties["cell_footprint"] = "oai33"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI33X4"]=Desc
Desc = cellDescClass("OAI33XL")
Desc.properties["cell_leakage_power"] = "296.650188"
Desc.properties["cell_footprint"] = "oai33"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A0', 'A1', 'A2', 'B0', 'B1', 'B2', 'Y']
Desc.add_arc("A0","Y","combi")
Desc.add_arc("A1","Y","combi")
Desc.add_arc("A2","Y","combi")
Desc.add_arc("B0","Y","combi")
Desc.add_arc("B1","Y","combi")
Desc.add_arc("B2","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A1","input")
Desc.add_pin("A0","input")
Desc.add_pin("A2","input")
Desc.add_pin("B0","input")
Desc.add_pin("B1","input")
Desc.add_pin("B2","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["OAI33XL"]=Desc
Desc = cellDescClass("OR2X1")
Desc.properties["cell_leakage_power"] = "741.994506"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["OR2X1"]=Desc
Desc = cellDescClass("OR2X2")
Desc.properties["cell_leakage_power"] = "790.519986"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["OR2X2"]=Desc
Desc = cellDescClass("OR2X4")
Desc.properties["cell_leakage_power"] = "1480.149126"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["OR2X4"]=Desc
Desc = cellDescClass("OR2XL")
Desc.properties["cell_leakage_power"] = "720.320526"
Desc.properties["cell_footprint"] = "or2"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["OR2XL"]=Desc
Desc = cellDescClass("OR3X1")
Desc.properties["cell_leakage_power"] = "1043.027928"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["OR3X1"]=Desc
Desc = cellDescClass("OR3X2")
Desc.properties["cell_leakage_power"] = "1104.376356"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["OR3X2"]=Desc
Desc = cellDescClass("OR3X4")
Desc.properties["cell_leakage_power"] = "2003.126760"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["OR3X4"]=Desc
Desc = cellDescClass("OR3XL")
Desc.properties["cell_leakage_power"] = "1068.089166"
Desc.properties["cell_footprint"] = "or3"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",16.632000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["OR3XL"]=Desc
Desc = cellDescClass("OR4X1")
Desc.properties["cell_leakage_power"] = "1329.513264"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["OR4X1"]=Desc
Desc = cellDescClass("OR4X2")
Desc.properties["cell_leakage_power"] = "1329.794334"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["OR4X2"]=Desc
Desc = cellDescClass("OR4X4")
Desc.properties["cell_leakage_power"] = "2411.185320"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["OR4X4"]=Desc
Desc = cellDescClass("OR4XL")
Desc.properties["cell_leakage_power"] = "1306.328472"
Desc.properties["cell_footprint"] = "or4"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'B', 'C', 'D', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_arc("D","Y","combi")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
Desc.add_pin("D","input")
CellLib["OR4XL"]=Desc
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
Desc = cellDescClass("RFRDX1")
Desc.properties["cell_leakage_power"] = "135.409968"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcout"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['BRB', 'RB']
Desc.add_arc("RB","BRB","combi")
Desc.set_job("inv") # (!RB)
Desc.add_param("area",16.632000);
Desc.add_pin("BRB","output")
Desc.add_pin_func("BRB","unknown")
Desc.add_pin("RB","input")
CellLib["RFRDX1"]=Desc
Desc = cellDescClass("RFRDX2")
Desc.properties["cell_leakage_power"] = "275.475654"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcout"
Desc.properties["area"] = "16.632000"
Desc.pinOrder = ['BRB', 'RB']
Desc.add_arc("RB","BRB","combi")
Desc.set_job("inv") # (!RB)
Desc.add_param("area",16.632000);
Desc.add_pin("BRB","output")
Desc.add_pin_func("BRB","unknown")
Desc.add_pin("RB","input")
CellLib["RFRDX2"]=Desc
Desc = cellDescClass("RFRDX4")
Desc.properties["cell_leakage_power"] = "531.211446"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "regcout"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['BRB', 'RB']
Desc.add_arc("RB","BRB","combi")
Desc.set_job("inv") # (!RB)
Desc.add_param("area",19.958400);
Desc.add_pin("BRB","output")
Desc.add_pin_func("BRB","unknown")
Desc.add_pin("RB","input")
CellLib["RFRDX4"]=Desc
Desc = cellDescClass("RSLATNX1")
Desc.properties["cell_leakage_power"] = "1143.365382"
Desc.properties["cell_footprint"] = "rslatn"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("RN","SN","hold_rising")
Desc.add_arc("SN","RN","hold_rising")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",36.590400);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("SN","clock")
Desc.add_pin("SN","input")
Desc.set_pin_job("RN","clock")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATNX1"]=Desc
Desc = cellDescClass("RSLATNX2")
Desc.properties["cell_leakage_power"] = "1700.400600"
Desc.properties["cell_footprint"] = "rslatn"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("RN","SN","hold_rising")
Desc.add_arc("SN","RN","hold_rising")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",36.590400);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("SN","clock")
Desc.add_pin("SN","input")
Desc.set_pin_job("RN","clock")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATNX2"]=Desc
Desc = cellDescClass("RSLATNX4")
Desc.properties["cell_leakage_power"] = "3041.396100"
Desc.properties["cell_footprint"] = "rslatn"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("RN","SN","hold_rising")
Desc.add_arc("SN","RN","hold_rising")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("SN","clock")
Desc.add_pin("SN","input")
Desc.set_pin_job("RN","clock")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATNX4"]=Desc
Desc = cellDescClass("RSLATNXL")
Desc.properties["cell_leakage_power"] = "1158.955938"
Desc.properties["cell_footprint"] = "rslatn"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("RN","SN","hold_rising")
Desc.add_arc("SN","RN","hold_rising")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",33.264000);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("SN","clock")
Desc.add_pin("SN","input")
Desc.set_pin_job("RN","clock")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATNXL"]=Desc
Desc = cellDescClass("RSLATX1")
Desc.properties["cell_leakage_power"] = "1082.604042"
Desc.properties["cell_footprint"] = "rslat"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'R', 'S', 'next']
Desc.add_arc("R","S","hold_falling")
Desc.add_arc("S","R","hold_falling")
Desc.add_arc("S","Q","preset")
Desc.add_arc("R","Q","clear")
Desc.add_arc("S","QN","clear")
Desc.add_arc("R","QN","preset")
Desc.add_param("area",33.264000);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.set_pin_job("S","clock")
Desc.add_pin("S","input")
Desc.set_pin_job("R","clock")
Desc.add_pin("R","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATX1"]=Desc
Desc = cellDescClass("RSLATX2")
Desc.properties["cell_leakage_power"] = "2029.699620"
Desc.properties["cell_footprint"] = "rslat"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'R', 'S', 'next']
Desc.add_arc("R","S","hold_falling")
Desc.add_arc("S","R","hold_falling")
Desc.add_arc("S","Q","preset")
Desc.add_arc("R","Q","clear")
Desc.add_arc("S","QN","clear")
Desc.add_arc("R","QN","preset")
Desc.add_param("area",39.916800);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.set_pin_job("S","clock")
Desc.add_pin("S","input")
Desc.set_pin_job("R","clock")
Desc.add_pin("R","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATX2"]=Desc
Desc = cellDescClass("RSLATX4")
Desc.properties["cell_leakage_power"] = "3690.986940"
Desc.properties["cell_footprint"] = "rslat"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'R', 'S', 'next']
Desc.add_arc("R","S","hold_falling")
Desc.add_arc("S","R","hold_falling")
Desc.add_arc("S","Q","preset")
Desc.add_arc("R","Q","clear")
Desc.add_arc("S","QN","clear")
Desc.add_arc("R","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.set_pin_job("S","clock")
Desc.add_pin("S","input")
Desc.set_pin_job("R","clock")
Desc.add_pin("R","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATX4"]=Desc
Desc = cellDescClass("RSLATXL")
Desc.properties["cell_leakage_power"] = "1037.644020"
Desc.properties["cell_footprint"] = "rslat"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['IQ', 'IQN', 'Q', 'QN', 'R', 'S', 'next']
Desc.add_arc("R","S","hold_falling")
Desc.add_arc("S","R","hold_falling")
Desc.add_arc("S","Q","preset")
Desc.add_arc("R","Q","clear")
Desc.add_arc("S","QN","clear")
Desc.add_arc("R","QN","preset")
Desc.add_param("area",33.264000);
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.set_pin_job("S","clock")
Desc.add_pin("S","input")
Desc.set_pin_job("R","clock")
Desc.add_pin("R","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["RSLATXL"]=Desc
Desc = cellDescClass("SDFFHQX1")
Desc.properties["cell_leakage_power"] = "2156.428980"
Desc.properties["cell_footprint"] = "sdffhq"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFHQX1"]=Desc
Desc = cellDescClass("SDFFHQX2")
Desc.properties["cell_leakage_power"] = "2729.157300"
Desc.properties["cell_footprint"] = "sdffhq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFHQX2"]=Desc
Desc = cellDescClass("SDFFHQX4")
Desc.properties["cell_leakage_power"] = "3940.032780"
Desc.properties["cell_footprint"] = "sdffhq"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFHQX4"]=Desc
Desc = cellDescClass("SDFFHQXL")
Desc.properties["cell_leakage_power"] = "1990.140840"
Desc.properties["cell_footprint"] = "sdffhq"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFHQXL"]=Desc
Desc = cellDescClass("SDFFNRX1")
Desc.properties["cell_leakage_power"] = "2345.923620"
Desc.properties["cell_footprint"] = "sdffnr"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",89.812800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNRX1"]=Desc
Desc = cellDescClass("SDFFNRX2")
Desc.properties["cell_leakage_power"] = "2879.366940"
Desc.properties["cell_footprint"] = "sdffnr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNRX2"]=Desc
Desc = cellDescClass("SDFFNRX4")
Desc.properties["cell_leakage_power"] = "3654.368460"
Desc.properties["cell_footprint"] = "sdffnr"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",116.424000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNRX4"]=Desc
Desc = cellDescClass("SDFFNRXL")
Desc.properties["cell_leakage_power"] = "2343.357540"
Desc.properties["cell_footprint"] = "sdffnr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNRXL"]=Desc
Desc = cellDescClass("SDFFNSRX1")
Desc.properties["cell_leakage_power"] = "2370.103740"
Desc.properties["cell_footprint"] = "sdffnsr"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",96.465600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSRX1"]=Desc
Desc = cellDescClass("SDFFNSRX2")
Desc.properties["cell_leakage_power"] = "2759.295780"
Desc.properties["cell_footprint"] = "sdffnsr"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",96.465600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSRX2"]=Desc
Desc = cellDescClass("SDFFNSRX4")
Desc.properties["cell_leakage_power"] = "4071.617280"
Desc.properties["cell_footprint"] = "sdffnsr"
Desc.properties["area"] = "126.403200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",126.403200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSRX4"]=Desc
Desc = cellDescClass("SDFFNSRXL")
Desc.properties["cell_leakage_power"] = "2312.230860"
Desc.properties["cell_footprint"] = "sdffnsr"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","RN","setup_falling")
Desc.add_arc("CKN","RN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",96.465600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSRXL"]=Desc
Desc = cellDescClass("SDFFNSX1")
Desc.properties["cell_leakage_power"] = "2248.174440"
Desc.properties["cell_footprint"] = "sdffns"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",79.833600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSX1"]=Desc
Desc = cellDescClass("SDFFNSX2")
Desc.properties["cell_leakage_power"] = "2532.186360"
Desc.properties["cell_footprint"] = "sdffns"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",83.160000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSX2"]=Desc
Desc = cellDescClass("SDFFNSX4")
Desc.properties["cell_leakage_power"] = "3560.523480"
Desc.properties["cell_footprint"] = "sdffns"
Desc.properties["area"] = "109.771200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",109.771200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSX4"]=Desc
Desc = cellDescClass("SDFFNSXL")
Desc.properties["cell_leakage_power"] = "2210.993820"
Desc.properties["cell_footprint"] = "sdffns"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","SN","setup_falling")
Desc.add_arc("CKN","SN","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",79.833600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNSXL"]=Desc
Desc = cellDescClass("SDFFNX1")
Desc.properties["cell_leakage_power"] = "1949.820660"
Desc.properties["cell_footprint"] = "sdffn"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNX1"]=Desc
Desc = cellDescClass("SDFFNX2")
Desc.properties["cell_leakage_power"] = "2451.716100"
Desc.properties["cell_footprint"] = "sdffn"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",83.160000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNX2"]=Desc
Desc = cellDescClass("SDFFNX4")
Desc.properties["cell_leakage_power"] = "3717.700740"
Desc.properties["cell_footprint"] = "sdffn"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",93.139200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNX4"]=Desc
Desc = cellDescClass("SDFFNXL")
Desc.properties["cell_leakage_power"] = "1830.436380"
Desc.properties["cell_footprint"] = "sdffn"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CKN', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CKN","SI","setup_falling")
Desc.add_arc("CKN","SI","hold_falling")
Desc.add_arc("CKN","SE","setup_falling")
Desc.add_arc("CKN","SE","hold_falling")
Desc.add_arc("CKN","D","setup_falling")
Desc.add_arc("CKN","D","hold_falling")
Desc.add_arc("CKN","Q","falling_edge")
Desc.add_arc("CKN","QN","falling_edge")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.set_pin_job("CKN","clock")
Desc.add_pin("CKN","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFNXL"]=Desc
Desc = cellDescClass("SDFFRHQX1")
Desc.properties["cell_leakage_power"] = "2426.084460"
Desc.properties["cell_footprint"] = "sdffrhq"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFRHQX1"]=Desc
Desc = cellDescClass("SDFFRHQX2")
Desc.properties["cell_leakage_power"] = "3340.574460"
Desc.properties["cell_footprint"] = "sdffrhq"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFRHQX2"]=Desc
Desc = cellDescClass("SDFFRHQX4")
Desc.properties["cell_leakage_power"] = "5083.953660"
Desc.properties["cell_footprint"] = "sdffrhq"
Desc.properties["area"] = "123.076800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",123.076800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFRHQX4"]=Desc
Desc = cellDescClass("SDFFRHQXL")
Desc.properties["cell_leakage_power"] = "2155.029300"
Desc.properties["cell_footprint"] = "sdffrhq"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFRHQXL"]=Desc
Desc = cellDescClass("SDFFRX1")
Desc.properties["cell_leakage_power"] = "2252.193660"
Desc.properties["cell_footprint"] = "sdffr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFRX1"]=Desc
Desc = cellDescClass("SDFFRX2")
Desc.properties["cell_leakage_power"] = "2826.379980"
Desc.properties["cell_footprint"] = "sdffr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFRX2"]=Desc
Desc = cellDescClass("SDFFRX4")
Desc.properties["cell_leakage_power"] = "3654.757260"
Desc.properties["cell_footprint"] = "sdffr"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",116.424000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFRX4"]=Desc
Desc = cellDescClass("SDFFRXL")
Desc.properties["cell_leakage_power"] = "2294.279640"
Desc.properties["cell_footprint"] = "sdffr"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFRXL"]=Desc
Desc = cellDescClass("SDFFSHQX1")
Desc.properties["cell_leakage_power"] = "2576.833560"
Desc.properties["cell_footprint"] = "sdffshq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSHQX1"]=Desc
Desc = cellDescClass("SDFFSHQX2")
Desc.properties["cell_leakage_power"] = "3345.045660"
Desc.properties["cell_footprint"] = "sdffshq"
Desc.properties["area"] = "93.139200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",93.139200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSHQX2"]=Desc
Desc = cellDescClass("SDFFSHQX4")
Desc.properties["cell_leakage_power"] = "4980.552300"
Desc.properties["cell_footprint"] = "sdffshq"
Desc.properties["area"] = "106.444800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",106.444800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSHQX4"]=Desc
Desc = cellDescClass("SDFFSHQXL")
Desc.properties["cell_leakage_power"] = "2344.833360"
Desc.properties["cell_footprint"] = "sdffshq"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSHQXL"]=Desc
Desc = cellDescClass("SDFFSRHQX1")
Desc.properties["cell_leakage_power"] = "2820.295260"
Desc.properties["cell_footprint"] = "sdffsrhq"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSRHQX1"]=Desc
Desc = cellDescClass("SDFFSRHQX2")
Desc.properties["cell_leakage_power"] = "3884.970600"
Desc.properties["cell_footprint"] = "sdffsrhq"
Desc.properties["area"] = "126.403200"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",126.403200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSRHQX2"]=Desc
Desc = cellDescClass("SDFFSRHQX4")
Desc.properties["cell_leakage_power"] = "5806.217700"
Desc.properties["cell_footprint"] = "sdffsrhq"
Desc.properties["area"] = "169.646400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",169.646400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSRHQX4"]=Desc
Desc = cellDescClass("SDFFSRHQXL")
Desc.properties["cell_leakage_power"] = "2570.755320"
Desc.properties["cell_footprint"] = "sdffsrhq"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SDFFSRHQXL"]=Desc
Desc = cellDescClass("SDFFSRX1")
Desc.properties["cell_leakage_power"] = "2335.442220"
Desc.properties["cell_footprint"] = "sdffsr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSRX1"]=Desc
Desc = cellDescClass("SDFFSRX2")
Desc.properties["cell_leakage_power"] = "2710.051020"
Desc.properties["cell_footprint"] = "sdffsr"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",96.465600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSRX2"]=Desc
Desc = cellDescClass("SDFFSRX4")
Desc.properties["cell_leakage_power"] = "4126.374900"
Desc.properties["cell_footprint"] = "sdffsr"
Desc.properties["area"] = "129.729600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",129.729600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSRX4"]=Desc
Desc = cellDescClass("SDFFSRXL")
Desc.properties["cell_leakage_power"] = "2319.289200"
Desc.properties["cell_footprint"] = "sdffsr"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",96.465600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSRXL"]=Desc
Desc = cellDescClass("SDFFSX1")
Desc.properties["cell_leakage_power"] = "2253.462120"
Desc.properties["cell_footprint"] = "sdffs"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSX1"]=Desc
Desc = cellDescClass("SDFFSX2")
Desc.properties["cell_leakage_power"] = "2514.565620"
Desc.properties["cell_footprint"] = "sdffs"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSX2"]=Desc
Desc = cellDescClass("SDFFSX4")
Desc.properties["cell_leakage_power"] = "3552.873840"
Desc.properties["cell_footprint"] = "sdffs"
Desc.properties["area"] = "106.444800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",106.444800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSX4"]=Desc
Desc = cellDescClass("SDFFSXL")
Desc.properties["cell_leakage_power"] = "2250.009900"
Desc.properties["cell_footprint"] = "sdffs"
Desc.properties["area"] = "79.833600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'SN', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","SN","setup_rising")
Desc.add_arc("CK","SN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",79.833600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFSXL"]=Desc
Desc = cellDescClass("SDFFTRX1")
Desc.properties["cell_leakage_power"] = "1944.981720"
Desc.properties["cell_footprint"] = "sdfftr"
Desc.properties["area"] = "73.180800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",73.180800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFTRX1"]=Desc
Desc = cellDescClass("SDFFTRX2")
Desc.properties["cell_leakage_power"] = "2533.974840"
Desc.properties["cell_footprint"] = "sdfftr"
Desc.properties["area"] = "86.486400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",86.486400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFTRX2"]=Desc
Desc = cellDescClass("SDFFTRX4")
Desc.properties["cell_leakage_power"] = "3813.167340"
Desc.properties["cell_footprint"] = "sdfftr"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFTRX4"]=Desc
Desc = cellDescClass("SDFFTRXL")
Desc.properties["cell_leakage_power"] = "1891.657800"
Desc.properties["cell_footprint"] = "sdfftr"
Desc.properties["area"] = "73.180800"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",73.180800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFTRXL"]=Desc
Desc = cellDescClass("SDFFX1")
Desc.properties["cell_leakage_power"] = "1901.653200"
Desc.properties["cell_footprint"] = "sdff"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",69.854400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFX1"]=Desc
Desc = cellDescClass("SDFFX2")
Desc.properties["cell_leakage_power"] = "2468.601360"
Desc.properties["cell_footprint"] = "sdff"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",83.160000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFX2"]=Desc
Desc = cellDescClass("SDFFX4")
Desc.properties["cell_leakage_power"] = "3783.497040"
Desc.properties["cell_footprint"] = "sdff"
Desc.properties["area"] = "96.465600"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",96.465600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFX4"]=Desc
Desc = cellDescClass("SDFFXL")
Desc.properties["cell_leakage_power"] = "1840.890240"
Desc.properties["cell_footprint"] = "sdff"
Desc.properties["area"] = "66.528000"
Desc.pinOrder = ['CK', 'D', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",66.528000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SDFFXL"]=Desc
Desc = cellDescClass("SEDFFHQX1")
Desc.properties["cell_leakage_power"] = "4276.299420"
Desc.properties["cell_footprint"] = "sedffhq"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",103.118400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SEDFFHQX1"]=Desc
Desc = cellDescClass("SEDFFHQX2")
Desc.properties["cell_leakage_power"] = "5224.166280"
Desc.properties["cell_footprint"] = "sedffhq"
Desc.properties["area"] = "113.097600"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",113.097600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SEDFFHQX2"]=Desc
Desc = cellDescClass("SEDFFHQX4")
Desc.properties["cell_leakage_power"] = "7512.740280"
Desc.properties["cell_footprint"] = "sedffhq"
Desc.properties["area"] = "126.403200"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",126.403200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SEDFFHQX4"]=Desc
Desc = cellDescClass("SEDFFHQXL")
Desc.properties["cell_leakage_power"] = "3828.703140"
Desc.properties["cell_footprint"] = "sedffhq"
Desc.properties["area"] = "103.118400"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_param("area",103.118400);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.set_job("flipflop")
CellLib["SEDFFHQXL"]=Desc
Desc = cellDescClass("SEDFFTRX1")
Desc.properties["cell_leakage_power"] = "4964.063940"
Desc.properties["cell_footprint"] = "sedfftr"
Desc.properties["area"] = "129.729600"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",129.729600);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFTRX1"]=Desc
Desc = cellDescClass("SEDFFTRX2")
Desc.properties["cell_leakage_power"] = "5104.135620"
Desc.properties["cell_footprint"] = "sedfftr"
Desc.properties["area"] = "133.056000"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",133.056000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFTRX2"]=Desc
Desc = cellDescClass("SEDFFTRX4")
Desc.properties["cell_leakage_power"] = "5368.704300"
Desc.properties["cell_footprint"] = "sedfftr"
Desc.properties["area"] = "139.708800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",139.708800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFTRX4"]=Desc
Desc = cellDescClass("SEDFFTRXL")
Desc.properties["cell_leakage_power"] = "4121.989560"
Desc.properties["cell_footprint"] = "sedfftr"
Desc.properties["area"] = "126.403200"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","RN","setup_rising")
Desc.add_arc("CK","RN","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",126.403200);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFTRXL"]=Desc
Desc = cellDescClass("SEDFFX1")
Desc.properties["cell_leakage_power"] = "2323.693980"
Desc.properties["cell_footprint"] = "sedff"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",89.812800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFX1"]=Desc
Desc = cellDescClass("SEDFFX2")
Desc.properties["cell_leakage_power"] = "2748.561660"
Desc.properties["cell_footprint"] = "sedff"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",99.792000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFX2"]=Desc
Desc = cellDescClass("SEDFFX4")
Desc.properties["cell_leakage_power"] = "3991.198860"
Desc.properties["cell_footprint"] = "sedff"
Desc.properties["area"] = "116.424000"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",116.424000);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFX4"]=Desc
Desc = cellDescClass("SEDFFXL")
Desc.properties["cell_leakage_power"] = "2299.904280"
Desc.properties["cell_footprint"] = "sedff"
Desc.properties["area"] = "89.812800"
Desc.pinOrder = ['CK', 'D', 'E', 'IQ', 'IQN', 'Q', 'QN', 'SE', 'SI', 'next']
Desc.add_arc("CK","SI","setup_rising")
Desc.add_arc("CK","SI","hold_rising")
Desc.add_arc("CK","SE","setup_rising")
Desc.add_arc("CK","SE","hold_rising")
Desc.add_arc("CK","D","setup_rising")
Desc.add_arc("CK","D","hold_rising")
Desc.add_arc("CK","E","setup_rising")
Desc.add_arc("CK","E","hold_rising")
Desc.add_arc("CK","Q","rising_edge")
Desc.add_arc("CK","QN","rising_edge")
Desc.add_param("area",89.812800);
Desc.set_pin_job("CK","clock")
Desc.add_pin("CK","input")
Desc.add_pin("E","input")
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("SI","input")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SE","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("flipflop")
CellLib["SEDFFXL"]=Desc
Desc = cellDescClass("TBUFIX1")
Desc.properties["cell_leakage_power"] = "252.730692"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX1"]=Desc
Desc = cellDescClass("TBUFIX12")
Desc.properties["cell_leakage_power"] = "4131.191160"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX12"]=Desc
Desc = cellDescClass("TBUFIX16")
Desc.properties["cell_leakage_power"] = "5367.510360"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",63.201600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX16"]=Desc
Desc = cellDescClass("TBUFIX2")
Desc.properties["cell_leakage_power"] = "411.636978"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "19.958400"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",19.958400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX2"]=Desc
Desc = cellDescClass("TBUFIX20")
Desc.properties["cell_leakage_power"] = "6694.808760"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",83.160000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX20"]=Desc
Desc = cellDescClass("TBUFIX3")
Desc.properties["cell_leakage_power"] = "1358.974746"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX3"]=Desc
Desc = cellDescClass("TBUFIX4")
Desc.properties["cell_leakage_power"] = "1732.646700"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX4"]=Desc
Desc = cellDescClass("TBUFIX8")
Desc.properties["cell_leakage_power"] = "2674.096740"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",43.243200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIX8"]=Desc
Desc = cellDescClass("TBUFIXL")
Desc.properties["cell_leakage_power"] = "252.730692"
Desc.properties["cell_footprint"] = "tbufi"
Desc.properties["area"] = "13.305600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",13.305600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFIXL"]=Desc
Desc = cellDescClass("TBUFX1")
Desc.properties["cell_leakage_power"] = "965.670174"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX1"]=Desc
Desc = cellDescClass("TBUFX12")
Desc.properties["cell_leakage_power"] = "4022.952480"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "49.896000"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",49.896000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX12"]=Desc
Desc = cellDescClass("TBUFX16")
Desc.properties["cell_leakage_power"] = "5071.021200"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX16"]=Desc
Desc = cellDescClass("TBUFX2")
Desc.properties["cell_leakage_power"] = "1067.512608"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX2"]=Desc
Desc = cellDescClass("TBUFX20")
Desc.properties["cell_leakage_power"] = "6496.329600"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",76.507200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX20"]=Desc
Desc = cellDescClass("TBUFX3")
Desc.properties["cell_leakage_power"] = "1257.502968"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX3"]=Desc
Desc = cellDescClass("TBUFX4")
Desc.properties["cell_leakage_power"] = "1649.253960"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "29.937600"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",29.937600);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX4"]=Desc
Desc = cellDescClass("TBUFX8")
Desc.properties["cell_leakage_power"] = "2558.827260"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",39.916800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFX8"]=Desc
Desc = cellDescClass("TBUFXL")
Desc.properties["cell_leakage_power"] = "944.502606"
Desc.properties["cell_footprint"] = "tbuf"
Desc.properties["area"] = "23.284800"
Desc.pinOrder = ['A', 'OE', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("OE","Y","three_state_disable")
Desc.add_arc("OE","Y","three_state_enable")
Desc.add_param("area",23.284800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("OE","input")
CellLib["TBUFXL"]=Desc
Desc = cellDescClass("TIEHI")
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "tiehi"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['Y']
Desc.set_job("supply1")
Desc.add_param("area",6.652800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TIEHI"]=Desc
Desc = cellDescClass("TIELO")
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "tielo"
Desc.properties["area"] = "6.652800"
Desc.pinOrder = ['Y']
Desc.set_job("supply0")
Desc.add_param("area",6.652800);
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
CellLib["TIELO"]=Desc
Desc = cellDescClass("TLATNRX1")
Desc.properties["cell_leakage_power"] = "861.759324"
Desc.properties["cell_footprint"] = "tlatnr"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNRX1"]=Desc
Desc = cellDescClass("TLATNRX2")
Desc.properties["cell_leakage_power"] = "1068.775884"
Desc.properties["cell_footprint"] = "tlatnr"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",46.569600);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNRX2"]=Desc
Desc = cellDescClass("TLATNRX4")
Desc.properties["cell_leakage_power"] = "1490.290002"
Desc.properties["cell_footprint"] = "tlatnr"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNRX4"]=Desc
Desc = cellDescClass("TLATNRXL")
Desc.properties["cell_leakage_power"] = "829.502694"
Desc.properties["cell_footprint"] = "tlatnr"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNRXL"]=Desc
Desc = cellDescClass("TLATNSRX1")
Desc.properties["cell_leakage_power"] = "1041.092190"
Desc.properties["cell_footprint"] = "tlatnsr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSRX1"]=Desc
Desc = cellDescClass("TLATNSRX2")
Desc.properties["cell_leakage_power"] = "1337.160474"
Desc.properties["cell_footprint"] = "tlatnsr"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSRX2"]=Desc
Desc = cellDescClass("TLATNSRX4")
Desc.properties["cell_leakage_power"] = "2098.212660"
Desc.properties["cell_footprint"] = "tlatnsr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",83.160000);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSRX4"]=Desc
Desc = cellDescClass("TLATNSRXL")
Desc.properties["cell_leakage_power"] = "961.330356"
Desc.properties["cell_footprint"] = "tlatnsr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("GN","RN","setup_rising")
Desc.add_arc("GN","RN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSRXL"]=Desc
Desc = cellDescClass("TLATNSX1")
Desc.properties["cell_leakage_power"] = "923.987250"
Desc.properties["cell_footprint"] = "tlatns"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",53.222400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSX1"]=Desc
Desc = cellDescClass("TLATNSX2")
Desc.properties["cell_leakage_power"] = "1148.793030"
Desc.properties["cell_footprint"] = "tlatns"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSX2"]=Desc
Desc = cellDescClass("TLATNSX4")
Desc.properties["cell_leakage_power"] = "1597.280310"
Desc.properties["cell_footprint"] = "tlatns"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSX4"]=Desc
Desc = cellDescClass("TLATNSXL")
Desc.properties["cell_leakage_power"] = "872.156808"
Desc.properties["cell_footprint"] = "tlatns"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("GN","SN","setup_rising")
Desc.add_arc("GN","SN","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",53.222400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNSXL"]=Desc
Desc = cellDescClass("TLATNX1")
Desc.properties["cell_leakage_power"] = "1347.486840"
Desc.properties["cell_footprint"] = "tlatn"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_param("area",36.590400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNX1"]=Desc
Desc = cellDescClass("TLATNX2")
Desc.properties["cell_leakage_power"] = "1746.021420"
Desc.properties["cell_footprint"] = "tlatn"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_param("area",39.916800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNX2"]=Desc
Desc = cellDescClass("TLATNX4")
Desc.properties["cell_leakage_power"] = "2663.067780"
Desc.properties["cell_footprint"] = "tlatn"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNX4"]=Desc
Desc = cellDescClass("TLATNXL")
Desc.properties["cell_leakage_power"] = "1223.907570"
Desc.properties["cell_footprint"] = "tlatn"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['D', 'GN', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("GN","D","setup_rising")
Desc.add_arc("GN","D","hold_rising")
Desc.add_arc("D","Q","combi")
Desc.add_arc("GN","Q","falling_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("GN","QN","falling_edge")
Desc.add_param("area",36.590400);
Desc.add_pin("D","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_pin_job("GN","clock")
Desc.add_pin("GN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATNXL"]=Desc
Desc = cellDescClass("TLATRX1")
Desc.properties["cell_leakage_power"] = "865.199718"
Desc.properties["cell_footprint"] = "tlatr"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATRX1"]=Desc
Desc = cellDescClass("TLATRX2")
Desc.properties["cell_leakage_power"] = "1036.609002"
Desc.properties["cell_footprint"] = "tlatr"
Desc.properties["area"] = "46.569600"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",46.569600);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATRX2"]=Desc
Desc = cellDescClass("TLATRX4")
Desc.properties["cell_leakage_power"] = "1513.070604"
Desc.properties["cell_footprint"] = "tlatr"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATRX4"]=Desc
Desc = cellDescClass("TLATRXL")
Desc.properties["cell_leakage_power"] = "829.144350"
Desc.properties["cell_footprint"] = "tlatr"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATRXL"]=Desc
Desc = cellDescClass("TLATSRX1")
Desc.properties["cell_leakage_power"] = "1003.185810"
Desc.properties["cell_footprint"] = "tlatsr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSRX1"]=Desc
Desc = cellDescClass("TLATSRX2")
Desc.properties["cell_leakage_power"] = "1291.005378"
Desc.properties["cell_footprint"] = "tlatsr"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",59.875200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSRX2"]=Desc
Desc = cellDescClass("TLATSRX4")
Desc.properties["cell_leakage_power"] = "2171.417220"
Desc.properties["cell_footprint"] = "tlatsr"
Desc.properties["area"] = "83.160000"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",83.160000);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSRX4"]=Desc
Desc = cellDescClass("TLATSRXL")
Desc.properties["cell_leakage_power"] = "968.955534"
Desc.properties["cell_footprint"] = "tlatsr"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'RN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("G","RN","setup_falling")
Desc.add_arc("G","RN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("RN","Q","clear")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_arc("RN","QN","preset")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("RN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSRXL"]=Desc
Desc = cellDescClass("TLATSX1")
Desc.properties["cell_leakage_power"] = "878.734170"
Desc.properties["cell_footprint"] = "tlats"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",53.222400);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSX1"]=Desc
Desc = cellDescClass("TLATSX2")
Desc.properties["cell_leakage_power"] = "1107.248778"
Desc.properties["cell_footprint"] = "tlats"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSX2"]=Desc
Desc = cellDescClass("TLATSX4")
Desc.properties["cell_leakage_power"] = "1609.635564"
Desc.properties["cell_footprint"] = "tlats"
Desc.properties["area"] = "69.854400"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",69.854400);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSX4"]=Desc
Desc = cellDescClass("TLATSXL")
Desc.properties["cell_leakage_power"] = "869.456430"
Desc.properties["cell_footprint"] = "tlats"
Desc.properties["area"] = "53.222400"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'SN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("G","SN","setup_falling")
Desc.add_arc("G","SN","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("SN","Q","preset")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_arc("SN","QN","clear")
Desc.add_param("area",53.222400);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("SN","input")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATSXL"]=Desc
Desc = cellDescClass("TLATX1")
Desc.properties["cell_leakage_power"] = "770.041080"
Desc.properties["cell_footprint"] = "tlat"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_param("area",36.590400);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATX1"]=Desc
Desc = cellDescClass("TLATX2")
Desc.properties["cell_leakage_power"] = "1004.987250"
Desc.properties["cell_footprint"] = "tlat"
Desc.properties["area"] = "39.916800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_param("area",39.916800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATX2"]=Desc
Desc = cellDescClass("TLATX4")
Desc.properties["cell_leakage_power"] = "1622.523960"
Desc.properties["cell_footprint"] = "tlat"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_param("area",56.548800);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATX4"]=Desc
Desc = cellDescClass("TLATXL")
Desc.properties["cell_leakage_power"] = "744.671880"
Desc.properties["cell_footprint"] = "tlat"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'Q', 'QN', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("D","QN","combi")
Desc.add_arc("G","QN","rising_edge")
Desc.add_param("area",36.590400);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.add_pin("QN","output")
Desc.add_pin_func("QN","unknown")
Desc.set_job("latch")
CellLib["TLATXL"]=Desc
Desc = cellDescClass("TTLATX1")
Desc.properties["cell_leakage_power"] = "1164.955770"
Desc.properties["cell_footprint"] = "ttlat"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'OE', 'Q', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("OE","Q","three_state_disable")
Desc.add_arc("OE","Q","three_state_enable")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("OE","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("latch")
CellLib["TTLATX1"]=Desc
Desc = cellDescClass("TTLATX2")
Desc.properties["cell_leakage_power"] = "1941.197400"
Desc.properties["cell_footprint"] = "ttlat"
Desc.properties["area"] = "63.201600"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'OE', 'Q', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("OE","Q","three_state_disable")
Desc.add_arc("OE","Q","three_state_enable")
Desc.add_param("area",63.201600);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("OE","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("latch")
CellLib["TTLATX2"]=Desc
Desc = cellDescClass("TTLATX4")
Desc.properties["cell_leakage_power"] = "3055.004100"
Desc.properties["cell_footprint"] = "ttlat"
Desc.properties["area"] = "76.507200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'OE', 'Q', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("OE","Q","three_state_disable")
Desc.add_arc("OE","Q","three_state_enable")
Desc.add_param("area",76.507200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("OE","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("latch")
CellLib["TTLATX4"]=Desc
Desc = cellDescClass("TTLATXL")
Desc.properties["cell_leakage_power"] = "918.875502"
Desc.properties["dont_touch"] = "true"
Desc.properties["dont_use"] = "true"
Desc.properties["cell_footprint"] = "ttlat"
Desc.properties["area"] = "43.243200"
Desc.pinOrder = ['D', 'G', 'IQ', 'IQN', 'OE', 'Q', 'next']
Desc.add_arc("G","D","setup_falling")
Desc.add_arc("G","D","hold_falling")
Desc.add_arc("D","Q","combi")
Desc.add_arc("G","Q","rising_edge")
Desc.add_arc("OE","Q","three_state_disable")
Desc.add_arc("OE","Q","three_state_enable")
Desc.add_param("area",43.243200);
Desc.add_pin("D","input")
Desc.set_pin_job("G","clock")
Desc.add_pin("G","input")
Desc.add_pin("IQ","output")
Desc.add_pin_func("IQ","unknown")
Desc.add_pin("OE","input")
Desc.add_pin("next","output")
Desc.add_pin_func("next","unknown")
Desc.add_pin("Q","output")
Desc.add_pin_func("Q","unknown")
Desc.add_pin("IQN","output")
Desc.add_pin_func("IQN","unknown")
Desc.set_job("latch")
CellLib["TTLATXL"]=Desc
Desc = cellDescClass("XNOR2X1")
Desc.properties["cell_leakage_power"] = "1496.827350"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2X1"]=Desc
Desc = cellDescClass("XNOR2X2")
Desc.properties["cell_leakage_power"] = "2696.948460"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "36.590400"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",36.590400);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2X2"]=Desc
Desc = cellDescClass("XNOR2X4")
Desc.properties["cell_leakage_power"] = "5408.167500"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2X4"]=Desc
Desc = cellDescClass("XNOR2XL")
Desc.properties["cell_leakage_power"] = "1317.856716"
Desc.properties["cell_footprint"] = "xnor2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XNOR2XL"]=Desc
Desc = cellDescClass("XNOR3X2")
Desc.properties["cell_leakage_power"] = "4481.070660"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XNOR3X2"]=Desc
Desc = cellDescClass("XNOR3X4")
Desc.properties["cell_leakage_power"] = "8438.400180"
Desc.properties["cell_footprint"] = "xnor3"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",99.792000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XNOR3X4"]=Desc
Desc = cellDescClass("XOR2X1")
Desc.properties["cell_leakage_power"] = "1704.108780"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XOR2X1"]=Desc
Desc = cellDescClass("XOR2X2")
Desc.properties["cell_leakage_power"] = "2882.649060"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "33.264000"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",33.264000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XOR2X2"]=Desc
Desc = cellDescClass("XOR2X4")
Desc.properties["cell_leakage_power"] = "5674.152060"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "56.548800"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",56.548800);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XOR2X4"]=Desc
Desc = cellDescClass("XOR2XL")
Desc.properties["cell_leakage_power"] = "1343.813166"
Desc.properties["cell_footprint"] = "xor2"
Desc.properties["area"] = "26.611200"
Desc.pinOrder = ['A', 'B', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_param("area",26.611200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("B","input")
CellLib["XOR2XL"]=Desc
Desc = cellDescClass("XOR3X2")
Desc.properties["cell_leakage_power"] = "4534.880580"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["area"] = "59.875200"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",59.875200);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XOR3X2"]=Desc
Desc = cellDescClass("XOR3X4")
Desc.properties["cell_leakage_power"] = "8686.940580"
Desc.properties["cell_footprint"] = "xor3"
Desc.properties["area"] = "99.792000"
Desc.pinOrder = ['A', 'B', 'C', 'Y']
Desc.add_arc("A","Y","combi")
Desc.add_arc("B","Y","combi")
Desc.add_arc("C","Y","combi")
Desc.add_param("area",99.792000);
Desc.add_pin("A","input")
Desc.add_pin("Y","output")
Desc.add_pin_func("Y","unknown")
Desc.add_pin("C","input")
Desc.add_pin("B","input")
CellLib["XOR3X4"]=Desc
