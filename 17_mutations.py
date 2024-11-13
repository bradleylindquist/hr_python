# We have seen that lists are mutable (they can be changed), 
# and tuples are immutable (they cannot be changed).

# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.

string = "abracadabra"
print(string[4])
# string[4] = 'k' #this throws an error
print(string[4])

# How would you approach this?
# One solution is to convert the string to a list and then change the value.

l = list(string)
l[4] = 'k'
string = ''.join(l)
print(string)

# Another approach is to slice the string and join it back.
# Example:

string = string[:4] + "k" + string[5:]
print(string)

# --------------solution--------------------------

def mutate_string(string, position1, position2, character1, character2):
    string = string[:position1] + character1 + string[position1 + 1:]
    string = string[:position2] + character2 + string[position2 + 1:]
    return(string)


a = 'lindquist'
b = 3
c = 6
d = 'k'
e = 'e'
print(mutate_string(a, b, c, d, e))