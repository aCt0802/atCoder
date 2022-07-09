h,w = map(int, input().split())
firstFLG = False
secondFLG = False
idx = 1
first = []
second = []

for i in range(h):
    row = 1
    for char in input():
        if char == 'o':
            if not firstFLG:
                firstFLG = True
                first.append(idx)
                first.append(row)
            elif not secondFLG:
                secondFLG = True
                second.append(idx)
                second.append(row)
                break
        row += 1
    idx += 1

ans = abs(first[0] - second[0]) + abs(first[1] - second[1])
print(ans)