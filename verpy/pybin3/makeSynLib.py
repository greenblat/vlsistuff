


def help_main(Env):
    Mod  = Env.Current
    Fout = open('%s.lib'%Mod.Module,'w')
    Lib = LIB.replace('MODULE',Mod.Module)
    Lib = Lib.replace('LIBRARY',Mod.Module)
    Fout.write(Lib)
    Fout.write(STRING0.replace('MODULE',Mod.Module))
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Str = False
        if 'input' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','input')
        elif 'inout' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','inout')
        elif 'output' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','output')

        if Str:
            Fout.write(Str)
        
    Fout.write('}\n')
    Fout.close()

STRING0 = '''
cell ("MODULE") {
       area : 2.4696; 
       cell_footprint : "MODULE";
       cell_leakage_power : 9.7972811e-03;
       pg_pin (VDD) {
            voltage_name : VDD;
            pg_type : "primary_power";
            direction : "input";
            related_bias_pin : "VBP";
       }
       pg_pin (VSS) {
            voltage_name : VSS;
            pg_type : "primary_ground";
            direction : "input";
            related_bias_pin : "VBN";
       }
'''

PIN = '''
       pin (PIN) {
            capacitance : 0.001700196;
            direction : "DIRECTION";
            fall_capacitance : 0.001695509;
            max_transition : 2.222;
            related_ground_pin : VSS;
            related_power_pin : VDD;
            rise_capacitance : 0.001704883;
       }
'''


LIB = '''
library (LIBRARY) {
    date : "2021/11/22 13:49:04";
    revision : "2035.13.73";
    comment : "Copyright 1997-2021 by Ilia";
    delay_model : table_lookup;
    voltage_unit : "1V";
    current_unit : "1mA";
    leakage_power_unit : "1nW";
    time_unit : "1ns";
    capacitive_load_unit (1, "pf");
    pulling_resistance_unit : "1kohm";
    default_threshold_voltage_group : HVT40;
    /*----------------------------------------------------------------------------*/
    /* Library parameters : */
    /*----------------------------------------------------------------------------*/
    library_features (report_delay_calculation, report_power_calculation);
    in_place_swap_mode : match_footprint;
    /*----------------------------------------------------------------------------*/
    /* Attribute defaults : */
    /*----------------------------------------------------------------------------*/
    default_max_transition : 2.00;
    default_cell_leakage_power : 0.00;
    default_leakage_power_density : 1;
    default_max_fanout : 50;
    default_fanout_load : 1.0;
    default_inout_pin_cap : 0.0;
    default_input_pin_cap : 0.0;
    default_output_pin_cap : 0.0;
    /*----------------------------------------------------------------------------*/
    /* Primetime threshold information: */
    /*----------------------------------------------------------------------------*/
    slew_derate_from_library : 0.5;
    input_threshold_pct_rise : 50;
    input_threshold_pct_fall : 50;
    output_threshold_pct_rise : 50;
    output_threshold_pct_fall : 50;
    slew_lower_threshold_pct_rise : 30;
    slew_upper_threshold_pct_rise : 70;
    slew_upper_threshold_pct_fall : 70;
    slew_lower_threshold_pct_fall : 30;

    /*----------------------------------------------------------------------------*/
    /* Environmental conditions: */
    /*----------------------------------------------------------------------------*/
    nom_process : 0.999998;
    nom_temperature : -40;
    nom_voltage : 0.99;
    operating_conditions (SSG0P99VN40C) {
        process : 0.999998;
        temperature : -40;
        voltage : 0.99;
        tree_type : best_case_tree;
    }
    default_operating_conditions : SSG0P99VN40C;
    /*----------------------------------------------------------------------------*/
    /* Derating parameters: */
    /*----------------------------------------------------------------------------*/
    k_process_cell_leakage_power : 0;
    k_process_internal_power : 0;
    k_temp_cell_fall : 0;
    k_temp_cell_leakage_power : 0;
    k_temp_cell_rise : 0;
    k_temp_fall_propagation : 0;
    k_temp_fall_transition : 0;
    k_temp_hold_fall : 0;
    k_temp_hold_rise : 0;
    k_temp_internal_power : 0;
    k_temp_rise_propagation : 0;
    k_temp_rise_transition : 0;
    k_temp_setup_fall : 0;
    k_temp_setup_rise : 0;
    k_volt_cell_fall : 0;
    k_volt_cell_leakage_power : 0;
    k_volt_cell_rise : 0;
    k_volt_fall_propagation : 0;
    k_volt_fall_transition : 0;
    k_volt_hold_fall : 0;
    k_volt_hold_rise : 0;
    k_volt_internal_power : 0;
    k_volt_rise_propagation : 0;
    k_volt_rise_transition : 0;
    k_volt_setup_fall : 0;
    k_volt_setup_rise : 0;
'''
