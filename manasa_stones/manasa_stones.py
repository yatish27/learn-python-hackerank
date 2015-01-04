k = int(input())

for _ in range(k):
    cnt = int(input())
    a = int(input())
    b = int(input())

    li = set()
    for i in range(cnt):
        li.add(a * i + b * (cnt - i - 1))

    for item in sorted(li):
        print(item, '', end='')
    print()
