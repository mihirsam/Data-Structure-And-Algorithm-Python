# basic binary search tree

temp = []

class Node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.lis = []

    def InsertNode(self, node, data):
        if self.root is None:
            self.root = Node(data)
        elif node.value <= data:
            if node.right is not None:
                self.InsertNode(node.right, data)
            else:
                node.right = Node(data)
        elif node.value > data:
            if node.left is not None:
                self.InsertNode(node.left, data)
            else:
                node.left = Node(data)
        
    def InOrder(self, node):
        if node:
            self.InOrder(node.left)
            print(f"{node.value} -> ", end="")
            self.InOrder(node.right)

    def SearchNode(self, node, data):
        if node:
            if node.value == data:
                return True
            elif node.value <= data:
                return self.SearchNode(node.right, data)
            elif node.value > data:
                return self.SearchNode(node.left, data)
        else:
            return False

    def SaveElement(self, node):
        if node:
            self.InOrder(node.left)
            self.lis.append(node.value)
            self.InOrder(node.right)

    def DeleteNode(self, node, data):
        if node:
            if node.value == data:
                self.lis = []
                self.SaveElement(node)
                print(self.lis)
                return True
            elif node.value < data:
                if self.SearchNode(node.right, data):
                    node.right = None
                return False
            elif node.value > data:
                if self.SearchNode(node.left, data):
                    node.left = None
                return False
        else:
            print("\nNode Not Found!")
            return False

if __name__ == "__main__":
    bst = BinarySearchTree()

    while True:
        choice = int(input("\n1. Display\n2. Insert\n3. Search Data\n4. Delete Node\n5. Exit\nChoice : "))

        if choice is 1:
            bst.InOrder(bst.root)
        elif choice is 2:
            data = int(input("\nEnter Data : "))
            bst.InsertNode(bst.root, data)
        elif choice is 3:
            data = int(input("\nEnter Data : "))
            print("\n",bst.SearchNode(bst.root, data))
        elif choice is 4:
            data = int(input("\nEnter Data To Delete : "))
            bst.DeleteNode(bst.root, data)

            bst.lis.remove(data)

            for item in bst.lis:
                bst.InsertNode(bst.root, item)
            print("\nNode Deleted!")
        elif choice is 5:
            break
        else:
            print("\nInvalid Input!")