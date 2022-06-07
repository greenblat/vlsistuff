

import logs


def help_main(Env):
    Mod = Env.Current
    for Alw,Body,Kind in Mod.alwayses:
        scanRst(Body)

def scanRst(Body):
    if type(Body) is list:
        if Body[0] == 'list':
            for Item in Body[1:]:
                scanRst(Item)
        elif Body[0] == 'ifelse':
            Cond = Body[1]
            if (Cond == 'softreset') or ((Cond[0] in ['!','~'])and(Cond[1] in ['rst_n','reset_n','rst'])):
                scanItems(Body[2])
        
def scanItems(Body):
    if Body[0] == 'list':
        for Item in Body[1:]:
            scanItems(Item)
    elif Body[0] == '<=':
        Net = Body[1]
        Val = Body[2]

        logs.log_info('initial %s  = %s;' % (Body[1],Body[2]))


        
