from src.linkedlist import LinkedList

def test_linkedlist_display(capfd):

    linkedlist = LinkedList()

    linkedlist.insert_head(value=3)
    
    linkedlist.insert(3, 2)
    linkedlist.insert(2, 1)
    linkedlist.insert(1, 0)

    linkedlist.display()

    out, err = capfd.readouterr()
    assert out == "3210"

def test_linkedlist_remove_first_node(capfd):

    linkedlist = LinkedList()

    linkedlist.insert_head(value=3)
    
    linkedlist.insert(3, 2)
    linkedlist.insert(2, 1)
    linkedlist.insert(1, 0)

    linkedlist.remove(3)

    linkedlist.display()

    out, err = capfd.readouterr()
    assert out == "210"

def test_linkedlist_remove_intermediate_node(capfd):

    linkedlist = LinkedList()

    linkedlist.insert_head(value=3)
    
    linkedlist.insert(3, 2)
    linkedlist.insert(2, 1)
    linkedlist.insert(1, 0)

    linkedlist.remove(2)

    linkedlist.display()

    out, err = capfd.readouterr()
    assert out == "310"

def test_linkedlist_remove_end_node(capfd):

    linkedlist = LinkedList()

    linkedlist.insert_head(value=3)
    
    linkedlist.insert(3, 2)
    linkedlist.insert(2, 1)
    linkedlist.insert(1, 0)

    linkedlist.remove(0)

    linkedlist.display()

    out, err = capfd.readouterr()
    assert out == "321"
