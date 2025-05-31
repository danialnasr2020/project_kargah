import re


def is_valid_code(code):
    return bool(re.fullmatch(r'[A-Za-z0-9]+', code))


n_and_t = input().split()
n = int(n_and_t[0])  
t = n_and_t[1]       

codes = []
for _ in range(n):
    codes.append(input().strip())


if t in codes and is_valid_code(t):
    print("yes")
else:
    print("no")

