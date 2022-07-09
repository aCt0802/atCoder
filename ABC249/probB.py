input_str = input()
lower_exist : bool = False
upper_exist : bool = False
is_good : bool = True
chars = []
for char in input_str:
    if char in chars:
        is_good = False
        break
    if not lower_exist:
        lower_exist = char.islower()
    if not upper_exist:
        upper_exist = char.isupper()
    chars.append(char)

if is_good:
    is_good = (lower_exist and upper_exist)

print("Yes" if is_good else "No")
