# Construct binary tree from post order and preorder traversal

class Node:
    def __init__(self, val = None):
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

    def ConsTree(self, PreOrder, PostOrder, root):
        
        n1 = PreOrder[PreOrder.index(root.value)+1]
        n2 = PostOrder[PostOrder.index(root.value)-1]

        if n1 == n2:
            root.left = Node(n1)
        else:
            root.left = Node(n1)
            root.right = Node(n2)

        mini_pre1 = PreOrder[PreOrder.index(n2):]
        mini_post1 = PostOrder[PostOrder.index(n1):PostOrder.index(n2)+1]

        if len(mini_pre1) > 1 and len(mini_post1) > 1:
            self.ConsTree(mini_pre1, mini_post1, root.right)
        
        mini_pre2 = PreOrder[PreOrder.index(n1):PreOrder.index(n2)]
        mini_post2 = PostOrder[:PostOrder.index(n1)+1]

        if len(mini_pre2) > 1 and len(mini_post2) > 1:
            self.ConsTree(mini_pre2, mini_post2, root.left)


if __name__ == "__main__":
    PreOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    InOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    PostOrder = ['D', 'E', 'B',  'F',  'C',  'A']

    bt = BinaryTree()
    bt.root = Node(PreOrder[0])

    bt.ConsTree(PreOrder, PostOrder, bt.root)
    bt.InOrder(bt.root)
