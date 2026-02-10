from src.circle_linkedlist import CircleLinkedList


def test_circle_linkedlist_display(capfd):

    circle_linkedlist = CircleLinkedList()

    circle_linkedlist.insert_head(value = 3)

    circle_linkedlist.insert(3, 2)
    circle_linkedlist.insert(2, 1)
    circle_linkedlist.insert(1, 0)

    assert circle_linkedlist.len() == 4

    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3210"

def test_circle_linkedlist_remove_head(capfd):

    circle_linkedlist = CircleLinkedList()

    circle_linkedlist.insert_head(value = 3)

    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3"

    circle_linkedlist.remove(3)
    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == ""

def test_circle_linkedlist_remove_only_head(capfd):
    
    circle_linkedlist = CircleLinkedList()

    circle_linkedlist.insert_head(value = 3)

    circle_linkedlist.insert(3, 2)
    circle_linkedlist.insert(2, 1)
    circle_linkedlist.insert(1, 0)

    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "3210"

    circle_linkedlist.remove(3)
    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "210"

def test_circle_linkedlist_revmoe_intermediate_node(capfd):

    circle_linkedlist = CircleLinkedList()

    circle_linkedlist.insert_head(value = 3)

    circle_linkedlist.insert(3, 2)
    circle_linkedlist.insert(2, 1)
    circle_linkedlist.insert(1, 0)

    circle_linkedlist.remove(2)
    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "310"

def test_circle_linkedlist_revmoe_end_node(capfd):

    circle_linkedlist = CircleLinkedList()

    circle_linkedlist.insert_head(value = 3)

    circle_linkedlist.insert(3, 2)
    circle_linkedlist.insert(2, 1)
    circle_linkedlist.insert(1, 0)

    circle_linkedlist.remove(0)
    circle_linkedlist.display()
    out, err = capfd.readouterr()
    assert out == "321"