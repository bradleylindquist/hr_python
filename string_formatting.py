def print_formatted(number):
    width = len(bin(number)[2:])  # Calculate the width for padding

    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(f"{decimal.rjust(width)} {octal.rjust(width)} {hexadecimal.rjust(width)} {binary.rjust(width)}")

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

print(print_formatted(5))

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