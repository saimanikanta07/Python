def find_second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest
lst = [5, 2, 8, 1, 7]
second_largest_number = find_second_largest(lst)
print("The second largest number is:", second_largest_number)
