class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # have a seen dictionary where key is the position of first string anagram group and value is the list of anagram groups. 
        # iterate the strs list then for each member, compare with first element of the list. If match, put in the list. If not, put in the new list
        results = []
        for i in strs:
            hasGroup = False
            for r in results:
                if self.isAnagram(i, r[0]):
                    r.append(i)
                    hasGroup = True
                    break
            if not hasGroup:
                results.append([i])
        return results

    def isAnagram(self, n: str, m: str):
        if len(n) != len(m):
            return False
        counts = [0] * 26
        for i in range(len(n)):
            counts[ord(n[i]) - ord("a")] += 1
            counts[ord(m[i]) - ord("a")] -= 1
        for j in counts:
            if j != 0:
                return False
        return True
