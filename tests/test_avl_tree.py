from src.avl_tree import AVLTree, inorder

def test_avl_tree():
    avl = AVLTree()
    root = None

    for v in [10, 20, 30, 40, 50, 25]:
        root = avl.insert(root, v)
    
    inorder(root)