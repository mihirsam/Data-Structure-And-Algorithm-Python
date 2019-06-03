# basic doubly linked list

class Node:
    def __init__(self, data=None):
        self.prev = None
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        ptr = self.head

        if (ptr.data == None):
            print("\nLinked List Is Empty!")
        else:
            while ptr is not None:
                print(f"{ptr.data} -> ", end="")
                ptr = ptr.next


if __name__ == "__main__":
    linkedList = LinkedList()

    first = Node(1)
    second = Node(2)
    third = Node(3)

    first.prev = None
    first.next = second
    second.prev = first
    second.next = third
    third.prev = second
    third.next = None

    linkedList.head = first

    linkedList.display()