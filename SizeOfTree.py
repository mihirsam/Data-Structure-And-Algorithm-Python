# find size of the tree

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def InOrder(self, node):
        if node:
            self.InOrder(node.left)
            print(f"{node.value} -> ", end="")
            self.InOrder(node.right)
        
    def Size(self, node):
        if node:
            lsize = self.Size(node.left)
            rsize = self.Size(node.right)
            return lsize + 1 + rsize
        else:
            return 0

if __name__ == "__main__":
    binarytree = BinaryTree()
    binarytree.root = Node(1)
    binarytree.root.left = Node(2)
    binarytree.root.right = Node(3)
    binarytree.root.left.left = Node(4)
    binarytree.root.left.right = Node(5)
    binarytree.root.left.left.right = Node(6)
    binarytree.root.right.left = Node(7)
    binarytree.root.right.left.right = Node(8)

    print("\nInOrder : ")
    binarytree.InOrder(binarytree.root)
    print("\nSize : ", binarytree.Size(binarytree.root))
