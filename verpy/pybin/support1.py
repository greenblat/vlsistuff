

import types,string
import db0

    
def extract_expr_nets(Sig):
    res = []
    if not Sig:
        return res 
    if type(Sig)==types.StringType:
        res.append(Sig)
    elif type(Sig)==types.IntType:
        pass
    elif type(Sig)==types.ListType:
        if Sig[0] in ['bin','hex','dec']:
            pass
        elif Sig[0]=='subbit':
            res.append(Sig[1])
        elif Sig[0]=='subbus':
            res.append(Sig[1])
        else:
            db0.log_err('extract_expr_nets %s '%(str(Sig)))
    else:
        db0.log_err('extract_expr_nets %s '%(str(Sig)))
    return res 


