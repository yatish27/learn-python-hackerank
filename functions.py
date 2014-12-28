import math 

def line_print():
    print('+', '-'*4)
    print('+', '-'*4)
    print('+')

    print('|', ' '*4)
    print('|', ' '*4)
    print('|', ' '*4)
    print('|', ' '*4)

line_print()

def fizz_buzz(n):
    if(n % 3 == 0):
        print("Fizz"),
    elif(n % 5 == 0):
        print("Buzz"),
    else:
        print(n),
    print("")    


for i in range(100):
    fizz_buzz(i)

str = "Yatish Mehta".count
print(str)
