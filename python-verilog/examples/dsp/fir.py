''' fir aluka
i didnt separate aluka from golden model.
but the inner loop of "run" can take data from files generated from matlab and compare them.

'''


import logs
import veri

DELAY = 2

class firClass:
    def __init__(self,Path):
        self.Path = Path
        self.values = [0,0,0,0,0,0,0,0,0]
        self.expecteds=[]

    def peek(self,Sig):
        return logs.peek('%s.%s'%(self.Path,Sig))

    def peek_mem(self,Sig,Ind):
        return logs.intx(veri.peek_mem('%s.%s'%(self.Path,Sig),str(Ind)))

    def run(self):
        Din = self.peek('din')
        self.values.pop(0)
        self.values.append(Din)

        denom = 0
        nomin = 0
        for II in range(0,9):
            Coef = self.peek_mem('coeffs',II)
            denom += Coef
            nomin += Coef * self.values[II]
        Result = nomin/denom
        self.expecteds.append(Result)

        if len(self.expecteds)>DELAY:
            Dout = self.peek('dout')
            Dexp = self.expecteds.pop(0)
            if Dout==Dexp:
                logs.log_correct('exp=%d dout=%d'%(Dexp,Dout))
            else:
                logs.log_wrong('exp=%d dout=%d'%(Dexp,Dout))

# beginning of non aluka mode:      
def main():
    ''' not implemented '''    
    ''' put here readers of input data and expected data files and call modified a bit run routine. '''

if __name__ == '__main__':
    main()

