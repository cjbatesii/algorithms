import random as rd
import time

########################################
# Quick Sort
# O()
########################################
def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[high] = lst[high], lst[i+1]
    return i+1

def quick_sort(lst, low, high):
    if low < high:
        pi = partition(lst, low, high)
        quick_sort(lst, low, pi-1)
        quick_sort(lst, pi+1, high)
    return lst

def sort_test():
    c = 0
    lst = []
    bar = '-'*27

    while c < 4499: 
        lst.append(rd.randint(1, 1000))
        c += 1
    print(bar)
    strt = time.perf_counter()
    quick_sort(lst, 0, len(lst)-1)
    endx = time.perf_counter()
    print(f'| Quick Sort     | {endx-strt:>.4f} |')
    print(bar)

if __name__ == "__main__":
    sort_test()