# In Python, a string can be split on a delimiter.

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



line = "this is a string"

line = line.split(' ')
print('-'.join(line))