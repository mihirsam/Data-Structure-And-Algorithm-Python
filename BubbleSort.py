# Bubble sort

import random

def BubbleSort(lis):
    for i in range(len(lis)):
        for j in range(len(lis)-i-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    
    print(lis)

lis = []
for i in range(100):
    lis.append(random.randint(0, 1000))

BubbleSort(lis)