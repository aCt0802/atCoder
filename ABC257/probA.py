n, x = map(int,input().split())
chars = "abcdefghijklmnopqrstuvwxyz".upper()
string = ''
for char in chars:
    string += char * n
print(string[x - 1])    