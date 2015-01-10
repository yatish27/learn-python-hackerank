#!/usr/bin/python3
import math


def love_letter(string):
    sum = 0
    for i in range(math.floor(len(string)/2)):
        sum += abs(ord(string[i]) - ord(string[len(string) - 1 - i]))
    return sum


if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        print(love_letter(input()))
