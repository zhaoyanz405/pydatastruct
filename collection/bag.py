from collection.node import Node


class Bag:
    def __init__(self):
        self.first = None
        self.size = 0

    def is_empty(self):
        return self.first is None

    def add(self, item):
        new_node = Node()
        new_node.item = item

        if not self.is_empty():
            new_node.next = self.first

        self.first = new_node
        self.size += 1

    def remove(self):
        if self.is_empty():
            raise ValueError("Can not remove value from an empty Bag.")

        item = self.first.item
        self.first = self.first.next
        return item
