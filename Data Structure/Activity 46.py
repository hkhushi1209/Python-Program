class shape:
    def __init__(self):
        print("Inside base class")
    def area(self):
        print("Inside base class")
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("Inside derived class")
    def area(self):
        print("Area of rectangle is:", self.length * self.breadth)

rect=rectangle(10, 52445)
rect.area()