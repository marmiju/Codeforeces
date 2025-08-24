#test case: 4

# 2
# ot
# 2
# ad
# DV

t = int(input())


for _ in range(t):

    n1 = int(input())
    a = input().lower()
    n2 = int(input())
    b = input().lower()
    c= input()
    for i in range(n2):
        if c[i] == 'V':
            a = b[i]+a
        else:
            a=a+b[i]

    print(a)






