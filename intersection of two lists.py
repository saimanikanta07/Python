def intersection_of_lists(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
result = intersection_of_lists(list1, list2)
print(result)
