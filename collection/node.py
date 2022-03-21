class Node:
    def __init__(self):
        self.item = None
        self.next = None

    def __next__(self):
        if self.next is None:
            raise StopIteration

        self = self.next
        return self
