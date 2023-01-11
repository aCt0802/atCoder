N, X, Y = map(int, input().split())
r = {
    N : 1
}
b = {}

can_continue = True

while(can_continue):
    r_levels = list(r.keys())
    for level in r_levels:
        if level != 1:
            if level in b.keys():
                b[level] += (X * r[level])
            else:
                b[level] = (X * r[level])
            if (level - 1) in r.keys():
                r[(level - 1)] += 1
            else:
                r[(level - 1)] = 1
            r.pop(level)
    b_levels = list(b.keys())
    for level in b_levels:
        if level != 1:
            if (level - 1) in b.keys():
                b[level - 1] += (Y * b[level])
            else:
                b[level - 1] = (Y * b[level])
            if (level - 1) in r.keys():
                r[(level - 1)] += 1
            else:
                r[(level - 1)] = 1
            b.pop(level)
    can_continue = ((list(r.keys()) != [1]) and (list(b.keys()) != [1]))

print(b.get(1, 0))