class Node:
    def __init__(self, value):
        self.value = value
        self.left: Node = None
        self.right: Node = None
        self.height: int = 1

class AVLTree:
    
    def height(self, node: Node):
        return node.height if node else 0

    def balance_factor(self, node: Node):
        return self.height(node.left) - self.height(node.right)
    
    def get_min_value_node(self, node: Node):
        current_node: Node = node
        while current_node.left:
            current_node = current_node.left
        return current_node

    def right_rotate(self, y: Node):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        ## 先算下面，再算上面
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x
    
    def left_rotate(self, x: Node):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        ## 先算上面，再算上面
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    def insert(self, node: Node, value):
        ## 1. BST Insert
        if not node:
            return Node(value)
        
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        ## 2. Update Height
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        ## 3. check balance
        balance = self.balance_factor(node)

        ## 4. Left - Left
        if balance > 1 and value < node.left.value:
            return self.right_rotate(node)
        
        ## 5. Right - Right
        if balance < -1 and value > node.right.value:
            return self.left_rotate(node)
        
        ## 6. Left - Right
        if balance > 1 and value > node.left.value:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        
        ## 7. Right - Left
        if balance < -1 and value < node.right.value:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node
    
    def delete(self, root: Node, value):

        ## 1. 標準 BST delete
        if not root:
            return root
        
        if value < root.left.value:
            root.left = self.delete(root.left, value)
        elif value > root.right.value:
            root.right = self.delete(root.right, value)
        else:
            ## Case 1 & Case 2: 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        
            ## Case 3: two child
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        
        ## 2. Update height
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        ## 3. Calculance balance factor
        balance = self.balance_factor(root)

        ## Left - Left
        if balance > 1 and self.balance_factor(root.left) >= 0:
            return self.right_rotate(root.left)

        ## Right - Right
        if balance < -1 and self.balance_factor(root.right) <= 0:
            return self.left_rotate(root.right)
        
        ## Left - Right
        if balance > 1 and self.balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        
        ## Right - Left
        if balance < -1 and self.balance_factor(root.right) < 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
        
    def search(self, root: Node, value) -> bool:
        if root is None:
            return False
        
        if value == root.value:
            return True
        elif value < root.value:
            return self.search(root.left, value)
        else:
            return self.search(root.right, value)

def inorder(tree: Node):
    if tree:
        inorder(tree.left)
        print(tree.value, end=" ")
        inorder(tree.right)