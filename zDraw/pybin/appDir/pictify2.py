def pictify(Glbs, Root, File) -> bool:
    if Root not in Glbs.details:
        logs.log_error('cannot pictify "%s" - not loaded' % (Root))
        Pic = dbase.PictureClass(Root)
        Pic.add_text("NO %s" % Root, (1, 2), 0)
        Pic.alines.append([(0, 0), (3, 3)])
        Pic.alines.append([(0, 3), (3, 0)])
        Glbs.pictures[Root] = Pic
        return False  # FIX
    Mod = Glbs.details[Root]
    Module = Mod.Module
    if File:
        File.write("picture %s\n" % Module)
    Names = {}
    Params = {}
    for Key in Mod.params:
        Obj = Mod.params[Key]
        if (Obj.Param == "name") and (Obj.Value != "$inst"):
            Names[Obj.Owner] = Obj.Value
        elif Obj.Owner not in Params:
            Params[Obj.Owner] = [(Obj.Param, Obj.Value)]
        else:
            Params[Obj.Owner].append((Obj.Param, Obj.Value))
    Inps = {}
    Outs = {}
    Inouts = {}
    LongestIn = 0
    LongestOut = 0
    LposIn, LposOut = [], []
    nInps, nOuts = 0, 0
    for Inst in Mod.instances:
        Obj = Mod.instances[Inst]
        Point = Obj.Point
        Rot = Obj.Rot
        if Obj.Type == "input":
            nInps += 1
            if Inst in Names:
                Inps[Names[Inst]] = Inst, Point, Rot
                LongestIn = max(LongestIn, len(nobus(Names[Inst])))
                LposIn.append((Point[1], Names[Inst]))
            else:
                Inps[Inst] = Inst, Point, Rot
                Names[Inst] = Inst
                LongestIn = max(LongestIn, len(nobus(Inst)))
                LposIn.append((Point[1], Names[Inst]))
        elif Obj.Type == "output":
            nOuts += 1
            if Inst in Names:
                Outs[Names[Inst]] = Inst, Point, Rot
                LongestOut = max(LongestOut, len(nobus(Names[Inst])))
                LposOut.append((Point[1], Names[Inst]))
            else:
                Outs[Inst] = Inst, Point, Rot
                LongestOut = max(LongestOut, len(nobus(Inst)))
                Names[Inst] = Inst, Point, Rot
                LposOut.append((Point[1], Names[Inst]))
        elif Obj.Type == "inout":
            if Inst in Names:
                Inouts[Names[Inst]] = Inst, Point, Rot
                LposOut.append((Point[1], Names[Inst]))
            else:
                Inouts[Inst] = Inst, Point, Rot
                Names[Inst] = Inst
                LposOut.append((Point[1], Names[Inst]))

    Max = Plus + max(len(LposIn), len(LposOut))
    Xspan = Plus + (LongestIn + LongestOut + len(Module)) * 0.3
    LposOut.sort()
    LposIn.sort()
    while len(LposOut) < Max:
        LposOut.append((False, False))
        LposOut.insert(0, (False, False))

    while len(LposIn) < Max:
        LposIn.append((False, False))
        LposIn.insert(0, (False, False))

    if File:
        pictifyToFile(File, LposIn, Plus, Xspan, LposOut, Max, Module)

    pictifyToDb(Glbs, LposIn, Plus, Xspan, LposOut, Max, Module)
    return True


def pictifyToDb(Glbs, LposIn, Plus, Xspan, LposOut, Max, Module) -> None:
    Pic = dbase.PictureClass(Module)
    Glbs.pictures[Module] = Pic
    for ind, (_, Inp) in enumerate(LposIn):
        if Inp:
            Pic.pins[nobus(Inp)] = "i", (0, ind * Plus)
            Pic.alines.append([(0, ind * Plus), (0.3, ind * Plus)])
            Pic.add_text(nobus(Inp), (0.4, ind * Plus - 0.2), 0)
    Right = 0.3 + Xspan
    for ind, (_, Out) in enumerate(LposOut):
        if Out:
            Pic.pins[nobus(Out)] = "o", (Right + 0.3, ind * Plus)
            Pic.alines.append([(Right, ind * Plus), (Right + 0.3, ind * Plus)])
            Pic.add_text(
                nobus(Out), (Right - 0.3 - (len(nobus(Out)) * 0.3), ind * Plus - 0.2), 0
            )
    Pic.alines.append([(0.3, -0.5), (0.3, (Max * Plus - 1))])
    Pic.alines.append([(Right, -0.5), (Right, Max * Plus - 1)])
    Pic.alines.append([(0.3, -0.5), (Right, -0.5)])
    Pic.alines.append([(0.3, Max * Plus - 1), (Right, Max * Plus - 1)])
    Half = Right / 2 - (len(Module) / 2) * 0.3
    Pic.add_text(Module, (Half, Max / Plus), 0)
    Pic.bbox()


def pictifyToFile(File, LposIn, Plus, Xspan, LposOut, Max, Module) -> None:
    for ind, (_, Inp) in enumerate(LposIn):
        if Inp:
            File.write("pic_pin %s i xy=0,%s\n" % (nobus(Inp), ind * Plus))
            File.write("pic_aline list=0,%s,0.3,%s\n" % (ind * Plus, ind * Plus))
            File.write("pic_text %s xy=%s,%s\n" % (nobus(Inp), 0.4, ind * Plus - 0.2))

    Right = 0.3 + Xspan
    for ind, (_, Out) in enumerate(LposOut):
        if Out:
            File.write(
                "pic_pin %s i xy=%s,%s\n" % (nobus(Out), Right + 0.3, ind * Plus)
            )
            File.write(
                "pic_aline list=%s,%s,%s,%s\n"
                % (Right, ind * Plus, Right + 0.3, ind * Plus)
            )
            File.write(
                "pic_text %s xy=%s,%s\n"
                % (nobus(Out), Right - 0.3 - (len(nobus(Out)) * 0.3), ind * Plus - 0.2)
            )

    # # verticals
    File.write("pic_aline list=0.3,-0.5,0.3,%s\n" % (Max * Plus - 1))
    File.write("pic_aline list=%f,-0.5,%f,%s\n" % (Right, Right, Max * Plus - 1))
    # # horizontals
    File.write("pic_aline list=%s,%s,%s,%s\n" % (0.3, -0.5, Right, -0.5))
    File.write(
        "pic_aline list=%s,%s,%s,%s\n" % (0.3, Max * Plus - 1, Right, Max * Plus - 1)
    )

    Half = Right / 2 - (len(Module) / 2) * 0.3
    File.write("pic_text %s xy=%s,%s\n" % (Module, Half, Max / Plus))

    File.write("end\n")
    File.close()

