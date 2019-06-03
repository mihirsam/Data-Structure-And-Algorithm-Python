# delete node from any position in singly linked list

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
            print("Linked List is Empty!")
        else:
            self.ptr = self.head

            while self.ptr is not None:
                print(f"{self.ptr.data} -> ", end="")
                self.ptr = self.ptr.next

    def insertPosition(self):
        position = int(input("\nEnter Position : "))
        data = int(input("Enter Data : "))
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
            flag = 0
            while self.temp is not None:
                if position == flag+1:
                    self.ptr.next = self.temp.next
                    self.temp.next = self.ptr
                    print("\nNode Inserted!")
                    break
                else:
                    self.temp = self.temp.next
                    flag += 1

    def deletePosition(self):
        position = int(input("\nEnter Position : "))

        if position is 0:
            if self.head.data is None:
                print("\nLinked List Is Empty!")
            else:
                if self.head.next is None:
                    self.head = Node()
                else:
                    self.head = self.head.next
                print("\nNode Deleted!")
        else:
            self.ptr = self.head
            self.temp = self.ptr

            flag = 0

            while self.ptr is not None:
                if position == flag:
                    self.temp.next = self.ptr.next
                    print("\nNode Deleted!")
                    break
                else:
                    self.temp = self.ptr
                    self.ptr = self.ptr.next
                    flag += 1

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n\n1. Display\n2. Insert At Position\n3. Delete Position\n4. Exit\nChoice : "))
        
        if choice == 1:
            linkedList.display()
        elif choice == 2:   
            linkedList.insertPosition()
        elif choice == 3:
            linkedList.deletePosition()
        elif choice == 4:
            break
        else:
            print("\nInvalid Input!")