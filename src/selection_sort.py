
def sort(input: list) -> list:

    for i in range(len(input) -1):
        min_index = i

        # 從未排序區找最小值
        for j in range(i + 1 , len(input)):
            if input[j] < input[min_index]:
                min_index = j

        # 把最小值換到正確位置
        input[i], input[min_index] = input[min_index], input[i]
    
    return input