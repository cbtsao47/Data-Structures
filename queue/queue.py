class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self, value):
        if not self.head:
            return None
        current_tail = self.tail
        while current_tail:
            current_tail = current_tail.next


class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = []

    def enqueue(self, item):
        self.storage.append(item)
        self.size = len(self.storage)

    def dequeue(self):
        if len(self.storage) > 0:
            item = self.storage.pop(0)
            self.size = len(self.storage)
            return item

    def len(self):
        return self.size
