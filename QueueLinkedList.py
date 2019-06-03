# Queue implemented with linked list

class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head.data is None:
            print("\nQueue is empty!")
        else:
            temp = self.head

            while True:
                if temp is None:
                    break
                else:
                    print(f"{temp.data}")
                    temp = temp.next
    
    def insertNode(self):
        dat = int(input("\nEnter Data : "))
        ptr = Node(dat)

        if self.head.data is None:
            ptr.next = None
            self.head = ptr
        else:
            ptr.next = self.head
            self.head = ptr
        print("\nNode Inserted!")

    def deleteNode(self):
        if self.head.data is None:
            print("\nQueue is empty!")
        else:
            if self.head.next is None:
                self.head = Node()
            else:
                ptr = self.head
                temp = ptr

                while True:
                    if ptr.next is None:
                        temp.next = None
                        break
                    else:
                        temp = ptr
                        ptr = ptr.next

            print("\nNode Deleted!")

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n1. Display\n2. Insert\n3. Delete\n4. Exit\nChoice : "))
        
        if choice is 1:
            linkedList.display()
        elif choice is 2:
            linkedList.insertNode()
        elif choice is 3:
            linkedList.deleteNode()
        elif choice is 4:
            break
        else:
            print("\nInvalid Input!")
                