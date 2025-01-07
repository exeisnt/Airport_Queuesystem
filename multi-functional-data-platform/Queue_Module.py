# --- Stack/Queue Module ---
class TwoStacksOneArray:
    """Implements two stacks in one array."""
    def __init__(self, size):
        self.array = [None] * size
        self.top1 = -1
        self.top2 = size

    def push1(self, value):
        if self.top1 + 1 == self.top2:
            raise OverflowError("Stack 1 Overflow")
        self.top1 += 1
        self.array[self.top1] = value

    def push2(self, value):
        if self.top1 + 1 == self.top2:
            raise OverflowError("Stack 2 Overflow")
        self.top2 -= 1
        self.array[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            raise IndexError("Stack 1 Underflow")
        value = self.array[self.top1]
        self.top1 -= 1
        return value

    def pop2(self):
        if self.top2 == len(self.array):
            raise IndexError("Stack 2 Underflow")
        value = self.array[self.top2]
        self.top2 += 1
        return value

class QueueLinkedList:
    """Implements queue using a linked list."""
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, value):
        new_node = self.Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue Underflow")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return value
