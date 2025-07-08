import random as rd
import time

# O(n^2) - quadratic time
def bubble_sort(lst):
    nlst = lst
    strt = time.perf_counter()
    for i in range(len(nlst)):
        for j in range(len(nlst)-i-1):
            if nlst[j] > nlst[j+1]:
                nlst[j], nlst[j+1] = nlst[j+1], nlst[j]
    endx = time.perf_counter()
    print(f'| Bubble Sort    | {endx-strt:>.4f} |')

def sort_test():
    c = 0
    lst = []
    bar = '-'*27

    while c < 4499: 
        lst.append(rd.randint(1, 1000))
        c += 1
    print(bar)
    bubble_sort(lst)
    print(bar)

if __name__ == "__main__":
    sort_test()