def union_of_lists(list1, list2):
    union = list(set(list1) | set(list2))
    return union
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
result = union_of_lists(list1, list2)
print(result)
