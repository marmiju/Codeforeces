T = int(input())

for _ in range(T):
    N, K, D = map(int, input().split())
    Ti = list(map(int, input().split()))

    flower_available_day = [0] * N
    total_plucks = 0

    for day in range(1, D + 1):
        available_flowers = []
        
        for i in range(N):
            if flower_available_day[i] < day:
                available_flowers.append(i)
        
        can_pluck = len(available_flowers) - K
        if can_pluck <= 0:
            continue

        for i in range(can_pluck):
            idx = available_flowers[i]
            flower_available_day[idx] = day + Ti[idx]
            total_plucks += 1

    print(total_plucks)
