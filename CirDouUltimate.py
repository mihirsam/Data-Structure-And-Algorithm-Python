# cicular doubly linked list

class Node:
    def __init__(self, data = None):
        self.next = None
        self.prev = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head.data is None:
            print("\nLinked List is Empty!")
        else:
            ptr = self.head

            while True:
                print(f"{ptr.data} -> ", end="")
                ptr = ptr.next

                if ptr is self.head:
                    break
    
    def insertPosition(self):
        pos = int(input("\nEnter Position : "))
        dat = int(input("Entre Data : "))

        ptr = Node(dat)

        if pos is 0:
            if self.head.data is None:
                ptr.prev = ptr
                ptr.next = ptr
                self.head = ptr
                print("\nNode Inserted!")
            else:
                temp = self.head

                while True:
                    if temp.next is self.head:
                        temp.next = ptr
                        ptr.prev = temp
                        ptr.next = self.head
                        self.head.prev = ptr
                        self.head = ptr

                        print("\nNode Inserted!")
                        break
                    else:
                        temp = temp.next

        else:
            if self.head.data is None:
                print("\nInvalid Index!")
            else:
                temp = self.head
                flag = 0

                while True:
                    if pos == flag+1:
                        nxt = temp.next
                        temp.next = ptr
                        ptr.prev = temp
                        ptr.next = nxt
                        nxt.prev = ptr
                        print("\nNode Inserted!")
                        break
                    else:
                        temp = temp.next
                        flag += 1

                    if temp is self.head:
                        print("\nInvalid Position")
                        break

    def deletePosition(self):
        pos = int(input("\nEnter Position : "))

        if self.head.data is None:
            print("\nLinked List Is Empty!")
        else:
            if pos is 0:
                if self.head.next is self.head:
                    self.head = Node()
                    print("\nNode Deleted!")
                else:
                    temp = self.head

                    while True:
                        if temp.next is self.head:
                            nxt = self.head.next
                            nxt.prev = temp
                            temp.next = nxt
                            self.head = nxt
                            print("\nNode Deleted!")
                            break
                        else:
                            temp = temp.next
            else:
                flag = 0
                temp = self.head

                while True:
                    if pos == flag and temp is not self.head:
                        prv = temp.prev
                        nxt = temp.next

                        prv.next = nxt
                        nxt.prev = prv

                        print("\nNode Deleted!")
                        break
                    else:
                        temp = temp.next
                        flag += 1

                    if temp is self.head:
                        print("\nInvalid Position!")
                        break

if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.head = Node()

    while True:
        choice = int(input("\n1. Display\n2. Insert\n3. Delete\n4. Exit\nChoice : "))
        
        if choice is 1:
            linkedList.display()
        elif choice is 2:
            linkedList.insertPosition()
        elif choice is 3:
            linkedList.deletePosition()
        elif choice is 4:
            break
        else:
            print("\nInvalid Input!")

