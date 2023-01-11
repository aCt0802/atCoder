import math


N,X,Y,Z = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

students = []

for i in range(N):
    students.append(
        {
            'id' : i,
            'id_r' : N-(i+1),
            'math' : listA[i],
            'eng' : listB[i],
            'sum' : listA[i] + listB[i]
        }
    )

math_sorted = sorted(students, key=lambda x:(x['math'], x['id_r']))[-1::-1]
passed = [s['id'] + 1 for s in math_sorted[0:X]]
math_unpassed = math_sorted[X::]

eng_sorted = sorted(math_unpassed, key=lambda x:(x['eng'], x['id_r']))[-1::-1]
passed.extend([s['id'] + 1 for s in eng_sorted[0:Y]])
eng_unpassed = eng_sorted[Y::]

sum_sorted = sorted(eng_unpassed, key=lambda x:(x['sum'], x['id_r']))[-1::-1]
passed.extend([s['id'] + 1 for s in sum_sorted[0:Z]])

for elem in sorted(passed):
    print(elem)