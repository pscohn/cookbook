#!/usr/bin/env python3


def binary_search(sorted_array, item, low, high):
    index = int(((high - low) / 2) + low)
    middle_item = sorted_array[index]
    if middle_item == item:
        return index
    elif len(sorted_array[low:high]) == 1 and middle_item != item:
        return None
    elif middle_item > item:
        return binary_search(sorted_array, item, 0, index)
    elif middle_item < item:
        return binary_search(sorted_array, item, index, high)





if __name__ == '__main__':
    main()

