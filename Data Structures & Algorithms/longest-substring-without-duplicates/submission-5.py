class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2 pointers i, j
        # i marks the beginning of a unique substring while j checks the next character is non-repeated
        # to check uniqueness, add all "seen characters" to a hash set with O(1) look up time
        n = len(s)
        if n == 0:
            return 0
        i = 0
        j = 0
        seen = set()
        max_length = 0
        while j < n:
            # if the next character is already in the set, lets just move i to j
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            max_length = max(max_length, len(seen))
            j += 1
        return max_length