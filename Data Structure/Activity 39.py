class Student:
    __schoolName = 'XYZ school'  # private class attribute

    def __init__(self, name, age):
        self.__name = name  # private instance attribute
    print(__schoolName)
    def __display(self):  # private method
        print('This is private method.')

std = Student("Bill", 25)
