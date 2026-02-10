from src.stack import Stack

def test_stack_display(capfd):

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.display()
    out, err = capfd.readouterr()
    assert out == "1234"

def test_stack_push(capfd):

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.display()
    out, err = capfd.readouterr()
    assert out == "1234"

def test_stack_pop(capfd):

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.pop()
    stack.pop()

    stack.display()
    out, err = capfd.readouterr()
    assert out == "12"

def test_stack_is_full():

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    assert stack.is_full() == True

def test_stack_is_empty():

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    assert stack.is_empty() == True

def test_stack_overlength(capfd):

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    out, err = capfd.readouterr()
    assert "堆疊已滿" in out

def test_stack_has_cleared(capfd):

    stack = Stack(4)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()

    out, err = capfd.readouterr()
    assert "堆疊是空的" in out