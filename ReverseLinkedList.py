# reversing linked list

class Node:
    def __init__(self, val = None):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.flagy = None

    def display(self):
        if self.head.value is None:
            print("\nLinked List is empty!")
        else:
            ptr = self.head

            while ptr is not None:
                print(f"{ptr.value} -> ", end="")
                ptr = ptr.next
        
    def InsertPosition(self):
        pos = int(input("\nEnter Position : "))
        data = int(input("Enter Data : "))

        ptr = Node(data)

        if pos == 0:
            if self.head.value is None:
                ptr.next = None
                self.head = ptr
            else:
                ptr.next = self.head
                self.head = ptr
            print("\nNode Inserted!")
        else:
            flag = 0
            temp = self.head

            while temp is not None:
                if pos == flag+1:
                    ptr.next = temp.next
                    temp.next = ptr
                    print("\nNode Inserted!")
                    break
                else:
                    temp = temp.next
                    flag += 1
    
    def ReverseList(self, node):
        if self.head == node:
            self.head.next.next = self.head
            self.head.next = None
            self.head = self.flagy
        else:
            ptr = self.head
            temp = ptr

            while ptr.next is not node:
                temp = ptr
                ptr = ptr.next

                if ptr.next is None:
                    self.flagy = ptr

            ptr.next = temp
            self.ReverseList(ptr) 



if __name__ == "__main__":
    linkedlist = LinkedList()

    while True:
        choice = int(input("\n1. Display\n2. Insert\n3. Reverse\n4. Exit\nChoice : "))

        if choice is 1:
            linkedlist.display()
        elif choice is 2:
            linkedlist.InsertPosition()
        elif choice is 3:
            linkedlist.ReverseList(None)
            linkedlist.display()
        elif choice is 4:
            break
        else:
            print("\nInvalid Input!")        