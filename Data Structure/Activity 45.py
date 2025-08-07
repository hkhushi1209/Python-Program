class shape():
    def __init__(self):
        print("Inside base class")
    def area(self):
        print("Inside base class")
class square(shape):
    def __init__(self,side):
        self.side=side
        print("Inside derived class")
    def area(self):
        print("Area of square :", self.side*self.side)

sq = square(10)
sq.area()