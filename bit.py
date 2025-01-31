
n = int(input())

x=0
for i in range(n) :
    value = input()

    if "++" in value :
        x += 1
    else : 
        x -=1

print(x)