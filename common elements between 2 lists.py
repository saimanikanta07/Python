def common_elements(list1, list2):
    common = list(set(list1) & set(list2))
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print(result)
