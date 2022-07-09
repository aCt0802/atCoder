batters : list = []
N = int(input())
nums : list = map(int, input().split())

for num in nums:
    batters.append(0)
    for i in range(len(batters)):
        batters[i-1] += num

count = 0
points = [batter for batter in batters if batter > 3]
print(len(points))
