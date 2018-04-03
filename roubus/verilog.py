
import os,sys,string
NewName = os.path.expanduser('~')
sys.path.append('%s/verification_libs'%NewName)
sys.path.append('models2')
sys.path.append('models')


import veri
import logs

from antWorkerClass import antWorkerClass
from cpu0WorkerClass import cpu0WorkerClass
from cpu1WorkerClass import cpu1WorkerClass
from ramWorkerClass import ramWorkerClass
from rx0WorkerClass import rx0WorkerClass
from tx2WorkerClass import tx2WorkerClass
from ddrWorkerClass import ddrWorkerClass
from adminWorkerClass import adminWorkerClass
from switch3WorkerClass import switch3WorkerClass

def aaa(A,B,C):
    print A,B,C

Workers={}
def initial(Id):
    Id = logs.intx(Id)
    PP = veri.peek_mem('tb.paths',str(Id))
    Path = logs.bin2str(PP)
    print 'my id',Id,Path
    Workers


cycles=0
def negedge():
    global cycles
    cycles += 1
    if cycles>1000: 
        logs.log_info('finish')
        veri.finish()
        sys.exit()

def str2(Id):
    return str(int(Id,2))



def work_ant(Id,Who):
    if Id not in Workers:
        PP = veri.peek_mem('tb.paths',str2(Id))
        Path = logs.bin2str(PP)
        Who = logs.bin2str(Who)
        Eval = '%sWorkerClass(Path)'%Who
        Obj = eval(Eval)
        Workers[Id] = Obj
        logs.log_info('who %s %s %s'%(Id,Who,Path))
    Workers[Id].run()



