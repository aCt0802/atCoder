N, M = map(int, input().split())
moneys = list(map(int, input().split()))
bonusNumbers : set = set({})
bonus = {}
for _ in range(M):
    num, price = map(int, input().split())
    bonusNumbers.add(num)
    bonus[num] = price