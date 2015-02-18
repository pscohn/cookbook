
class Stack:
    def __init__(self, stack=[]):
        self.stack = stack
        self.cur = 0

    def __repr__(self):
        return '[' + ', '.join(map(str, self.stack)) + ']'

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur == len(self.stack):
            self.cur = 0
            raise StopIteration()
        item = self.stack[self.cur]
        self.cur += 1
        return item

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            removed = self.stack[-1]
            self.stack = del(self.stack[-1])
            return removed

    @property
    def size(self):
        return len(self.stack)

    @property
    def is_empty(self):
        return len(self.stack) == 0

class StackLinked:
    def __init__(self):
        self.first = None

    def push(self, data):
        self.first = Node(data, next_node=self.first)

    def pop(self):
        if self.first is None:
            return
        old_first = self.first
        self.first = self.first.next_node
        return old_first.data

    @property
    def size(self):
        if self.first is None:
            return 0

        length = 1
        cur = self.first
        while cur.next_node is not None:
            length += 1
            cur = cur.next_node
        return length

    @property
    def is_empty(self):
        return self.first is None

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
