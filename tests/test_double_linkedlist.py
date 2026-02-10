from src.double_linkedlist import DoubleLinkedList


def test_double_linkedlist_display(capfd):

    double_linkedlist = DoubleLinkedList()

    double_linkedlist.insert_head(value = 3)

    double_linkedlist.insert(3, 2)
    double_linkedlist.insert(2, 1)
    double_linkedlist.insert(1, 0)

    assert double_linkedlist.len() == 4

    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3210"

def test_double_linkedlist_remove_head(capfd):

    double_linkedlist = DoubleLinkedList()

    double_linkedlist.insert_head(value = 3)

    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3"

    double_linkedlist.remove(3)
    out, err = capfd.readouterr()
    assert out == ""

def test_double_linkedlist_remove_only_head(capfd):

    double_linkedlist = DoubleLinkedList()

    double_linkedlist.insert_head(value = 3)

    double_linkedlist.insert(3, 2)
    double_linkedlist.insert(2, 1)
    double_linkedlist.insert(1, 0)

    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3210"

    double_linkedlist.remove(3)
    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "210"

def test_double_linkedlist_remove_intermediate_node(capfd):

    double_linkedlist = DoubleLinkedList()

    double_linkedlist.insert_head(value = 3)
    
    double_linkedlist.insert(3, 2)
    double_linkedlist.insert(2, 1)
    double_linkedlist.insert(1, 0)
    
    double_linkedlist.remove(2)
    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "310"

def test_double_linkedlist_remove_end_node(capfd):

    double_linkedlist = DoubleLinkedList()

    double_linkedlist.insert_head(value = 3)

    double_linkedlist.insert(3, 2)
    double_linkedlist.insert(2, 1)
    double_linkedlist.insert(1, 0)

    double_linkedlist.remove(0)
    double_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "321"