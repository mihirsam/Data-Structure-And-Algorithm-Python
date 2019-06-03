# Inserting at position in singly linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):

        if self.head.data is None:
            print("\nLinked List is empty!\n")
        else:
            self.ptr = self.head
            while self.ptr.next is not None:
                print(f"{self.ptr.data} -> ", end="")

                self.ptr = self.ptr.next

    def insertPosition(self):

        position = int(input("\nEnter Position Index : "))
        data = int(input("Enter Data : "))
        flag = 0
        self.ptr = Node(data)
        self.temp = self.head

        while self.temp is not None:
            if position is 0:
                self.ptr.next = self.head
                self.head = self.ptr
                break

            elif position == flag+1:
                self.ptr.next = self.temp.next
                self.temp.next = self.ptr
                break

            else:
                flag += 1
                self.temp = self.temp.next
                


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n\n1. Display\n2. Insert At Position\n3. Exit\nChoice : "))
        
        if choice == 1:
            linkedList.display()
        elif choice == 2:
            linkedList.insertPosition()
        elif choice == 3:
            break
        else:
            print("\nInvalid Input!")