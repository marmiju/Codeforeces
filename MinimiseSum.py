t=int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    min_so_far = float('inf')
    original = 0

    for x in a:
        min_so_far = min(min_so_far,x)
        original += min_so_far
    
    result = original
    for i in range(n):
        for j in range(i+1, n):
            temp = a[:]
            temp[i]+= temp[j]
            temp[j] = 0
            min_so_far = float('inf')
            total = 0

            for x in temp:
                min_so_far = min(min_so_far,x)
                total += min_so_far
            result = min(result,total)
    
    print(result)


    



