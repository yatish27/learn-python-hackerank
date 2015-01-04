import collections
string = input()

h = collections.Counter(string)

flag = 0

for value in h.values():
    if value % 2 != 0:
        flag += 1

print("YES" if flag > 1 else "NO")
