def concatenate_lists(lists):
    concatenated_list = []
    for lst in lists:
        concatenated_list += lst
    return concatenated_list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
lists = [list1, list2, list3]
result = concatenate_lists(lists)
print(result)
