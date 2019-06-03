# Insert last in doubly linked

class Node:
    def __init__(self, data=None):
        self.prev = None
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head.data is None:
            print("\nLinked List Is Empty!")
        else:
            ptr = self.head

            while ptr is not None:
                print(f"{ptr.data} -> ", end="")
                ptr = ptr.next

    def insertEnd(self):
        data = int(input("\nEnter Data : "))
        
        if self.head.data is None:
            self.head.data = data
        else:
            ptr = self.head

            while ptr is not None:
                if ptr.next is None:
                    temp = Node(data)
                    ptr.next = temp
                    temp.prev = ptr
                    break
                else:
                    ptr = ptr.next


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n1. Display\n2. Insert End\n3. Exit\nChoice : "))
        
        if choice is 1:
            linkedList.display()
        elif choice is 2:
            linkedList.insertEnd()
        elif choice is 3:
            break
        else:
            print("\nInvalid Input!")