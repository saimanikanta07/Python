import random
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
lst = [1, 2, 3, 4, 5]
shuffled_lst = shuffle_list(lst)
print(shuffled_lst)
