# LATEST FIXES
1. reg with access=w1c is clear on write ones. Incoming read-only bus sets (by ORing with register)) bits in flipflop register. reading it does nothing. writing to it will clear all bits active in PWDATA.

# LATEST FIXES

1. double fields allowed. Add suffix=SUF or prefix=SUF to the "reg" and all double fields 
    will be uniquified. If some reg doesnt have suffix/prefix, it's whole name will be used as prefix.
    suffix/prefix not used if the field is unique in the first place.

2. Order of modules in output verilog. first comes the enclosing apb module, then enclosed ram module.
3. description can be now in the form of  desc="dad afwerw werwerwe werwer\nwede". It means, it can spread over several lines. And if it has spaces or newlines - must be enclosed in "..."
4.Fields can have "align" parameter.   wid=8 align=16   : means, the field is 8 bits, but occupies 16 bits of the register layout.
5. added "templates" and "instances" of these templates. look in example. 
6. if in reg there is param in the form  "fields=external" - the regfile will output one bus and prepare <MOD>.splits file to be usable elsewhere.
field external=true   : means the verilog will output whole bus. Separate "include" file will have the fields break down. Helps move multi-field  busses across hierarchies.

7. rw_pulse and ro_pulse can have "ready=true" parameter. It means ro_pulse will force "not pready" until "<REG>_ready goes up. The idea is to sync read only read and write to unrelated clock.



# Short cheat sheet for regfile.py

 - empty =  means result when reading from non-address
 - bus may be ram or apb 
 - width is data width. address width is automatic
 - access can be rw ro  rw_pulse ro_pulse
 - first token in every line defines the line.
 - it may be: chip(once) reg array gap ram or external.
 - array has additional parameter depth=17
 - ram has wid and depth. creates interface to simple ram. not instanced inside.
 - gap can have either  abs=0x1000  or  align=8
 - fields belong to preceding reg
 - not every reg has to have reg. 
 - external : similar to ram. but no depth.
 - rw_pulse, will add pulse output to indicate this reg was written. good for driving fifos.
 - ro_pulse, will add pulse output yo indicate this reg was read. good for reading from fifos.


# usage
    read examples/*.regfile files.
    they have most of the options.
    use "run" script to test whether the script works.

