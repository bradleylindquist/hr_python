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

def print_rangoli(size):
    a = "abcdefghijklmnopqrstuvwxyz"
    lines = []
    for row in range(size): #build each row
        print_ = "-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])

    width = len(lines[0]) #calculate the width
    
    for row in range(size-1, 0, -1): #upper rangoli
        print(lines[row].center(width, '-'))
        
    for row in range(size): #lower rangoli
        print(lines[row].center(width, '-'))

print_rangoli(6)

# ---------------------explanation-------------------

# Building Each Row 
# 1. The for loop iterates through numbers from 0 to size-1 (inclusive).
# 2. a[row:size] slices the alphabet string to get letters starting from index row to the end of the 
#     rangoli size (e.g., for row = 1 and size = 4, this gives "bcde").
# 3. "-".join(a[row:size]) joins these letters with hyphens (e.g., "b-c-d-e").
# 4. print_[::-1] reverses the string (e.g., "e-d-c-b").
# 5. print_[1:] removes the first character to avoid repetition in the middle of the row (e.g., "d-c-b-e").
# 6. lines.append(print_[::-1] + print_[1:]) combines the reversed part and the sliced part to form a 
#     symmetric row (e.g., "e-d-c-b-c-d-e").


# Calculating the Width 
# 1. The width of the pattern is determined by the length of the first row. 
#     This ensures all rows are centered properly.


# Printing the Upper Part of the Rangoli
# 1. The loop iterates through lines in reverse order (excluding the first row).
# 2. lines[row].center(width, '-') centers each row using the total width, filling empty spaces with hyphens.

# Printing the Lower Part of the Rangoli 
# 1. This loop iterates through lines in the original order to print the lower half of the rangoli (including the middle row).