counts = {

}
s = input()
for char in s:
    if char in counts.keys():
        counts[char] += 1
    else:
        counts[char] = 1

ans = [key for key, num in counts.items() if num == 1]

if len(ans) == 0:
    print(-1)
else:
    print(ans[0])