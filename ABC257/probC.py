N = int(input())
S = input()
W = list(map(int, input().split()))

search = min(W)
maxW = max(W) + 1

ans_list = []

lenW = len(W)

while(search != maxW):
    print("search : {}".format(search))
    count = 0
    for i in range(lenW):
        temp = W[i]
        assumed_addlut = '1' if temp >= search else '0'
        if S[i] == assumed_addlut:
            count+= 1
    ans_list.append(count)
    minus = search - 0.1
    plus = search + 0.1
    count = 0
    for i in range(lenW):
        temp = W[i]
        assumed_addlut = '1' if temp >= minus else '0'
        if S[i] == assumed_addlut:
            count+= 1
    ans_list.append(count)
    count = 0
    for i in range(lenW):
        temp = W[i]
        assumed_addlut = '1' if temp >= plus else '0'
        if S[i] == assumed_addlut:
            count+= 1
    ans_list.append(count)
    search += 1

print(max(ans_list))