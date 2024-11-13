# Given an integer, n, print the following values for each integer i from 1 to n:
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (capitalized)
# 4. Binary

# Function Description
# Complete the print_formatted function in the editor below.
# print_formatted has the following parameters:
# int number: the maximum value to print

# Prints
# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.
    
# Input Format
# A single integer denoting n.

def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width for padding, use binary since it's the largest

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

print_formatted(19)

# -------------------------------------------

# Explanation:

# width calculation: The width variable is calculated as the length of the binary representation of the given number (excluding the '0b' prefix). This ensures that all the columns are properly aligned.

# Loop: The code iterates from 1 to the given number.

# Formatting: For each iteration:

# The decimal value is simply the string representation of i.

# The octal value is calculated using the oct() function, and the '0o' prefix is removed.

# The hexadecimal value is calculated using the hex() function, and the '0x' prefix is removed. The result is converted to uppercase.

# The binary value is calculated using the bin() function, and the '0b' prefix is removed.
# Printing: The rjust() method is used to right-align each value within the calculated width, ensuring that the table is properly formatted.