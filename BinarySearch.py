# simple binary search
import random

lis = []

for i in range(0, 100):
    lis.append(random.randint(0, 1000))

lis.sort()
print(lis)

def BinarySearch(begin, end, num):
    if begin >= end:
        print("\nnumber Not found!")
    elif num > lis[int((begin+end)/2)]:
        begin = int((begin+end)/2) + 1
        print(f"\nbegin : {begin}\nEnd : {end}")
        BinarySearch(begin, end, num)

    elif num < lis[int((begin+end)/2)]:
        end = int((begin+end)/2) - 1
        print(f"\nbegin : {begin}\nEnd : {end}")
        BinarySearch(begin, end, num)

    elif num == lis[int((begin+end)/2)]:
        print(f"\nbegin : {begin}\nEnd : {end}")
        print("\nNumber Found")

    

num = int(input("\nEnter Number : "))
BinarySearch(0, 99, num)