 - addrwid 32
 - addrwidth 32
 - bus apb
 - width 32


|addr|reg   |field|pos|access|width|reset|desc|
|----|------|-----|---|------|-----|-----|----|
|0x0|enable| | |rw|1|0x0|"enable"|
|0x4|scalefactor| | |rw|4|0x0|"scale back factor of sum before output"|
|0x8|coeffs|**array**  depth=|8|rw|8| |"coeffs"|
|0x28|goods| | |ro|32| |"number of no saturations"|
|0x2c|bads| | |ro|32| |"number of saturations"|
