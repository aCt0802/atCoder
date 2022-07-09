ms = {}
for i in range(int(input())):
    query = list(input().split())
    if query[0] == '1':
        ms[query[1]] = ms.get(query[1], 0) + 1
    elif query[0] == '2':
        ms[query[1]] -= min(int(query[2]), ms.get(query[1], 0))
    elif query[0] == '3':
        msList = [int(key) for key, val in ms.items() if val > 0]
        print(max(msList) - min(msList))