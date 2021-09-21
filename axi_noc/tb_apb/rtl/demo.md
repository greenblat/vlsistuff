 - addrwid 20
 - bus apb
 - empty 0xdeadbeaf
 - reset async
 - width 32


|addr|reg   |field|pos|access|width|reset|desc|
|----|------|-----|---|------|-----|-----|----|
|0x0|key0| | |rw|128| |"key for 64 bit encryptions"|
|0x10|key1| | |rw|128| |"key for 64 bit encryptions"|
|0x20|limits0|**array**  depth=|8|rw|20| |" 8 low limit regs"|
|0x40|limits1|**array**  depth=|8|rw|20| |" 8 high limit regs"|
