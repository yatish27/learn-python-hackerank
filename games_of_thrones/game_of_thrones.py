string = input()

h = {}
for i in string:
    h.setdefault(i, 0)
    h[i]+=1

flag = 0

for value in h.values():
    if(value % 2 == 0):  
        continue
    else:
        flag+=1
  
if (flag > 1): 
    print("NO") 
else:
    print("YES")

