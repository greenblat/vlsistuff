
'''
frame driver
'''


import logs
import veri
import sys,string,os
import random

class frameDriverClass(logs.driverClass):
    def __init__(self,Path,Monitors,Renames={}):
        logs.driverClass.__init__(self,Path,Monitors)
        self.Queue = []
        self.Renames = Renames
        self.force('hsync',0)
        self.force('vsync',0)
        self.force('data',0)
        self.Params = {}
        self.Params['columns'] = 1240
        self.Params['rows'] = 1240
        self.Params['hgap'] = 300
        self.Params['vgap'] = 300
        self.Params['buswidth'] = 24
        self.Params['pixelwidth'] = 8
        self.Params['pixelsperclock'] = 3
        self.X = 0
        self.Y = 0
        self.Active = False
        
    def setup(self,Params):
        List = Params.split()
        for PrmVal in List:
            Prm,Val = PrmVal.split('=')
            try:
                self.Params[Prm]=eval(Val)
            except:
                self.Params[Prm]=Val

    def force(self,Sig,Val):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        logs.driverClass.force(self,Sig,Val)

    def peek(self,Sig):
        if Sig in self.Renames: Sig = self.Renames[Sig]
        return logs.driverClass.peek(self,Sig)


    def action(self,Txt):
        wrds = Txt.split()
        Cmd = wrds[0]
        if Cmd=='run':
            self.Active = True
        elif Cmd=='setup':
            self.setup(' '.join(wrds[1:]))
        else:
            logs.log_error('action %s is not recognized'%Cmd)



    def run(self):
        if self.waiting>0:
            self.waiting -= 1
            return
        if self.state=='idle':
            self.waiting = self.Params['vgap']
            self.state = 'start'
            return
        if self.state=='start':
            self.force('vsync',1)
            self.waiting = self.Params['hgap']
            self.state = 'line'
            return
        if self.state=='line':
            self.force('hsync',1)
            self.force('data',self.inventData(self.X,self.Y))
            self.X += 1
            if self.X >= self.Params['columns']:
                self.state = 'endofline'
            return
        if self.state=='endofline':
            self.force('hsync',0)
            self.force('data',0)
            self.X = 0
            self.Y += 1
            if self.Y >= self.Params['rows']:
                self.Y = 0
                self.waiting = self.Params['vgap']
                self.state =  'idle'
                self.force('vsync',0)
            else:
                self.waiting = self.Params['hgap']
                self.state = 'line'
            
    def inventData(self,X,Y):
        Pixwid = self.Params['pixelwidth'] 
        Pixels = self.Params['pixelsperclock']
        if Pixels==1:
            X = random.randint(0,(1<<Pixwid)-1)
            return X

        if Pixels==2:
            X = random.randint(0,(1<<Pixwid)-1)
            Y = random.randint(0,(1<<Pixwid)-1)
            return (Y<<Pixwid)+X

        if Pixels==3:
            X = random.randint(0,(1<<Pixwid)-1)
            Y = random.randint(0,(1<<Pixwid)-1)
            Z = random.randint(0,(1<<Pixwid)-1)
            Pix =  (Z<<(2*Pixwid)) + (Y<<Pixwid)+X
            return Pix



