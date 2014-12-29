#!/usr/bin/python3
def calculate_height(num):
    init = 1
    for i in range(num):
        if((i % 2) == 0):
            init*=2
        else:
            init+=1
    return init            
        
if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        print(calculate_height(int(input())))                     
