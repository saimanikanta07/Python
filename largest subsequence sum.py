def largest_subsequence_sum(lst):
    max_sum = lst[0]  
    current_sum = lst[0]  

    
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)  
        max_sum = max(max_sum, current_sum)  

    return max_sum

lst = [1, -2, 3, 4, -5, 2, 7]
result = largest_subsequence_sum(lst)
print(result)
