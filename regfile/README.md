
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

