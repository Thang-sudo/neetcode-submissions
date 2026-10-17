class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []

        def dfs(i: int):
            if len(combination) == k:
                result.append(combination.copy())
                return
            for j in range(i, n + 1):
                combination.append(j)
                dfs(j + 1)
                combination.pop()
        dfs(1)
        return result


