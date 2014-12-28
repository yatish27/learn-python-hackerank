#!/usr/bin/python3

def alternating_char_count(string):
    cnt = 0
    for i in range(len(string)):
        if(string[i] == string[i+1]):
            cnt+=1
    return cnt

if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        print(alternating_char_count(input()))
