
def sort(input: list) -> list:

    for i in range(len(input)):
        for j in range(0, len(input) -1 ):
            if input[j] > input[j + 1]:
                input[j], input[j + 1] = input[j + 1], input[j]
    
    return input
