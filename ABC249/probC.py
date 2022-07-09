n, k = map(int, input().split())
str_list = []
for i in range(n):
    str_list.append(input())
max_chars : int = 0
chara_dict = {}
for bit in range(2 ** n):
    chara_dict = {}
    for index in range(n):
        if ((bit >> index) & 1):
            for chara in str_list[index]:
                if chara not in chara_dict.keys():
                    chara_dict[chara] = 1
                else:
                    chara_dict[chara] += 1
    chara_list = []
    for key, value in chara_dict.items():
        if value == k:
            chara_list.append(key)
    max_chars = max(max_chars, len(chara_list))
print(max_chars)