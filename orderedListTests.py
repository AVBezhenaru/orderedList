def reverse(self):
    buf = None
    node = self.head

    while node is not None:
        buf = node.prev
        node.prev = node.next
        node.next = buf
        node = node.prev

    if buf is not None:
        self.tail = self.head
        self.head = buf.prev