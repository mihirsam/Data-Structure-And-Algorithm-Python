# prims algorithm for minimum spanning tree
import sys
sys.setrecursionlimit(10000)
def ConnectNode():
    n1 = input("\nEnter Node 1 : ")
    n2 = input("Enter Node 2 : ")
    weight = int(input("Enter Weight : "))

    if n1 in graph.keys():
        graph[n1].append((n1, n2, weight))
    else:
        graph[n1] = [(n1, n2, weight)]

    if n2 in graph.keys():
        graph[n2].append((n1, n2, weight))
    else:
        graph[n2] = [(n1, n2, weight)]

    print("\nNode Connected!")

def PrimsAlgo(node):
    visited.append(node)

    for item in graph[node]:
        if item not in dotted:
            dotted.append(item)

    weight = 1000
    temp = None

    for item in dotted:
        if item[0] not in visited or item[1] not in visited:
            if weight > item[2]:
                weight = item[2]
                temp = item
    if temp != None:
        final.append(temp)
        dotted.remove(temp)


        #print(f"\nVisited : {visited}\nDotted : {dotted}\nFinal : {final}")

        if temp[0] not in visited:
            PrimsAlgo(temp[0])
        elif temp[1] not in visited:
            PrimsAlgo(temp[1])
        
    
    
    


graph = {'A' : [('A', 'C', 3)], 'B' : [('B', 'C', 10), ('B', 'D', 4)], 'C' : [('A', 'C', 3), ('B', 'C', 10), ('C', 'D', 2), ('C', 'E', 6)], 'D' : [('C', 'D', 2), ('D', 'E', 1)], 'E' : [('C', 'E', 6), ('D', 'E', 1)]}
dotted = []
visited = []
final = []

while True:
    choice = int(input("\n1. Connect\n2. Prims\n3. Exit\nChoice : "))

    if choice is 1:
        ConnectNode()
    elif choice is 2:
        PrimsAlgo('B')
        print(f"\nFinal : {final}\nVisited : {visited}\nDotted : {dotted}")

        cost = 0
        for item in final:
            cost += item[2]
        print(f"\nCost = {cost}")
    elif choice is 3:
        break
    else:
        print("\nInvalid Input!")