class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combination = []
        # i represents the smallest number in the range allowed to add 
        def dfs(i: int):
            # if combination already has enough numbers, add it to the result array
            if len(combination) == k:
                result.append(combination.copy())
                return
            # Try every possible number in allowed range
            # we want to try from i to avoid duplicated combination
            for j in range(i, n + 1):
                # Add current j to this position in combination
                combination.append(j)
                # Recursively add digits to the next position in combination
                dfs(j + 1)
                # pop j so that we can replace it with j + 1 in the current position. This will allows us to form a new combination with no duplication
                combination.pop()
        dfs(1)
        return result


