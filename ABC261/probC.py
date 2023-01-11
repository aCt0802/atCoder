N = int(input())
strings : set = set({})
count : dict = {}
for i in range(N):
    temp = input()
    if temp in strings:
        print('{}({})'.format(temp,count[temp]))
        count[temp] += 1
    else:
        count[temp] = 1
        strings.add(temp)
        print(temp)