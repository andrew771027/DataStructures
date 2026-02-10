class Queue:
    
    def __init__(self, size: int):
        self.size: int = size
        self.data: list = [0] * self.size
        self.front: int = -1
        self.back: int = -1
    
    def is_full(self) -> bool:
        return self.back == self.size -1

    def is_empty(self) -> bool:
        return self.front == self.back

    def en_queue(self, value):
        if self.is_full():
            print("佇列已滿")
        else:
            self.back += 1
            self.data[self.back] = value
    
    def de_queue(self):
        if self.is_empty():
            print("佇列是空的")
        else:
            self.front += 1
            return self.data[self.front]
    
    def display(self):
        for index in range(self.front + 1, self.back+1):
            print(self.data[index], end="")
        

