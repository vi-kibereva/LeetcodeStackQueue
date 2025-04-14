import ctypes
class Queue:
    INITIAL_SIZE = 3
    def __init__(self):
        py_obj = ctypes.py_object * self.INITIAL_SIZE
        self._data = py_obj()
        self.logical_size = 0
        self.physical_size = self.INITIAL_SIZE
        self.clear(None)

    def clear(self, value):
        for i in range(self.physical_size):
            self._data[i] = value

    def push(self, value):
        if self.logical_size == self.physical_size:
            self.extend()
        self._data[self.logical_size] = value
        self.logical_size += 1

    def extend(self):
        py_obj = ctypes.py_object * (self.physical_size *2)
        new_data = py_obj()
        for i in range(self.logical_size):
            new_data[i] = self._data[i]
        self._data = new_data
        self.physical_size *=2

    def peek(self):
        if self.logical_size == 0:
            raise IndexError
        return self._data[0]

    def pop(self):
        if self.logical_size == 0:
            raise IndexError
        result = self._data[0]
        self.logical_size -= 1
        for i in range(self.logical_size):
            self._data[i] = self._data[i+1]
        if self.logical_size <= self.physical_size/4 and self.physical_size//2 > self.INITIAL_SIZE:
            self.shrink()
        return result

    def shrink(self):
        py_obj = ctypes.py_object * int(self.physical_size//2)
        new_data = py_obj()
        for i in range(self.logical_size):
            new_data[i] = self._data[i]
        self._data = new_data
        self.physical_size //=2

    def __str__(self):
        result = ''
        for i in self:
            result += str(i)
        return result

    def __iter__(self):
        return self.next()

    def next(self):
        for i in range(self.logical_size):
            yield self._data[i]

    def __len__(self):
        return self.logical_size


class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.push(x)

    def pop(self) -> int:
        for i in range(len(self.q1)-1):
            a = self.q1.pop()
            self.q2.push(a)
        result = self.q1.pop()
        for i in range(len(self.q2)):
            a = self.q2.pop()
            self.q1.push(a)
        return result

    def __str__(self):
        return str(self.q1)

    def top(self) -> int:
        for i in range(len(self.q1)-1):
            a = self.q1.pop()
            self.q2.push(a)
        result = self.q1.pop()
        self.q2.push(result)
        for i in range(len(self.q2)):
            a = self.q2.pop()
            self.q1.push(a)
        return result

    def empty(self) -> bool:
        return len(self.q1) == 0

