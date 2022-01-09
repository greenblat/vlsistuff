#! /usr/bin/env python3
import os,sys,string

HELP = '''
invocation:  libertySynthetic.py  <setupfilename>

the script reads json setup file and creates liberty file accordingly
Example:
{
 "library" : "messica",
"cells"   : {
    "AND4" : { "area" : 10, "timing" : 5 }
    ,"NOR3" : { "area" : 15, "timing" : 7 }
    ,"MX2X" : { "area" : 15, "timing" : 7, "function" : " (S && A) | (!S && B)" }
}
}

'''

import json
from typing import Any, Dict, List, Optional, Tuple

def main():
    if len(sys.argv) == 1:
        print(HELP)
        return
    Fname = sys.argv[1]
    Libname = 'BASIC'
    json_info = ReadJson(Fname)
    CELLS = []
    for Inst in json_info:
        if Inst == 'library':
            Libname = json_info[Inst]
        elif Inst == 'cells':
            Cells = json_info[Inst]
            for Cell in Cells:
                Data = Cells[Cell]
                print(Libname,Cell,Data)
                CELLS.append((Cell,Data))

    Flib = open('%s.lib' % Libname,'w')
    Fnotime = open('%s_no_time.lib' % Libname,'w')
    Flib.write(HEADER.replace('LIBRARY',Libname))
    Fnotime.write(HEADER.replace('LIBRARY',Libname))
    for Cell,Data in CELLS:
        Head = CELLHEADER.replace('CELL',Cell.replace('"',''))
        Head = Head.replace('AREA',get_param('area',Data,'10'))
        OutPin,NoPin = outPin(Cell,Data)
        Flib.write(Head)
        Flib.write(OutPin)
        Fnotime.write(Head)
        Fnotime.write(NoPin)
        Inps = inPins(Cell,Data)
        for Inp in Inps:
            Pin = inPin(Cell,Inp,Data)
            Flib.write(Pin)    
            Fnotime.write(Pin)    
        Flib.write('}\n')
        Fnotime.write('}\n')

    Timing1 = CLK2Q.replace('PIN','CK')
    Timing1 = Timing1.replace('DELAY','2')
    Flops = FLOPS.replace('CLK2Q',Timing1)

    Timing2 = SETUP.replace('PIN','CK')
    Timing2 = Timing2.replace('SETUP','1')
    Flops = Flops.replace('SETUP',Timing2)
    Flib.write(Flops)
    Fnotime.write(Flops)


    Flib.write('}\n')
    Flib.close()
    Fnotime.write('}\n')
    Fnotime.close()

def outPin(Cell,Data):
    Str = '    pin (Y) {\n    direction : output;\n    capacitance : 0.0;\n   function : "%s";\n    \n ' % outFunction(Cell,Data)
    Notime = Str + '}\n'
    Pins = inPins(Cell,Data)
    for Pin in Pins:
        Tim = TIMING.replace('PIN',Pin)
        Delay = get_param('timing',Data,5)
        Tim = Tim.replace('DELAY',Delay)
        Str += Tim
    return Str + '\n}\n',Notime
def inPins(Cell,Data):
    if Cell == 'INV': return ['A']
    if Cell == 'BUF': return ['A']
    if simpleGate(Cell):
        Num = int(Cell[-1])
        X = 'ABCDEFGHKLMNOPQRST'
        Y = list(X)
        return Y[:Num]
    else:
        Func = get_param('function',Data,'A')
        List = []
        for Chr in Func:
            if Chr in string.ascii_uppercase:
                if Chr not in List: List.append(Chr)
        return List
        

def simpleGate(Cell):
    if Cell.startswith('AND') and (len(Cell) == 4): return True
    if Cell.startswith('NAND') and (len(Cell) == 5): return True
    if Cell.startswith('OR') and (len(Cell) == 3): return True
    if Cell.startswith('NOR') and (len(Cell) == 4): return True
    if Cell.startswith('XOR') and (len(Cell) == 4): return True
    if Cell.startswith('XNOR') and (len(Cell) == 5): return True
    if Cell in ['BUF','INV']: return True
    return False


def inPin(Cell,Pin,Data):
    Str = '    pin (%s) {\n    direction : input;\n    capacitance : 1.0;\n    }\n' % Pin
    return Str

def outFunction(Cell,Data):
    Pins = inPins(Cell,Data)
    if simpleGate(Cell):
        if 'INV' in Cell: Pstr = '!%s' % Pins[0]
        elif 'BUF' in Cell: Pstr = '%s' % Pins[0]
        elif 'AND' in Cell: Pstr = ' & '.join(Pins)
        elif 'XOR' in Cell: Pstr = ' ^ '.join(Pins)
        elif 'XNOR' in Cell: Pstr = ' ^ '.join(Pins)
        elif 'OR' in Cell: Pstr = ' | '.join(Pins)
    
        if (Cell[0] == 'N') or Cell.startswith('XNOR'):
            Pstr = '!( %s )' % Pstr
        return Pstr
    return get_param('function',Data,'A')



def get_param(What,Data,Default):
    if What in Data:
        return str(Data[What])
    return str(Default)

def ReadJson(file: str) -> Dict[str, Any]:
    if file and os.path.exists(file):
        with open(file, encoding="utf8") as ff: 
            return json.loads(ff.read())
    else:
        print("Error: File not exists:", file)
        raise FileNotFoundError

HEADER = '''
library (LIBRARY)  {
    date			: "today";
    revision			: "evision:";
    delay_model			: table_lookup;
    voltage_unit                : "1V";
    current_unit		: "1mA";
    leakage_power_unit          : 1pW;
    time_unit                   : "1ns";
    capacitive_load_unit (1.00000,pf);
    pulling_resistance_unit	: "1kohm";
    in_place_swap_mode		  : match_footprint;


    default_max_transition        : 2.00;
    default_cell_leakage_power    : 0.00;
    default_leakage_power_density : 1;
    default_max_fanout            : 15;
    default_fanout_load           : 1.0;
    default_inout_pin_cap         : 0.0;
    default_input_pin_cap         : 0.0;
    default_output_pin_cap        : 0.0;

    slew_derate_from_library      : 0.5;
    input_threshold_pct_rise 	  : 50;
    input_threshold_pct_fall 	  : 50;
    output_threshold_pct_rise 	  : 50;
    output_threshold_pct_fall 	  : 50;
    slew_lower_threshold_pct_rise : 30;
    slew_upper_threshold_pct_rise : 70;
    slew_upper_threshold_pct_fall : 70;
    slew_lower_threshold_pct_fall : 30;

    nom_process                 : 1.0;
    nom_temperature             : 125.0000;
    nom_voltage                 : 1.0800;
    operating_conditions(OUR_TIMING) {
	process		: 1.0;
	temperature	: 125.0000;
	voltage		: 1.800;
	tree_type	: "best_case_tree" ;
    }
    default_operating_conditions : OUR_TIMING;

    /*----------------------------------------------------------------------------*/
    /* Derating parameters: */
    /*----------------------------------------------------------------------------*/
    k_process_cell_leakage_power : 0;
    k_process_internal_power     : 0;
    k_temp_cell_fall             : 0;
    k_temp_cell_leakage_power    : 0;
    k_temp_cell_rise             : 0;
    k_temp_fall_propagation      : 0;
    k_temp_fall_transition       : 0;
    k_temp_hold_fall             : 0;
    k_temp_hold_rise             : 0;
    k_temp_internal_power        : 0;
    k_temp_rise_propagation      : 0;
    k_temp_rise_transition       : 0;
    k_temp_setup_fall            : 0;
    k_temp_setup_rise            : 0;
    k_volt_cell_fall             : 0;
    k_volt_cell_leakage_power    : 0;
    k_volt_cell_rise             : 0;
    k_volt_fall_propagation      : 0;
    k_volt_fall_transition       : 0;
    k_volt_hold_fall             : 0;
    k_volt_hold_rise             : 0;
    k_volt_internal_power        : 0;
    k_volt_rise_propagation      : 0;
    k_volt_rise_transition       : 0;
    k_volt_setup_fall            : 0;
    k_volt_setup_rise            : 0;

    /*----------------------------------------------------------------------------*/
    /* Lookup tables: */
    /*----------------------------------------------------------------------------*/
    lu_table_template(template_3x3) {
       variable_1 : total_output_net_capacitance;
       variable_2 : input_net_transition;
       index_1 ("0, 1, 2");
       index_2 ("0.01, 0.026135, 0.4682");
    }



'''

CELLHEADER = '''
   cell("CELL") {
      area : AREA;
'''
#      timing_sense : positive_unate;

TIMING = '''
    timing() {
      related_pin : "PIN";
      cell_rise(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY");
      }
      rise_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5","0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }
      cell_fall(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY");
      }
      fall_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5", "0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }
    }
   
'''


FLOPS = '''
cell  ( DFF )   {  
  area : 10 ; 
  pin ( D )   { 
    direction : input ; 
    nextstate_type : data ; 
    capacitance : 0.001 ; 
    SETUP
  } 
  pin ( CK )   { 
    direction : input ; 
    clock : true ; 
    capacitance : 0.001 ; 
  } 
  ff ( IQ,IQN )   { 
    clocked_on : "CK" ; 
    next_state : "D" ; 
   } 
  pin ( Q )   { 
    direction : output ; 
    capacitance : 0.0 ; 
    function : "IQ" ; 
    CLK2Q
  } 
 } 


cell  ( DFFRN )   {  
  area : 10 ; 
  pin ( D )   { 
    direction : input ; 
    nextstate_type : data ; 
    capacitance : 0.001 ; 
    SETUP
   } 
  pin ( CK )   { 
    direction : input ; 
    clock : true ; 
    capacitance : 0.001 ; 
  } 
  pin ( RN )   { 
    direction : input ; 
    capacitance : 0.001 ; 
   } 
  ff ( IQ,IQN )   { 
    clocked_on : "CK" ; 
    next_state : "D" ; 
    clear  : "!RN" ; 
   } 
  pin ( Q )   { 
    direction : output ; 
    function : "IQ" ; 
    CLK2Q
  } 
} 

cell  ( DFFSN )   {  
  area : 10 ; 
  pin ( D )   { 
    direction : input ; 
    capacitance : 0.001 ; 
    SETUP
  } 
  pin ( CK )   { 
    direction : input ; 
    clock : true ; 
    capacitance : 0.001 ; 
  } 
  pin ( SN )   { 
    direction : input ; 
    capacitance : 0.001 ; 
  } 
  ff ( IQ,IQN )   { 
    clocked_on : "CK" ; 
    next_state : "D" ; 
    preset : "!SN" ; 
   } 
  pin ( Q )   { 
    direction : output ; 
    function : "IQ" ; 
    CLK2Q
  } 
} 
'''

SETUP = '''
    timing() {
      related_pin : "PIN";
      timing_type : setup_rising;
      rise_constraint(template_3x3) {
        index_1 ("0.05, 2.3, 4.5"); 
        index_2 ("0.05, 2.3, 3.3"); 
        values ( "SETUP, SETUP, SETUP", "SETUP, SETUP, SETUP", "SETUP, SETUP, SETUP");
      }      
      fall_constraint(template_3x3) {
        index_1 ("0.05, 2.3, 4.5"); 
        index_2 ("0.05, 2.3, 3.3"); 
        values ( "SETUP, SETUP, SETUP", "SETUP, SETUP, SETUP", "SETUP, SETUP, SETUP");
      }      
    }

'''

CLK2Q = '''
    timing() {
      related_pin : "PIN";
      timing_type : rising_edge;
      cell_rise(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY");
      }
      rise_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5","0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }
      cell_fall(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY", "DELAY, DELAY, DELAY");
      }
      fall_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5", "0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }
    }
   
'''




if __name__ == '__main__': main()
