
import logs

def help_main(Env):
    Mod = Env.Current
    if Mod.alwayses == []:
        combicell(Mod)
    else:
        flipflopcell(Mod)

def flipflopcell(Mod):
    Lines = []
    Lines.append('`timescale 1ns / 1ps\nmodule %s (\n' % Mod.Module)
    Pref = ' '
    Outs = []
    Inps = []
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Dir == 'input':
            Lines.append('    %sinput [63:0] %s\n' % (Pref,Net))
            Pref = ','
            Inps.append(Net)
        elif Dir == 'output':
            Lines.append('    %soutput reg [63:0] %s\n' % (Pref,Net))
            Outs.append(Net)
            Pref = ','
    Lines.append(');\n')
    Lines.extend(Lines1)
    Lines.append('reg [63:0] IQ,IQN;\n')
    Inps.sort()
    ALLS = []
    for Inp in Inps:
        ALLS.append('%s[0]' % Inp)
    ALLS = ','.join(ALLS)

    Alw = Mod.alwayses[0]
    Sense = Alw[0]
    Body = Alw[1]
    Mod.FF = {}
    Cpins = []
    for Inp in Inps:
        if sense(Inp,Sense):
            Cpins.append(Inp)

    Dpins = []
    if Body[0] == 'ifelse':
        Cond = Body[1]
        Yes0 = Body[2]
        No0 = Body[3]

        Var0 = Yes0[1]
        Val0 = Yes0[2]
        Dpins.append(Val0)

        Var1 = No0[1]
        Val1 = No0[2]
        Dpins.append(Val1)

        Expr = ['question',Cond,Val0,Val1]
        Mod.FF[Var0] = Expr
    elif Body[0] == "<=":
        Var0 = Body[1]
        Val0 = Body[2]
        Dpins.append(Val0)
        Mod.FF[Var0] = Val0
        
    else:
        logs.log_error("ALWAYS BODY %s" % str(Body))
    Funcs = {}
    for Out in Outs:
        Func = getFunc(Mod,Out)
        Funcs[Out] = Func
        writeDelayFuncOut(Mod,Out)
    Dpins = cleanDpins(Dpins)
    for Pos,Inp in enumerate(Inps):
#        Lines.append('integer %s_interconnect = 0;\n' % Inp)
        if sense(Inp,Sense):
#            Lines.append('integer prev%s = 0;\n' % Inp)
            for Out in Outs:
                Lines.append('always @(%s[0]) begin\n' % sense(Inp,Sense))
                Func = getFunc(Mod,Out)
#                Lines.append('    #(%s_interconnect);\n' % Inp)
                Lines.append('    $python("flopcheck_clk()",Instance,"%s","%s");\n' % (Inp,' '.join(Dpins)))
#                Lines.append('    prev%s = $stime;\n' % Inp)
                Lines.append('    I%s[0] = %s;\n' % (Out,Funcs[Out]))
                Lines.append('    if (I%s[0] !== %s[0]) begin\n' % (Out,Out))
                Lines.append('        I%s[7:1] = 0;\n' % (Out))
                Lines.append('        I%s[15:8] = %s[15:8];\n' % (Out,Inp))
                Lines.append('        I%s[31:16] = 0;\n' % Out)
                Lines.append('        I%s[47:32] = %s[47:32];\n' % (Out,Inp))
                Lines.append('        I%s[63:48] = selfid;\n' % Out)
                Lines.append('        $python("dly_%s_%s()",Instance,"%s");\n' % (Mod.Module,Out,Inp))
                Lines.append('        Delay = I%s[0] ? Dly1 : Dly0;\n' % Out)
                Lines.append('        #(Delay);\n')
                Lines.append('        %s = I%s;\n' % (Out,Out))
                Lines.append('    end\n')
                Lines.append('end\n')
        else:
            Lines.append('always @(%s[0]) begin\n' % Inp)
#            Lines.append('    #(%s_interconnect);\n' % Inp)
            Lines.append('    $python("flopcheck_data()",Instance,"%s","%s");\n' % (Inp,' '.join(Cpins)))
            Lines.append('end\n')
        Lines.append("integer time_%s = 0; always @(%s) time_%s = $stime();\n" % (Inp,Inp,Inp))
    Lines.append('endmodule\n')
    Fout = open('%s.sdfv' % Mod.Module,"w")
    for Line in Lines:
        Fout.write(Line)
    Fout.close()

def cleanDpins(Dpins):
    Res = []
    for D in Dpins:
        if (type(D) is str) and D[0].isalpha():
            Res.append(D)
    return Res

def sense(Inp,Sense):
    if Sense[0] == 'list':
        for Item in Sense[1:]:
            if Item[2] == Inp:
                return "%s %s" % (Item[1],Item[2])
    elif (Inp == Sense[2]):
        return "%s %s" % (Sense[1],Sense[2])
    return False

def combicell(Mod):
    Lines = []
    Lines.append('`timescale 1ns / 1ps\nmodule %s (\n' % Mod.Module)
    Pref = ' '
    Outs = []
    Inps = []
    Mod.FF = {}
    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        if Dir == 'input':
            Lines.append('    %sinput [63:0] %s\n' % (Pref,Net))
            Pref = ','
            Inps.append(Net)
        elif Dir == 'output':
            Lines.append('    %soutput reg [63:0] %s\n' % (Pref,Net))
            Outs.append(Net)
            Pref = ','
            writeDelayFuncOut(Mod,Net)
    Lines.append(');\n')
    Lines.extend(Lines0)
    for Lt in Outs:
        Lines.append('reg [63:0] YY_%s;\n' % Lt)
    Inps.sort()
    ALLS = []
    for Inp in Inps:
        ALLS.append('%s[0]' % Inp)
    ALLS = ','.join(ALLS)
    Funcs = {}
    for Out in Outs:
        Func = getFunc(Mod,Out)
        Funcs[Out] = Func
    for Pos,Inp in enumerate(Inps):
#        Lines.append('integer %s_interconnect = 0;\n' % Inp)
        for Out in Outs:
            Lines.append('always @(%s) begin\n' % Inp)
#            Lines.append('    #(%s_interconnect);\n' % Inp)
            Func = getFunc(Mod,Out)
            Lines.append('    YY_%s[0] = %s;\n' % (Out,Funcs[Out]))
            Lines.append('    if (YY_%s[0] !== %s[0]) begin\n' % (Out,Out))
#            Lines.append('        YY_%s[7:1] = ((^%s[7:1]) === 1\'bx) ? 1 : (%s[7:1]+1);\n' % (Out,Inp,Inp))
            Lines.append('        YY_%s[7:1] = %s[7:1]+1;\n' % (Out,Inp))
            Lines.append('        YY_%s[63:8] = %s[63:8];\n' % (Out,Inp))
            Lines.append('        $python("dly_%s_%s()",Instance,"%s");\n' % (Mod.Module,Out,Inp))
            Lines.append('        Delay = YY_%s[0] ? Dly1 : Dly0;\n' % Out)
            Lines.append('        #(Delay);\n')
            Lines.append('        %s = YY_%s;\n' % (Out,Out))
            Lines.append('    end\n')
            Lines.append('end\n')
    Lines.append('endmodule\n')
    Fout = open('%s.sdfv' % Mod.Module,"w")
    for Line in Lines:
        Fout.write(Line)
    Fout.close()

def getFunc(Mod,Net):
    for Dst,Src,_,_ in Mod.hard_assigns:
        if Dst == Net:
            if (type(Src) is str)and (Src in Mod.nets):
                return getFunc(Mod,Src)
            elif (Src[0] == '!') and (Src[1] in Mod.FF):
                IQ = getFunc(Mod,Src[1])
                return '~%s' % IQ
            else:
                Src = replaceZeroes(Src[:])
                return Mod.pr_expr(Src)
            return Src
    if Net in Mod.FF:
        Src = Mod.FF[Net]
        if (type(Src) is str)and (Src in Mod.nets):
            YY =  getFunc(Mod,Src)
            return YY
        else:
            Src = replaceZeroes(Src[:])
            return Mod.pr_expr(Src)
    return Net

def replaceZeroes(Lst):
    if type(Lst) is str:
        if Lst == 'question': return Lst
        if Lst[0] in '|()&^!~': return Lst
        if "[0]" in Lst: return Lst
        return '%s[0]' % Lst
    if type(Lst) is list:
        for ind,Item in enumerate(Lst):
            X = replaceZeroes(Item)
            Lst[ind] = X
    return Lst


Lines0 = '''
reg [1023:0] Instance;
initial begin
    $sformat(Instance,"%m");
end
integer Delay,Dly0,Dly1; initial begin Delay=1; Dly0=1; Dly1 = 1; end
'''

Lines1 = '''
reg [1023:0] Instance;
reg [15:0] selfid;
initial begin
    #1;
    $sformat(Instance,"%m");
    tb.Ids = tb.Ids + 1;
    selfid = tb.Ids;
    tb.Names[selfid] = Instance;
    tb.Kinds[selfid] = 2;
    $display("ACQUIRE %s %d 2", Instance,selfid);
end
integer Delay,Dly0,Dly1; initial begin Delay=1; Dly0=1; Dly1 = 1; end

'''

def writeDelayFuncOut(Mod,Out):
    Fname = "delayfuncs/dly_%s_%s.py" % (Mod.Module,Out)
    Fout = open(Fname,"w")
    Fout.write("def dly_%s_%s (Inst,Inps,Pos):\n" % (Mod.Module,Out))
    Fout.write("    print(veri.stime(),'DELAY %s')\n" % Mod.Module)
    Fout.write("    Instx = logs.bin2str(Inst)\n")
    Fout.write("    veri.force('%s.Delay' % Instx,'5')\n")
    Fout.close()


if __name__ == '__main__': main()
