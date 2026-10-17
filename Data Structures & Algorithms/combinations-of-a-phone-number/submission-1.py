class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        combination = []
        # i is the digit that we're processing
        def dfs(i: int):
            if len(combination) == len(digits):
                result.append("".join(combination))
                return
            for j in digit_to_chars[digits[i]]:
                combination.append(j)
                dfs(i + 1)
                combination.pop()
        dfs(0)
        return result
