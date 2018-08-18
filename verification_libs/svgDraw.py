#! /usr/bin/python
import os,sys,string
import logs


Header0 = '''
<!DOCTYPE html>
<html>
<body>
'''
Footer0='''
</svg>
</body>
</html>
'''


class svgDraw:
    def __init__(self,Wx,Wy,Fname,Banner='my svg',Background='white'):
        self.File = open('%s.html'%Fname,'w')
        self.File.write('%s'%Header0)
        self.File.write('<h1>%s</h1>\n'%Banner)
        self.File.write('<svg width="%s" height="%s" style="background-color:%s;" >\n'%(Wx,Wy,Background))
        self.Wx=Wx
        self.Wy=Wy
        self.svgOne=3

    def draw_polyline(self,Points,Color='black'):
        self.File.write('<polyline points="')
        for (X,Y) in Points:
            self.File.write('%s,%s '%(X,Y))
        self.File.write('"\nstyle="fill:none;stroke:%s;stroke-width:1" />\n'%Color)

    def draw_text(self,Txt,X,Y,Color='black'):
        self.File.write('<text x="%s" y="%s" fill="%s">%s</text>\n'%(X,Y,Color,Txt))


    def close(self):
        self.File.write(Footer0)
        self.File.close()

    def svgAdd(self,X,Y,Label,Mul=1):
        Fact = self.svgOne*Mul
        self.draw_polyline([(X-Fact,Y-Fact),(X-Fact,Y),(X,Y),(X,Y-Fact),(X-Fact,Y-Fact)],'green')
        self.draw_text(X,Y,Label,'red')

#xs=75.191772 ys=195.466385 x=74.500000 y=196.500000 laplscore=49.642036 edge_score=5.400705 mini=0
def demo():
    Fname = sys.argv[1]
    svg = svgDraw(256,256,'demo')
    File = open(Fname)
    ok=True
    while ok:
        line = File.readline()
        if line=='': ok=False
        Vars = logs.parseVars(line)
        if 'x' in Vars:
            X = int(float(Vars['x']))
            Y = int(float(Vars['y']))
            svg.svgAdd(X,Y,'.')

if __name__=='__main__':
    demo()

