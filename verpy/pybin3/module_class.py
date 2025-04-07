import types,string,sys,os
import logs
import traceback
import matches
import math

logs.print_warning_messages = False

MathOps = ('** ~| ~& ~^ !^ + - * / ^ % & | && || ! ~ < > << >> >>> == <= >= != !== ~& === !==').split()
class module_class:
    def __init__(self,Name,Kind='module'):
        self.Module=Name
        self.Kind=Kind
        self.defines={}
        self.includes=[]
        self.nets={}
        self.netParams={}
        self.mems={}
        self.genvars={}
        self.insts={}
        self.alwayses=[]
        self.initials=[]
        self.hard_assigns=[]
        self.generates=[]
        self.parameters={}
        self.localparams={}
        self.defparams={}
        self.functions={}
        self.pragmas=[]
        self.newvers=[]
        self.tasks={}
        self.typedefs={}
        self.enums={}
        self.modports={}
        self.Vars={}
        self.interfaces={}
        self.version = 102
        self.stat_types={}
        self.deepInstNames = True
        self.inventedNets = 0
        self.remarks = []
    def cleanZeroNets(self):
        return
    def create_stat_types(self):
        for Inst in self.insts:
            Type = self.insts[Inst].Type
            if Type not in self.stat_types:
                self.stat_types[Type]=1
            else:
                self.stat_types[Type] +=1

    def sig_width(self,Net):
        if (type(Net) is str) and (Net in self.nets):
            _,Wid = self.nets[Net]
            if type(Wid) is int:
                return 1
            if len(Wid) == 2:
                H = self.compute_int(Wid[0])
                L = self.compute_int(Wid[1])
                return abs(H-L)+1
            if Wid[0] == 'packed':
                H = self.compute_int(Wid[1][0])
                L = self.compute_int(Wid[1][1])
                W0 = abs(H-L)+1
                H = self.compute_int(Wid[2][0])
                L = self.compute_int(Wid[2][1])
                W1 = abs(H-L)+1
                return W0 * W1
            logs.log_error('sig_width on %s got %s wid' % (Net,Wid))

        return 1


    def pr_expr(self,Expr):
        return pr_expr(Expr)
    def add_interface(self,Type,Inst,Dir):
        self.interfaces[Inst]=(Dir,Type)
    def add_typedef(self,Name,Items):
        self.typedefs[Name]=Items
    def add_enum(self,Name,Items):
        self.enums[Name]=Items
    def add_modport(self,Name,Items):
        self.modports[Name]=Items
    def add_generate(self,Statement):
        self.generates.append(Statement)
    def add_task(self,Name,Body,Ldefs=False):
        self.tasks[Name]=(Body,Ldefs);
    def add_always(self,Body,When=False,Kind='always'):
        List = support_set(Body,False)+support_set(When,False)
        self.checkDefined(List)
        self.alwayses.append((When,Body,Kind))
    def add_initial(self,Body):
        self.initials.append(Body)
    def add_include(self,Expr):
        self.includes.append(Expr)
    def add_define(self,Name,Expr):
        self.defines[Name]=Expr
    def add_net(self,Name,Dir,Wid):
        if Name:
            self.add_sig(Name,Dir,Wid)
    def add_sig(self,Name,Dir,Wid):
        if Wid==1: Wid=0
        if (Name == '&&'): breakIt() 
        if (type(Name) is str)and('{' in Name):
            return Name
        if (type(Name) is str)and('[' in Name)and (Name[0] != '\\'):
            BB = parseBus(Name)
            if len(BB) == 3:
                Bus,Hi,Lo  = BB
                return self.add_sig(['subbus',Bus,Hi,Lo],Dir,Wid)
            elif len(BB) == 5:
                return self.add_sig(BB[0],Dir,('packed',(BB[1],BB[2]),(BB[3],BB[4])))
            else:
                logs.log_error('add_sig got %d %s' % (len(BB),BB))
                return BB

        if Name=='':
            Name = 'net_%dx'%self.inventedNets
#            if Name == 'net_3x':  breakIt();
            self.inventedNets += 1
            self.add_sig(Name,Dir,Wid)
#            print("ADDSIG",Name)
            return Name
        if (type(Name) is str)and(Name[0] in '0123456789'): return Name
        if Dir not in ['input wire','output wire','wire','reg','input','output','output reg','integer','inout','tri0','tri1','output reg signed','wire signed','signed wire','reg signed','output signed','input logic','output logic','logic','genvar','output signed','input signed','wire signed','inout wire']:
            logs.log_error('add_sig got of %s dir="%s"'%(Name,Dir))
            return Name
            
        if Dir=='genvar':
            self.genvars[Name]=True
            return
            

        if Dir=='input wire': Dir='input'
        if Name=='repeat':
            logs.log_info('repeat??')
            traceback.print_stack(None,None,logs.Flogs[0])
            sys.exit()
            return Name


        if type(Name) is list:
            if Name[0] == 'subbus':
                self.add_sig(Name[1],Dir,(eval(str(Name[2])),eval(str(Name[3]))))
                return Name
            elif Dir in ['reg','wire','logic']:
                for Sig in Name:
                    self.add_sig(Sig,Dir,Wid)
            else:
                logs.log_error('add_sig got list: %s %s %s' % (str(Name),Dir,Wid))
            return Name
        if type(Name) is tuple:
            return Name
        if (Dir=='wire')and(Name in self.nets)and(Wid==0):
            return Name
        if (Dir=='wire')and(Name not in self.nets)and(type(Wid) is int):
            if Wid<2: 
                self.nets[Name] = ('wire',0)
            else:
                self.nets[Name] = ('wire',(Wid-1,0))
            return Name
        if (Dir=='reg')and(Name in self.nets):
            Pdir,Pwid=self.nets[Name]
            if (type(Wid) is tuple)and(type(Pwid) is tuple):
                Wid = list(Wid)
                Wid[0] = max(Pwid[0],Wid[0])
                Wid[1] = min(Pwid[1],Wid[1])
            if 'reg' in Pdir:
                return
            if Pdir == 'wire':
                self.nets[Name]='reg',Wid
                return
            if Pdir!='output':
               logs.log_error('module %s sig %s got reg but was=%s'%(self.Module,Name,Pdir))
               return
            self.nets[Name]='output reg',Wid
            return Name
        if Name in self.nets:
            WasDir,WasWid = self.nets[Name]
            logs.log_warning('net %s defined twice? was=%s,%s  now=%s,%s'%(Name,WasDir,WasWid,Dir,Wid))
            return Name
        else:
            WasDir='wire'
            WasWid=0
        if Dir=='wire':
            Dir=WasDir

        if (Wid==0):
            self.nets[Name] =  Dir,WasWid 
        elif(type(Wid) is tuple):
            self.nets[Name]=Dir,Wid
        elif (type(Wid) is int)and(Wid>1):
            self.nets[Name]=Dir,(Wid-1,0)
        elif (type(Wid) is int)and(Wid==1):
            self.nets[Name]=Dir,0
        elif(type(Wid) is list):
            if Name not in self.netParams:
                self.netParams[Name]={}
            try:
                for Prm,Val in Wid:
                    self.netParams[Name][Prm]=Val
            except:
                pass

        else:
            logs.log_err('add_sig %s (%s) got width %s'%(Name,Dir,Wid))
            traceback.print_stack(None,None,logs.Flogs[0])

        return Name

    def add_mem(self,Name,Dir,Wid,Wid2):
        if type(Name) is list:
            for NN in Name:
                self.nets[NN]=(Dir,('double',Wid,Wid2))
        else:
           self.nets[Name]=(Dir,('double',Wid,Wid2))
    def add_parameter(self,Name,Expr):
        self.parameters[Name]=Expr
    def add_localparam(self,Name,Expr):
        self.localparams[Name]=Expr

    def add_hard_assign(self,Dst,Src,Strength='',Delay=''):
        if (Dst =='')or(Dst==False):
            logs.log_err('add_hard_assign got dst="%s" and src="%s"'%(Dst,Src))
            traceback.print_stack(None,None,logs.Flogs[0])
            return           
        L1 = support_set(Dst,False)+support_set(Src,False)
        self.checkDefined(L1)
        self.hard_assigns.append((Dst,Src,Strength,Delay))

    def checkDefined(self,List):
        for Net in List:
            if '[' in Net:
                Net = Net[:Net.index('[')]

            Net = pureNet(Net)
            if (not myExtras(Net))and(Net not in self.nets)and(Net not in self.parameters)and(Net[0] not in '0123456789')and(Net not in self.localparams)and(Net not in self.genvars)and ('.' not in Net):
                logs.log_err('%s: net %s used before defined (%s) %s'%(self.Module,Net,Net in self.nets,'defined localparams %s %s '%(list(self.localparams.keys())[:10],list(self.parameters.keys())[:10])))
                traceback.print_stack(None,None,logs.Flogs[0])

    def duplicate_inst(self,Inst,Inst2):
        Obj = self.insts[Inst]
        NewObj = instance_class(Obj.Type,Inst2)
        self.insts[Inst2]=NewObj
        for Pin in Obj.conns:
            self.add_conn(Inst2,Pin,Obj.conns[Pin])

    def add_inst_conns(self,Type,Inst,List):
        if Inst == '': Inst = inventInst(Type)
        Obj = self.add_inst(Type,Inst)
        self.add_conns(Inst,List)
        return Obj

    def add_inst(self,Type,Inst):
        if Inst == '': Inst = inventInst(Type)
        InstObj = instance_class(Type,Inst)
        if Inst in self.insts:
            logs.log_warning("replacing %s %s with %s %s instance in %s" % (Inst,self.insts[Inst].Type,Inst,Type,self.Module))
        self.insts[Inst]=InstObj
        return InstObj
    def add_inst_param(self,Inst,Prm,Val):
        Obj = self.insts[Inst]
        Obj.add_param(Prm,Val)

    def add_conn(self,Inst,Pin,Sig):
        if (type(Sig) is list)and(len(Sig)==1):
            Sig = Sig[0]
        Obj = self.insts[Inst]
        Sig1 = busify_x(Sig)
        self.check_net_def(Sig1)
        Obj.add_conn(Pin,Sig1)
    def add_conns(self,Inst,List):
        for (Pin,Sig) in List:
            self.add_conn(Inst,Pin,Sig)
    def add_function(self,Name,Wid,Defs,Statement):
        self.functions[Name]=(Wid,Defs,Statement)

    def dump(self,Fname = '?'):
        if Fname == '?':
            Fname = '%s.dump'%self.Module
        File = open(Fname,'w') 
        
        File.write('module %s\n'%(self.Module))
        for Def in self.defines:
            File.write('    define %s %s\n'%(Def,self.defines[Def]))
        for Prm in self.parameters:
            File.write('    parameter %s %s\n'%(Prm,self.parameters[Prm]))
        for Sig in self.nets:
            File.write('    net %s %s\n'%(Sig,self.nets[Sig]))
        for HAS in self.hard_assigns:
            File.write('    assign %s\n'%(str(HAS)))
        for Func in self.functions:
            File.write('    function %s %s\n'%(Func,self.functions[Func]))
        for Func in self.tasks:
            File.write('    task %s\n'%(Func,self.tasks[Func]))
        for Alw in self.alwayses:
            File.write('    always %s\n'%(str(Alw)))
        for Alw in self.generates:
            File.write('    generate %s\n'%(str(Alw)))
        for Inst in self.insts:
            self.insts[Inst].dump(File)
        File.write('endmodule\n')
        File.close()

    def dump_new_style_header(self,Fout):
        Fout.write('%s %s'%(self.Kind,pr_expr(self.Module)))
        if list(self.parameters.keys())!=[]:
            Pref=''
            Fout.write(' #( ')
            for Prm in self.parameters:
                if Prm != '__builtins__':
                    Fout.write('%sparameter %s = %s'%(Pref,pr_expr(Prm),pr_expr(self.parameters[Prm])))
                    if Prm in self.nets: self.nets.pop(Prm)
                    Pref=','
            Fout.write(') ')
        IOS=[]
        NOIOS=[]
        IFS=[]
        NOIFS=[]
        for Sig in self.interfaces:
            Def = self.interfaces[Sig]
            if Def[0]=='ext':
                Dir=Def[1]
                IFS.append((Dir,Sig))
            else:
                NOIFS.append((Sig,Def))

        for Sig in self.nets:
            Dir,Wid = self.nets[Sig]
            if is_external_dir(Dir) and (Sig):
                IOS.append((Sig,Dir,Wid))
            else:
                NOIOS.append((Sig,Dir,Wid))
        if (IOS==[])and(IFS==[]):
            Fout.write(';\n')
        else:
            Fout.write('(\n')
            IOS.sort()
            Pref=''
            for (Name,Dir,Wid) in IOS:
                Fout.write('    %s%s %s %s\n'%(Pref,pr_dir(Dir),pr_wid(Wid),pr_expr(Name)))
                Pref=','
            for (Type,Inst) in IFS:
                Fout.write('    %s%s %s\n'%(Pref,pr_dir(Type),pr_dir(Inst)))
                Pref=','
                
            Fout.write(');\n')
        return NOIOS,NOIFS

    def dump_old_style_header(self,Fout):
        Fout.write('%s %s'%(self.Kind,pr_expr(self.Module)))
        IOS=[]
        NOIOS=[]
        for Sig in self.nets:
            Dir,Wid = self.nets[Sig]
            if Dir in ['input wire','input','output','inout','output reg','output wire','inout wire']:
                IOS.append((Sig,Dir,Wid))
            else:
                NOIOS.append((Sig,Dir,Wid))
        if IOS==[]:
            Fout.write(';\n')
        else:
            IOS.sort()
            Fout.write('(%s\n'%pr_expr(IOS[0][0]))
            for (Name,_,_) in IOS[1:]:
                Fout.write('    ,%s\n'%pr_expr(Name))
            Fout.write(');\n')
        for Prm in self.parameters:
            Fout.write('parameter %s = %s;\n'%(pr_expr(Prm),pr_expr(self.parameters[Prm])))
        for (Name,Dir,Wid) in IOS:
#            if is_double_def(Wid):
#                if Wid[0]=='packed':
#                    Fout.write('%s %s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid[1]),pr_wid(Wid[2]),pr_expr(Name)))
#                else:
#                    Fout.write('%s %s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid[1]),pr_expr(Name),pr_wid(Wid[2])))
#            else:
             Fout.write('%s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid),pr_expr(Name)))
        return NOIOS,[]

    def orderLocalParams(self):
         Base = []
         Keys = list(self.localparams.keys())
         Len = len(Keys)
         while Keys!=[]:
            for Lparam in Keys:
                Expr = self.localparams[Lparam]
                Sup = support_set(Expr)
                if (Sup == []): 
                    Base.append(Lparam)
                    Keys.remove(Lparam)
                elif allIn(Sup,self.parameters.keys()):
                    Base.append(Lparam)
                    Keys.remove(Lparam)
                elif allIn(Sup,Base):
                    Base.append(Lparam)
                    Keys.remove(Lparam)
            if len(Keys)==Len:
                logs.log_warning('orderLocalParams didnt shrink, keys left= %s'%str(Keys))
                Keys = []
            Len = len(Keys)
         return Base                    

    def expandInstArrays(self):
        Insts = list(self.insts.keys())
        for Inst in Insts:
            Obj = self.insts[Inst]
            if 'inst_width' in Obj.params:
                (Hi,Lo) = Obj.params['inst_width'][1]
                Wid = Hi-Lo+1
                for Ind in range(Hi,Lo-1,-1):
                    New = self.add_inst(Obj.Type,Inst+'_'+str(Ind))
                    for Pin in Obj.conns:
                        Sig = Obj.conns[Pin]
                        if type(Sig) is str:
                            New.conns[Pin] = Sig
                        elif Sig[0] in ['subbus']:
                            New.conns[Pin] = ('subbit',Sig[1],Ind)
                        elif Sig[0] in ['subbit','subbus','hdig','bin']:
                            New.conns[Pin] = Sig
                        elif (type(Sig) is list)and(Sig[0] == 'curly'):
                            New.conns[Pin] = Sig[Ind+1]
                        else:
                            logs.log_error('%s expand %s %s %d -> %s  %s'%(Mod.Module,Inst,Obj.Type,Wid,type(Sig),Sig))

                self.insts.pop(Inst)
                

    def dump_verilog(self,Fout=False,Flags = {'style':'new','mergehards':False,'endmodule':True}):
        ExtF = True
        if not Fout:
            ExtF = False
            Fout = open('%s.dumpv' % self.Module,"w")
        elif type(Fout) is str:
            Fout = open(Fout,"w")
            ExtF = False
        if 'style' not in Flags: Flags['style'] = 'new'
        if 'endmodule' not in Flags: Flags['endmodule'] = True
        if 'mergehards' not in Flags: Flags['mergehards'] = False

        for Note in self.remarks:
            Fout.write('// %s\n' % str(Note))
        logs.setCurrentModule('dump_verilog')
        self.expandInstArrays()
        if Flags['style'] == 'new': 
            NOIOS,NOIFS=self.dump_new_style_header(Fout)
        else:
            NOIOS,NOIFS=self.dump_old_style_header(Fout)

        Hards,Ordered = [],[]
#        if Flags['mergehards'] == True: 
#            Hards,Ordered = self.prepareForMerges()
        for Prm in self.includes:
            Fout.write('`include "%s"\n'%(Prm))
        Lparams = self.orderLocalParams()
        for Prm in self.localparams:
            if Prm not in Lparams:
                Fout.write('localparam %s = "%s";\n'%(pr_expr(Prm),self.localparams[Prm]))
        for Prm in Lparams:
            Fout.write('localparam %s = %s;\n'%(pr_expr(Prm),pr_expr(self.localparams[Prm])))
        for (Name,Dir,Wid) in NOIOS:
#            if is_double_def(Wid):
#                if Wid[0]=='packed':
##                    Fout.write('%s %s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid[1]),pr_wid(Wid[2]),pr_expr(Name)))
#                else:
#                    Fout.write('%s %s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid[1]),pr_expr(Name),pr_wid(Wid[2])))
            if (Name not in Ordered):
                Fout.write('%s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid),pr_expr(Name)))
        for (Name,Def) in NOIFS:
            Type=Def[1]
            Conns=Def[2]
            Str=''
            res=verilog_conns(Conns)
            Fout.write('%s %s(%s);\n'%(Type,Name,','.join(res)))

        for Name in self.mems:
            (Dir,Wid1,Wid2)=self.mems[Name]
            Fout.write('%s %s %s %s;\n'%(pr_dir(Dir),pr_wid(Wid1),pr_expr(Name),pr_wid(Wid2)))

        for ABCD in self.pragmas:
            Fout.write('PRAGMA %s\n' % str(ABCD))
#            Fout.write('(* %s lnum=%s *)\n'%(A[:-1],C[:-1]))
        for Name in self.modports:
            List = self.modports[Name]
            res=[]
            for XX in List:
                if type(XX) is tuple:
                    Str = '%s %s'%(XX[0],XX[1])
                else:
                    Str = XX
                res.append(Str)
            Big = ', '.join(res)
            Fout.write('modport %s ( %s );\n'%(Name,Big))
        for Name in self.genvars:
            Fout.write('genvar %s;\n'%(Name))
        for Name in self.enums:
            List = self.enums[Name]
            if type(List) is tuple:
                if List[0]=='width_singles':
                    Wid = List[1]
                    Str = ', '.join(List[2])
                    Fout.write('typedef enum logic [%s:%s] { %s } %s\n'%(Wid[0],Wid[1],Str,Name))
                elif List[0]=='singles':
                    Str = ', '.join(List[1])
                    Fout.write('typedef enum logic { %s } %s\n'%(Str,Name))
                else:
                    logs.log_err('!!!typedef enum { %s } %s\n'%(self.enums[Name],Name))
            else:
                logs.log_err('!!!typedef enum { %s } %s\n'%(self.enums[Name],Name))
        for Name,List in self.typedefs:
            Fout.write('typedef struct packed { %s } %s\n'%(self.typedefs[Name],Name))
        for (Dir,Wid,(Dst,Src,A,B)) in Hards:
            Src0 = clean_br(pr_expr(Src))
            Dst0 = pr_expr(Dst)
            if 'output' in Dir:
                Fout.write('assign  %s = %s;\n'%(Dst0,Src0))
            else:
                Fout.write('%s %s %s = %s;\n'%(Dir,pr_wid(Wid),Dst0,Src0))
        for (Dst,Src,Strength,Dly) in self.hard_assigns:
            if (Dst=='//'):
                Fout.write('// %s\n'%Src)
            else:
                Src1 = clean_br(pr_expr(Src))
                if len(Src1)>120:
                    Src2 = Src1.split('$$$')
                    Src1 = '\n  '.join(Src2)
                else:
                    Src1 = Src1.replace('$$$','')
                Src2 = splitLong(Src1)
                Fout.write('assign %s %s %s = %s;\n'%(pr_strength(Strength),pr_dly(Dly),pr_expr(Dst),Src2))
        for Inst in self.insts:
            self.insts[Inst].dump_verilog(Fout)
        for Dprm in self.defparams:
            Space = ''
            if Dprm[0][0] == '\\': Space = ' '

            Inst = simplestr(Dprm[0])


            if len(Dprm) == 3:
                Fout.write('defparam %s%s.%s  = %s ;\n' % (Inst,Space,Dprm[2],pr_expr(self.defparams[Dprm])))
            elif len(Dprm) == 2:
                Fout.write('defparam %s%s.%s = %s ;\n' % (Inst,Space,Dprm[1],pr_expr(self.defparams[Dprm])))
            elif len(Dprm) == 1:
                Fout.write('defparam %s%s = %s ;\n' % (Inst,Space,pr_expr(self.defparams[Dprm])))
            else:
                Fout.write('// ERROR: 000%d defparam %s %s ;\n' % (len(Dprm),Dprm,pr_expr(self.defparams[Dprm])))
        for Task in self.tasks:
            self.dump_task(Task,Fout)
        for Func in self.functions:
            self.dump_function(Func,Fout)
        for Initial in self.initials:
            self.dump_initial(Initial,Fout)
        for Generate in self.generates:
            Fout.write('generate\n')
            if Generate[0] in ['for','if','ifelse']:
                Statement = pr_stmt(Generate,'    ',True)
                Fout.write('%s\n'%Statement)
            elif Generate[0] == 'assigns':
                Statement = pr_stmt(Generate[1],'    ',True)
                Fout.write('%s\n'%Statement)
            else:
                for Item in Generate:
                    Statement = pr_stmt(Item,'    ',True)
                    Fout.write('%s\n'%Statement)
            Fout.write('endgenerate\n')
        for Always in self.alwayses:
            if Always:
                dump_always(Always,Fout)
    
        if Flags['endmodule']:
            Fout.write('end%s\n\n'%self.Kind)
        if not ExtF:
            Fout.close()
        
    def prepareForMerges(self):
        Readies = []
        for Net in self.nets:
            Dir,_ = self.nets[Net]
            if ('input' in Dir)or('reg' in Dir):
                Readies.append(Net)
        for Param in self.parameters:
            Readies.append(Param)
    
        logs.log_debug('readies %s'%str(Readies))
        Ordered = []
        Hards = []
        dones = 1
        while dones>0:
            dones = self.merge_round(Readies,Ordered,Hards)
            logs.log_info('dones=%d'%dones)
        logs.log_info('merged %d'%len(Hards))
        logs.log_info('left %d'%len(self.hard_assigns))
        return Hards,Ordered
    
    
    def merge_round(self,Readies,Ordered,Hards):
        Ind = 0
        dones = 0
        while Ind<len(self.hard_assigns):
            Dst,Src,A,B = self.hard_assigns[Ind]
            Set = support_set(Src,False)
            Dset = support_set(Dst)
            Ok = goodToGo(Set,Readies,Ordered)
            if not Ok:
                logs.log_debug('failed %s net=%s ok=%s dset=%s   set=%s'%(Failed,Dst,Ok,Dset,Set))
            if Ok and (len(Dset)==1)and(Dset[0]==Dst)and not self.is_external(Dst) :
                logs.log_debug('ok net=%s'%(Dst))
                if Dst in self.nets:
                    Dir,Wid = self.nets[Dst]
                    self.nets.pop(Dst)
                else:
                    Dir,Wid = 'wire',1
                Hards.append((Dir,Wid,(Dst,Src,A,B)))
                Ordered.append(Dst)
                self.hard_assigns.pop(Ind)
                dones =+ 1
            else:
                Ind += 1
        return dones
          
    
    def dump_function(self,Func,Fout):
        X = self.functions[Func]
        Fout.write('function %s %s;\n'%(pr_wid(X[0]),Func))
        if X[1]!=[]:
            for Item in X[1]:
                if (type(Item) is list)and(len(Item)==4):
                    Fout.write('%s %s %s;\n'%(Item[3],pr_wid(Item[2]),Item[1]))
                else:
                    logs.log_err('dump_function ldefs %s '%(Item))
        Fout.write(pr_stmt(X[2],''))
        Fout.write('endfunction\n')

    def dump_task(self,Task,Fout):
        X = self.tasks[Task]
        if type(X) is list:
            Fout.write('task %s;\nbegin\n'%Task)
            Y = pr_stmt(X,'')
            Fout.write(Y)
            Fout.write('end\nendtask\n')
            return
        if type(X) is tuple:
            if len(X)==2:
                Body=X[0]
                Ldefs = X[1]
                Fout.write('task %s;\n'%Task)
                if Ldefs:
                    for Item in Ldefs:
                        if (type(Item) is tuple)and(len(Item)==3):
                            Fout.write('%s %s %s;\n'%(Item[2],pr_wid(Item[1]),Item[0]))
                        else:
                            logs.log_err('dump_task ldefs %s %s'%(Item,Ldefs))
                Fout.write('begin\n')
                Fout.write(pr_stmt(Body,''))
                Fout.write('end\nendtask\n')
                return

        logs.log_err('dump_task %s %s'%(Task,X))



    def dump_initial(self,Initial,Fout):
        if len(Initial)==0:
            return
        Statement = pr_stmt(Initial,'    ',True)
        if type(Initial) is tuple:
            Fout.write('initial %s'%(Statement.lstrip()))
        else:
            Fout.write('initial begin\n')
            Fout.write('%s'%Statement)
            Fout.write('end\n')

    def get_width(self,Net):
        if type(Net) is str:
            if Net in self.nets:
                Dir,Wid = self.nets[Net]
                return Wid
            else:
                logs.log_err('get_width got unexist net %s'%Net)
                return 0
        else:
            logs.log_err('get_width expects simple token ,it got %s'%str(Net))
            return 0

    def check_interfaces(self):
        Sigs = {}
        for Inst in self.insts:
            Obj = self.insts[Inst]
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                if type(Sig) is str:
                    Sigs[Sig]=1
        Dels=[]
        for Inst in self.insts:
            if Inst in Sigs:
                self.interfaces[Inst]=('int',self.insts[Inst].Type,self.insts[Inst].conns)
                Dels.append(Inst)
        for Inst in Dels:
            self.insts.pop(Inst)
                    



    def check_net_def(self,Net):
        if not Net: return
        if type(Net) is int: return
        if type(Net) is str:
            if "'" in Net: return
            if Net in self.insts:
                return
            if Net in self.interfaces:
                return

            Sig1 = busify_x(Net)
            if Sig1!=Net:
                self.check_net_def(Sig1)
                return
            if (Net not in self.nets)and(Net not in self.parameters)and(Net not in self.localparams):
                self.add_sig(Net,'wire',0)
                logs.log_warning('net %s defined by connection'%Net)
            return
        if type(Net) is tuple:
            self.check_net_def(list(Net))
            return
        if type(Net) is list:
            if Net[0]=='bus':
                for NN in Net[1:]:
                    self.check_net_def(NN)
                return                    
            if Net[0]=='dotted':
                return
            if Net[0]=='define':
                return
            if Net[0]=='sub_slice':
                return
            if Net[0]=='sub_slicebit':
                return
            if Net[0] in ['functioncall','funccall']:
                return
            if Net[0]=='subbit':
                Name = Net[1]
                Ind = make_int(Net[2])
                if type(Ind) is int:
                    if Name not in self.nets:
                        self.add_sig(Name,'wire',(Ind,Ind))
                        return
                    (Dir,WW) = self.nets[Name]
                    if (type(WW) is tuple)and(len(WW)==2):
                        (H,L)=WW
                        H = make_int(H)
                        L = make_int(L)
                        if type(H) is int:
                            H = max(H,Ind)
                        if type(L) is int:
                            L = min(L,Ind)
                        self.nets[Name]=(Dir,(H,L))
                    elif (type(WW) is tuple)and(len(WW)==3):
                        if WW[0] not in ['packed','double']:
                            logs.log_error('definition(1) of net %s dir=%s and wid "%s" is wrong  (%s)'%(Name,Dir,WW,Net))
                    elif (type(WW) is int):
                        self.nets[Name]=(Dir,(Ind,0))
                    else:
                        logs.log_error('definition(2) of net %s dir=%s and wid "%s" is wrong  (%s) ind %d  %s'%(Name,Dir,WW,Net,Ind,WW))
                return
            if Net[0]=='subbus':
                Name = Net[1]
                if len(Net)==3:
                    Ind0 = self.compute_int(Net[2][0])
                    Ind1 = self.compute_int(Net[2][1])
                else:
                    Ind0 = (Net[2])
                    Ind1 = Net[3]
                if Name not in self.nets:
                    logs.log_warning('declared new bus, deduced from connections %s: wire [%s:%s] %s;'%(self.Module,Ind0,Ind1,Name))
                    self.add_sig(Name,'wire',(Ind0,Ind1))
                    return
                (Dir,WW) = self.nets[Name]
                if type(WW) is tuple:
                    if WW[0]=='double':
                        return
                    if WW[0]=='packed':
                        logs.log_warning('packed: do something about it net=%s ww=%s'%(Net,WW))
                        return
                    (H,L)=WW
                    try:
                        H = max(evalz(H),evalz(Ind0))
                        L = min(evalz(L),evalz(Ind1))
                        self.nets[Name]=(Dir,(H,L))
                    except:
                        pass
                elif type(WW) is int:
                    try:
                        H = max(WW,evalz(Ind0))
                        L = min(WW,evalz(Ind1))
                        self.nets[Name]=(Dir,(H,L))
                    except:
                        pass
                    
                    
                else:
                    logs.log_error('check net def got width  name=%s dir=%s ww=%s'%(Name,Dir,WW))
                    self.nets[Name]=(Dir,WW)
                return


            if Net[0]=='curly':
                if Net[1]=='repeat':
                    for NN in Net[2:]:
                        self.check_net_def(NN)
                    return
                for NN in Net[1:]:
                    self.check_net_def(NN)
                return
            if Net[0] in ['const','hex','bin','dig']:
                return
            if Net[0] == 'repeat':
                self.check_net_def(Net[2])
                return
            if Net[0] in MathOps+['question','?']:
                for NN in Net[1:]:
                    self.check_net_def(NN)
                return

        logs.log_error('check_net_def module=%s net=%s (%s)'%(self.Module,Net,type(Net)))
        traceback.print_stack(None,None,logs.Flogs[0])

    def del_inst(self,Inst):
        Inst = clean_inst(Inst)
        if Inst in self.insts:
            self.insts.pop(Inst)
        elif '\\'+Inst in self.insts:
            self.insts.pop('\\'+Inst)
        else:
            logs.log_error('INST %s not in %s' % (Inst,self.Module))
#            for In in self.insts:
#                logs.log_info('>>> "%s"' % In)

    def relax_instance_wires_names(self):
        Insts = self.insts.keys()
        for Inst in Insts:
            Inst2 = self.relax_name(Inst)
            if Inst2!=Inst:
                Obj = self.insts[Inst]
                self.insts.pop(Inst)
                self.insts[Inst2]=Obj
                Obj.Name=Inst2
#                self.duplicate_inst(Inst,Inst2)
                
        Insts = self.insts.keys()
        Renames={}
        for Inst in Insts:
            Obj = self.insts[Inst]
            Pins = Obj.conns.keys()
            for Pin in Pins:
                Net =  Obj.conns[Pin]
                Net1 = busify_x(self.relax_name(Net,False))
                if Net!=Net1:
                    Obj.conns[Pin]=Net1
                    Renames[Net]=Net1
                    
        for Net in Renames:
            if Net in self.nets:
                self.nets.pop(Net)
        for Net in Renames:
            Net1 = Renames[Net]
            self.check_net_def(Net1)

                
    def recompute_instance_wires(self,Env):
        Wires = {}
        for Inst in self.insts:
            Obj=self.insts[Inst]
            for Pin in Obj.conns:
                Net = Obj.conns[Pin]
                self.recompute_instance_wires_helper(Net,Wires)
            Env.try_and_load_module(Obj.Type,Env)
            if Obj.Type in Env.Modules:
                Son = Env.Modules[Obj.Type]
                for Pin in Obj.conns:
                    Net = Obj.conns[Pin]
                    if type(Net) is str:
                        if Pin in Son.nets:
                            _,Wid = Son.nets[Pin]
                            if Net in self.nets:
                                Dir,_ = self.nets[Net]
                                self.nets[Net] = Dir,Wid
                            else:
                                self.nets[Net] = 'wire',Wid


        Nets = list(self.nets.keys())
        for Net in Nets:
            (Dir,WW)=self.nets[Net]
            if (Dir=='wire')and(Net not in Wires):
                logs.log_info('removing not in wires %s'%(Net))
                self.nets.pop(Net)
        for Wire in Wires:
            if Wire not in self.nets:
                Hi,Lo = Wires[Wire]
                if Hi==0:
                    self.add_sig(Wire,'wire',0)
                else:
                    self.add_sig(Wire,'wire',(Hi,Lo))


    def recompute_instance_wires_helper(self,Net,Wires):
        if not Net:
            pass
        elif type(Net) is str:
            if "'" in Net:
                pass
            elif Net not in Wires:
                Wires[Net]=(0,0)
        elif isinstance(Net,(tuple,list)):
            if Net[0] == 'bin':
                pass
            elif Net[0] in ['|']:
                for Def in Net[1:]:
                    self.recompute_instance_wires_helper(Def,Wires)
            elif Net[0] in ['curly']:
                for Def in Net[1:]:
                    self.recompute_instance_wires_helper(Def,Wires)
            elif Net[0] in ['subbit','subbus']:
                Name = Net[1]
                if Net[0]=='subbit':
                    Hi = int(Net[2])
                    Lo = Hi
                elif Net[0]=='subbus':
                    if len(Net) == 4:
                        Hi = int(Net[2])
                        Lo = int(Net[3])
                    else:
                        Hi = int(Net[2][0])
                        Lo = int(Net[2][1])
                if Name in Wires:
                    WasHi=Wires[Name][0]
                    WasLo=Wires[Name][1]
                    Hi = max(Hi,WasHi)
                    Lo = min(Lo,WasLo)
                Wires[Name]=(Hi,Lo)
            else:
                logs.log_err('net %s is strange for recompute_instance_wires'%(str(Net)))

                
    def mergeNetTableBusses(self):
        Keys = list(self.netTable.keys())
        for Key in Keys:
            if Key and ('[' in Key):
                Bus = Key[:Key.index('[')]
                if Bus in self.netTable:
                    Lbus = self.netTable[Key]
                    self.netTable[Bus].extend(Lbus)
                    self.netTable.pop(Key)
                else:
                    Lbus = self.netTable[Key]
                    self.netTable[Bus] = Lbus
                    self.netTable.pop(Key)

    def buildNetTable(self):
        self.prepareNetTable()
    def prepareNetTable(self,Bussed=False):
        netTable={}
        self.typesTable = {}
        for Net in self.nets:
            Dir,Wid = self.nets[Net]
            if 'input' in Dir:
                netTable[Net] = [(self.Module,'input',Dir)]
            elif 'output' in Dir:
                netTable[Net] = [(self.Module,'output',Dir)]
            elif 'inout' in Dir:
                netTable[Net] = [(self.Module,'inout',Dir)]
                
        for Inst in self.insts:
            Obj = self.insts[Inst]
            Type = Obj.Type
            if Type not in self.typesTable: self.typesTable[Type] = []
            self.typesTable[Type].append(Inst)
            for Pin in Obj.conns:
                NN = Obj.conns[Pin]
                Supset = support_set(NN,Bussed)
                for AA in Supset:
                    Net = hashit(AA)
                    if Net not in netTable:
                        netTable[Net]=[]
                    netTable[Net].append((Inst,Type,Pin))
        self.netTable = netTable
        return netTable

    def prepareBusNetTable(self):
        netTable={}
        for Net in self.nets:
            Dir,Wid = self.nets[Net]
            if 'input' in Dir:
                netTable[Net] = [(self.Module,'input',Dir)]
            elif 'output' in Dir:
                netTable[Net] = [(self.Module,'output',Dir)]
            elif 'inout' in Dir:
                netTable[Net] = [(self.Module,'inout',Dir)]
                
        for Inst in self.insts:
            Obj = self.insts[Inst]
            Type = Obj.Type
            for Pin in Obj.conns:
                NN = Obj.conns[Pin]
                if (type(NN) is list)and(NN[0]=='curly'):
                    for Item in NN[1:]:
                        Net = debus(Item)
                        if Net not in netTable:
                            netTable[Net]=[]
                        netTable[Net].append((Inst,Type,Pin))
                else:
                    Net = debus(NN)
                    if Net not in netTable:
                        netTable[Net]=[]
                    netTable[Net].append((Inst,Type,Pin))
        self.netTable = netTable
        return netTable


    def relax_name(self,Name,Simple=True):
        if not Name:
            return Name
        if type(Name) is list:
            if Name[0] in ['subbit','subbus']:
                Name[1]=relax_name(Name[1],Simple)
            return Name
        if type(Name)is not str:
            return Name
        if Name[0]=='\\':
            Name=Name[1:]
        for Char in ' /.*[]':
             Name = Name.replace(Char,'_')
        if Simple and ('[' in Name):
            Name = Name.replace('[','_')
            Name = Name.replace(']','_')
        return Name        

    def fix_conn_table(self,Net):
        Sigi = self.relax_name(Net,True)
        Supset = support_set(Sigi)
        for Sigx in Supset:
            if Sigx in self.netsTable:
                List = self.netsTable[Sigx]
                After=[]
                for Inst,Type,Pin in List:
                    if Inst in self.insts:
                        if Pin in self.insts[Inst].conns:
                            Con = self.insts[Inst].conns[Pin]
                            if Con==Net:
                                After.append((Inst,Type,Pin))
                if len(After)!=len(List):
                    self.netsTable[Sigx]=After
                    

    def build_connections_table(self):
        self.create_connections_table()
    def create_connections_table(self):
        self.netsTable={}
        for Inst in self.insts:
            Obj = self.insts[Inst]
            Type = Obj.Type
            for Pin in Obj.conns:
                Sig = Obj.conns[Pin]
                if type(Sig) is int:
                    pass
                else:
                    Sigi = self.relax_name(Sig,True)
                    Supset = support_set(Sigi)
                    for Sigx in Supset:
                        if '[' in Sigx:
                            Sigx  = Sigx[:Sigx.index('[')]
                        if Sigx not in self.netsTable:
                            self.netsTable[Sigx] = [(Inst,Type,Pin)]
                        else:
                            self.netsTable[Sigx].append((Inst,Type,Pin))
         
    def compute_int(self,Item,Shout=True):
        if type(Item) is int:
            return Item
        if type(Item) is str:
            if Item[0] in '0123456789':
                return int(Item)
            if Item in self.parameters:
                X = self.parameters[Item]
                return self.compute_int(X,Shout)
            if Item in self.localparams:
                X = self.localparams[Item]
                return self.compute_int(X,Shout)
    
        if type(Item) is list:
            if Item[0] in ['-','+','*','/','==']:
                A = self.compute_int(Item[1],Shout)
                B = self.compute_int(Item[2],Shout)
                try:
                    return int(eval('%s%s%s'%(A,Item[0],B)))
                except:
                    return [Item[0],A,B]
            if Item[0] in ['dig']:
                return self.compute_int(Item[2],Shout)
            if Item[0] in ['functioncall']:
                if Item[1]=='$clog2':
                    Val = self.compute_int(Item[2][0],Shout)
                    Wid = len(bin(int(Val)+1))-2
                    return Wid
            if Item[0] == 'subbit':
                return Item
            if Item[0] == 'hex':
                return int(Item[2],16)
            if Item[0] == 'dig':
                return int(Item[2],10)
            if Item[0] == 'bin':
                return int(Item[2],2)
        if Shout:
            logs.log_err('compute_int failed on "%s" %s'%(str(Item),self.Module),False)
            traceback.print_stack(None,None,logs.Flogs[0])
        return 'str'



    def createUsedRtlNets(self):
        self.usedRtlNets = {} 
        for Edge,Body,_ in self.alwayses:
            Sup  = support_set(Body,True)
            for Item in Sup: 
                if Item not in self.usedRtlNets:
                    self.usedRtlNets[Item] = ['rtl']
 
        for (Dst,Src,_,_) in self.hard_assigns:
            Sup = support_set(Src,False)
            for Item in Sup: 
                if Item in self.usedRtlNets:
                    self.usedRtlNets[Item] = ['rtl','hard']
                else:
                    self.usedRtlNets[Item] = ['hard']
    def is_output(self,Net):
        if Net not in self.nets: return False
        Dir,Wid = self.nets[Net]
        return 'output' in Dir

    def is_input(self,Net):
        if Net not in self.nets: return False
        Dir,Wid = self.nets[Net]
        return 'input' in Dir

    def is_inout(self,Net):
        if Net not in self.nets: return False
        Dir,Wid = self.nets[Net]
        return 'inout' in Dir

    def is_external(self,Net):
        if type(Net) is str:
            if Net not in self.nets: return False
            Dir,Wid = self.nets[Net]
            if 'output' in Dir: return True
            if 'input' in Dir: return True
            if 'inout' in Dir: return True
            return False
        if Net[0] in ('subbus','subbit'):
            return self.is_external(Net[1])
        if Net[0] in ('hex','dig','bin'): return False
        return False

    def computeWidth(self,Wid):
        if Wid in ['0',0]: return 1
        if type(Wid) is int: return Wid
        if type(Wid) is tuple:
            if len(Wid)==2:
                Hi = self.compute_int(Wid[0])
                Lo = self.compute_int(Wid[1])
                if (type(Hi) is int)and(type(Lo) is int):
                    WW = Hi-Lo+1
                    return WW
        if Wid[0] == 'packed':
            Hi = self.compute_int(Wid[1][0])
            Lo = self.compute_int(Wid[1][1])
            Many = abs(Hi-Lo)+1
            Hi = self.compute_int(Wid[2][0])
            Lo = self.compute_int(Wid[2][1])
            One = abs(Hi-Lo)+1
            Two = 1
            if len(Wid) == 4:
                Hi = self.compute_int(Wid[3][0])
                Lo = self.compute_int(Wid[3][1])
                Two = abs(Hi-Lo)+1

            return Many*One*Two

        logs.log_error('computeWidth got "%s"'%(str(Wid)))
        return 1

    def createCode(self,Code):
        if len(Code)==1:
            self.createCode(Code[0])
        elif (Code[0] == 'named_begin'):
            self.createCode(Code[2])
        elif (Code[0] == 'list'):
            for Item in Code[1:]:
                self.createCode(Item)
        elif (Code[0] == 'declare'):
            self.nets[Code[2]] = Code[1],Code[3]
        elif (Code[0] == 'always'):
            self.alwayses.append((Code[1][0],Code[2],'always'))
        elif (Code[0] == 'assigns'):
            self.createCode(Code[1])
        elif (Code[0] == '='):
            self.hard_assigns.append((Code[1],Code[2],'',''))
        else:                
            logs.log_error('done know to create code from %s' % (str(Code)))
        

    def explodeBus(self, Net, Pin, Expected=0):
        if not Net:
            return []
        elif type(Net) is int:
            return []
        elif type(Net) is str:
            if Net in self.parameters:
                return self.explodeBus(self.parameters[Net], Pin, Expected)
            if Net in self.nets:
                _, Wid = self.nets[Net]
                if Wid == 0:
                    return [(Net, Pin)]
                elif type(Wid) is list:
                    return []
                elif type(Wid) is tuple:
                    if len(Wid) == 2:
                        Low, High = Wid
                        return self.explodeBus(
                            ["subbus", Net, Low, High], Pin, Expected
                        )
                    if Wid[0] == "double":
                        Wid0 = Wid[1]
                        Wid1 = Wid[2]
                        Res = []
                        pinind = 0
                        for KK in range(Wid0[0], Wid0[1]):
                            for LL in range(Wid1[0], Wid1[1]):
                                Res.append(
                                    (
                                        f"{Net}[{KK}][{LL}]",
                                        f"{Pin}[{pinind}]",
                                    )
                                )
                                pinind += 1
                        return Res
                    if (Wid[0] == "packed") and (len(Wid) == 3):
                        Wid0 = Wid[1]
                        Wid1 = Wid[2]
                        Res = []
                        pinind = 0
                        for KK in range(Wid0[0], Wid0[1]):
                            for LL in range(Wid1[0], Wid1[1]):
                                Res.append(
                                    (
                                        f"{Net}[{KK}][{LL}]",
                                        f"{Pin}[{pinind}]",
                                    )
                                )
                                pinind += 1
                        return Res
                    logs.log_error(
                        "explodeBus of net {} met strange width {}".format(
                            Net, str(Wid)
                        )
                    )

            return [(Net, Pin)]
        elif (type(Net) is list) and (Net[0] == "subbit") and (Net[1] in self.nets):
            _, Wid = self.nets[Net[1]]
            if (type(Wid) is str) and (Wid[0] in ["packed", "double"]):
                Wid1 = Wid[2]
                Res = []
                pinind = 0
                for LL in range(Wid1[0], Wid1[1] + 1):
                    Res.append(
                        (
                            f"{Net[1]}[{Net[2]}][{LL}]",
                            f"{Pin}[{pinind}]",
                        )
                    )
                    pinind += 1
                return Res

            return [(f"{Net[1]}[{Net[2]}]", Pin)]
        elif (type(Net) is list) and (Net[0] == "subbit"):
            return [(f"{Net[1]}[{Net[2]}]", Pin)]

        elif (type(Net) is list) and (Net[0] in ['+','-']):
            return []
        elif (type(Net) is list) and (Net[0] == "subbus"):
            Bus = Net[1]
            if len(Net) == 3:
                Lo, Hi = Net[2]
            else:
                Lo, Hi = Net[2], Net[3]

            if "__builtins__" in self.parameters.keys():
                self.parameters.pop("__builtins__")

            Hi = deepEval(pr_expr(Hi), self.parameters)
            Lo = deepEval(pr_expr(Lo), self.parameters)
            Res = []
            run = 0
            Lo = int(Lo)
            Hi = int(Hi)
            if (Lo<0)or(Hi<0): Hi,Lo = 31,0
            if Lo<=Hi:
                for ind in range(Lo, Hi + 1):
                    Res.append((f"{Bus}[{ind}]", f"{Pin}[{run}]"))
                    run += 1
            else:
                for ind in range(Lo, Hi-1,-1):
                    Res.append((f"{Bus}[{ind}]", f"{Pin}[{run}]"))
                    run += 1
            return Res
        elif (type(Net) is list) and (Net[0] == "sub_slicebit"):
            Bus = Net[1]
            Ind0 = eval(pr_expr(Net[2]), self.parameters)
            Ind1 = eval(pr_expr(Net[3]), self.parameters)
            return [(f"{Bus}[{Ind0}][{Ind1}]", Pin)]

        elif (type(Net) is list) and (Net[0] == "curly"):
            Res = []
            for Item in Net[1:]:
                More = self.explodeBus(Item, Pin)
                for A, _ in More:
                    Res.append(A)
            for ind, Item in enumerate(Res):
                Res[ind] = Item, f"{Pin}[{ind}]"
            return Res
        elif (type(Net) is list) and (Net[0] == "hex"):
            if Net[1] == "":
                Wid = Expected
            else:
                Wid = int(Net[1])
            Val = int(Net[2], 16)
            Res = []
            for ii in range(Wid):
                Res.append((["bin", 1, (Val >> ii) & 1], f"{Pin}[{ii}]"))
            return Res
        else:
            logs.log_error("explodeBus got %s %s" % (str(Net),type(Net)))
            return []

    def use_defparams(self):
        for DFPRM in list(self.defparams.keys()):
            Val = self.defparams[DFPRM]
            if len(DFPRM) == 1:
                DFPRM0 = DFPRM[0]
                ww = DFPRM0.split('.')
                Inst,Prm  = ww
    
            if len(DFPRM) == 3:
                Inst = DFPRM[0]
                Prm = DFPRM[2]
    
            if Inst not in self.insts:
                logs.log_error('INST %s of defparam %s is not instance dfprm=%s val=%s' % (Inst,Prm,DFPRM,Val))
    
            else:
                self.insts[Inst].params[Prm] = Val
                self.defparams.pop(DFPRM)
    def exprWidth(self,Expr):
        if type(Expr) is str:
            if Expr in self.nets:
                return self.sig_width(Expr)
        if type(Expr) is list:
            if Expr[0] == 'bin': return evalz(Expr[1])
            if Expr[0] == 'hex': return evalz(Expr[1])
            if Expr[0] == 'dig': return evalz(Expr[1])
            if Expr[0] == 'subbit': return 1
            if Expr[0] == 'subbus': 
                if len(Expr) == 4:
                    Hi = Expr[2]
                    Lo = Expr[3]
                    return Hi-Lo+1
                else:
                    Hi = Expr[2][0]
                    Hi = self.compute_int(Hi)
                    Lo = Expr[2][1]
                    Lo = self.compute_int(Lo)
                    return Hi-Lo+1
            if Expr[0] in ['!','&&','||','<','>','!=','==','<=','>=']: return 1 
            if Expr[0] == 'curly':
                Wid = 0
                for Item in Expr[1:]:
                    Now = self.exprWidth(Item)
                    Wid += Now
                return Wid
            if Expr[0] == 'case':
                logs.log_info("XXXXX %s" % str(Expr))
                return 0


        logs.log_error("EXPR WIDTH %s %s" % (self.Module,Expr))
        return 0
    

def pureNet(Net):
    if type(Net) is str: return Net
    if type(Net) is int: return Net
    if type(Net) is tuple:
        return purrNet(list(Net))
    if type(Net) is list:
        if Net[0] == 'subbus': 
            return pureNet(Net[1])
        if Net[0] == 'subbit': 
            return pureNet(Net[1])
    logs.log_error('pureNet got "%s"' % str(Net))
    return str(Net)

def deepEval(Expr, Params_in):
    if type(Expr) is int:
        return Expr
    if (type(Expr) is str) and Expr.isnumeric():
        return int(Expr)

    Params = Params_in.copy()
    for Prm in Params:
        Val = Params[Prm]
        if (type(Val) is str) and Val.isnumeric():
            Params[Prm] = eval(Val)
    if "__builtins__" in Params.keys():
        Params.pop("__builtins__")
    if (type(Expr) is str) and (Expr in Params):
        return deepEval(Params[Expr],Params)
    Keys = list(Params.keys())
    for Prm in Keys:
        Val = Params[Prm]
        if type(Val) is str:
            Val = Val.replace('"', "")
            Val2 = eval(Val, Params, {"math": math})
            if "__builtins__" in Params.keys():
                Params.pop("__builtins__")
            Params[Prm] = Val2
        if type(Val) is list:
            if Val[0] == 'functioncall':
                if Val[1] == '$clog2':
                    Params[Prm] = deepEval(Val[2][0], Params)
            else:
                Params[Prm] = pr_expr(Val)
                Params[Prm] = deepEval(pr_expr(Val), Params)
    try:
        Exp0 = eval(pr_expr(Expr), Params, {"math": math})
    except:
        if "__builtins__" in Params.keys():
            Params.pop("__builtins__")
        logs.log_error(f"deepEval2 {pr_expr(Expr)} {Params}")
        return -1

    if type(Exp0) is int:
        return str(Exp0)
    if type(Exp0) is list:
        Exp0 = pr_expr(Expr)
    try:
        Exp1 = eval(Exp0, Params, {"math": math})
        if type(Exp1) is int:
            return str(Exp1)
        Exp2 = eval(Exp1, Params, {"math": math})
        if type(Exp2) is int:
            return Exp2
        Exp3 = eval(Exp2, Params, {"math": math})
        return Exp3
    except:
        if "__builtins__" in Params.keys():
            Params.pop("__builtins__")

    return 0


def dump_always(Always,Fout):
    if len(Always)==3:
        
        Timing = pr_timing(Always[0])
        Statement = pr_stmt(Always[1],'    ',True)
        Kind=Always[2]
        while '$$$' in Statement:
            ind = Statement.index('$$$')
            if ind>80:
                Repl='    \n'
            else:
                Repl = ''
            Statement = Statement[:ind]+Repl+Statement[ind+4:]
        Str = ''
        if Timing=='':
#                Fout.write('%s begin\n'%Kind)
            Str += '%s begin\n'%Kind
    
        else:
#            Fout.write('%s @(%s) begin\n'%(Kind,Timing))
            Str += '%s @(%s) begin\n'%(Kind,Timing)

#            Fout.write('%s'%Statement)
#            Fout.write('end\n')
        Str += Statement
        Str += 'end\n'
        if Fout: Fout.write(Str)
        return Str
    logs.log_err('dump_always %d %s'%(len(Always),Always))
    return ''

OPS =  ['%','~&','~|','**','~^','^','=','>=','=>','*','/','<','>','+','-','~','!','&','&&','<=','>>','>>>','<<','||','==','!=','|','!==','===']
KEYWORDS = ('subbit subbus curly while else sub_slice sub_slicebit taskcall functioncall named_begin unsigned if for ifelse edge posedge negedge list case casex casez default double_sub wait #').split()

def support_set(Sig,Bussed=True):
    Set = support_set__(Sig,Bussed)
    Set.sort()
    ind=0
    while ind<(len(Set)-1):
        if Set[ind]==Set[ind+1]:
            Set.pop(ind)
        else:
            ind += 1
    return Set
        


def support_set__(Sig,Bussed):
    if (Sig=='')or not Sig:             return []
    if (Sig=='$unconnected'):           return []
    if (Sig=='$unsigned'):              return []
    if (Sig=='$signed'):              return []
    if (Sig=='$random'):              return []
    if type(Sig) is int:    return []
    if type(Sig) is float:    return []
    if type(Sig) is str: 
        if Sig[0]=='`': return []
        if Sig[0]=='"': return []
        if Sig in OPS : return []
        if Sig in '0123456789' : return []
        if Sig in KEYWORDS : return []
        return [Sig]
    if isinstance(Sig,(tuple,list)):
        if len(Sig)==1:
            return support_set__(Sig[0],Bussed)
        if Sig[0] in ['define','const','bin','hex','dig','taskcall','dotted','$random']:
            return []
        if Sig[0]=='curly':
            Ind = 1
            if Sig[1]=='repeat': Ind=3
            res=[]
            for X in Sig[Ind:]:
                XY = support_set__(X,Bussed)
                res.extend(XY)
            return res
        if Sig[0]=='repeat':
            return support_set__(Sig[2],Bussed)
        if Sig[0]=='subbit':
            Sub = support_set__(Sig[2],Bussed)
            if Bussed:
                if Sub==[]:
                    return ['%s[%s]'%(Sig[1],Sig[2])]
                else:
                    return [Sig[1]]+Sub
            else:
                return [Sig[1]]+Sub
        if Sig[0]=='subbus':
            if Bussed:
                if len(Sig)==3:
                    return ['%s[%s:%s]'%(Sig[1],Sig[2][0],Sig[2][1])]
                elif len(Sig)==4:
                    return ['%s[%s:%s]'%(Sig[1],Sig[2],Sig[3])]
                else:
                    logs.log_err('untreated (712)support set expr %s'%(str(Sig)))
                    return []
            else:
                return [Sig[1]]
    
        if Sig[0] in OPS:
            return support_set__(Sig[1:],Bussed)
    
        if Sig[0] in ['question','?']:
            if type(Sig) is tuple: Sig = list(Sig)
            while len(Sig)<4:  Sig.append('err')
            try:
                return support_set__(Sig[1],Bussed)+support_set__(Sig[2],Bussed)+support_set__(Sig[3],Bussed)
            except:
                return support_set__(Sig[1],Bussed)+support_set__(Sig[2],Bussed)
        if Sig[0] in ['functioncall']:
            return support_set__(Sig[2],Bussed)

        res=[]
        if Sig[0]=='named_begin':
            Sigg = Sig[2:]
        else:
            Sigg = Sig[:]
        for X in Sigg:
            XY = support_set__(X,Bussed)
            res.extend(XY)
        return res


    logs.log_err('(1124) untreated support set expr %s %s'%(type(Sig),str(Sig)))
    return []





def hasit(Net):
    if type(Net) is list:
        return tuple(Net)
    return Net



class instance_class:
    def __init__(self,Type,Name):
        self.Type=Type
        self.Name=Name
        self.conns={}
        self.params={}
        self.specials={}
        self.comment=''

    def add_conn(self,Pin,Sig):
        if Pin in self.conns:
            logs.log_warning('replacing connection pin=%s inst=%s was=%s now=%s'%(Pin,self.Name,self.conns[Pin],Sig))
        self.conns[Pin]=Sig

    def add_param(self,Prm,Val):
        self.params[Prm]=Val
    def dump(self,File):
        File.write('instance %s %s %s\n'%(self.Type,hashit(self.Name),self.params))
        for Pin in self.conns:
            File.write('      conn pin=%s sig=%s\n'%(Pin,self.conns[Pin]))





    def dump_verilog(self,Fout):
        Prms = pr_inst_params(self.params)
        Many = pr_width_param(self.params)
        Fout.write('%s %s %s %s'%(pr_expr(self.Type),Prms,simplestr(pr_expr(self.Name)),Many))
        if self.conns.keys()==[]:
            Fout.write(';\n')
            return
        Fout.write('(')
        Pref='    '
        res=[]
        if ('pin0' in self.conns)and('pin1' in self.conns):
            Pins = list(self.conns.keys())
            Pins.sort()
            for Pin in Pins:
                Expr = pr_expr(self.conns[Pin])
                res.append('%s'%(Expr))

        else:
            res=verilog_conns(self.conns)
            res.sort()
        Comment = self.comment
        if Comment!='':
            Comment = '    // %s'%Comment
        try1 = ', '.join(res)
        if (len(try1)<80):
            Fout.write('%s);%s\n'%(try1,Comment))
        else:
            try2 = ('\n%s,'%Pref).join(res)
            Fout.write('%s);%s\n'%(try2,Comment))


def expr_width(Expr,Mod):
    if type(Expr) is str:
        if Expr in Mod.nets:
            return Mod.sig_width(Expr)
        else:
            logs.log_error('expr_width %s' % str(Expr))
            return 1
    if type(Expr) is int: return 32

    if type(Expr) is list:
        if Expr[0] in ['hex','dig','bin']: return Expr[1]
        if Expr[0] == 'bus': return len(Expr)-1
        if Expr[0] == 'subbus':
            Hi = Expr[2][0]
            Lo = Expr[2][1]
            return  Hi-Lo+1

    logs.log_error('expr_width %s' % str(Expr))
    return 1






def pr_width_param(Dir):
    if 'inst_width' not in Dir.keys(): return ''
    return '#(%s)'%pr_expr(Dir['inst_width'])


def pr_inst_params(Dir):
    if Dir.keys()==[]:
        return ''
    if 0 in Dir:
        res = []
        i = 0
        while i in Dir.keys():
            V = pr_expr(Dir[i])
            i+=1
            res.append(V)
        return '#(%s)'%(', '.join(res))
    res=[]
    for Prm in Dir.keys():
        if Prm != 'inst_width':
            Val = Dir[Prm]
            X = '.%s(%s)'%(pr_expr(Prm),pr_expr(Val))
            res.append(X)
    if res==[]: return ''
    return '#(%s)'%(', '.join(res))

def pr_timing(List):
    if isinstance(List,(list,tuple)):
        if List[0]=='list':
            res = map(pr_expr,List[1:])
            res = map(str,res)
            return ' or '.join(res)
        if len(List)==1:
            return pr_timing(List[0])
    return str(pr_expr(List))

def pr_stmt(List,Pref='',Begin=False):
    if List==None: return '%s;'%Pref
    if List == 'no_op': return 'no_op;'
    if type(List) is tuple:
        return pr_stmt(list(List),Pref,Begin)
    if (type(List) is int):
        return str(List)
    if (List==[]):
        return 'begin /* empty */ end '
    if (type(List) is list)and(len(List)==1):
        return pr_stmt(List[0],Pref,Begin)
    if (type(List) is list)and(len(List)>2)and(List[0]=='list')and(List[1]=='list'):
        logs.log_warning('ilia double list def')
        return pr_stmt(List[2],Pref,Begin)
    if (type(List) is list)and(List[0]=='list'):
        if len(List)==2:
            return pr_stmt(List[1],Pref,Begin)
        if Begin:
            Res=''
            Pref2=Pref
        else:
            Res='%sbegin\n'%Pref
            Pref2=Pref+'    '
        for X in List[1:]:
            Y = pr_stmt(X,Pref2)
            Res = Res + Y
        if Begin:
            return Res
        else:
            return Res+'%send\n'%Pref
    elif  type(List) is list:
        if List[0]=='comment':
            res = '%s//'%Pref
            for II in List[1:]:
                X = pr_expr(II)
                res += ' %s'%X
            return '%s\n'%(res)

        if List[0]=='list':
            logs.log_warning('ilia double list def')
            List = List[1:]
        if List[0] in ['genvar','integer']:
            Kind = List[0]
            LL = pr_expr(List[1])
            return '%s%s %s ;\n'%(Pref,Kind,LL)
            
        if List[0]=='assign':
            Dst = pr_expr(List[1])
            Src = pr_expr(List[2])
            return '%sassign %s = %s;\n'%(Pref,Dst,Src)
        if List[0]=='fork':
            CC = ['list']+List[1:]
            Fork = pr_stmt(CC,Pref+'    ',True)
            return '%sfork\n%s%sjoin\n'%(Pref,Fork,Pref)
        if List[0]=='$finish':
            return List[0]
        if List[0] == 'dotted':
            Txt = pr_expr(List)
            return '%s%s;\n'%(Pref,Txt)
        if List[0] == 'wait':
            Dly = clean_br(pr_expr(List[1]))
            return '%swait(%s);\n'%(Pref,Dly)
        if List[0] == '#':
            Dly = clean_br(pr_expr(List[1]))
            return '%s#(%s);\n'%(Pref,Dly)
            
        if List[0] in ['<=','=']:
            Dst = clean_br(pr_expr(List[1]))
            Src =split_expr(List[2],Pref+'    ')
            return '%s%s %s %s;\n'%(Pref,Dst,List[0],Src)
        if List[0]=='ifelse':
            if len(List)>4:
                logs.log_err('ifelse structure has too many items %d > %d %s'%(len(List),4,str(List)))
            Cond = clean_br(pr_expr(List[1]))
            Yes = pr_stmt(List[2],Pref+'    ',True)
            if len(List)<4:
                logs.log_err('illegal ifelse len=%d'%len(List))
                return '<><><><>'
            elif List[3]==[]:
                return '<><><>'
            elif not List[3]:
                return '<>fls<><>'
            elif List[3][0] in ['ifelse','if']:
                No = pr_stmt(List[3],Pref,True)
                No = No.lstrip()
                return '%sif(%s) begin\n%s%send else %s'%(Pref,Cond,Yes,Pref,No)
            else:
                No = pr_stmt(List[3],Pref+'    ',True)
                return '%sif(%s) begin\n%s%send else begin\n%s%send\n'%(Pref,Cond,Yes,Pref,No,Pref)
        if List[0]=='if':
            if len(List)>3:
                logs.log_err('if structure has too many items %d > %d %s'%(len(List),3,str(List)))
            Cond = clean_br(pr_expr(List[1]))
            Yes = pr_stmt(List[2],Pref+'    ',True)
            return '%sif(%s) begin\n%s%send\n'%(Pref,Cond,Yes,Pref)
        if List[0] in ['functioncall','funccall','syscall']:
            res = map(pr_expr,List[2])
            res2 = ','.join(res)
            return '%s%s(%s);\n'%(Pref,List[1],res2)
        if List[0]in ['unique_case','case','casez','casex']:
            Case = List[0].replace('unique_','unique ')
            Cond = clean_br(pr_expr(List[1]))
            Str = '%s%s (%s)\n'%(Pref,Case,Cond)
            LLL = List[2]
            if (len(LLL)>0)and(LLL[0]=='list'):
                LLL = LLL[1:]
            for Item in LLL:
                if len(Item)==2:
                    Switch,Stmt=Item
                    if (type(Switch) is list)and(len(Switch)==1):
                        Str += '%s%s: '%(Pref+'    ',pr_expr(Switch[0]))
                    else:
                        Str += '%s%s: '%(Pref+'    ',pr_expr(Switch))
                    X = pr_stmt(Stmt,Pref+'    ')
                    X = X.lstrip()
                    if (X==''): X = ';'
                    Str += X
                elif (len(Item)==4)and(Item[0]=='default'):
                    Str += '%sdefault: ;\n'%(Pref+'   ')
                else:
                    logs.log_err('bad case item "%s"'%str(Item))
            Str = Str + '%sendcase\n'%Pref
            return  Str
        if List[0]=='return':
            Val = pr_expr(List[1])
            return '%sreturn %s;\n'%(Pref,Val)


        if List[0]=='while':
            Cond = clean_br(pr_expr(List[1]))
            X = pr_stmt(List[2],Pref+'    ',True)
            Str = '%swhile(%s)begin\n'%(Pref,Cond)
            Str += X
            Str += '%send\n'%(Pref)
            return Str
        if List[0]=='for':
            Cond = clean_br(pr_expr(List[2]))
            X = pr_stmt(List[4],Pref+'    ',True)
            A1 = pr_assign_list(List[1])
            A2 = pr_assign_list(List[3])
            Str = '%sfor(%s;%s;%s)begin\n'%(Pref,A1,Cond,A2)
            Str += X
            Str += '%send\n'%(Pref)
            return Str
        if List[0]=='taskcall':
            if List[1]=='break': return ''
            Str = '%s%s;'%(Pref,List[1])
            return Str
        if List[0]=='disable':
            Str = '%sdisable %s;\n'%(Pref,List[1])
            return Str
        if List[0]=='release':
            Str = '%srelease %s;\n'%(Pref,List[1])
            return Str
        if List[0]=='force':
            Str = '%sforce %s = %s;\n'%(Pref,List[1],clean_br(pr_expr(List[2])))
            return Str
        if List[0]=='named_begin':
            X = pr_stmt(List[2],Pref+'    ',True)
            Str = '%sbegin :%s\n%s%send\n'%(Pref,List[1],X,Pref)
            return Str
        if List[0]=='empty_begin_end':
            Str = '%sbegin end\n'%(Pref)
            return Str
        if List[0]=='instance':
            Params = List[3]
            if type(Params) is list:
                PP = []
                for (A,B) in Params:
                    PP.append('.%s(%s)'%(pr_expr(A),pr_expr(B)))
                Prms = '#(%s)'%','.join(PP)                    
            else:
                Prms = pr_inst_params(List[3])
            Str0 = '%s %s %s('%(pr_expr(List[1]),Prms,pr_expr(List[2]))
            Conns = List[4]
            Pref=' '
            res=[]
            if ('pin0' in Conns)and('pin1' in Conns):
                Pins = Conns.keys()
                Pins.sort()
                for Pin in Pins:
                    Expr = pr_expr(Conns[Pin])
                    res.append('%s'%(Expr))
    
            else:
                res=verilog_conns(Conns)

            try1 = ', '.join(res)
            if (len(try1)<80):
                Str0 += '%s);\n'%(try1)
            else:
                try2 = ('\n%s,'%Pref).join(res)
                Str0 += '%s);\n'%(try2)

            return Str0

        if List[0]=='always':
            Str = dump_always([List[1],List[2],List[0]],False)
            return Str

        if List[0]=='assigns':
            L1 = List[1]
            if L1[0]=='list':
                res=''
                for Stmnt in L1[1:]:
                    if Stmnt[0]=='=':
                        Dst = pr_expr(Stmnt[1])
                        Src = pr_expr(Stmnt[2])
                        res += '%sassign %s = %s;\n'%(Pref,Dst,Src)
                    else:
                        logs.log_error('assigns got L1=%s  List=%s'%(L1,List))
                return res    
            else:
                logs.log_error('assigns got L1=%s  List=%s'%(L1,List))

        Vars = matches.matches(List,'parameter ? ?')
        if Vars:
            return '%sparameter %s  = %s;\n'%(Pref,Vars[0],pr_expr(Vars[1]))
        Vars = matches.matches(List,'localparam ? ?')
        if Vars:
            return '%slocalparam %s  = %s;\n'%(Pref,Vars[0],pr_expr(Vars[1]))

        Vars = matches.matches(List,'declare ? ? ?')
        if Vars:
            if Vars[2]==0: Vars[2]=''
            elif (Vars[2][0]=='double'):
                return '%s%s %s %s %s;\n'%(Pref,Vars[0],pr_wid(Vars[2][1]),Vars[1],pr_wid(Vars[2][2]))
            else:
                return '%s%s %s %s;\n'%(Pref,Vars[0],pr_wid(Vars[2]),Vars[1])

        if List[0]=='declare':
            Vars = matches.matches(List,'declare wire ? ?')
            if Vars:
                return 'wire %s;\n'%Vars[0]
            Vars = matches.matches(List,'declare reg ? ?')
            if Vars:
                return 'reg %s;\n'%Vars[0]
        if List[0]=='assigns':
            Vars =  matches.matches(List[1],'= ? ?',False)
            if Vars:
                Dst = pr_expr(Vars[0])
                Src = pr_expr(Vars[1])
                return 'assign %s = %s;\n'%(Dst,Src)

        if List[0]=='reg':
            if (type(List[1]) is str):
                if List[1][0]=='width':
                    Hi = pr_expr(List[1][1])
                    Lo = pr_expr(List[1][2])
                    return 'reg [%s:%s] %s;'%(Hi,Lo,List[1])
                return 'ewrror'
            else:
                return 'reg %s;'%List[1]
                
    if List in ['ILIA_FALSE','ILIA_TRUE']: return List                
    if type(List) is str:
        if List=='empty_begin_end': return ''

    if (type(List) is list)and(len(List)==1):
        return pr_stmt(List[0])

    if type(List) is tuple:
        return pr_stmt(list(List))

    logs.log_err('untreated for prnt stmt %s %s'%(Pref,List))
    traceback.print_stack(None,None,logs.Flogs[0])
    return '[error %s]'%str(List)

def split_expr(List,Pref):
    return clean_br(pr_expr(List))


def pr_assign_list(List):
    if List==[]:
        return ''
    res = []
    if List[0]=='list':
        return pr_assign_list(List[1:])
    if List[0]=='=':
        Dst = pr_expr(List[1])
        Src = clean_br(pr_expr(List[2]))
        return '%s=%s'%(Dst,Src)
        
    for Item in List:
        Res = pr_assign_list(Item)
        res.append(Res)
    return ', '.join(res)

def clean_br(Txt):
    Txt = str(Txt)
    if Txt=='':
        return ''
    if (Txt[0]=='(')and(Txt[-1]==')')and('?' not in Txt):
        return Txt[1:-1]
    return Txt

def pexpr(Src):
    return clean_br(pr_expr(Src))

def pr_dly(Dly):
    if not Dly: return ''
    if len(Dly)==0:
        return ''
    if Dly=='':
        return ''
    res=[]
    for (A,B) in Dly:
        res.append(pr_expr(B))
    return '#(%s)'%(', '.join(res))
def pr_strength(Strength):
    if Strength=='':
        return ''
    if not Strength: return ''
    A,B = Strength
    return str('(%s,%s)'%(A,B))

def pr_dir(Dir):
    if Dir=='signed wire': return 'wire signed'
    if Dir=='signed': return 'wire signed'
    return Dir

def pr_wid(Wid):
    if Wid==None:
        logs.log_err('wid is none error')
        traceback.print_stack(None,None,logs.Flogs[0])
        return 'wid is none error!!'
    if type(Wid) is int:
        if Wid<2:
            return ''
        return '[%s:0]'%(pr_expr(Wid-1))
    if (len(Wid)==3)and(Wid[0]=='double'):
        return '%s%s'%(pr_wid((Wid[2][1],Wid[2][0])),pr_wid(Wid[1]))
        
    if (len(Wid)==3)and(Wid[0]=='packed'):
        return pr_wid(Wid[1])+pr_wid(Wid[2])
    if (len(Wid)==4)and(Wid[0]=='packed'):
        return pr_wid(Wid[1])+pr_wid(Wid[2])+pr_wid(Wid[3])
    if len(Wid)==3:
        logs.log_err('pr_wid %s'%(str(Wid)))
        traceback.print_stack(None,None,logs.Flogs[0])
        return str(Wid)
    return '[%s:%s]'%(pr_expr(Wid[0]),pr_expr(Wid[1]))

def pr_replace(What):
    if What=='': return ''
    if What[0]=='\\':
        return What+' '
    return What
def pr_expr(What):
    if type(What) is int:
        return str(What)
    if type(What) is float:
        return str(What)
    if type(What) is str:
        return pr_replace(What)
    if not What:
        return ''
    if What[0]=='bus':
        X = ['curly']+What[1:]
        return pr_expr(X)
    if What[0]=='wire':
        return What[1]
    if (len(What)>1)and(What[1]=='token'):
        return What[0]
    if What[0]=='dotted':
        LL = map(pr_expr,What[1])
        LL = map(str,LL)
        return '.'.join(LL)
    if What[0]=='edge':
        return '%s %s'%(What[1],pr_expr(What[2]))
    if What[0]=='subbit':
        return '%s[%s]'%(pr_expr(What[1]),pr_expr(What[2]))
    if What[0]=='sub_slice':
        return '%s[%s][%s:%s]'%(pr_expr(What[1]),pr_expr(What[2]),pr_expr(What[3][0]),pr_expr(What[3][1]))
    if What[0] in ['double_sub','sub_slicebit']:
        return '%s[%s][%s]'%(pr_expr(What[1]),pr_expr(What[2]),pr_expr(What[3]))
    if What[0]=='subbus':
        if len(What)==4:
            return '%s[%s:%s]'%(pr_expr(What[1]),pr_expr(What[2]),pr_expr(What[3]))
        elif (len(What)==3):
            try:
                return '%s[%s:%s]'%(pr_expr(What[1]),pr_expr(What[2][0]),pr_expr(What[2][1]))
            except:
                logs.log_error('#1198# whatlen=3 %s'%str(What))
                return '"%s"'%str(What)
        else:
            logs.log_err('pr_expr %s'%(str(What)))
            return 'ERROR%s'%str(What)
    if What[0]=='bin':
        return "%s'b%s"%(What[1],What[2])
    if What[0]=='const':
        return "%s'%s"%(What[1],What[2])
    if What[0]=='hex':
        Hex = What[2]
        while Hex[0]=='_': Hex = Hex[1:]
        if What[1] in ['0',0]:
            return "'h%s"%(Hex)

        if len(What)==2: return What[1]
        return "%s'h%s"%(What[1],Hex)
    if What[0]=='dig':
        if (len(What[2])>0)and(What[2][0]=="'"): What[2] = What[2][1:]
        return "%s'd%s"%(What[1],What[2])
    if What[0] in MathOps+['!','~']:
        if len(What)==2:
            return '(%s%s)'%(What[0],pr_expr(What[1]))
        if simply_computable(What):
            X,_ = simply_computable(What)
            return str(X)
        res=[]
        for X in What[1:]:
            Y = str(pr_expr(X))
            res.append(Y)
        res1 = '(%s)'%(' %s '%What[0]).join(res)
        return res1

    if What[0]in ['=']:
        Dst  = pr_expr(What[1])
        Src  = pr_expr(What[2])
        return '%s = %s' % (Dst,Src)

    if What[0]in ['?','question']:
        Cond = pr_expr(What[1])
        Yes = pr_expr(What[2])
        if len(What)<4:
            No = 'error!!!!'
        else:
            No = pr_expr(What[3])

        Short = '(%s ? %s : %s)'%(Cond,Yes,No)
        if len(Short)<120:
            return Short
        
        return '(%s ? %s :\n     %s)'%(Cond,Yes,No)

    if What[0]=='width':
        W = What[1]
        return '[%s:%s]'%(pr_expr(W[0]),pr_expr(W[1]))
    if What[0]=='curly':
        if What[1]=='repeat':
            return '{ %s { %s }}'%(pr_expr(What[2]),pr_expr(What[3]))
        if one_bus(What[1:]):
            Bus,H,L=one_bus(What[1:])
            return pr_expr(['subbus',Bus,(H,L)])
        if single_bits(What[1:]):
            Wid,Val=single_bits(What[1:])
            if type(Val) is str:
                return pr_expr(['const',Wid,'b%s'%Val])
            else:
                return pr_expr(['const',Wid,'h%x'%Val])
        res = map(pr_expr,What[1:])
        return '{%s}'%(', '.join(res))    
    if What[0]=='define':
        if len(What)==2:
            return What[1]
        Expr  = pr_expr(What[2])
        return '%s(%s)'%(What[1],Expr)
    if What[0] in ['functioncall','funccall']:
        if len(What[2])==1:
            Str = '%s(%s)'%(What[1],pr_expr(What[2][0]))
        else:
            Str = '%s(%s)'%(What[1],pr_expr(What[2]))
        return Str
    if What[0]=='repeat':
        Str = '{%s{%s}}'%(pr_expr(What[1]),pr_expr(What[2]))
        return Str

    if isinstance(What,(tuple,list)):
        if simply_computable(What):
            X,_ = simply_computable(What)
            return str(X)
        LL=[]
        for X in What:
            Y = pr_expr(X)
            LL.append(Y)
        return ','.join(LL)

    logs.pStack('pr_expr %s'%(str(What)))
    return str('error '+str(What))


def splitLong(res1):
    if len(res1)<120: return res1
    if '+' in res1:
        ww = res1.split('+')
        res2 = ('\n    +').join(ww)
        return res2

    return res1

def simply_computable(What):
    if type(What) is int:
        return What,'aa'
    if type(What) is float:
        return What,'aa'
    if (What[0] in ['-','+','*','/'])and(len(What)==3):
        if  simply_computable(What[1]) and simply_computable(What[2]):
            A,_ = simply_computable(What[1])
            B,_ = simply_computable(What[2])
            return eval('%s%s%s'%(A,What[0],B)),'aa'
    return False        

def one_bus(List):
    if type(List) is not list:
        return False
    Run = -1
    Bus = False
    H=-1
    for Item in List:
        if type(Item) is not list:
            return False
        if Item[0]!='subbit':
            return False
        if not Bus:
            Bus=Item[1]
        elif (Bus!=Item[1]):
            return False
        try:
            Ind = int(Item[2])
        except:
            return False
        if Run<0:
            Run=Ind
            H=Ind
        elif (Ind!=(Run-1)):
            return False
        Run=Ind

    return Bus,H,Run

def single_bits(List):
    if type(List)is not list:
        return False
    if len(List)==0:
        return False
    Bits = []
    Run = -1
    Bus = False
    H=-1
    for Item in List:
        if type(Item) is not list:
            return False
        if (Item[0]=='const')and(Item[1] in ['1',1]):
            Bits.append(compute1(Item[2]))
        elif (Item[0]=='bin')and(Item[1] in ['1',1]):
            Bits.append(compute1(Item[2]))
        elif (Item[0]=='hex')and(Item[1] in ['1',1]):
            Bits.append(compute1(Item[2]))
        else:
            return False
    Bits1 = ''.join(map(str,Bits))
    Len1 = len(Bits1)
    if 'x' in Bits1: return Len1,Bits1
    if 'z' in Bits1: return Len1,Bits1
    return Len1,int(Bits1,2)

def compute1(Item):
    if type(Item) is int:
        return Item
    if type(Item) is str:
        if Item[0] in '0123456789':
            return int(Item)
        if Item in ['b0','b1']:
            return int(Item[1])
        if Item=='x': return 'x'

    if type(Item) is list:
        if Item[0] in ['-','+','*','/']:
            A = compute1(Item[1])
            B = compute1(Item[2])
            X = '%s %s %s'%(A,Item[0],B)
            try:
                return eval(X)
            except:
                logs.log_err('failed compute of "%s"'%str(X))
                return 1
        if Item[0] in ['dig']:
            return compute1(Item[2])


    logs.pStack('compute1 in moduleClass faiuled on "%s" %s'%(Item,type(Item)))
    return str(Item) 


def clean_inst(Inst):
    if (type(Inst) is not str):
        return Inst 
    Inst = Inst.replace('\\','')
    Inst = Inst.replace('[','_')
    Inst = Inst.replace(']','_')
    return Inst    

def busify_x(Sig):
    if (type(Sig) is str)and('[' in Sig)and(Sig[-1]==']')and(Sig[0]!='\\'):
        ind = Sig.index('[')
        Net = Sig[:ind]
        Inds = Sig[ind+1:-1]
        if ':' in Inds:
            ww = Inds.split(':')
            return ['subbus',Net,ww[0],ww[1]]
        return ['subbit',Net,Inds]
    return Sig

def relax_inst_name(Name):
    if isinstance(Name,(tuple,list)):
        if Name[0] in ['subbit']:
            return '%s_%s_'%(Name[1],Name[2])        
    return relax_name(Name)

def relax_name(Name,Simple=True):
    if not Name:
        return Name
    if isinstance(Name,(tuple,list)):
        if Name[0] in ['subbit','subbus']:
            Name[1]=relax_name(Name[1],Simple)
        return Name
    if type(Name) is not str:
        return Name
    if Name[0]=='\\':
        Name=Name[1:]
    Name = Name.replace('/','_')
    Name = Name.replace('.','_')
    if Simple and ('[' in Name):
        Name = Name.replace('[','_')
        Name = Name.replace(']','_')
    return Name        

def hashit(End):    
    if type(End) is list:
        if End[0]=='subbit': return pr_expr(End)
        if End[0]=='subbus': return pr_expr(End)
        for X in End:
            RR = []
            if type(X) is list:
                RR.append(tuple(X))
            else:
                RR.append(X)
        return tuple(RR)
    else:
        return End 


def is_double_def(Wid):
    if isinstance(Wid,(tuple,list,int)):
        return False
    if (len(Wid)==3)and(Wid[0] in ['packed','double']):
        return True
    if len(Wid)!=2:
        logs.log_err('bad width definition, ilia!  %s '%(str(Wid)))
        traceback.print_stack(None,None,logs.Flogs[0])
        return False
    
    return False        
    
def make_int(Str):
    try:
        return int(Str)
    except:
        return Str

def verilog_conns(Conns):
    if type(Conns) is list:
        return verilog_conns_list(Conns)
    elif type(Conns) is dict:
        return verilog_conns_dict(Conns)

def verilog_conns_list(Conns):
    res=[]
    for PS in Conns:
        [Pin,Sig]=PS
        if Sig=='':
            Expr=''
        else:
            Expr = pr_expr(Sig)
        res.append('.%s(%s)'%(pr_expr(Pin),Expr))
    return res


def verilog_conns_dict(Conns):
    res=[]
    for Pin in Conns:
        if Pin=='*':
            res.append('.*')
        else:
            Sig = Conns[Pin]
            if Sig=='':
                Expr=''
            else:
                Expr = pr_expr(Sig)
            res.append('.%s(%s)'%(pr_expr(Pin),Expr))
    return res

def orderHardAssigns(Mod,Env,Fout):
    HAS = {}
    Ordered=[]
    Ins = []
    Regs = []
    for Net in Mod.nets:
        Dir,_ = Mod.nets[Net]
        if 'input' in Dir: Ins.append(Net)
        if 'reg' in Dir: Regs.append(Net)

    for ind,(Dst,Src,_,_) in enumerate(Mod.hard_assigns):
        if Dst!='//':
            Sup0 = support_set(Dst,False)
            Sup1 = support_set(Src,False)
            HAS[ind]=(Sup0,Sup1)

    ReadyList = Ins[:]+Regs[:]
    WorkList = HAS.keys()
    ok=True
    while ok and (len(WorkList)!=0):
        pos=0
        while pos<len(WorkList):
            ind = WorkList[pos]
            Dst,Src = HAS[ind]
            if allReady(Src,ReadyList):
                WorkList.pop(pos)
                pos=999999
                ReadyList.extend(Dst)
                Ordered.append(ind)
        ok =  pos==999999

def allReady(Src,Ready):
    for Item in Src:
        if Item not in Ready: return False
    return True

def is_external_dir(Dir):
    return ('input' in Dir)or('output' in Dir)or('inout' in Dir)


def myExtras(Token):
    return Token in '( ) $time $realtime $stime wait # $high $signed empty_begin_end unique_case $display'.split()

def evalz(What):
    try:
        return eval(What)
    except:
        return What


INSTS = {}
def inventInst(Type):
    if Type not in INSTS:
        INSTS[Type]= 0 
    INSTS[Type]  += 1
    return '%s%s'%(Type,INSTS[Type])





def goodToGo(Set,Readies,Ordered):
    global Failed
    for Net in Set:
        if (Net not in Readies) and (Net not in Ordered): 
            Failed = Net
            return False
    return True

def allIn(Sup,Base):
    for A in Sup:
        if A not in Base: return False
    return True

def parseBus(Name):
    if Name[0] == '\\': return Name
    if '[' not in Name: return Name
    Name = Name.replace('[',' ')
    Name = Name.replace(']','')
    Name = Name.replace(':',' ')
    W3 = Name.split()
    try:
        if len(W3)==5: return [W3[0],eval(W3[1]),eval(W3[2]),eval(W3[3]),eval(W3[4])]
        if len(W3)==3: return [W3[0],eval(W3[1]),eval(W3[2])]
        if len(W3)==2: return [W3[0],eval(W3[1]),eval(W3[1])]
        logs.log_error('PARSE BUS %s' % Name)
    except:
        logs.log_error('PARSE BUS %s' % Name)
    return Name

def debus(Sig):
    Sig = pr_expr(Sig)
    if '[' in Sig: return Sig[:Sig.index('[')]
    if type(Sig) is str: return Sig 
            

def simplestr(Txt):
    X = Txt.replace('[','_')
    X = X.replace(']','_')
    X = X.replace('\\','')
    X = X.replace('~','_')
    X = X.replace('.','_')
    return X

def breakIt():
    print("BREAK %d %d %d" % 'no')

def splitBits(Expr,Mod,Mwid=64):
    if type(Expr) is int: 
        Res = [] 
        for ii in range(Mwid):
            X = (Expr>>ii) & 1
            if (X==1):
                Res.append('vcc')
                Mod.add_sig('vcc','input',0)
            else:
                Res.append('gnd')
                Mod.add_sig('gnd','input',0)
        Res.reverse()    
        return Res

    if type(Expr) is str:
        if Expr in Mod.parameters:
            Val = splitBits(Mod.parameters[Expr],Mod)
            return Val
        if Expr in Mod.localparams:
            Val = splitBits(Mod.localparams[Expr],Mod)
            return Val

        if Expr in Mod.nets:
            _,Wid = Mod.nets[Expr]
            if Wid in [0,1,'0','1']:
                return [Expr]
            if type(Wid) is int:
                print("SPLIT ERROR",Expr)
                return [Expr]
            if type(Wid) is tuple:
                if Wid[0] == 'packed':
                    Hi1 = Mod.compute_int(Wid[1][0])
                    Lo1 = Mod.compute_int(Wid[1][1])
                    Hi = max(Hi1,Lo1)
                    Lo = min(Hi1,Lo1)
                    
                    Hi2 = Mod.compute_int(Wid[2][0])
                    Lo2 = Mod.compute_int(Wid[2][1])

                    Hi_ = max(Hi2,Lo2)
                    Lo_ = min(Hi2,Lo2)
                    Res = ['bus']
                    while Lo2<= Hi2:
                        HH = Hi
                        while Lo_<= HH:
                            Res.append('%s[%s][%s]' % (Expr,Hi2,HH))
                            HH -= 1
                        Hi2 -= 1
                    return Res
                else:
                    Hi,Lo = Wid
                    Hi = Mod.compute_int(Hi)
                    Lo = Mod.compute_int(Lo)
                    Res = ['bus']
                    while Lo <= Hi:
                        Sig = '%s[%s]' % (Expr,Hi)
                        Res.append(Sig)
                        Hi -= 1
                    return Res
            logs.log_error('splitBits %s failed' % str(Expr))

    if type(Expr) is list:
        if len(Expr) == 1:
            return splitBits(Expr[0],Mod,Mwid)
        if Expr[0] == 'subbit':
            return ['%s[%s]' % (Expr[1],Expr[2])]
        if Expr[0] == 'curly':
            return Expr[1:]
    if type(Expr) is str: return [Expr]

    print("ERROR EXPR SPLIT",Expr)
    breakIt()
    return [Expr]


    
