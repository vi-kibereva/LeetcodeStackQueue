class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, data=None):
        if not data:
            self.head = None
        elif isinstance(data, (int, float, bool)):
            self.head = Node(data)
        else:
            self.head = None
            for obj in data:
                if self.head:
                    cur.next = Node(obj)
                    cur = cur.next
                else:
                    self.head = Node(obj)
                    cur = self.head

    def __str__(self):
        if not self.head:
            return ''
        result = ''
        cur = self.head
        while cur:
            result += str(cur.data)
            cur= cur.next
        return result

    def next(self):
        if self.head is None:
            raise StopIteration
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next

    def __iter__(self):
        return self.next()

    def push(self, item):
        if not self.head:
            self.head = Node(item)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(item)

    def peek(self):
        if self.is_empty():
            raise IndexError
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur.data

    def pop(self):
        if self.is_empty():
            raise IndexError
        cur = self.head
        if not cur.next:
            result = cur.data
            self.head = None
            return result
        while cur.next.next:
            cur = cur.next
        result = cur.next
        cur.next = None
        return result.data

    def is_empty(self):
        if not self.head:
            return True
        return False

    def __len__(self):
        if not self.head:
            return 0
        cur = self.head
        counter = 0
        while cur:
            counter += 1
            cur = cur.next
        return counter

    def clear(self):
        self.head = None

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack1.push(x)

    def pop(self) -> int:
        while len(self.stack1) > 1:
            cur = self.stack1.pop()
            self.stack2.push(cur)
        result = self.stack1.pop()
        while self.stack2:
            cur = self.stack2.pop()
            self.stack1.push(cur)
        return result

    def peek(self) -> int:
        while len(self.stack1) > 1:
            cur = self.stack1.pop()
            self.stack2.push(cur)
        result = self.stack1.pop()
        self.stack2.push(result)
        while self.stack2:
            cur = self.stack2.pop()
            self.stack1.push(cur)
        return result

    def empty(self) -> bool:
        return self.stack1.is_empty()

    def __str__(self):
        return str(self.stack1)