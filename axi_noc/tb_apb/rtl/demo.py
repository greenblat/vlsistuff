
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


ADDR_MAP["key0"] = 0x0
key0 = 0x0
DEFAULTS["key0"] = 0x0
ADDR_MAP["key1"] = 0x10
key1 = 0x10
DEFAULTS["key1"] = 0x0
