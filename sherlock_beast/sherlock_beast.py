cnt = int(input())


def calc(num):
    mi = -1
    for i in range(num + 1):
        if(i % 3 == 0 and (num - i) % 5 == 0):
            mi = i
    return mi


for _ in range(cnt):
    num = int(input())
    if num < 3:
        print("-1")
    else:
        mi = calc(num)
        if(mi == -1):
            print("-1")
        else:
            print("5" * mi + "3" * (num - mi))
