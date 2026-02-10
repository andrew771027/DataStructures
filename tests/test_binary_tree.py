from src.binary_tree import BinaryTree, preorder, postorder, inorder, levelorder

def test_binary_tree():

    btree_1 = BinaryTree("A")
    btree_2 = BinaryTree("B")
    btree_3 = BinaryTree("C")
    btree_4 = BinaryTree("D")
    btree_5 = BinaryTree("E")
    btree_6 = BinaryTree("F")
    btree_7 = BinaryTree("G")

    btree_1.set_left(btree_2)
    btree_1.set_right(btree_3)
    
    btree_2.set_left(btree_4)
    btree_2.set_right(btree_5)

    btree_3.set_left(btree_6)
    btree_3.set_right(btree_7)

def test_binary_tree_preorder(capfd):

    btree_1 = BinaryTree("A")
    btree_2 = BinaryTree("B")
    btree_3 = BinaryTree("C")
    btree_4 = BinaryTree("D")
    btree_5 = BinaryTree("E")
    btree_6 = BinaryTree("F")
    btree_7 = BinaryTree("G")

    btree_1.set_left(btree_2)
    btree_1.set_right(btree_3)
    
    btree_2.set_left(btree_4)
    btree_2.set_right(btree_5)

    btree_3.set_left(btree_6)
    btree_3.set_right(btree_7)

    root = btree_1

    preorder(root)
    out, err = capfd.readouterr()
    assert out == "ABDECFG"

def test_binary_tree_postorder(capfd):

    btree_1 = BinaryTree("A")
    btree_2 = BinaryTree("B")
    btree_3 = BinaryTree("C")
    btree_4 = BinaryTree("D")
    btree_5 = BinaryTree("E")
    btree_6 = BinaryTree("F")
    btree_7 = BinaryTree("G")

    btree_1.set_left(btree_2)
    btree_1.set_right(btree_3)
    
    btree_2.set_left(btree_4)
    btree_2.set_right(btree_5)

    btree_3.set_left(btree_6)
    btree_3.set_right(btree_7)

    root = btree_1

    postorder(root)
    out, err = capfd.readouterr()
    assert out == "DEBFGCA"
    
def test_binary_tree_inorder(capfd):

    btree_1 = BinaryTree("A")
    btree_2 = BinaryTree("B")
    btree_3 = BinaryTree("C")
    btree_4 = BinaryTree("D")
    btree_5 = BinaryTree("E")
    btree_6 = BinaryTree("F")
    btree_7 = BinaryTree("G")

    btree_1.set_left(btree_2)
    btree_1.set_right(btree_3)
    
    btree_2.set_left(btree_4)
    btree_2.set_right(btree_5)

    btree_3.set_left(btree_6)
    btree_3.set_right(btree_7)

    root = btree_1

    inorder(root)
    out, err = capfd.readouterr()
    assert out == "DBEAFCG" 

def test_binary_tree_levelorder(capfd):

    btree_1 = BinaryTree("A")
    btree_2 = BinaryTree("B")
    btree_3 = BinaryTree("C")
    btree_4 = BinaryTree("D")
    btree_5 = BinaryTree("E")
    btree_6 = BinaryTree("F")
    btree_7 = BinaryTree("G")

    btree_1.set_left(btree_2)
    btree_1.set_right(btree_3)
    
    btree_2.set_left(btree_4)
    btree_2.set_right(btree_5)

    btree_3.set_left(btree_6)
    btree_3.set_right(btree_7)

    root = btree_1

    levelorder(root)
    out, err = capfd.readouterr()
    assert out == "ABCDEFG"