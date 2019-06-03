# breadth first search 

adjList = {}
queue = []
res = []

"""
numNode = int(input("\nEnter Number Of Node : "))

for i in range(1, numNode+1):
    conNode = input(f"\nEnter Node Connected to Node {i} : ")
    conNode = conNode.split(' ')
    conNode  = [int(x) for x in conNode]
    adjList[i] = conNode
"""
adjList = {1 : [2, 4], 2 : [1, 3, 5, 7, 8], 3 : [2, 4, 9, 10], 4 : [1, 3], 5 : [2, 6, 7, 8], 6 : [5], 7 : [2, 5, 8], 8 : [2, 5, 7], 9 : [3], 10 : [3]}
queue.append(list(adjList.keys())[0])
print(adjList, queue)
def BFS():
    node = queue.pop(0)

    for i in adjList[node]:
        if i not in queue and i not in res:
            queue.append(i)
    
    res.append(node)

    if len(queue) != 0:
        BFS()
BFS()
print(res)