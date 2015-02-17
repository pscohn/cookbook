#!/usr/bin/env python
import sys

numbers = [5,4,1,8,7,2,6,3]

numbers = [5,9,12,3,1,53,193,6]

def sort_two(array_2):
    if len(array_2) != 2:
        raise Exception('array is not len 2')
    
    if array_2[0] > array_2[1]:
        r = [array_2[1], array_2[0]]
    else:
        r = array_2
    return r

def sort_array(array):
    if array == []:
        return array
    if len(array) == 1:
        return array

    half = int(len(array)/2)
    split1 = array[0:half]
    split2 = array[half:]

    if len(split1) > 2:
        r1 = sort_array(split1)
    elif len(split1) == 2:
        r1 = sort_two(split1)

    if len(split2) > 2:
        r2 = sort_array(split2)
    elif len(split2) == 2:
        r2 = sort_two(split2)

#    print(r1, r2)
    result = merge(r1, r2)

    return result

def merge(split1, split2):
    result = []
    j = 0
    k = 0
#    print('merging', split1, split2)
    for _ in range(0, len(split1)+len(split2)):
#        print(_)
        if j >= len(split1):
            result.append(split2[k])
            k += 1
            continue
        elif k >= len(split2):
            result.append(split1[j])
            j += 1
            continue
        if split1[j] <= split2[k]:
            result.append(split1[j])
            j += 1
        else:
            result.append(split2[k])
            k += 1
#    print('merge result:', result)
    return result

def merge_sort(array):
    half = int(len(array)/2)
    split1 = sort_array(array[0:half])
    split2 = sort_array(array[half:])
#    print('s1,s2', split1, split2)

    result = merge(split1, split2)
#    print('result', result)
    return result

def count_inversions_brute(array):
    sort = merge_sort(array)
    inversions = 0
    for i, _ in enumerate(array):
        for j, _ in enumerate(sort[i:]):
#            print(array, sort[i:])
            if array[i] > sort[j]:
                inversions += 1
    return inversions

def count_inversions(array):
    length = len(array)
    if array == []:
        return [], 0
    elif len(array) == 1:
        return array, 0
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]], 1
        else:
            return array, 0

    half = int(length / 2)
    first = array[0:half]
    second = array[half:]
    count_first, first_inversions = count_inversions(first)
    count_second, second_inversions = count_inversions(second)
    inversions = first_inversions + second_inversions
    j = 0
    k = 0
    result = []

    for _ in range(0, len(count_first) + len(count_second)):
        if j >= len(count_first):
            result += count_second[k:]
            break
        elif k >= len(count_second):
            result += count_first[j:]
            break
        elif count_first[j] <= count_second[k]:
            result.append(count_first[j])
            j += 1
        elif count_first[j] > count_second[k]:
            result.append(count_second[k])
            k += 1
            inversions += len(count_first[j:])

    return result, inversions

