from src.queue import Queue

def test_queue_display(capfd):

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)

    queue.display()
    out, err = capfd.readouterr()
    assert out == "1234"   

def test_queue_is_empty():

    queue = Queue(4)
    assert queue.is_empty() == True

def test_queue_is_full():

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)

    assert queue.is_full() == True
    
def test_queue_en_queue(capfd):

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)

    queue.display()
    out, err = capfd.readouterr()
    assert out == "1234"   

def test_queue_de_queue(capfd):

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)

    queue.display()
    out, err = capfd.readouterr()
    assert out == "1234"

    queue.de_queue()
    queue.de_queue()
    queue.display()
    out, err = capfd.readouterr()
    assert out == "34"   

def test_queue_overlength(capfd):

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)
    queue.en_queue(5)

    out, err = capfd.readouterr()
    assert "佇列已滿" in out
    
def test_queue_has_cleared(capfd):

    queue = Queue(4)
    queue.en_queue(1)
    queue.en_queue(2)
    queue.en_queue(3)
    queue.en_queue(4)
    
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()
    queue.de_queue()

    out, err = capfd.readouterr()
    assert "佇列是空的" in out
    