def find_digits(num):
    s = 0
    for i in list(num):
        if int(i) == 0:
            continue
        if int(num) % int(i) == 0:
            s += 1
    print(s)

count = int(input())

for _ in range(count):
    num = input()
    find_digits(num)
