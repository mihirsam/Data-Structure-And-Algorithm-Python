# Universal value tree problem
# problem : https://www.youtube.com/watch?v=7HgsS8bRvjo&list=PLCTG5hBk3snlhbV7nsUBP9gkaGkpCu26D&index=22&t=236s

class Node:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def UnivalTree(self, node, flag):
        if node:
            if node.left is None and node.right is None:
                flag += 1
                return flag
            elif node.left.value == node.right.value and node.left.value == node.value:
                flag += 1
            return flag + self.UnivalTree(node.left, 0) + self.UnivalTree(node.right, 0)
            


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = Node(0)
    bt.root.left = Node(1)
    bt.root.right = Node(0)
    bt.root.right.left = Node(1)
    bt.root.right.right = Node(0)
    bt.root.right.left.left = Node(1)
    bt.root.right.left.right = Node(1)

    print(bt.UnivalTree(bt.root, 0))
