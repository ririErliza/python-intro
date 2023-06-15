
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

from new import Student

class Person(Student):
    pass # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

p1 = Person()
print(p1.name) # Tim