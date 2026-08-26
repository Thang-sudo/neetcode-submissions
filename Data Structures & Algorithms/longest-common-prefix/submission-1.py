class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        matchPrefix = True
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    matchPrefix = False
            if matchPrefix:
                prefix += strs[0][i]
            else:
                break
        return prefix




        