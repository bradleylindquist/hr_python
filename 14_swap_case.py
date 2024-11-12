

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