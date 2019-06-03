# Construct tree from inorder and post order
# Code working, can't get it to print
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
            #temp = None
            print(exec("{}.{}" .format(node, 'value')))
            #print(f"{temp} -> ", end="")
            self.PreOrder(node.left)
            self.PreOrder(node.right)

    def ConsTree(self, lis, PostOrder, root, mode):
        maxIndex = 0

        for item in lis:
            if PostOrder.index(item) > maxIndex:
                maxIndex = PostOrder.index(item)
        
        exec("{}.{} = {}" .format(root, mode, PostOrder[maxIndex]))

        try:
            lefty = lis[0:lis.index(PostOrder[maxIndex])]
        except:
            lefty = []
        
        try:
            righty = lis[lis.index(PostOrder[maxIndex])+1:]
        except:
            righty = []

        if len(lefty) == 1:
            exec("{}.left = lefty[0]" .format(PostOrder[maxIndex]))
        elif len(lefty) > 1:
            self.ConsTree(lefty, PostOrder, PostOrder[maxIndex], 'left')
        else:
            pass

        if len(righty) == 1:
            exec("{}.left = righty[0]" .format(PostOrder[maxIndex]))
        elif len(righty) > 1:
            self.ConsTree(righty, PostOrder, PostOrder[maxIndex], 'right')
        else:
            pass



if __name__ == "__main__":
    bt = BinaryTree()
    
    PostOrder = input("\nEnter Post Order : ")
    InOrder = input("\nEnter In Order : ")

    PostOrder = PostOrder.split(' ')
    InOrder = InOrder.split(' ')

    PostOrder = ['D', 'E', 'B',  'F',  'C',  'A']
    InOrder = ['D', 'B', 'E', 'A', 'F', 'C']

    for item in PostOrder:
        exec("{0} = Node(item)" .format(item))
    
    root = PostOrder[-1]
    left = InOrder[0:InOrder.index(root)]
    
    try:
        right = InOrder[InOrder.index(root)+1:]
    except:
        right = []

    bt.ConsTree(left, PostOrder, root, 'left')
    bt.ConsTree(right, PostOrder, root, 'right')

    #exec("bt.PreOrder({})" .format(root))