# Consider a list (list = []). You can perform the following commands:
# 1. insert i e: Insert integer e at position i.
# 2. print: Print the list.
# 3. remove e: Delete the first occurrence of integer e.
# 4. append e: Insert integer  at the end of the list.
# 5. sort: Sort the list.
# 6. pop: Pop the last element from the list.
# 7. reverse: Reverse the list.

# Initialize your list and read in the value of n followed by n lines of commands 
#     where each command will be one of the 7 types listed above. 
#     Iterate through each command in order and perform the corresponding operation on your list.

# if __name__ == '__main__':
#     N = int(input())

N = ['insert', [0, 5], 
     'insert', [1, 10],
     'insert', [0, 6],
     'print',
     'remove', [6],
     'append', [9],
     'append', [1],
     'sort',
     'print',
     'pop',
     'reverse',
     'print']
    
list=[];

index = 0
while index < len(N):
    if N[index] == 'insert':
        list.insert(N[index + 1][0], N[index + 1][1])
    elif N[index] == 'append':
        list.append(N[index + 1][0])
    elif N[index] == 'pop':
        list.pop()
    elif N[index] == 'print':
        print(list)
    elif N[index] == 'remove':
        list.remove(N[index + 1][0])
    elif N[index] == 'sort':
        list.sort()
    elif N[index] == 'reverse':
        list.reverse()
    index +=1

# below: need input().split() if the data input isn't in a list already

# for x in N:
#     # x=input().split();
#     if x == "insert":
#         list.insert(int((x + 1)[1]),int((x + 1)[2]))
#     elif x == "append":
#         list.append(int((x + 1)[1]))
#     elif x == "pop":
#         list.pop();
#     elif x == "print":
#         print(list)
#     elif x == "remove":
#         list.remove(int((x + 1)[1]))
#     elif x == "sort":
#         list.sort();
#     elif x == 'reverse':
#         list.reverse();
#     else:
#         continue