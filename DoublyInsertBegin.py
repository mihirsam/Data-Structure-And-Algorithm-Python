# Insert node at begining of doubly linked list

class Node:
    def __init__(self, data = None):
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

    def insertBegin(self):
        data = int(input("\nEnter Data : "))
        
        if self.head.data is None:
            self.head.data = data
        else:
            ptr = Node(data)
            ptr.next = self.head
            self.head.prev = ptr
            self.head = ptr
    
if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n1. Display\n2. Insert Node\n3. Exit\nChoice : "))
        
        if choice is 1:
            linkedList.display()
        elif choice == 2:
            linkedList.insertBegin()
        elif choice == 3:
            break
        else:
            print("\nInvalid Input!")