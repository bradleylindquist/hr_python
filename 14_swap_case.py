# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# I used a while loop 

s = 'HackerRank.com presents "Pythonist 2".'

empty = []
i = 0
while i < len(s):
  if s[i] == s[i].lower():
    empty.append(s[i].upper())
  else:
    empty.append(s[i].lower())
  i+=1
print("".join(empty))