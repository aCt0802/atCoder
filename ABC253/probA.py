import statistics
a,b,c = map(float, input().split())
ans = 'Yes' if statistics.median(sorted([a,b,c])) == b else 'No'
print(ans)