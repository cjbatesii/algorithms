import random as rd
import time

def selection_sort(lst):
    strt = time.perf_counter()
    for i in range(len(lst)):
        min_ind = i
 
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_ind]:
                min_ind = j
        lst[i], lst[min_ind] = lst[min_ind], lst[i]
    endx = time.perf_counter()
    print(f'| Selection Sort | {endx-strt:>.4f} |')
    return lst

def sort_test():
    c = 0
    lst = []
    bar = '-'*27

    while c < 4499: 
        lst.append(rd.randint(1, 1000))
        c += 1
    print(bar)
    selection_sort(lst)
    print(bar)

if __name__ == "__main__":
    sort_test()