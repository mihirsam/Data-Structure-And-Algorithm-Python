# Divide and conquer method to find min and max of list containing 2^n elements

def MINMAX(S):
    if len(S) == 2:
        return (max(S[0], S[1]), min(S[0], S[1]))

    else:
        S1 = S[0:int(len(S)/2)]
        S2 = S[int(len(S)/2):]

        (max1, min1) = MINMAX(S1)
        (max2, min2) = MINMAX(S2)

        return (max(max1, max2), min(min1, min2))

lis = [1, 2, 3, 4, 5, 6, 7, 8]

print(MINMAX(lis))