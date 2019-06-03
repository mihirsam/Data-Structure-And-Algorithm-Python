# depth first search
import sys
sys.setrecursionlimit(100000)
stack = []
res = []
adjList = {1 : [2, 4], 2 : [1, 3, 5, 7, 8], 3 : [2, 4, 9, 10], 4 : [1, 3], 5 : [2, 6, 7, 8], 6 : [5], 7 : [2, 5, 8], 8 : [2, 5, 7], 9 : [3], 10 : [3]}

res.append(1)

def DFS(node):
    flag = 0
    for item in adjList[node]:
        if item not in res:
            res.append(item)
            stack.append(node)
            DFS(item)
            flag += 1
    
    if flag == 0 and len(stack) != 0:
        DFS(stack.pop(-1))

DFS(1)
print(res)