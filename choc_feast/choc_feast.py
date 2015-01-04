import math 

T = int(input())

for i in range(T):
    N,C,M = [int(x) for x in input().split()]
    answer, carry = int(N/C), 0
    dist = answer
    while((dist+carry) >= M):
        dist, carry = divmod(dist + carry, M)
        answer+=dist

    print(answer)        
