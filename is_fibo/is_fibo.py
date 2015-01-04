def is_fibo(num):
    items = [0, 1]
    while(items[-1] <= num):
        if items[-1] == num:
            return True
        items.append(items[-1] + items[-2])
    return False


count = int(input())

for _ in range(count):
    num = int(input())
    print("IsFibo" if is_fibo(num) else "IsNotFibo")
