class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class CircleLinkedList:
    def __init__(self):
        self.head: Node = None
    
    def insert_head(self, value):
        self.head = Node(value)
        self.head.next = self.head
    
    def insert(self, target_value, value):
        current_node: Node = self.head
        new_node: Node = Node(value)

        while True:
            if current_node.data == target_value:
                break
            current_node = current_node.next

        new_node.next = current_node.next
        current_node.next = new_node
    
    def remove(self, target_value):

        # previous_node：永遠指向 current_node 的前一個節點
        # current_node：從 head.next 開始找
        # 因為如果要刪 head，你需要知道「最後一個節點」，而在環狀串列中，最後一個節點的 next 會指向 head
        previous_node: Node = self.head         
        current_node: Node = self.head.next
        
        while True:
            if current_node.data == target_value:
                break

            # current_node = 要被刪的節點
            # previous_node = 它前面的節點
            previous_node = current_node
            current_node = current_node.next

        # Case 1：只有一個節點，且刪的就是它
        if current_node == self.head and self.head.next == self.head:
            self.head = None
        # Case 2：刪的是 head，但串列有多個節點
        elif current_node == self.head:
            self.head = self.head.next
            previous_node.next = self.head
        # Case 3：刪的是中間或尾端節點（不是 head）
        else:
            previous_node.next = current_node.next 

    def len(self):
        length: int = 0
        
        if self.head == None:
            return length
        else:
            current_node:Node = self.head.next
            
            while current_node != self.head:
                current_node = current_node.next
                length += 1
            
            return length + 1 

    def display(self):
        
        current_node: Node = self.head

        for _ in range(self.len()):
            print(current_node.data, end = "")
            current_node = current_node.next