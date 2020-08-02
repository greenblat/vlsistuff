
import os,sys,string
import types
import logs
import traceback
import random

from scan_rtl import  scan_statements,is_edged_timing,get_sensitivity_list,compute1
from extract_expr_nets import extract_sigs
from rtl_width import  get_width
from module_class import module_class,instance_class,pr_expr
from executes import try_and_load_module
import logs

def help_main(Env):
    Mod = Env.Current
    Env.Flib = open('%s.lib'%Mod.Module,'w')
    Flib = Env.Flib
    Flib.write('%s'%string.replace(HEADER,'XXXX',Mod.Module))
    Flib.write('cell(%s) {\n%s\n'%(Mod.Module,HEADER2))
    IOS = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Nets = expandBus(Net,Wid)
        if Dir in ['output','input','output reg']:
            Dirx = string.replace(Dir,' reg','')
            for N1 in Nets: IOS.append((N1,Dirx))
    IOS.sort()
    for Pin,Dir in IOS:
        Str = string.replace(PIN,'PIN',Pin)
        Str = string.replace(Str,'DIR',Dir)
        Flib.write(Str)
    Flib.write('}\n')
    Flib.write('}\n')
    Flib.close()


def expandBus(Net,Wid):
    if type(Wid)==types.TupleType:
        Hi = int(Wid[0])
        Lo = int(Wid[1])
        Nets=[]
        for II in range(Hi,Lo-1,-1):
            Sig = '%s[%d]'%(Net,II)
            Nets.append(Sig)
        return Nets
    return [Net]



PIN = '''
    pin(PIN) {
        direction : DIR ;
        capacitance : 0.003 ; 
    }
'''


HEADER2 = '''
    area         : 50912.028;
    dont_use     : TRUE;
    dont_touch   : TRUE;
    interface_timing : TRUE;
'''




HEADER = '''
library(XXXX) {
    delay_model : table_lookup;
  in_place_swap_mode : match_footprint;
  library_features(report_delay_calculation);
    date : "Mon Oct 21 09:59:52 PDT 2002";
  comment : "Copyright (c) 2002 Artisan Components, Inc.  All Rights Reserved.";
    time_unit : "1ns";
  voltage_unit : "1V";
  current_unit : "1mA";
  pulling_resistance_unit : "1kohm";
  leakage_power_unit : "1pW";
  capacitive_load_unit (1.0,pf);
    nom_process     : 1;
  nom_temperature : 125;
  nom_voltage     : 1.62;
  operating_conditions(slow) {
    process	: 1;
    temperature	: 125;
    voltage	: 1.62;
    tree_type	: balanced_tree;
  }
  default_operating_conditions : slow;
    slew_lower_threshold_pct_fall : 10.0;
  slew_upper_threshold_pct_fall : 90.0;
  slew_lower_threshold_pct_rise : 10.0;
  slew_upper_threshold_pct_rise : 90.0;
  input_threshold_pct_fall      : 50.0;
  input_threshold_pct_rise      : 50.0;
  output_threshold_pct_fall     : 50.0;
  output_threshold_pct_rise     : 50.0;
    default_leakage_power_density	: 0.0;
  slew_derate_from_library	: 1;
  default_cell_leakage_power	: 0.0;
  default_fanout_load	: 1.0;
  default_output_pin_cap	: 0.0;
  default_inout_pin_cap	: 0.0035;
  default_input_pin_cap	: 0.0035;
  default_max_transition	: 4.5;
    lu_table_template(delay_template_7x1) {
    variable_1 : input_net_transition;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  power_lut_template(energy_template_7x1) {
    variable_1 : input_transition_time;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  lu_table_template(delay_template_7x7) {
    variable_1 : input_net_transition;
    variable_2 : total_output_net_capacitance;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
    index_2 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  power_lut_template(energy_template_7x7) {
    variable_1 : input_transition_time;
    variable_2 : total_output_net_capacitance;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
    index_2 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  power_lut_template(energy_template_1x7) {
    variable_1 : total_output_net_capacitance;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  power_lut_template(energy_template_7x3x3) {
    variable_1 : input_transition_time;
    variable_2 : total_output_net_capacitance;
    variable_3 : equal_or_opposite_output_net_capacitance;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
    index_2 ("1000, 1001, 1002");
    index_3 ("1000, 1001, 1002");
  }
  power_lut_template(passive_energy_template_1x7) {
    variable_1 : input_transition_time;
    index_1 ("1000, 1001, 1002, 1003, 1004, 1005, 1006");
  }
  lu_table_template(setup_template_3x3) {
    variable_1 : constrained_pin_transition;
    variable_2 : related_pin_transition;
    index_1 ("1000, 1001, 1002");
    index_2 ("1000, 1001, 1002");
  }
  lu_table_template(hold_template_3x3) {
    variable_1 : constrained_pin_transition;
    variable_2 : related_pin_transition;
    index_1 ("1000, 1001, 1002");
    index_2 ("1000, 1001, 1002");
  }
  lu_table_template(recovery_template_3x3) {
    variable_1 : constrained_pin_transition;
    variable_2 : related_pin_transition;
    index_1 ("1000, 1001, 1002");
    index_2 ("1000, 1001, 1002");
  }
  lu_table_template(removal_template_3x3) {
    variable_1 : constrained_pin_transition;
    variable_2 : related_pin_transition;
    index_1 ("1000, 1001, 1002");
    index_2 ("1000, 1001, 1002");
  }
    k_process_cell_leakage_power	: 0;
  k_temp_cell_leakage_power	: 0;
  k_volt_cell_leakage_power	: 0;
  k_process_internal_power	: 0;
  k_temp_internal_power	: 0;
  k_volt_internal_power	: 0;
  k_process_rise_transition	: 1;
  k_temp_rise_transition	: 0;
  k_volt_rise_transition	: 0;
  k_process_fall_transition	: 1;
  k_temp_fall_transition	: 0;
  k_volt_fall_transition	: 0;
  k_process_setup_rise	: 1;
  k_temp_setup_rise	: 0;
  k_volt_setup_rise	: 0;
  k_process_setup_fall	: 1;
  k_temp_setup_fall	: 0;
  k_volt_setup_fall	: 0;
  k_process_hold_rise	: 1;
  k_temp_hold_rise	: 0;
  k_volt_hold_rise	: 0;
  k_process_hold_fall	: 1;
  k_temp_hold_fall	: 0;
  k_volt_hold_fall	: 0;
  k_process_min_pulse_width_high	: 1;
  k_temp_min_pulse_width_high	: 0;
  k_volt_min_pulse_width_high	: 0;
  k_process_min_pulse_width_low	: 1;
  k_temp_min_pulse_width_low	: 0;
  k_volt_min_pulse_width_low	: 0;
  k_process_recovery_rise	: 1;
  k_temp_recovery_rise	: 0;
  k_volt_recovery_rise	: 0;
  k_process_recovery_fall	: 1;
  k_temp_recovery_fall	: 0;
  k_volt_recovery_fall	: 0;
  k_process_cell_rise	: 1;
  k_temp_cell_rise	: 0;
  k_volt_cell_rise	: 0;
  k_process_cell_fall	: 1;
  k_temp_cell_fall	: 0;
  k_volt_cell_fall	: 0;
  k_process_wire_cap	: 0;
  k_temp_wire_cap	: 0;
  k_volt_wire_cap	: 0;
  k_process_wire_res	: 0;
  k_temp_wire_res	: 0;
  k_volt_wire_res	: 0;
  k_process_pin_cap	: 0;
  k_temp_pin_cap	: 0;
  k_volt_pin_cap	: 0;
    output_voltage(GENERAL) {
    vol	: 0.4;
    voh	: VDD - 0.4;
    vomin	: -0.5;
    vomax	: VDD + 0.5;
  }
  input_voltage(CMOS) {
    vil	: 0.3 * VDD;
    vih	: 0.7 * VDD;
    vimin	: -0.5;
    vimax	: VDD + 0.5;
  }
  input_voltage(TTL) {
    vil	: 0.8;
    vih	: 2;
    vimin	: -0.5;
    vimax	: VDD + 0.5;
  }
'''
