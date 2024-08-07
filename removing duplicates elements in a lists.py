def remove_duplicates(lst):
    return list(set(lst))
lst = [1, 2, 3, 2, 1, 3, 4, 5, 4, 4]
unique_lst = remove_duplicates(lst)
print(unique_lst)
