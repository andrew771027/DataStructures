class Node:
    def __init__(self, value):
        self.value = value
        self.right: Node = None
        self.left: Node = None

class BinarySearchTree:
    def __init__(self, value):
        self.root: Node = Node(value)
    
    def insert(self, current_node: Node, value) -> Node:
        if current_node is None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.insert(current_node.left, value)
        else:
            current_node.right = self.insert(current_node.right, value)

        return current_node
    
    def search(self, current_node: Node, value) -> bool:
        if current_node is None:
            return False
        
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self.search(current_node.left, value)
        else:
            return self.search(current_node.right, value)
    
    def delete(self, current_node: Node, value) -> Node:
        if current_node is None:
            return None
        
        if current_node.value > value:
            current_node.left = self.delete(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.delete(current_node.right, value)
        else:
            # Case 1 & 2 最多只有一個子節點
            # 沒有左子樹，用右子樹取代
            # 沒有右子樹，用左子樹取代
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Case 3: two children 有左右兩個子節點
            # 找：
            # 1. 右子樹中最小的節點（in-order successor）
            # 或
            # 2. 左子樹中最大的節點（in-order predecessor）
            
            temp = current_node.right
            while temp.left is not None:
                temp = temp.left

            # 用該值取代目前節點
            # 再把那個「被拿來用的節點」刪掉
            current_node.value = temp.value
            current_node.right = self.delete(current_node.right, temp.value)

        return current_node

    def search_and_delete(self, value):
        if self.search(self.root, value):
            self.root = self.delete(self.root, value)


def inorder(tree: Node):
    if tree:
        inorder(tree.left)
        print(tree.value, end=" ")
        inorder(tree.right)