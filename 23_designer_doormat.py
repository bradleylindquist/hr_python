# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following specifications:
# 1. Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# 2. The design should have 'WELCOME' written in the center.
# 3. The design pattern should only use |, . and - characters.

n = 11
m = 3*n


# top half (n / 2 minus 1 rows)
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))

# middle row including 'WELCOME' (1 line)
print('WELCOME'.center(m,'-'))

# bottom half (n / 2 minus 1 rows)
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))