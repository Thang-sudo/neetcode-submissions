class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c1 = c2 = 0
        n1 = len(word1)
        n2 = len(word2)
        result = ""
        while c1 < n1 and c2 < n2:
            result += word1[c1]
            result += word2[c2]
            c1 += 1
            c2 += 1
        if c1 < n1:
            result += word1[c1:]
        if c2 < n2:
            result += word2[c2:]
        return result

        