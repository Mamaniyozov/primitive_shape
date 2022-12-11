from polygon import Poligon
from math import sqrt
class Trangle(Poligon):       
    
    def getPerimeter(self ):
        return 2*(sqrt(((self.hight)**2+(self.width/2)**2)))+self.width
    def getArea(self):
        return (self.hight*self.width)/2
s=Trangle(12,7)
print(s.getPerimeter())
print(s.getArea())
    
