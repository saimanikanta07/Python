def find_max_min(lst):
    max_num = max(lst)
    min_num = min(lst)
    return max_num, min_num
lst = [5, 2, 9, 1, 7]
max_num, min_num = find_max_min(lst)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
