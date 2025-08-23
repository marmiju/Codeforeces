n = input().strip()

count = sum(1 for d in n if d in '47')


if all(ch in '47' for ch in str(count)) and count > 0:
    print("YES")
else:
    print("NO")

       
