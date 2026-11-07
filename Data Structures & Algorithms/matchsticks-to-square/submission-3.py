class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        # sort in descending order, so that if adding the next largest stick to the side exceed the target length then return False. Stop going for this path
        matchsticks.sort(reverse = True)
        sides = [0] * 4
        target_length = sum(matchsticks) // 4
        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            stick = matchsticks[i]
            # Try add stick to top
            for j in range(4):
                sides[j] += stick
                if sides[j] <= target_length and dfs(i + 1):
                    return True
                sides[j] -= stick
            return False
        return dfs(0)