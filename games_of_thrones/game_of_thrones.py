string = input()

h = {}
for i in string:
    h.setdefault(i, 0)
    h[i]+=1

flag = 0

for value in h.values():
    (value % 2 == 0) ? continue : flag+=1
  
(flag > 1) ? print("NO") : print("YES")

