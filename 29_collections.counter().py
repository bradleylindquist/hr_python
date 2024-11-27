from collections import Counter
a = int(input())
b = Counter(map(int, input().split()))
c = int(input())

answer = 0
for i in range(c):
    shoe_size, price = map(int, input().split())
    if b[shoe_size]: 
        b[shoe_size] -= 1
        answer += price
print(answer)
