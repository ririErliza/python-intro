#----------------------READING FILES---------------------------
''' the txt file needs to be at the same folder as this app.py'''

coun_file = open('countries.txt','r')
# print('is this readable? ', coun_file.readable()) # True
# print(coun_file.readline()) # gonna print the first line
# # Indonesia
# print(coun_file.readline()) # this will print the second line (it prints in sequence)
# # Malaysia

# print(coun_file.readlines()) # print everything
# # ['Brunei\n', 'Singapore\n', 'Thailand\n', 'Kamboja\n', 'Vietnam\n', 'Laos\n', 'Philipines']

# print(coun_file.read())

# Indonesia
# Malaysia
# Brunei
# Singapore
# Thailand
# Kamboja
# Vietnam
# Laos
# Philipines

# print(coun_file.read(3)) # Return the 3 first characters of the file
# # Ind

# print(coun_file.readlines()[3]) # Return the 4th data in list
# # SIngapore

# for lines in coun_file.readlines():
#     print(lines)

# Indonesia

# Malaysia

# Brunei

# Singapore

# Thailand

# Kamboja

# Vietnam

# Laos

# Philipines

coun_file.close()


'''----------------------WRITING FILES----------------------'''

# "a" - Append - will append to the end of the file
coun_file = open('newFile.txt','a')
coun_file.write('\nNew again,\nanother new,\nsomething else')
#this will append it to the file
coun_file.close()


# # "w" - Write - will overwrite any existing content
# coun_file = open('newFile.txt','w')
# coun_file.write('Woops I have deleted the content')
# #this will rewrite everything in the file
# coun_file.close()


'''----------------------CREATE NEW FILE------------------'''

# f = open('myfile.txt', 'x')


'''----------------------DELETE A FILE--------------------'''

# import os
# os.remove('myfile.txt')  #the simple way


'''
check if file exists,
then delete it: 
'''


import os
if os.path.exists('myfile.txt'):
    os.remove('myfile.txt')
else:
    print('File doesnt exist')


