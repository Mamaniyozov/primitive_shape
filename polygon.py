class Poligon:
    def __init__(self,hight,width):
        self.hight=hight
        self.width=width
        
    def getArea(self ):     
        return  self.hight*self.width
    def getPerimeter(self ):
        return 2*self.hight + self.width*2
    
