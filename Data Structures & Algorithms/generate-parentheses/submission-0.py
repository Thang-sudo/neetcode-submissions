class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        combination = []
        def dfs(openN: int, closedN: int):
            # If we used all available parentheses then we should add this string 
            if openN == n and closedN == n:
                res.append("".join(combination))
                return

            # Case where we choose open parenthese
            if openN < n:
                combination.append("(")
                dfs(openN + 1, closedN)
                combination.pop()
            if closedN < openN:
                # Case where we choose closed parenthese
                combination.append(")")
                dfs(openN, closedN + 1)
                combination.pop()
        dfs(0, 0)
        return res
