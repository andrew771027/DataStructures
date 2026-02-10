def sort(input: list) -> list:
    for i in range(1, len(input)):
        key = input[i]      # 目前要插入的元素
        j = i - 1
        
        # 將比 key 大的元素往右移
        while j >= 0 and input[j] > key:
            input[j + 1] = input[j]
            j -= 1
        
        # 把 key 放到正確位置
        input[j+1] = key
    
    return input