def find_element_indices(lst, element):
    indices = []
    for i in range(len(lst)):
        if lst[i] == element:
            indices.append(i)
    return indices
lst = [1, 2, 3, 2, 1, 3, 4, 5, 4, 4]
element = 4
indices = find_element_indices(lst, element)
print(indices)
