H1, W1 = map(int, input().split())
vector1 = []
for _ in range(H1):
    vector1.append(list(map(int, input().split())))

print("vector1")
print(vector1)

H2, W2 = map(int, input().split())
vector2 = []
for _ in range(H2):
    vector2.append(list(map(int, input().split())))

print("vecto2")
print(vector2)

end_flg = False

ans_flg = False

for vec1idx in range(H1):
    if end_flg:
        break
    start = 0
    end = W2
    while end <= W1:
        if end_flg:
            break
        if vector1[start:end] == vector2[0]:
            if end_flg:
                break
            #合致しなければskip
            #すべて見終わる前にindexがoverすれば答えはtrue
            vec2idx = 1
            for vec1 in vector1[vec1idx + 1:vec1idx + 2]:
                print("比較元")
                print(vec1[start, end])
                print("比較先")
                print(vector2[vec2idx])
                if end_flg:
                    break
                if vec1[start, end] == vector2[vec2idx]:
                    vec2idx += 1
                if vec2idx == W2 + 1:
                    ans_flg = True
                    end_flg = True
        start += 1
        end += 1

ans = 'Yes' if ans_flg else 'No'
print(ans)