class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
    def set_right(self, tree: BinaryTree):
        self.right = tree
    
    def set_left(self, tree: BinaryTree):
        self.left = tree


def preorder(tree: BinaryTree):
    if tree:
        print(tree.value, end="")
        preorder(tree.left)
        preorder(tree.right)

def postorder(tree: BinaryTree):
    if tree:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.value, end="")

def inorder(tree: BinaryTree):
    if tree:
        inorder(tree.left)
        print(tree.value, end="")
        inorder(tree.right)

queue = []
def levelorder(tree: BinaryTree):
    queue.append(tree)
    while (len(queue) > 0):
        print(queue[0].value, end="")
        if queue[0].left != None:
            queue.append(queue[0].left)
        if queue[0].right != None:
            queue.append(queue[0].right)
        del queue[0]