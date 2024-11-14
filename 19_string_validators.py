# Python has built-in string validation methods for basic data. 
# It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# # str.isalnum() - This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# print('ab123'.isalnum())

# # str.isalpha() - This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# print('abcD'.isalpha())

# # str.isdigit() - This method checks if all the characters of a string are digits (0-9).
# print('1234'.isdigit())

# # str.islower() - This method checks if all the characters of a string are lowercase characters (a-z).
# print('abcd123#'.islower())

# # str.isupper() - This method checks if all the characters of a string are uppercase characters (A-Z).
# print('ABCD123#'.isupper())

# Task
# You are given a string s.
# Your task is to find out if the string s contains: 
#   alphanumeric characters, 
#   alphabetical characters, 
#   digits, 
#   lowercase and 
#   uppercase characters.

# On the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# On the second line, print True if  has any alphabetical characters. Otherwise, print False.
# On the third line, print True if  has any digits. Otherwise, print False.
# On the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# On the fifth line, print True if  has any uppercase characters. Otherwise, print False.

s = 'qA2'

a = False
index = 0
while index < len(s):
    if s[index].isalnum():
        a = True
        break
    index +=1

b = False
index = 0
while index < len(s):
    if s[index].isalpha():
        b = True
        break
    index +=1

c = False
index = 0
while index < len(s):
    if s[index].isdigit():
        c = True
        break
    index +=1

d = False
index = 0
while index < len(s):
    if s[index].islower():
        d = True
        break
    index +=1

e = False
index = 0
while index < len(s):
    if s[index].isupper():
        e = True
        break
    index +=1
    
print(a, b, c, d, e, sep='\n')
