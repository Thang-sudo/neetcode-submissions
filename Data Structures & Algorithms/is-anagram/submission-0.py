class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both strings have same length first -> return False if not equal
        # Sort both array in the same order
        # have i, j pointer that iterate s, t strings. If there's a difference return False.
        # if completets the loop, then return True
        if len(s) != len (t):
            return False
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
