from polygon import Poligon
class Square(Poligon):
    pass
    def __init__(self,hight):
        self.hight=hight     
        self.width=hight
x=Square(10)
print(x.getPerimeter())