import math

cnt = int(input())

for i in range(cnt):
    answer = 0
    st, ed = [int(x) for x in input().split()]

    for j in range(int(math.sqrt(st)), int(math.sqrt(ed) + 1)):
        if((j * j) in range(st, ed + 1)):
            answer += 1
    print(answer)
