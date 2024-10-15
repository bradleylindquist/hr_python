# Let's learn about list comprehensions! You are given three integers  and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, 0<=i<=x; 0<=j<=y; 0<=k<=z. Please use list comprehensions rather than multiple loops, as a learning exercise.

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

x = 1
y = 1
z = 2
n = 3

x_values = [ x for x in range(x + 1)]
y_values = [ y for y in range(y + 1)]
z_values = [ z for z in range(z + 1)]

permutations = []

# Nested loops to generate the permutations
for x in x_values:
    for y in y_values:
        for z in z_values:
            permutations.append([x, y, z])

answer = [x for x in permutations if sum(x) != n]
print(answer)



