import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+", "*", "-", "/"}
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
        }
        stack = []
        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            if i in operands:
                second = stack.pop()
                first = stack.pop()
                result = int(ops[i](first, second))
                stack.append(result)
        return stack.pop()