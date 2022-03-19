from collection.node import Node, iter_nodes


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

    def __iter__(self):
        return iter_nodes(self.first)
