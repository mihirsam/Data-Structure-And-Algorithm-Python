# implementing normal linked list using class

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head

        while(temp != None):
            print(f"{temp.data} -> ", end="")
            temp = temp.next

if __name__ == "__main__":
    first = Node(0)
    second = Node(1)
    third = Node(2)

    linkedList = LinkedList()
    linkedList.head = Node()

    first.data = 0
    first.next = second

    second.data = 1
    second.next = third

    third.data = 2
    third.next = None

    linkedList.head = first
    linkedList.display()