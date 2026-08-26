class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # GOAL: find the shortest substring that contains all characters in string t with the same frequency
        # TRIGGER TO RECOGNIZE:
        # "shortest/ longest substring satisfy a constraint" + "contains all of X"
        # => variable size window (two pointers, expand right/ shrink left)
        # CORE IDEA:
        # Keep a signed "need" map to show how many more of a particular do I need to form a valid string
        # There are 3 cases for "need" map:
        # - need[i] > 0: I still need more of this character
        # - need[i] == 0: I have just right of this character
        # - need[i] < 0: this character is unecessary
        # To avoid iterating this "need" map for every iteration 
        # -> add an overal "needed_count" integer to keep track total of characters needed to form a substring
        # A substring becomes VALID when "needed_count" is 0
        # ALGORITHM:
        #   1. ledger = Counter(t); needed = len(t).
        #   2. Expand right over s:
        #        ledger[c] -= 1 (ALWAYS, so surplus goes negative)
        #        if ledger[c] >= 0: needed -= 1   # this copy actually filled a gap
        #   3. While needed == 0 (valid): record window length (right-left+1),
        #        then shrink left:
        #          ledger[s[left]] += 1
        #          if ledger[s[left]] >= 1: needed += 1   # removed a critical copy -> now invalid
        #          left += 1
        #   4. Track best by (start, length); slice s once at the end. inf => return ""
        # WHY DECREMENT ALWAYS: the ledger must mirror the real window contents so the
        #   LEFT pointer can tell a harmless extra (ledger stays <=0) from a critical
        #   removal (ledger crosses back to >=1). Without negatives you can't distinguish
        #   these (the "aa"/"aa" bug).
        #
        # COMPLEXITY: each char enters/leaves the window once -> O(n) time, O(alphabet) space.
        #
        # GOTCHAS:
        #   - window length is right-left+1 (inclusive), not right-left
        #   - "counted" boundary is ledger >= 0 after decrement (0 satisfies a need)
        #   - default answer = "" when no valid window (best_len stays inf)

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


