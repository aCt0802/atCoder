N, M = map(int, input().split())
listA = list(map(int, input().split()))
listB = map(int, input().split())

ans = 'Yes'

for elemB in listB:
    if elemB in listA:
        index = listA.index(elemB)
        listA.pop(index)
    else:
        ans = 'No'

print(ans)