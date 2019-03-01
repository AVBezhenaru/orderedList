class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 == v2:
            return 0

        elif v1 < v2:
            return -1

        elif v1 > v2:
            return +1

    def add(self, value):
        node = self.head
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            self.tail = newNode
            newNode.next = None
            newNode.prev = None
            return

        while node:

            if self.__ascending is True:

                if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0:
                    self.head = newNode
                    self.head.next = node
                    node.prev = self.head
                    return

                if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                    if node.next == None:
                        self.tail.next = newNode
                        newNode.prev = self.tail
                        self.tail = newNode
                        return

                    node = node.next

                if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0:
                    node.prev.next = newNode
                    newNode.next = node
                    newNode.prev = node.prev
                    node.prev = newNode
                    return

            if self.__ascending is False:

                if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                    self.head = newNode
                    self.head.next = node
                    node.prev = self.head
                    return

                if self.compare(node.value, value) == 1 or self.compare(node.value, value) == 0:
                    if node.next == None:
                        self.tail.next = newNode
                        newNode.prev = self.tail
                        self.tail = newNode
                        return

                    node = node.next

                if self.compare(node.value, value) == -1 or self.compare(node.value, value) == 0:
                    node.prev.next = newNode
                    newNode.next = node
                    newNode.prev = node.prev
                    node.prev = newNode
                    return

    def find(self, val):
        node = self.head

        while node:
            if node.value == val:
                return node

            elif self.__ascending is True and node.value > val:
                return None

            elif self.__ascending is False and node.value < val:
                return None

            node = node.next

        return None

    def delete(self, val):
        if self.head == None:
            return None

        node = self.head

        if self.head.value == val:
            if self.head.next == None:
                self.head = None
                self.tail = None
                return

            node.next.prev = None
            self.head = node.next
            return

        while node:
            if node.value == val:
                if node.next == None:
                    self.tail = node.prev
                    self.tail.next = None
                    return

                node.prev.next = node.next
                node.next.prev = node.prev
                return

            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        count = 0

        while node:
            count += 1
            node = node.next

        return count

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):

    def compare(self, v1, v2):
        v1 = v1.strip()
        v2 = v2.strip()

        if v1 == v2:
            return 0

        elif v1 < v2:
            return -1

        elif v1 > v2:
            return +1


