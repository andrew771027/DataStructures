class Stack:
    def __init__(self, size: int):
        self.size: int = size
        self.data:list = [0] * self.size
        self.top = -1

    def is_full(self) -> bool:
        return self.top == self.size - 1
    
    def is_empty(self) -> bool:
        return self.top == -1

    def push(self, value) -> None:
        if self.is_full():
            print("堆疊已滿")
        else:
            self.top += 1
            self.data[self.top] = value
    
    def pop(self):
        if self.is_empty():
            print("堆疊是空的")
        else:
            item = self.data[self.top]
            self.top -= 1
            return item
    
    def display(self):
        if not self.is_empty():
            for index in range(0, self.top + 1):
                print(self.data[index], end="")

            