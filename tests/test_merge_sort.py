from src.merge_sort import sort

def test_sort():

    input = [5, 3, 1, 9, 10]

    output = sort(input)

    assert output == [1, 3, 5, 9, 10] 