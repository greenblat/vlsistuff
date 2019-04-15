


import sys,string
import datetime

def record():
    Script  = sys.argv[0] 
    Date = datetime.date.today()
    DDD = str(Date.day)+'_'+str(Date.month)+'_'+str(Date.year)
    Frec = open('/Users/ilia/records.python','a')
    Frec.write('%s %s %s\n'%(Script,Date,string.join(sys.argv,' ')))
    Frec.close()



    





record()
