
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


ADDR_MAP["enable"] = 0x0
enable = 0x0
DEFAULTS["enable"] = 0x0
ADDR_MAP["scalefactor"] = 0x4
scalefactor = 0x4
DEFAULTS["scalefactor"] = 0x0
ADDR_MAP["goods"] = 0x28
goods = 0x28
DEFAULTS["goods"] = 0x0
ADDR_MAP["bads"] = 0x2c
bads = 0x2c
DEFAULTS["bads"] = 0x0
