class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # no child or no cookies
        if not s or not g:
            return 0
        g.sort()
        s.sort()
        # i is the child
        # j is the cookie
        # you try to give the child a cookie j
        # if the size doesnt make the child content => move j up -> if no more cookies -> break the loop
        # if the size make the child content -> move both i and j meaning you give the child the cookie and ready to give another cookie to the next child
        # since the child greed in incremental order, if the current cookie doesnt make the child content, it wont make the later child content
        i, j = 0, 0
        result = 0
        while i < len(g):
            # not content
            if s[j] < g[i]:
                j += 1
            else:
                i += 1
                j += 1
                result += 1
            # no more cookies to give
            if j == len(s):
                break
        return result
        
        