# implementing binary tree

nodeNum = 0

class Node:
    def __init__(self, val = None):
        global nodeNum

        self.left = None
        self.right = None
        self.value = val
        self.nodeVal = nodeNum

        nodeNum += 1

    
class BinaryTree:
    def __init__(self):
        self.root = None

    def displayInOrder(self, node):
    # left-root-right
        if node:
            self.displayInOrder(node.left)
            print(f"{node.value} - ", end="")
            self.displayInOrder(node.right)

    def displayPreOrder(self, node):
    # root-left-right
        if node:
            print(f"{node.value} - ", end="")
            self.displayPreOrder(node.left)
            self.displayPreOrder(node.right)
            
    def displayPostOrder(self, node):
    # left-right-root
        if node:
            self.displayPostOrder(node.left)
            self.displayPostOrder(node.right)
            print(f"{node.value} - ", end="")


if __name__ == "__main__":
    tree = BinaryTree()
    tree.root = Node(0)

    oneLeft = Node(1)
    twoLeft = Node(2)
    threeLeft = Node(3)
    
    oneRight = Node(4)
    twoRight = Node(5)
    threeRight = Node(6)

    tree.root.left = oneLeft
    tree.root.right = oneRight

    oneLeft.left = twoLeft
    oneLeft.right = twoRight

    oneRight.left = threeLeft
    oneRight.right = threeRight

    tree.displayInOrder(tree.root)
    print("\n\n")
    tree.displayPreOrder(tree.root)
    print("\n\n")
    tree.displayPostOrder(tree.root)
