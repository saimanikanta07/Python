def find_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency
lst = [1, 2, 3, 2, 1, 3, 4, 5, 4, 4]
frequency = find_frequency(lst)
print(frequency)
