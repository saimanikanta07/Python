def kth_smallest_element(lst, k):
    lst.sort()
    return lst[k-1] 
lst = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
k = 3
result = kth_smallest_element(lst, k)
print(result)
