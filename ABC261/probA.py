l1, r1, l2, r2 = map(int, input().split())

red = set({})
temp = l1
while(temp <= r1):
    red.add(temp)
    temp+=1

blue = set({})
temp = l2
while(temp <= r2):
    blue.add(temp)
    temp+=1

ans = len(red.intersection(blue)) - 1

if ans < 0:
    ans = 0

print(ans)