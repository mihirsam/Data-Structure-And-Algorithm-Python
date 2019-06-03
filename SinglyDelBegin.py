# delete starting node from singly linked list

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        
        if self.head.data is None:
            print("\nLinked List Is Empty!")
        else:
            self.temp = self.head

            while self.temp is not None:
                print(f"{self.temp.data} -> ", end="")
                self.temp = self.temp.next
        
    def insertPosition(self):

        position = int(input("\nEnter Position Index : "))
        data = int(input("Enter Data : "))
        flag = 0
        self.ptr = Node(data)

        if position is 0:
            if self.head.data is None:
                self.ptr.next = None
                self.head = self.ptr
            else:
                self.ptr.next = self.head
                self.head = self.ptr
        
        else:
            self.temp = self.head

            while self.temp is not None:
                if position == flag+1:
                    self.ptr.next = self.temp.next
                    self.temp.next = self.ptr
                    break

                else:
                    flag += 1
                    self.temp = self.temp.next


    def deleteBegin(self):
        if self.head.data is None:
            print("\nLinked List Is empty!")
        else:
            self.head = self.head.next


if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n\n1. Display\n2. Insert At Position\n3. Delete Begining\n4. Exit\nChoice : "))
        
        if choice == 1:
            linkedList.display()
        elif choice == 2:   
            linkedList.insertPosition()
        elif choice == 3:
            linkedList.deleteBegin()
        elif choice == 4:
            break
        else:
            print("\nInvalid Input!")