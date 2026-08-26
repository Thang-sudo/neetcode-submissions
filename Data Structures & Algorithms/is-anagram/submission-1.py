class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialize an list with size of 26 represents 26 characters in alphabetical table
        # assuming both s string and t string have the same size
        # iterate over the list of s, any character seen in s then plus 1, any number seen in t then - 1 in the "seen" list
        # after iterating the list, check all elements if they all equal to 0. If anything not equal to 0 then return False
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for i in range(len(s)):
            # find the s' character in counts list:
            counts[ord(s[i]) - ord("a")] += 1
            # find the t' character in counts list:
            counts[ord(t[i]) - ord("a")] -= 1
        for c in counts:
            if c != 0:
                return False
        return True
