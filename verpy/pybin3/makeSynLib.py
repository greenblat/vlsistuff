


def help_main(Env):
    Mod  = Env.Current
    Fout = open('%s.lib'%Mod.Module,'w')
    Lib = LIB.replace('MODULE',Mod.Module)
    Lib = Lib.replace('LIBRARY',Mod.Module)
    Fout.write(Lib)
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if externalDir(Dir)and(Wid!=0)and( type(Wid) is tuple):
            H,L = Wid
            Name = '%s_%s_%s'%(Net,H,L)
            Type = TYPE.replace('TYPE',Name)
            Type = Type.replace('HHH',str(H))
            Type = Type.replace('LLL',str(L))
            Bits = H-L+1
            Type = Type.replace('BITS',str(Bits))
            Fout.write(Type)
            
    Fout.write(CELL.replace('MODULE',Mod.Module))
    Inputs = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if 'input' in Dir:
            Inputs.append(Net)
            
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        Str = False
        if (Wid!=0)and(type(Wid) is tuple) and externalDir(Dir):
            H,L = Wid
            Name = '%s_%s_%s'%(Net,H,L)
            Bus = BUS.replace('TYPE',Name)
            Bus = Bus.replace('BUS',Net)
            Pin = PIN.replace('PIN','%s[%s:%s]' % (Net,H,L))
            if 'input' in Dir:
                Bus = Bus.replace('DIRECTION','input')
                Pin = Pin.replace('DIRECTION','input')
                Pin = Pin.replace('TIMING','')
            elif 'inout' in Dir:
                Bus = Bus.replace('DIRECTION','inout')
                Pin = Pin.replace('DIRECTION','inout')
            elif 'output' in Dir:
                Bus = Bus.replace('DIRECTION','output')
                Pin = Pin.replace('DIRECTION','output')
            Fout.write(Bus)

            Fout.write(Pin)
            Fout.write('    }\n')

        elif 'input' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','input')
            Str = Str.replace('TIMING','')
        elif 'inout' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','inout')
        elif 'output' in Dir:
            Str = PIN.replace('PIN',Net)
            Str = Str.replace('DIRECTION','output')
            tim = ''
            for Inp in Inputs:
                tim += TIMING.replace('INPIN',Inp)
            Str = Str.replace('TIMING',tim)
        if Str:
            Fout.write(Str)
        
    Fout.write('    }\n')
    Fout.write('}\n')
    Fout.close()

def externalDir(Dir):
    if 'input' in Dir: return True
    if 'inout' in Dir: return True
    if 'output' in Dir: return True
    return False

TYPE = '''
    type ( TYPE ) {
        base_type : array;
        data_type : bit;
        bit_width : BITS;
        bit_from  : HHH;
        bit_to    : LLL;
        downto    : true;
    }
'''

BUS = '''
       bus(BUS) {
            bus_type : TYPE;
            direction            : DIRECTION;
            switch_pin           : false;
            power_down_function  : "!VDD + VSS";
            related_power_pin    : VDD;
            related_ground_pin   : VSS;
'''



CELL = '''
cell ("MODULE") {
       area : 2.4696; 
       cell_footprint : "MODULE";
       cell_leakage_power : 9.7972811e-03;
       pg_pin (VDD) {
            voltage_name : VDD;
            pg_type : "primary_power";
            direction : "input";
       }
       pg_pin (VSS) {
            voltage_name : VSS;
            pg_type : "primary_ground";
            direction : "input";
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
            TIMING
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
    bus_naming_style         : "%s[%d]" ;
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

    define(ecsm_version, library, float);

   define_group(ecsm_waveform, rise_transition);
   define_group(ecsm_waveform, fall_transition);

   define(values, ecsm_capacitance, string);
   define(index_1, ecsm_waveform, string);
   define(values, ecsm_waveform, string);
   define_group(ecsm_capacitance, pin);
   define_group(ecsm_capacitance, bus);
   define(index_1, ecsm_capacitance, string);

   define( ecsm_vtp, library, float );
   define( ecsm_vtn, library, float );

   ecsm_vtp     : 0.479;
   ecsm_vtn     : 0.482;

   ecsm_version : 2.0;

   voltage_map (VDD, 0.99) ;
   voltage_map (VSS, 0.0) ;

   lu_table_template(template_3x3) {
       variable_1 : total_output_net_capacitance;
       variable_2 : input_net_transition;
       index_1 ("0, 1, 2");
       index_2 ("0.01, 0.026135, 0.4682");
    }




'''

TIMING = '''

    timing() {
      related_pin : "INPIN";
      cell_rise(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "1, 1, 1", "1, 1, 1", "1, 1, 1"); 
      }    
      rise_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5","0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }    
      cell_fall(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "1, 1, 1", "1, 1, 1", "1, 1, 1"); 
      }    
      fall_transition(template_3x3) {
        index_1 ("0, 1.0, 2.0");
        index_2 ("0, 1.0, 2.0");
        values ( "0.5, 0.5, 0.5", "0.5, 0.5, 0.5", "0.5, 0.5, 0.5");
      }    
    }    
'''   






