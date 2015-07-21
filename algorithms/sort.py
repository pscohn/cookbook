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
