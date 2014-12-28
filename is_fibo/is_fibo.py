def is_fibo(num):
    items = [0, 1]
    while(items[-1] <= num):
        if(items[-1] == num):
            print("isFibo")
            return
        items.append(items[-1] + items[-2])
    print("IsNotFibo")    
    return    

count  =  int(input())
                        
for _ in range(count):
    num = int(input())
    is_fibo(num)


