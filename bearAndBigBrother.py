liak, bear = map(int,input().split())
count = 0

while liak <= bear:
    liak *= 3
    bear *= 2
    count += 1
print(count)

