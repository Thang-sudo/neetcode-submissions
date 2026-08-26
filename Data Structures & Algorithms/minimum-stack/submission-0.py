class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        
    def push(self, val: int) -> None:
        min_value = math.inf
        if len(self.stack):
            min_value = min(val, self.prefix[-2])
        else:
            min_value = val

        self.stack.append(val)
        self.prefix.extend([min_value, val])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            del self.prefix[-2:]

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.prefix[-2]
        return None
        
