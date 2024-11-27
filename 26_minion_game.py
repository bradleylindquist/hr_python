# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string, s.
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring:
# A player gets +1 point for each occurrence of the substring in the string .
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Print: the winner's name and score, separated by a space on one line, or Draw if there is no winner

# --------------------solution-------------------------- 

from itertools import combinations

string = 'BANANANAAS'

x = len(string) + 1
empty = []
index = 1

while index < x:
    empty.append([string[i:i+index] for i in range(len(string) - index + 1)])
    index += 1

stuart = []
kevin = []

for x in empty:
    for y in x:
        if y[0] == 'A' or y[0] == 'E' or y[0] == 'E' or y[0] == 'O' or y[0] == 'U':
            kevin.append(y)
        else:
            stuart.append(y)

if len(kevin) > len(stuart):
    print('Kevin ' + str(len(kevin)))
elif (len(stuart) > len(kevin)):
    print('Stuart ' + str(len(stuart)))
else:
    print('Draw')

# ------------------opt-----------------------

# Optimizations:
# 1. Avoid creating all substrings explicitly: Generating all substrings is memory-intensive 
#     and can be avoided by directly calculating the contribution of each character.

# 2. Simplify vowel check: Use a set for faster membership testing.

# 3. Eliminate unnecessary lists: stuart and kevin lists are unnecessary; instead, we can directly count the scores.

# 4. Reduce redundancy in checks: Combine conditions where applicable.

def minion_game(string):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

# Example usage
minion_game('BANANANAAS')


# Explanation of the Optimized Code:

# 1. Score Calculation: For each character, its score is based on how many substrings it can generate, 
#     which is length - i (all substrings starting from this character).

# 2. Vowel Check: We use a set (vowels) for O(1) membership testing.

# 3. Memory Efficiency: Instead of storing substrings, the code directly calculates the scores for Stuart 
#     (consonants) and Kevin (vowels).

# 4. Readability: The code is more compact and easier to follow.
