n,x,y = map(int,input().split())
number = input()
val = list(map(int,str(number)))


if(val[x-1] % val[y-1] == 0 or val[y-1] % val[x-1] == 0):
    print("YES")
else:
    print("NO")