N, X = map(int, input().split())
n = 0
nums = []
while n < N:
    a,b =map(int, input().split())
    nums.append([a,b])
    n += 1
ans = 'No'
for i in range(2 ** N):
    sum = 0
    for j in range(N):
        if ((i >> j) & 1):
            sum += nums[j][0]
        else:
            sum += nums[j][1]
    if sum == X:
        ans = 'Yes'
        break
print(ans)