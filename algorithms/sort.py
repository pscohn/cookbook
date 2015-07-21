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

def insertion(numbers):
    for i, _ in enumerate(numbers):
        j = i
        while j > 0 and numbers[j] < numbers[j-1]:
            numbers = swap(numbers, j, j-1)
            j -= 1
    return numbers
