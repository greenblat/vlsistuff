
import os,sys,string
import types
import traceback


import module_class
import logs


def help_main(Env):
    Mod = Env.Current
    for Dst,Src,_,_ in Mod.hard_assigns:
        Set = module_class.support_set(Src)
        logs.log_info('%s <- %s'%(Dst,Set))

    for Net in Mod.nets:
        Dir,Wid = Mod.nets[Net]
        logs.log_info('net %s  --- dir=%s wid=%s'%(Net,Dir,Wid))

    for Always in Mod.alwayses :
        logs.log_info('always %s'%str(Always))


    for Inst in Mod.insts:
        Obj = Mod.insts[Inst]
        logs.log_info('inst=%s kind=%s pins=%s'%(Inst,Obj.Type,Obj.conns.keys()))


    if Mod.functions.keys()==[]:
        logs.log_info('no functions defined')
    if Mod.tasks.keys()==[]:
        logs.log_info('no tasks defined')
    if Mod.generates==[]:
        logs.log_info('no generates defined')
#  functions generates tasks

    Dir = dir(Mod)
    for Item in Dir:
        print Item,type(eval('Mod.%s'%Item))


