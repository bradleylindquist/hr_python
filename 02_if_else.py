# Task
# Given an integer, , perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, .
# Constraints

# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.



# input:
# if __name__ == '__main__':
#     n = int(input().strip())

n = 20

if (n % 2 != 0):
  print('Weird')
elif (n == 2 or n == 4):
  print('Not Weird')
elif (n <= 20):
  print('Weird')
else:
  print('Not Weird')

# ----------------opt-----------------

n = 22

if n % 2 != 0 or (6 <= n <= 20):
    print('Weird')
else:
    print('Not Weird')
