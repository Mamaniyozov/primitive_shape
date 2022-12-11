from polygon import Poligon
class Trangle(Poligon):
    def __init__(self,hight,tomonlar):
        self.hight=hight
        self.tomonlar=tomonlar
        
    
    def getPerimeter(self ):
        return self.hight*self.tomonlar
s=Trangle(12,7)
print(s.getPerimeter())
    
