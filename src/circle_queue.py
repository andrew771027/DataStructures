class CircleQueue:
    def __init__(self, size:int):
        self.size: int = size
        self.data: list = [0] * self.size
        self.front = 0
        self.back = 0
    
    def is_full(self):
        # 浪費一個空間
        # 環狀佇列浪費一個空間，是為了在只使用 front 與 back 指標的情況下，能夠明確區分「佇列為空」與「佇列已滿」兩種狀態。
        # 若不要浪費空間，需要有另一個變數來判斷
        return self.front == ((self.back + 1) % self.size)

    def is_empty(self):
        return self.front == self.back

    def en_queue(self, value):
        if self.is_full():
            print("環狀佇列已滿")
        else:
            self.data[self.back] = value
            self.back = (self.back + 1) % self.size
    
    def de_queue(self):
        if self.is_empty():
            print("環狀佇列是空的")
        else:
            item = self.data[self.front]
            self.front = (self.front + 1) % self.size
            return item
    
    def display(self):
        if not self.is_empty():
            if self.back > self.front:
                for index in range(self.front, self.back):
                    print(self.data[index], end="")
            else:
                for index in range (self.front, self.size):
                    print(self.data[index], end="")
                for index in range (0, self.back):
                    print(self.data[index], end="")