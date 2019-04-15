


import sys,string
import datetime

def record():
    Script  = sys.argv[0] 
    Date = datetime.date.today()
    DDD = str(Date.day)+'_'+str(Date.month)+'_'+str(Date.year)
    try:
        Frec = open('~/records.python','a')
    except:
        Frec = open('~/records.python','w')
    Frec.write('%s %s %s\n'%(Script,Date,string.join(sys.argv,' ')))
    Frec.close()



    





record()
