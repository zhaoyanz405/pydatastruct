class Node:
    def __init__(self):
        self.item = None
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.size = 0

    def push(self, item):
        new_node = Node()
        new_node.item = item

        old_node = self.first
        new_node.next = old_node
        self.first = new_node

        self.size += 1

    def pop(self):
        item = self.first.item
        self.first = self.first.next
        self.size -= 1

        return item
