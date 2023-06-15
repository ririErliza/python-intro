'''----------------TRY EXCEPT------------------------'''

# teling the user that the input is invalid

# try:
#     x=int(input('Input an integer : '))
#     print(x)
# except:
#     print('Something went wrong, that\'s not integer')
# #Input an integer : r
# #Something went wrong, that's not integer

try:
    x=int(input('Input an integer : '))
    print(x)
except ValueError:
    print('Value is not integer')

# # Input an integer : e
# # Value is not integer

try:
    x=int(input('Input an integer : '))
    print(x)
except:
    print('Not correct')
else:
    print('Correct!')

# # Input an integer : e
# # Not correct


try:
    x=int(input('Input an integer : '))
    print(x)
except:
    print('Not correct')
finally: # this will run either there is an error or not
    print('TrymExcept Finished!')

