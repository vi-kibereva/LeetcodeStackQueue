from collections import deque, defaultdict
class FreqStack:
    '''
    Class for frequency stack
    '''
    def __init__(self):
        self._data = deque()
        self.counter = defaultdict(int)
    def push(self, val: int) -> None:
        '''
        Push
        '''
        self._data.append(val)
        self.counter[val] += 1
    def pop(self) -> int:
        '''
        Pop
        '''
        max_count = max(self.counter.values())
        temp = deque()
        for _ in range(len(self._data)):
            result = self._data.pop()
            if self.counter[result] == max_count:
                for _ in range(len(temp)):
                    self._data.append(temp.pop())
                self.counter[result] -=1
                return result
            else:
                temp.append(result)
