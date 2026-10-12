class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combination = []
        def dfs(openN: int, closedN: int):
            if openN == n and closedN == n:
                res.append("".join(combination))
            # case pick open paren if we haven't used all the open paren
            if openN < n:
                combination.append("(")
                dfs(openN + 1, closedN)
                combination.pop()
            # case pick closed paren only if number of used closed paren doesn't exceed that of open paren
            if closedN < openN:
                combination.append(")")
                dfs(openN, closedN + 1)
                combination.pop()
        dfs(0, 0)
        return res