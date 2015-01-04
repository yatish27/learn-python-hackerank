import functools
import fractions


def gcd(numbers):
    return functools.reduce(fractions.gcd, numbers)

cnt = int(input())

for _ in range(cnt):
    k = int(input())
    li = [int(x) for x in input().split()]
    print("YES" if gcd(li) == 1 else "NO")
