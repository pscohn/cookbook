#!/usr/bin/env python3


def three_sum_brute(array):
    count = 0
    for x in range(0, len(array)):
        for y in range(x+1, len(array)):
            for z in range(y+1, len(array)):
                if array[x] + array[y] + array[z] == 0:
                    count +=1
    return count

def three_sum(array):
    count = 0


    return count



if __name__ == '__main__':
    main()

