
def sort(input: list) -> list:
    # Base case：長度 0 或 1 已經排序好
    if len(input) <= 1:
        return input
    
    # 1️⃣ 分割（Divide）
    mid = len(input) // 2
    left = sort(input[mid:])
    right = sort(input[:mid])

    # 2️⃣ 合併（Conquer）
    return merge(left, right)

def merge(left: list, right: list) -> list:
    result = []
    i = j = 0

    # 比較左右陣列，依序放入結果
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 將剩餘元素補上
    result.extend(left[i:])
    result.extend(right[j:])

    return result
