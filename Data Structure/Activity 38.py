# Person class
class Person( object ):

    # __init__ is known as the constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name)
        print(self.age)

# Student class
class Student ( Person ):
    def __init__( self,name, age, course, school):
        self.course = course
        self.school = school

        # invoking the __init__ of the parent
        Person.__init__(self, name, age)
# creation of an object variable or an instance
a = Student('Khushi', 12, 7, "Podar International School")

# calling a function of the class Person using its instance
a.display()