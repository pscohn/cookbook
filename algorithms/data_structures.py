



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
            self.stack = self.stack[:-1]
            return removed

    @property
    def size(self):
        return len(self.stack)

    @property
    def is_empty(self):
        return True if len(self.stack) == 0 else False

class StackLinked:
    def __init__(self):
        self.node = None

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            removed = self.stack[-1]
            self.stack = self.stack[:-1]
            return removed

    @property
    def size(self):
        return len(self.stack)

    @property
    def is_empty(self):
        return True if len(self.stack) == 0 else False

class Link:
    def __init__(self, data, nextlink=None):
        self.data = data
        self.nextlink = nextlink
