# Inserting in singly linked list from the end

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def display(self):
        if self.head.data is None:
            print("\nThe Linked List is empty!")
        else:
            self.temp = self.head

            while self.temp is not None:
                print(f"{self.temp.data} -> ", end="")
                self.temp = self.temp.next

    def insertBegin(self):
        data = int(input("\nEnter Data : "))
        self.temp = Node(data)

        if self.head.data is None:
            self.temp.next = None
            self.head = self.temp

        else:
            self.temp.next = self.head
            self.head = self.temp

    
    def insertEnd(self):
        data = int(input("\nEnter Data : "))
        self.ptr = Node(data)
        self.ptr.next = None

        if self.head.data is None:
            self.head = self.ptr
        else:
            self.temp = self.head
            while self.temp is not None:
                if self.temp.next is None:
                    self.temp.next = self.ptr
                    break
                else:
                    self.temp = self.temp.next
            

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n\n1. Display\n2. Insert At Begining\n3. Insert At End\n4. Exit\nChoice : "))
        
        if choice == 1:
            linkedList.display()
        elif choice == 2:
            linkedList.insertBegin()
        elif choice == 3:
            linkedList.insertEnd()
        elif choice == 4:
            break
        else:
            print("\nInvalid Input!")