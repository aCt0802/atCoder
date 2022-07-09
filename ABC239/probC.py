# https://atcoder.jp/contests/abc239/tasks/abc239_c

a,b,c,d = map(int, input().split())
nums = [0,1,2,3,4,5]
ansList = []
for i in nums:
    for j in nums:
        if (a - (a + i)) * (a - (a + i)) + (b - (b + j)) * (b - (b + j)) == 5:
            ansList.append([a + i, b + j])
        if (a - (a - i)) * (a - (a - i)) + (b - (b - j)) * (b - (b - j)) == 5:
            ansList.append([a - i, b - j])
        if (a - (a - i)) * (a - (a - i)) + (b - (b + j)) * (b - (b + j)) == 5:
            ansList.append([a - i, b + j])
        if (a - (a + i)) * (a - (a + i)) + (b - (b - j)) * (b - (b - j)) == 5:
            ansList.append([a + i, b - j])
print("確認 : ", ansList)

ans = "No"
for assumed in ansList:
    if (((c - assumed[0]) * (c - assumed[0])) + ((d - assumed[1]) * (d - assumed[1]))) == 5:
        ans = "Yes"
        break

print(ans)