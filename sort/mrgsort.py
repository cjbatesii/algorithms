import random as rd
import time

########################################
# Merge Sort
# O()
########################################
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    # Divide the list in two halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Sort the halves recursively
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the Sorted Halves
    return merge(left_half, right_half)

def merge(left, right):
    merged_lst = []
    i = 0
    j = 0

    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            merged_lst.append(left[i])
            i += 1
        else:
            merged_lst.append(right[j])
            j += 1

    # Add remaining elements from l/r
    while i < len(left):
        merged_lst.append(left[i])
        i += 1
    while j < len(right):
        merged_lst.append(right[j])
        j +=1
    return merged_lst

def sort_test():
    c = 0
    lst = []
    bar = '-'*27

    while c < 4499: 
        lst.append(rd.randint(1, 1000))
        c += 1
    print(bar)
    strt = time.perf_counter()
    merge_sort(lst)
    endx = time.perf_counter()
    print(f'| Merge Sort     | {endx-strt:>.4f} |')
    print(bar)

if __name__ == "__main__":
    sort_test()