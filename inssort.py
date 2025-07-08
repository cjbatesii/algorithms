import random as rd
import time

def insertion_sort(lst):
    strt = time.perf_counter()
    for i in range(1, len(lst)):
        val = lst[i]
        j   = i-1

        while (j >= 0) and (val < lst[j]):
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = val
    endx = time.perf_counter()
    print(f'| Insertion Sort | {endx-strt:.4f} |')
    return lst

def sort_test():
    c = 0
    lst = []
    bar = '-'*27

    while c < 4499:
        lst.append(rd.randint(1, 1000))
        c += 1
    print(bar)
    insertion_sort(lst)
    print(bar)

if __name__ == "__main__":
    sort_test()