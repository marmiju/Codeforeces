def longest(arr: list[int]) -> int:
    s = sorted(arr) # 1 2 3 4 100 200
    for i,val in enumerate(s):
        if i+1 is not s[i]+1:
            print(i+1)
            return i+1

    


print(longest([100, 4, 200, 1, 3, 2]))
