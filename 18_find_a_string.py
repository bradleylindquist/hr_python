# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

# NOTE: String letters are case-sensitive.

# Input Format
# The first line of input contains the original string. The next line contains the substring.

# Constraints
# length between 1 and 200
# Each character in the string is an ascii character.

# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

string = 'ABCDCDC'
sub_string = 'CDC'

count = 0
index = 0
while index < (len(string) - len(sub_string) + 1):
    if(string[index:(index + len(sub_string))] == sub_string):
        count +=1
    index +=1
        
print(count)