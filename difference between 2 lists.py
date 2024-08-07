def difference_of_lists(list1, list2):
    difference = list(set(list1) - set(list2))
    return difference
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
result = difference_of_lists(list1, list2)
print(result)
