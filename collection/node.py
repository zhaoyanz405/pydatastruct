class Node:
    def __init__(self):
        self.item = None
        self.next = None


def iter_nodes(node):
    while True:
        yield node.item
        if not node.next:
            break

        node = node.next
