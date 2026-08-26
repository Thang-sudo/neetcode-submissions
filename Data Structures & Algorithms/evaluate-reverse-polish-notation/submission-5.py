import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = []
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            if i in ops:
                second = stack.pop()
                first = stack.pop()
                result = int(ops[i](first, second))
                stack.append(result)
        return stack.pop()