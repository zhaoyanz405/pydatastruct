from collection.node import Node


def test_node_next():
    n = Node()
    n.item = 0

    n2 = Node()
    n2.item = 1
    n.next = n2

    n3 = next(n)
    assert n3.item == n2.item
