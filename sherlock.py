import functools
import fractions


def gcd(numbers):
    return functools.reduce(fractions.gcd, numbers)

cnt = int(input())

for _ in range(cnt):
    k = int(input())
    li = [int(x) for x in input().split()]
    if(gcd(li) == 1):
        print("YES")
    else:
        print("NO")
        
