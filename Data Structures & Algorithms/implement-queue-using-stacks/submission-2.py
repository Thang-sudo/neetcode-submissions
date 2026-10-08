class MyQueue:
    # Use 2 stacks. in_stack to contain the incoming order of element
    # out_stack contains the reverse order of in_stack, by popping all elements in in_stack and append them to the out_stack.
    # The first element to come off the queue is the last element of the out_stack
    # Therefore, we'll peek the last element in out stack or pop the last element of out_stack
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        # Get the reverse order
        if not self.out_stack:
            while self.in_stack:
                i = self.in_stack.pop()
                self.out_stack.append(i)
        return self.out_stack.pop()
        
    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        if not self.in_stack and not self.out_stack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()