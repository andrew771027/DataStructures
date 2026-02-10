from src.circle_queue import CircleQueue

def test_queue_display(capfd):

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)

    queue.display()
    out, err = capfd.readouterr()
    assert out == "123"   


def test_queue_is_empty():

    queue = CircleQueue(4)
    assert queue.is_empty() == True

def test_queue_is_full():

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)

    assert queue.is_full() == True
    
def test_queue_en_queue(capfd):

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    
    queue.display()
    out, err = capfd.readouterr()
    assert out == "123"   

def test_queue_de_queue(capfd):

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    
    queue.display()
    out, err = capfd.readouterr()
    assert out == "123"

    queue.de_queue()
    queue.de_queue()
    queue.display()
    out, err = capfd.readouterr()
    assert out == "3"   

def test_queue_overlength(capfd):

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)
    
    out, err = capfd.readouterr()
    assert "環狀佇列已滿" in out
    
def test_queue_has_cleared(capfd):

    queue = CircleQueue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()

    out, err = capfd.readouterr()
    assert "環狀佇列是空的" in out
    