def sort(input: list) -> list:
    # Base case
    if len(input) <= 1:
        return input
    
    # 1️⃣ 選 pivot（這裡選最後一個）
    pivot = input[-1]

    # 2️⃣ Partition
    left = []
    right = []

    for x in input[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    # 3️⃣ 遞迴排序 + 合併
    return sort(left) + [pivot] + sort(right)