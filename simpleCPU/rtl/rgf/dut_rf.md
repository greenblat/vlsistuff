 - addrwid 16
 - empty 0xdeadbeef
 - reset async
 - width 32


|addr|reg   |field|pos|access|width|reset|desc|
|----|------|-----|---|------|-----|-----|----|
|0x0|version| | |ro|32|0x122dd0a|"version date"|
|0x4|reg0| | |rw|96| |"first wide register"|
|0x10|status| | |ro|32| |"value of counter"|
|0x14|counter_start| | |rw_pulse|32| |"start the counter"|
|0x18|interrupts| | |w1c|32| |"interrupts keeper"|
|0x1c|set_interrupt| | |rw_pulse|5| |"sat named interrupt"|
