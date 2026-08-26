class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frequency_t = Counter(t)
        needed = len(t)
        shortest_substr = s
        found_valid = False
        best_len = float('inf')
        best_right = best_left = 0

        left = 0
        for right in range(len(s)):
            # if the new character in window belongs to t, then decrement needed
            frequency_t[s[right]] -= 1
            if frequency_t[s[right]] >= 0:
                needed -= 1
                # if this is a valid substring, we should try to remove as many extra characters as possible
            while needed == 0:
                found_valid = True
                if best_len > right - left:
                    best_len = right - left
                    best_right = right
                    best_left = left
                # shrink by moving the left pointer until the substring becomes invalid
                # check if we're removing a valid character
                frequency_t[s[left]] += 1
                if frequency_t[s[left]] >= 1:
                    needed += 1
                left += 1
        if best_len != float('inf'):
            return s[best_left : best_right + 1]
        else:
            return ""


