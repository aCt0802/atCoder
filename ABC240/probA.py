a, b = map(int, input().split())
num = [a, b]
if num == [1, 10] or num == [10, 1]:
    print('Yes')
else:
    if abs(num[0] - num[1]) == 1:
        print('Yes')
    else:
        print('No')