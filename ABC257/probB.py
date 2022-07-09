N,K,Q = map(int, input().split())
peace = list(map(int, input().split()))
L = list(map(int, input().split()))

peace = sorted(peace)

for i in range(Q):
    location = peace[L[i] - 1]
    if location == N:
        pass
    else:
        findFLG = False
        for p in peace:
            if p == (location + 1):
              findFLG = True  
        if not findFLG:
            peace[L[i] - 1] += 1
        else:
            pass

print(' '.join(map(str, peace)))