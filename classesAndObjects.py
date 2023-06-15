# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.


'''-----------------CLASS----------------------'''

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x) 

# 5

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age= age

# p1 = Person('John', 87)
# print(p1.name) # John
# print(p1.age) # 87

# The __str__() function controls what should be returned when the class object is represented as a string.

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1) # <__main__.Person object at 0x00000253E301FFD0>



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) # John(36)



# name = input ('Enter your name: ')
# age = input('Enter your age: ')
# p1 = Person(name,age)
# print(p1.name)
# print(p1.age)

# Hill
# 65


'''----------------OBJECT METHOD-------------------'''
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Example
# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " i am ", self.age, " years old")

p1 = Person("Diana", 35)
p1.myfunc()

# Hello my name is Diana i am  35  years old

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


'''----------------The self Parameter------------------'''
# the self parameter is a reference to the current instance of the class, and
# is used to access variables that belongs to the class
# it doesnt have to be named 'Self', we can call it whatever we like
# but it has to be the first parameter of any function in the class

class Fruit:
    def __init__(object, name, flavor):
        object.name = name
        object.flavor = flavor
    
    def myfunc(whichfruit):
        print('This is ' + whichfruit.name + ' , it tastes ' + whichfruit.flavor)

f1 = Fruit('Banana', 'most of the time sweet')
f1.myfunc()

# This is Banana , it tastes most of the time sweet

#----modify object properties----

f1.flavor = 'bitter'

print(f1.flavor)

# bitter

#----delete object properties----

# del f1.flavor
# print(f1.flavor)
# AttributeError: 'Fruit' object has no attribute 'flavor' (coz it has been deleted)

#----delete object -----

# del f1

# print(f1) 
# NameError: name 'f1' is not defined. (coz it has been deleted)

#----PASS Statement -----

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Basket:
    pass

# will show nothing at terminal



