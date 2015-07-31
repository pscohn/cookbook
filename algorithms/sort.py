import math

def swap(numbers, i, j):
    temp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = temp
    return numbers

def selection(numbers):
    for i, num in enumerate(numbers):
        current_min = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[current_min]:
                current_min = j
        if current_min != i:
            numbers = swap(numbers, i, current_min)
    return numbers

def insertion(numbers, width=1):
    for i in range(0, len(numbers)):
        j = i
        while j > width-1 and numbers[j] < numbers[j-width]:
            numbers = swap(numbers, j, j-width)
            j -= width
    return numbers

def shell(numbers):
    #TODO
    numbers = insertion(numbers, 4)
    numbers = insertion(numbers, 3)
    return insertion(numbers)

def merge(numbers):
    if len(numbers) == 1 or numbers == []:
        return numbers

    mid = math.floor(len(numbers) / 2)
    split1 = numbers[:mid]
    split2 = numbers[mid:]
    sorted1 = merge(split1)
    sorted2 = merge(split2)

    i = 0
    j = 0
    final = []
    while i < len(sorted1) or j < len(sorted2):
        if i<len(sorted1) and (j == len(sorted2) or sorted1[i] <= sorted2[j]):
            final.append(sorted1[i])
            i += 1
        else:
            final.append(sorted2[j])
            j += 1
    return final

def quicksort_partition(numbers):
    lo = numbers[0]
    i = 1
    j = len(numbers) - 1
    while i <= j:
        if numbers[i] <= lo:
            i += 1
        elif numbers[j] >= lo:
            j -= 1
        else:
            numbers = swap(numbers, i, j)
            i += 1
            j -= 1

    numbers = swap(numbers, 0, j)
    return numbers
