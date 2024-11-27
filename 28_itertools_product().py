# itertools.product()
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# You are given a two lists A and B. Your task is to compute their cartesian product AxB.

# Example:

# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
#  

# -------------solution-----------------

from itertools import product

# A = list(map(int, input().split())) #input in HR
# B = list(map(int, input().split()))

A = [1, 2, 9]
B = [3, 4]

print(*list(product(A, B)))


# Code Explanation:
# 1. from itertools import product

# The itertools.product() function computes the Cartesian product of input iterables.
# In this case, it takes the lists A and B as input and generates all possible ordered pairs 
# (a,b), where a is from A and b is from B.

# 2. A = list(map(int, input().split()))

# input() reads a single line of input as a string.
# .split() splits the string into a list of substrings based on spaces.
# map(int, ...) converts each substring to an integer.
# list(...) converts the resulting map object into a list.
# Result: 
# A becomes a list of integers input by the user.

# 3. B = list(map(int, input().split()))
# This does the same as the previous step but for the second input line, creating a list B of integers.

# 4. print(*list(product(A, B)))
# product(A, B) generates all ordered pairs (a,b), where a is from A and b is from B.
# list(product(A, B)) converts the generator object into a list of tuples.
# * unpacks the list, passing each tuple as a separate argument to print(). 
#     This results in the tuples being printed in a single line, separated by spaces.