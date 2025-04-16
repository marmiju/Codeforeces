import math

n = int(input())

s = list(map(int, input().split()))

sum = 0

for i in s :
    sum += i

result = math.ceil(sum / 4)  
print(result) 