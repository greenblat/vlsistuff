
helpString = '''
commands:
import <module>       :  import python module, later " 
source <fname>        :  read script and execute all commands
include               :  read script,alias source
glv [1/0]             :  glv 1 will switch to using GLV parser, glv 0 is yacc parser.
top <modulename>      :  set top to module
set  VAR VALUE        :  assign VALUE to VAR variable     
load <fname>          :  load  verilog file
dirs                  :  searchdirs. if not given more dirs it will print current set.
load_mvlg <mvlgfile>  :  load all files mentioned in mvlg file.
load_deep             :  not yet.
pwd                   :  print path 
conn Net              :  connections of Net in current module
conn Net Module       :  connections of Net in  Module module
nets                  :  all I/O nets in corrent module 
nets Module           :  all I/O nets in  Module
father                :  caller of current module
father Module         :  caller of Module
find                  :  not working yet.
cd Mod1.Mod2.Mod3     :  change to Path.
insts                 :  list of current module instances 
insts Module          :  list  of Module instance
ls [Dir]              :  list of verilog files in dir or first SearchDirs.
loaded                :  list of loaded modules
os  wrds              :  make command of wrds and os.system it. 
vi                    :  edit the code of currrent module
open                  :  edit the code of currrent module
vi Module             :  edit the code of this module
open  Module          :  edit the code of this module


'''
