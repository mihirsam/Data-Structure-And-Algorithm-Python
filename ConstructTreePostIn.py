# Construct tree from inorder and post order
# another approach

class Node:
    def __init__(self, val = None):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def PreOrder(self, node):
        if node:
            print(f"{node.value} -> ", end="")
            self.PreOrder(node.left)
            self.PreOrder(node.right)

    def ConsTree(self, lis, PostOrder, root, mode):
        maxIndex = 0

        for item in lis:
            if PostOrder.index(item) > maxIndex:
                maxIndex = PostOrder.index(item)

        if mode is 'left':
            root.left = Node(PostOrder[maxIndex])
        else:
            root.right = Node(PostOrder[maxIndex])

        try:
            lefty = lis[0:lis.index(PostOrder[maxIndex])]
        except:
            lefty = []
        
        try:
            righty = lis[lis.index(PostOrder[maxIndex])+1:]
        except:
            righty = []

        if len(lefty) == 1:
            if mode is 'left':
                root.left.left = Node(lefty[0])
            else:
                root.right.left = Node(lefty[0])
        elif len(lefty) > 1:
            if mode is 'left':
                self.ConsTree(lefty, PostOrder, root.left, 'left')
            else:
                self.ConsTree(lefty, PostOrder, root.right, 'left')
        else:
            pass

        if len(righty) == 1:
            if mode is 'right':
                root.right.right = Node(righty[0])
            else:
                root.left.right = Node(righty[0])
        elif len(righty) > 1:
            if mode is 'left':
                self.ConsTree(righty, PostOrder, root.left, 'right')
            else:
                self.ConsTree(righty, PostOrder, root.right, 'right')
        else:
            pass



if __name__ == "__main__":
    bt = BinaryTree()
    
    #PostOrder = input("\nEnter Post Order : ")
    #InOrder = input("\nEnter In Order : ")

    #PostOrder = PostOrder.split(' ')
    #InOrder = InOrder.split(' ')

    PostOrder = ['D', 'E', 'B',  'F',  'C',  'A']
    InOrder = ['D', 'B', 'E', 'A', 'F', 'C']

    for item in PostOrder:
        exec("{0} = Node(item)" .format(item))
    
    bt.root = Node(PostOrder[-1])

    try:
        left = InOrder[0:InOrder.index(bt.root.value)]
    except:
        left = []
    try:
        right = InOrder[InOrder.index(bt.root.value)+1:]
    except:
        right = []

    bt.ConsTree(left, PostOrder, bt.root, 'left')
    bt.ConsTree(right, PostOrder, bt.root, 'right')
    bt.PreOrder(bt.root)