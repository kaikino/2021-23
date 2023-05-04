from graphics import *
from math import *
k=100
cx,cy,cz=1,1,100
    
def renderX(x,y,z):
    return(-k*tan(atan(z/x)-atan(cz/cx)))
def renderY(x,y,z):
    return(k*tan(acos(sqrt(x^2+z^2)/sqrt(x^2+y^2+z^2))-acos(sqrt(cx^2+cz^2)/sqrt(cx^2+cy^2+cz^2))))

def drawPoint(x,y,z):
    d = Circle(Point(renderX(x,y,z),renderY(x,y,z)), 1)
    d.draw(win)
    print (renderX(x,y,z),renderY(x,y,z))

win = GraphWin("My Circle", 1000, 1000)
    
drawPoint(50,50,50)
drawPoint(100,50,50)
drawPoint(50,100,50)
drawPoint(100,100,50)
drawPoint(50,50,100)
drawPoint(100,50,100)
drawPoint(50,100,100)
drawPoint(100,100,100)

win.getMouse() # pause for click in window
win.close()
    
