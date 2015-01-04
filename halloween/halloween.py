cnt = int(input())

for i in range(cnt):
    k = int(input())
    if(k % 2 == 0):
        print(int((k/2) * (k/2)))
    else:
        print(int(int(k/2) * (int(k/2) + 1)))
