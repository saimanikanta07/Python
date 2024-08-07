def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_numbers(lst)
print(result)
