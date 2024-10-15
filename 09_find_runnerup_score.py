# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

arr = [2, 3, 6, 6, 5]

x=list(set(arr)) # arr becomes a set, which removes dupes, then converts to a list
x.remove(max(x)) #remove the highest score from the list
print(max(x)) #print the new highest score in the list