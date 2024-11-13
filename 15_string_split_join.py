# In Python, a string can be split on a delimiter.

# input: a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings. It splits at each " ", or open space
# print a
# output: ['this', 'is', 'a', 'string']

# Joining a string is simple:
# a = "-".join(a) #we're joining, but putting a hyphen between
# print a
# output: this-is-a-string 


# Task
# 1. You are given a string. Split the string on a " " (space) delimiter and join using a hyphen.

# Function Description:
# 1. Complete the split_and_join function in the editor below.
# 2. split_and_join has the following parameters:
#   string line: a string of space-separated words

# Returns
# 1. string: the resulting string

# Input Format
# 1. The one line contains a string consisting of space separated words.

def split_and_join(line):
  line = line.split(' ')
  return('-'.join(line))

sentence1 = "this is a string"
sentence2 = "a no rough stuff type deal"
print(split_and_join(sentence1))
print(split_and_join(sentence2))