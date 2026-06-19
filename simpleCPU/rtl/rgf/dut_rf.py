
FIELDS = {}
REGS = {}
DEFAULTS = {}
ADDR_MAP = {}
# = (Width, Offset)


def prepfield(Name, Val):
    if Name in FIELDS:
        (Wid, Off) = FIELDS[Name]
        Mask = (1 << Wid)-1
        Res = (Mask & Val) << Off
        return Res, ~(Mask << Off)
    return 0, 0xffffffff


def setField(Reg, Field, Val):
    if Field == 'default':
        REGS[Reg] = DEFAULTS[Reg]
        return
    Prep, Mask = prepfield(Field, Val)
    if Reg not in REGS:
        REGS[Reg] = DEFAULTS[Reg]
    REGS[Reg] = (REGS[Reg] & Mask) | Prep


ADDR_MAP["version"] = 0x0
version = 0x0
DEFAULTS["version"] = 0x122dd0a
ADDR_MAP["reg0"] = 0x4
reg0 = 0x4
DEFAULTS["reg0"] = 0x0
ADDR_MAP["status"] = 0x10
status = 0x10
DEFAULTS["status"] = 0x0
ADDR_MAP["counter_start"] = 0x14
counter_start = 0x14
DEFAULTS["counter_start"] = 0x0
ADDR_MAP["interrupts"] = 0x18
interrupts = 0x18
DEFAULTS["interrupts"] = 0x0
ADDR_MAP["set_interrupt"] = 0x1c
set_interrupt = 0x1c
DEFAULTS["set_interrupt"] = 0x0
