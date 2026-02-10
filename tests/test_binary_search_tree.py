from src.binary_search_tree import BinarySearchTree, inorder

def test_binary_search_tree(capfd):

    bst = BinarySearchTree(10)
    bst.insert(bst.root, 5)
    bst.insert(bst.root, 3)
    bst.insert(bst.root, 7)
    bst.insert(bst.root, 12)
    bst.insert(bst.root, 11)
    bst.insert(bst.root, 13)

    inorder(bst.root)

    out, err = capfd.readouterr()
    assert out == "3 5 7 10 11 12 13 "

def test_binary_search_tree_delete(capfd):

    bst = BinarySearchTree(10)
    bst.insert(bst.root, 5)
    bst.insert(bst.root, 3)
    bst.insert(bst.root, 7)
    bst.insert(bst.root, 12)
    bst.insert(bst.root, 11)
    bst.insert(bst.root, 13)

    inorder(bst.root)

    out, err = capfd.readouterr()
    assert out == "3 5 7 10 11 12 13 "

    bst.search_and_delete(5)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "3 7 10 11 12 13 "

    bst.search_and_delete(10)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "3 7 11 12 13 "
    
    bst.search_and_delete(11)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "3 7 12 13 "

    bst.search_and_delete(13)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "3 7 12 "

    bst.search_and_delete(7)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "3 12 "

    bst.search_and_delete(3)
    inorder(bst.root)
    out, err = capfd.readouterr()
    assert out == "12 "
