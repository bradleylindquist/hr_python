# You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w.

# Function Description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# 1. string string: a long string
# 2. int max_width: the width to wrap to

# Returns
# string: a single string with newline characters ('\n') where the breaks should be

# Input Format
# The first line contains a string, string.
# The second line contains the width, max_width.

# In Python, the textwrap module is used for formatting and wrapping text. It provides several convenient functions to handle text wrapping, filling, and other formatting operations, especially when working with long strings or paragraphs that need to fit within a certain width.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

print(wrap(string, max_width))