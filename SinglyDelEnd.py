# Delete end node from singly linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        print("\n\n")
        if self.head.data is None:
            print("\nLinked List Is Empty!\n")
        else:
            self.ptr = self.head

            while self.ptr is not None:
                print(f"{self.ptr.data} -> ", end="")
                self.ptr = self.ptr.next

    def insertPosition(self):
        position = int(input("Enter Position : "))
        data = int(input("\nEnter Data : "))
        self.ptr = Node(data)

        if position is 0:
            if self.head.data is None:
                self.ptr.next = None
                self.head = self.ptr
                print("\nNode Inserted!")
            else:
                self.ptr.next = self.head
                self.head = self.ptr
                print("\nNode Inserted!")
        else:
            self.temp = self.head
            self.flag = 0
            while self.temp is not None:
                if position == self.flag+1:
                    self.ptr.next = self.temp.next
                    self.temp.next = self.ptr
                    print("\nNode Inserted!")
                    break
                else:
                    self.temp = self.temp.next
                    self.flag += 1

    def deleteEnd(self):
        if self.head.data is None:
            print("\nLinked List Is Empty!")
        elif self.head.next is None:
            self.head = Node()
        else:
            self.temp = self.head
            self.prev = self.temp

            while self.prev is not None:
                if self.temp.next is None:
                    self.prev.next = None
                    print("\nNode Deleted!")
                    break
                else:
                    self.prev = self.temp
                    self.temp = self.temp.next
    

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n\n1. Display\n2. Insert At Position\n3. Delete End\n4. Exit\nChoice : "))
        
        if choice == 1:
            linkedList.display()
        elif choice == 2:   
            linkedList.insertPosition()
        elif choice == 3:
            linkedList.deleteEnd()
        elif choice == 4:
            break
        else:
            print("\nInvalid Input!")
