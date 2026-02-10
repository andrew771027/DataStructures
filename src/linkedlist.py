class Node:

    def __init__(self, value):
        self.data = value
        self.next: Node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_head(self, value):
        self.head = Node(value)
        self.head.next = None
    
    def insert(self, target_value, value):
        current_node: Node = self.head
        new_node = Node(value)
        
        while current_node != None:
            if current_node.data != target_value:
                current_node = current_node.next
            else:
                break

        new_node.next = current_node.next
        current_node.next = new_node
    
    def remove(self, target_value):
        current_node: Node = self.head
        
        while current_node != None:
            if current_node.data == target_value:
                break
            previous_node: Node = current_node
            current_node = current_node.next

        if current_node == self.head:
            self.head = self.head.next
        else:
            previous_node.next = current_node.next

    def display(self):
        current_node: Node = self.head

        while current_node != None:
            print(current_node.data, end = "")
            current_node = current_node.next