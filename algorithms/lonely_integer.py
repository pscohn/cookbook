#!/usr/bin/env python3
from collections import defaultdict

def lonely_integer(array):
    count = defaultdict(int)
    for i in array:
        count[i] += 1
    for k, v in count.items():
        if v == 1:
            return k

def main():
    size = input()
    items = input()
    array = items.split()
    result = lonely_integer(array)
    print(result)


if __name__ == '__main__':
    main()

