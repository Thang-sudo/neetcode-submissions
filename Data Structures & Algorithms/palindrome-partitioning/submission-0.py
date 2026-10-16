class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        # for every character in string s. Keep trying to add the next character to the partition until they're no longer a valid palindrome
        def isValidPalindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        def dfs(i: int):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i, len(s)):
                if isValidPalindrome(i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return result
