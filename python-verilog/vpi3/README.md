# How to install  for Linux 
**for iverilog look below**

1. cd goto to where You want my vlsistuff installed. best: your home (~)
2. git clone https://github.com/greenblat/vlsistuff.git
3. cd vlsistuff/python-verilog/vpi3/
4. copy vpi3.setup to my_vpi3.setup
5. edit my_vpi3.setup to reflect Your system.
6. source my_vpi3.setup
5. run comp_linux


8. If Your server doesnt have libpython3.X.so - You need to beg IT, or install yourself.
   cd vlsistuff/external_software
   source python_run
   this will install python3.10 in ~/lib and ~/include and ~/bin/
   modify my_vpi3.setup to reflect these paths (PYTHONLIB and PYTHONINC1)

9. in cadence  
    copy run_cadence to Your preferred simulation location and modify the script to match Your system.
    source my_vpi3.setup
    invoke run_cadence to run the test.


# Install for icarus / iverilog

1. source my_vpi3.setup 
2. run comp3_icarus 
3. cd to 



