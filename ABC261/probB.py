N = int(input())

table = []

for _ in range(N):
    temp = []
    for char in input():
        temp.append(char)
    table.append(temp)

ans = "correct"

for i in range(N):
    if ans == "incorrect":
        break
    for j in range(N):
        if table[i][j] == "D" and table[j][i] == "D":
            continue
        elif table[i][j] == "L" and table[j][i] == "W":
            continue
        elif table[i][j] == "W" and table[j][i] == "L":
            continue
        elif table[i][j] == "-" and table[j][i] == "-":
            continue
        else:
            ans = "incorrect"
            break

print(ans)