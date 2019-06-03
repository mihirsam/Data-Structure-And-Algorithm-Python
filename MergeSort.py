# Merge Sort 
# Merge

import random
import sys

sys.setrecursionlimit(10000)

def Merge(l, m, h):
    one = lis[l:m+1]
    two = lis[m+1:]

    flag = l

    while (len(one) != 0 and len(two) != 0):
        if one[0] <= two[0]:
            lis[flag] = one[0]
            one.pop(0)
        else:
            lis[flag] = two[0]
            two.pop(0)

        flag += 1

    if len(one) != 0:
        for item in one:
            lis[flag] = item
            flag += 1
    
    if len(two) != 0:
        for item in two:
            lis[flag] = item
            flag += 1

def MergeSort(l, h):
    if l < h:
        m = int((l+h)/2)
        
        MergeSort(l, m)
        MergeSort(m+1, h)
        Merge(l, m, h)


lis = []

for i in range(9):
    lis.append(random.randint(0, 20))

print(lis)
print(sorted(lis))
MergeSort(0, 8)
print(lis)