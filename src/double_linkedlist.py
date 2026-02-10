class Node:
    def __init__(self, value):
        self.data = value
        self.previous = None
        self.next = None

class DoubleLinkedList:

    def __init__(self):
        self.head: Node = None
    
    def insert_head(self, value):
        self.head = Node(value)
        self.head.next = self.head
        self.head.previous = self.head

    def insert(self, target_value, value):

        current_node: Node = self.head
        new_node: Node = Node(value)

        while True:
            if current_node.data == target_value:
                break
            current_node = current_node.next
        
        new_node.next = current_node.next
        new_node.previous = current_node
        
        current_node.next.previous = new_node
        current_node.next = new_node

    def remove(self, target_value):
        current_node: Node = self.head

        while True:
            if current_node.data == target_value:
                break
            current_node = current_node.next
        
        if current_node == self.head and self.head.next == self.head:
            self.head = None

        elif current_node == self.head:
            self.head = current_node.next
        
        if self.head != None:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
    
    def len(self):
        length: int = 0

        if self.head == None:
            return 0
        
        else:
            current_node: Node = self.head.next
            
            while current_node != self.head:
                length += 1
                current_node = current_node.next
            
            return length + 1
    
    def display(self):

        current_node: Node = self.head

        for _ in range(self.len()):
            print(current_node.data, end="")
            current_node = current_node.next