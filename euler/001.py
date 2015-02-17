#!/usr/bin/env python3


def get_multiples(x, y, maximum):
    for i in range(0, maximum):
        if i % x == 0 or i % y == 0:
            yield i 

def main():
    result = sum(get_multiples(3, 5, 1000))
    print(result)



if __name__ == '__main__':
    main()

