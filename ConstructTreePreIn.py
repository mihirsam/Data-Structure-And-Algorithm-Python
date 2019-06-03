# Construct Binary tree from pre-order and in-order

class Node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None

    
class BinaryTree:
    def __init__(self):
        self.root = None

    def PostOrder(self, node):
        if node:
            self.PostOrder(node.left)
            self.PostOrder(node.right)
            print(f"{node.value} -> ", end="")

    def ConsTree(self, lis, preorder, root, mode):
        minIndex = preorder.index(lis[0])

        for item in lis:
            if preorder.index(item) < minIndex:
                minIndex = preorder.index(item)
        
        if mode is 'left':
            root.left = Node(preorder[minIndex])
        else:
            root.right = Node(preorder[minIndex])

        try:
            lefty = lis[0:lis.index(preorder[minIndex])]
        except:
            lefty = []

        try:
            righty = lis[lis.index(preorder[minIndex])+1 : ]
        except:
            righty = []

        if len(lefty) == 1:
            if mode is 'left':
                root.left.left = Node(lefty[0])
            else:
                root.right.left = Node(lefty[0])
        elif len(lefty) > 1:
            if mode is 'left':
                self.ConsTree(lefty, preorder, root.left, 'left')
            else:
                self.ConsTree(lefty, preorder, root.right, 'left')

        if len(righty) == 1:
            if mode is 'left':
                root.left.right = Node(righty[0])
            else:
                root.right.right = Node(righty[0])
        elif len(righty) > 1:
            if mode is 'left':
                self.ConsTree(righty, preorder, root.left, 'right')
            else:
                self.ConsTree(lefty, preorder, root.right, 'right')

if __name__ == "__main__":
    PreOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    InOrder = ['D', 'B', 'E', 'A', 'F', 'C']

    bt = BinaryTree()
    bt.root = Node(PreOrder[0])

    try:
        lefty = InOrder[0:InOrder.index(bt.root.value)]
    except:
        lefty = []

    try:
        righty = InOrder[InOrder.index(bt.root.value)+1:]
    except:
        righty = []

    bt.ConsTree(lefty, PreOrder, bt.root, 'left')
    bt.ConsTree(righty, PreOrder, bt.root, 'right')
    bt.PostOrder(bt.root)