


import sys,string
import datetime

def record():
    Script  = sys.argv[0] 
    Date = datetime.date.today()
    DDD = str(Date.day)+'_'+str(Date.month)+'_'+str(Date.year)
    NewName = os.path.expanduser('~')
    try:
        Frec = open('%s/records.python'%NewName,'a')
    except:
        Frec = open('%s/records.python'%NewName,'w')
    Frec.write('%s %s %s\n'%(Script,Date,string.join(sys.argv,' ')))
    Frec.close()



    





record()
