# #---------------------------------------------------printing----------------------------------------------------------------------

# print('Hello World, welcome')
# print('Welcome')
# print('My Name is Lili I am', 100, 'years')


# #---------------------------------------------------variables-----------------------------------------------------------------------

# name = 'Tim'

# """
# name is the name of variable

# 'Tim' is the value
# """

# print(name)

# print(name + 'is a boy')
# print(name + 'is 18')
# print(name + 'is from Turkey')

# #-----------------------------------------------------data types : string--------------------------------------------------------------------



# name = 'Roy'
# age = 18

# print(name)
# print(name + 'is a boy')
# print(name,'is', age)


# """
# string
# number/integer
# boolean
# """

# ##### String #####

# print('Hi. How are you')
# print('Hi. \nHow are you')
# print('Hi. \'How are you\'') #using backslash to show a quote

# fruit = 'Banana'
# print(fruit[2]) #print letter at index 2
# print(fruit.upper())
# print(fruit.islower()) #false coz must all lowercase
# print(fruit.lower())
# print(fruit.isupper()) #false coz must all uppercase
# print(fruit.upper().isupper()) #true
# print(fruit) #Banana
# print(len(name)) #3 to get the length of a string
# print(fruit.index('a')) # 1
# print(fruit.replace('a', 'i')) #Binini


# #-----------------------------------------------------data types : number/integer --------------------------------------------------------------------

# print(75) # print number directly

# number = 79
# print(number) # print variable with value of integer/number

# print(1+2)  # perform arithmatic operation
# print(2.5 + 1.25)
# print( 64/8)
# print(5*3)
# print(20%6)

# number2 = str(number) #convert number to string
# print(number2)
# # print('number is' + number) #concatenate string with number will give error result
# print('this is the number ' + number2) #work out because number2 is already converted to string

# print(-5)
# print(abs(-5)) #will give absolute number of this value, 5
# print(max(4,1,6)) #get highest number, 6
# print(min(2,1,-3)) # -3
# print(round(3.5)) #4
# print(bin(3)) # return the binary string, 0b11

# # methods above are built in
# # there are methods that need importing  math library first


# ###### number method that we need to import first ########
# from math import * # importing everything with this asterix

# print(sqrt(100)) #10.0

# #-----------------------------------------------------getting user's input--------------------------------------------------------------------
# # animal = input('Input Your Fav Animal: ') # saving the input that user type in a variable called animal
# # flower = input('Input Your Fav Flower: ')
# # age= int(input('Input your age: ')) # this is integer not a string
# # print('Your fav animal is ' + animal + ' and your fav flower is ' + flower + ' also you are', age, 'years old')



# #-----------------------------------------------------simple word replacement-----------------------------------------------------------
# # sentence = input('Enter your sentence: ')
# # print('Your sentence is: ', sentence)
# # word1 = input('Enter the word to replace: ')
# # word2 = input('Enter the word to replace it with: ')
# # print(sentence.replace(word1,word2))

# #------------------------------------------------------------LIST---------------------------------------------------------------------

# countries = ['UK', 'Ghana', 'Nigeria', 'Australia']
# print(countries) # ['UK', 'Ghana', 'Nigeria', 'Australia']
# print(countries[0]) # UK
# print(countries[-1]) # Australia  --- will get the value from the back
# print(countries[2][0]) # N   --- getting the initial letter of the country at index 2
# print(countries[1:]) # ['Ghana', 'Nigeria', 'Australia']
# print(countries[2:4]) # ['Nigeria', 'Australia']
# print(type(countries)) # <class 'list'>

# countries[0] = 'USA'  # replace UK with USA
# print(countries) # ['USA', 'Ghana', 'Nigeria', 'Australia']

# print(len(countries)) #4

# countries [2] = 2
# countries [3] = True



# print(type(countries[2])) # <class 'int'>
# print(type(countries[3])) # <class 'bool'>

# print(countries)

# laptops =list(('Dell', 'HP', 'Lenovo', 'MAC'))  #another way to create a list
# print(laptops) # ['Dell', 'HP', 'Lenovo', 'MAC']

# #-----------------LIST METHODS------------------
# list1 =[1,2,3,4,5]
# list2 = ['banana', 'apples', 'mangos','oranges']

# #joining list
# list1.extend(list2)
# print(list1)
# #answer: [1, 2, 3, 4, 5, 'banana', 'apples', 'mangos', 'oranges']

# #adding data to the list
# list2.append('cherries')
# print(list2)
# #answer:['banana', 'apples', 'mangos', 'oranges', 'cherries']

# list2.insert(1,'pears')
# print(list2)
# #answer : ['banana', 'pears', 'apples', 'mangos', 'oranges', 'cherries']
# # data inserted at specific position

# #finding data at certain position
# print(list2.index('mangos')) #3



# #getting the length of the list
# print(len(list2)) #-- 6
# print(len(list1)) #-- 9

# #removing data from list
# list2.remove('banana')
# list2.remove('oranges')
# list2.remove('apples')
# print(list2)
# #answer : ['pears', 'mangos', 'cherries']


# #knowing how many times values appearing in the list
# print(list2.count('mangos')) # 1 (appear just 1)
# print(list2.count('apples')) # 0 (coz we had removed it from the list)


# #emptying thee list
# list1.clear()
# print(list1) # [] (the list is now empty)

# list3 = [3,5,7,1,2,8,4,3,0]
# #sorting the list
# list3.sort()
# print(list3) # [0, 1, 2, 3, 3, 4, 5, 7, 8]

# list3.reverse()
# print(list3) # [8, 7, 5, 4, 3, 3, 2, 1, 0]

# #copying list to new variable
# list4 = list3.copy()
# print(list4) # [8, 7, 5, 4, 3, 3, 2, 1, 0]

# #remove the last value in the list
# list4.pop()
# print(list4) # [8, 7, 5, 4, 3, 3, 2, 1]

# #remove certain value
# list4.pop(0)
# print(list4) #[7, 5, 4, 3, 3, 2, 1]

# del list4[0]
# print(list4) #[5, 4, 3, 3, 2, 1]

# #del the list
# del list3
# #print(list3) #if we print now we will get : NameError: name 'list3' is not defined. -- because the code is deleted so it doesnt exist anymore and cant be printed


# #----------------------------TUPLES-------------------------------

# #tuples are used to store multiple items in a single variable
# #tuples are immutable - we can't change any value in a tupple

# three_numbers = (1,2,3)
# print(three_numbers) # (1, 2, 3)

# print(three_numbers[0])  # 1



# four_numbers = (1,2,3,1) #repetition in tupple is fine

# # length of tupple
# print(len(four_numbers))  # 4

# # type
# print(type(four_numbers)) # <class 'tuple'>

# # tupple allows various data types
# strings = ('home', 'land', 'earth')
# boo = (True, False, True)
# mix = (1, 'Home', True, 'Land')

# print(type(mix[0])) # <class 'int'>

# #assigning new value to tupple
# #three_numbers[1] = 23
# # print(three_numbers) # TypeError: 'tuple' object does not support item assignment
# # because we cannot change values in tupple


# #---------------------------FUNCTIONS-----------------------------

# # a block of code which performs a particular tasks
# # remember in python indentation is very important

# def greetings_function():
#     print('Welcome User')

# #now this is our of the function
# #we call the function
# greetings_function() # Welcome User

# # passing arguments / parameters

# def greetings_function(name):
#     print('Welcome '+ name)

# greetings_function('John') # Welcome John

# # greetings_function(34) # TypeError: can only concatenate str (not "int") to str

# # solving

# def greetings_function(name):
#     print('Welcome '+ str(name))

# greetings_function(34) # Welcome 34

# # passing 2 params

# def greetings_function(name, age):
#     print('Welcome '+ name + ' . You are '+ str(age)+ ' years old.')


# greetings_function('Jack',27) # Welcome Jack . You are 27 years old.
# greetings_function(name = 'Jack',age=27) #' the same thing'
# # using asteriks * if we dont know what we are passing

# def greetings_function(*names):
#     print('Welcome '+ names[1]) #passing the index is necessary

# greetings_function('Jack', 'Jill', 'Zoe')

# #def greetings_function(*names):
#    # print('Welcome '+ names)    --- this will result an error

# # greetings_function('Jack', 'Jill', 'Zoe') # TypeError: can only concatenate str (not "tuple") to str


# # using input from users
# def greetings_function(name, age):
#     print('Welcome '+ name + ' . You are '+ str(age)+ ' years old.')


# #name = input('Enter your name: ')
# #age = input('Enter your age: ')
# # greetings_function(name, age)


# #-------------------------RETURN KEYWORDS-------------------------

# # return statement will give us an output / feedback of what has been executed
# # return statement sgows the end of the function
# # we don't write anything after that return keyword

# def add_numbers(num1, num2):
#     return num1 + num2

# # print(add_numbers(1,2)) # 3

# # num1=int(input('Enter first number: '))
# # num2=int(input('Enter second number: '))

# # print(add_numbers(num1,num2))
# # Enter first number: 3
# # Enter second number: 6
# # 9

# def add_numbers(num1, num2):
#     print('The total is ')
#     return num1 + num2

# # num1=int(input('Enter first number: '))
# # num2=int(input('Enter second number: '))

# # print(add_numbers(num1,num2))
# # Enter first number: 5
# # Enter second number: 9
# # The total is
# # 14

# def add_numbers(num1, num2):
#     return num1 + num2
#     print('The total is ') # this wont be print out because return statement is the end of the function

# # num1=int(input('Enter first number: '))
# # num2=int(input('Enter second number: '))

# # print(add_numbers(num1,num2))
# # Enter first number: 3
# # Enter second number: 4
# # 7


# #----------------------------IF------------------------------------

# a = 5
# b = 3

# if a > b:
#     print(str(a) + ' is greater than ' + str(b))
#     # this code will only be executed if a greater than b, otherwise the code wont be executed

#     # 5 is greater than 3

# a = 3
# b = 3

# if a == b:
#     print(str(a) + ' is equal to ' + str(b))
#     # this code will only be executed if a EQUAL to b, otherwise the code wont be executed

#     # 3 is equal to 3

# a = 'Tim'
# b = 'Tim'

# if a == b:
#     print('a is equal to b')
#     # a is equal to b

# a = True

# if a == True:
#     print('a is True')
#     # a is True


# a = False

# if a != True:
#     print('a is False')
#     # a is False


# a = 8
# b = 5

# if a >= b:
#     print('True')
#     # True

# ##### IF ELSE #####

# a = 1
# b = 2

# if a == b:
#     print('A equals B')
# else:
#     print('A not equals B')

# # A not equals B

# b = False

# if b == True:
#     print('B is true')
# else:
#     print('B is not true')

# # B is not true

# a = 'Maggie'

# if a == True:
#     print('A is true')
# elif a == False:
#     print('A is false') # we can add how many elif as required
# else:
#     print('A is none of the two')

# # A is none of the two

# boy = True
# short = True

# if boy == True or short == True:
#     print ('He is a boy or he is short')
# elif boy == False:
#     print('Not a boy')
# else:
#     print('None of the two')

# # He is a boy or he is short

# if boy == True or short == False:
#     print ('He is a boy or he is short')
# elif boy == False:
#     print('Not a boy')
# else:
#     print('None of the two')

# # He is a boy or he is short
# # because OR just need one of the statement to be True
# # so it will still print the result

# if boy == True and short == False:
#     print ('He is a boy or he is short')
# elif boy == False:
#     print('Not a boy')
# else:
#     print('None of the two')

# # None of the two
# # with AND, we need to have both statement to be True

# value = int(input('Input a value: '))

# if type(value) == str:
#     print (value + ' is a string')
# else:
#     print('Not a String')

# code above cause an error

# if we want to check whether user input is string or int, we can use code below

# def check_type(value):
#     if value.strip().isdigit():
#         print(value, ' is an INTEGER')
#     else:
#         print(value + ' is a STRING')

# check1 = input("Type here number or words : ")
# check_type(check1)


# modulo

# value = int(input('Input a number: '))

# if value%5 == 0:
#     print(value, 'can be divided by 5')
# else:
#     print(value, 'can\'t divided by 5')

#-------------------------Build A Function---------------------------
#-------------------to check if a number is EVEN or ODD--------------

# num = int(input('Enter a number: '))

# if num%2 == 0:
#     print('Thas is an EVEN number')
# else:
#     print('That is an ODD number')


#-------------------------DICTIONARIES---------------------------

# dictinaries are used to store data values in the key value pairs
# dictionaries are also data type like list or strings
# changeable, we can modify them
# dictionaries dont allow DUPLICATE (unlike list and tuple)
# the values can be any data types

# my_dict = {
#     'name': 'Tim',
#     'age' : 25,
#     'is_tall' : True,
#     'nationality': 'African',
#     'Qualification': 'College',
#     'friends': ['Zoe', 'Frank', 'Nigel', 'Maddie']
# }


# print(type(my_dict)) 

# print(my_dict) 
# # {'name': 'Tim', 'age': 25, 'nationality': 'African', 'Qualification': 'College'}

# print(my_dict['name'])
# # Tim

# print(len(my_dict))
# # 6

# x = my_dict['friends']
# print(x)  #['Zoe', 'Frank', 'Nigel', 'Maddie']


#----------------------WHILE LOOPS------------------------------

# allow us to loop through a block of code, while a certain condition is true

i = 1

# while i < 6:
#     print(i)
#     i += 1

# 1
# 2
# 3
# 4
# 5

# while i < 6 or i == 6:
#     print(i)
#     i += 1
# 1
# 2
# 3
# 4
# 5
# 6

# while i < 6 or i == 10:
#     print(i)
#     i += 1

# 1
# 2
# 3
# 4
# 5

# while i < 6 and i == 10:
#     print(i)
#     i += 1

# no result is printed because AND needs both condition to be true


# #-----------------------FOR LOOPS------------------------------

# # for loops use to iterate over a sequence
# # looping over a sequence that can either be a list, tupple, dictionary, even strings, or a range of numbers


# for letter in 'Hello':
#     print(letter)

# # H
# # e
# # l
# # l
# # o

# mylist = ['ji', 'je', 'jo']

# for value in mylist:
#     print(value)

# # ji
# # je
# # jo


# for value in mylist:
#     print(value)
#     if value == 'je':
#         break

# # ji
# # je

# for value in mylist:
#     if value == 'je':
#         break
#     print(value)

# # ji

# mydict = {
#     'name': 'john',
#     'age':13,
#     'city': 'Bonn'
# }

# for value in mydict:
#     print(value)

# # name
# # age
# # city

# for x in range(4):
#     print(x)
# # 0
# # 1
# # 2
# # 3

# for x in range(8,11):
#     print(x)

# # 8
# # 9
# # 10

# for x in range(13,15):
#     print(x)
# else:
#     print('Finished Looping!!')

# # 10
# # 13
# # 14
# # Finished Looping!!

#-----------------------2D LISTS-------------------------------
#---------------------NESTED LOOP------------------------------

# like we have multiple lists inside a list variable

my_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# print(my_list) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(my_list[0]) # [1, 2, 3]
# print(my_list[0][0]) # 1

# for lists in my_list:
#     print(lists)

# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# for lists in my_list:
#     for row in lists:
#         print(row)

'''
1
2
3
4
5
6
7
8
9
'''

#-----------------------COMMENTS------------------------------

# using this # to comment or ''' ---- '''

