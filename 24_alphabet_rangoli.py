# You are given an integer, . Your task is to print an alphabet rangoli of size N. 
# (Rangoli is a form of Indian folk art based on creation of patterns.)

#size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# ----------------------solution---------------------------

n = 11
m = 3*n

# top half (n / 2 minus 1 rows)
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))

N = 5

print('a'.center((N - 1)**2 + 1, '-'))