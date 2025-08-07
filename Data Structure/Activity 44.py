print("OOPS : Object Oriented programming")
class car:
    def __init__(self,name,color): #constructor initialize data members
        self.name = name
        self.color = color # instance data members

    def display(self):
        print("Car name: ",self.name,"Car Color: ",self.color)

#object creation
car1=car("BMW", "RED")
car2 = car("AUDI", "BLACK")
car1.display()
car2.display()