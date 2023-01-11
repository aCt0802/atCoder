R, C = map(int, input().split())

w = abs(7 - (R - 1))
h = abs(7 - (C - 1))

if max(w, h) % 2 == 0:
    print("white")
else:
    print("black")
