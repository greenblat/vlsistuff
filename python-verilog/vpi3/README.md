# How to install  

1. cd goto to where You want my vlsistuff installed. best: your home (~)
2. git clone https://github.com/greenblat/vlsistuff.git
3. cd vlsistuff/python-verilog/vpi3/
4. cp comp_linux_local  comp_linux_mine
5. edit comp_linux_mine


this is the file:

set INC1 = /home/iliag/local/include/python3.X
set LIB = /home/iliag/local/lib
set MTI_HOME = /tools/cdnc/XCELIUM/current/tools.lnx86/include/


gcc  -c -O3 src/vpi3_local.c src/qq64.c \
     -Wall \
     -I$INC1 \
     -I$MTI_HOME \
     -fPIC \



ld -shared  -export-dynamic  \
    -o my_vpi3.so \
    vpi3_local.o qq64.o \
    -L/usr/lib \
    -L$LIB \
    -lpython3.X \
    -lc  -lpthread -lutil \


6. modify  INC1/LIB/MTI_HOME  lines to match Your server.
   INC1  =  change to the path where include/python3.X
   LIB where the libpython3.X.so (or dylib) is.
   MTI_HOME = where cadence or synopsys simulators includes are.
   replace all python3.X to python3.10 (or 8 or 9)

7. make sure all python3.X letters are the same and match the version of python. best is 10 for now.

8. If Your server doesnt have libpython3.X.so - You need to beg IT, or install yourself.
   cd vlsistuff/external_software
   source python_run
   this will install python3.10 in ~/lib and ~/include and ~/bin/
   Add /home/YOU/lib to Your LD_LIBRARY_PATH (setenv or export).
    usually:  setenv LD_LIBRARY_PATH   /home/jacob/lib        ---- will do the trick.

    in ~/bin/ You will find pip3.10 - but it refuses to install packages, because of some SSH issue. I dont know how to solve that. If You do - share with me, please.

9. in cadence or synopsys run scripts add 
add full path of "my_vpi3.so" - look in above directory for activation_cadence synopsys for example.
