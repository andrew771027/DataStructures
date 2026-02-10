
def sort(input: list) -> list:
    n = len(input)

    # 1️⃣ 建立 Max Heap
    for i in range(n // 2 - 1 , -1, -1 ):
        heapify(input, n ,i)

    # 2️⃣ 一個一個取出最大值
    for i in range(n - 1, 0, -1):
        # 把最大值（arr[0]）移到最後
        input[0], input[i] = input[i], input[0]
        # 對剩下的元素重新 heapify
        heapify(input, i ,0)
    
    return input

def heapify(input: list, heap_size: int, root_index: int):
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    # 左子節點
    if left < heap_size and input[left] > input[largest]:
        largest = left
    
    # 右子節點
    if right < heap_size and input[right] > input[largest]:
        largest = right
    
     # 如果最大值不是 root，交換並繼續調整
    if largest != root_index:
        input[root_index], input[largest] = input[largest], input[root_index]
        heapify(input, heap_size, largest)