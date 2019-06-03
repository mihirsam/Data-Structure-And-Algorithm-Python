# kruskals algorithm for minimum spanning tree

import sys
sys.setrecursionlimit(10000)

    
def setGroup(edge):
    keyList = []
    for key in graph.keys():
        if edge[0] in graph[key] and edge[1] in graph[key]:
            return False
        elif edge[0] in graph[key] and edge[1] not in graph[key]:
            graph[key].append(edge[1])
            mainGraph[key].append(edge)
            keyList.append(key)
        elif edge[1] in graph[key] and edge[0] not in graph[key]:
            graph[key].append(edge[0])
            mainGraph[key].append(edge)
            keyList.append(key)

    print("\nBefore graph: ", graph,"\nMain graph : ", mainGraph)

    if len(keyList) == 0:
        mainGraph[len(mainGraph)+1] = [edge]
        graph[len(graph)+1] = [edge[0], edge[1]]

    elif len(keyList) > 1:
        graph[keyList[0]] + graph[keyList[1]]
        
        temp = []

        for item in graph[keyList[0]]:
            if item not in temp:
                temp.append(item)

        graph[keyList[0]] = temp
        del graph[keyList[1]]
        del mainGraph[keyList[1]]
        del keyList[1]

        # graph.pop('keylist[1]', None)
    
    print("\nBefore graph: ", graph,"\nMain graph : ", mainGraph)


InitGraph = {'A' : [('A', 'C', 3)], 'B' : [('B', 'C', 10), ('B', 'D', 4)], 'C' : [('A', 'C', 3), ('B', 'C', 10), ('C', 'D', 2), ('C', 'E', 6)], 'D' : [('C', 'D', 2), ('D', 'E', 1)], 'E' : [('C', 'E', 6), ('D', 'E', 1)]}
graph = {}
mainGraph = {}
sortedGraph = []


for sets in InitGraph.values():
    for item in sets:
        if item not in sortedGraph:
            sortedGraph.append(item)

for i in range(0, len(sortedGraph)):
    for j in range(0, len(sortedGraph)-i-1):
        if sortedGraph[j][2] > sortedGraph[j+1][2]:
            sortedGraph[j], sortedGraph[j+1] = sortedGraph[j+1], sortedGraph[j]

print("Sorted : ", sortedGraph)

for item in sortedGraph:
    setGroup(item)

print(mainGraph)

