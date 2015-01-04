#!/usr/bin/python3


def calculate_unfairness(items):
    items.sort()
    min2 = items[-1]
    for i in range(cnt - k + 1):
        if(min2 > (items[i + k - 1] - items[i])):
            min2 = items[i + k - 1] - items[i]
    return min2


if __name__ == '__main__':
    cnt = int(input())
    k = int(input())
    items = []
    for _ in range(cnt):
        items.append(int(input()))
    print(calculate_unfairness(items))
