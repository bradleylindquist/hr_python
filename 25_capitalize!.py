# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.

# Given a full name, your task is to capitalize the name appropriately.
# Input Format
# A single line of input containing the full name, S.

# Constraints
# The string consists of alphanumeric characters and spaces.
# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

# .split() method wasn't working on HR. Need this solution to keep the correct number of empty spaces

s = 'hello  world'

empty = []
for x in s:
    empty.append(x)
print(empty)

if (empty[0].isalpha() and empty[0].islower()):
    empty[0] = empty[0].capitalize()

index = 0
while index < len(empty):
    if(empty[index] == ' ' and empty[index + 1].isalpha() and empty[index + 1].islower()):
        empty[index + 1] = empty[index + 1].capitalize()
    index +=1
print(''.join(empty))
