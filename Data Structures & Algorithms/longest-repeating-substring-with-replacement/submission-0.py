
class FrequencyTracker:
    def __init__(self):
        self.max_freq = 0
        self.freq_key = defaultdict(set) # frequency -> set of keys => need this when removing character from substring
        self.key_freq = defaultdict(int) # key -> frequency

    def increment(self, key):
        f = self.key_freq[key]
        # frequency updated -> need to move key to the next frequency bucket
        if f:
            self.freq_key[f].discard(key)
        self.freq_key[f + 1].add(key)
        # update frequency for this character
        self.key_freq[key] += 1
        self.max_freq = max(self.key_freq[key], self.max_freq)
    
    def decrement(self, key):
        f = self.key_freq[key]
        if f == 0:
            return
        # Move key to lower frequency bucket if possible
        if f:
            self.freq_key[f].discard(key)
        if f - 1 > 0:
            self.freq_key[f - 1].add(key)
            # update frequency for this character
            self.key_freq[key] -= 1
        else:
            # Remove from key-frequency map if frequency reaches 0
            del self.key_freq[key]
        # Update the max value if there's no other character in top buckets
        while self.max_freq > 0 and len(self.freq_key[self.max_freq]) == 0:
            self.max_freq -= 1

    def get_max(self):
        # Return tuple of (key, max_key)
        return self.max_freq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        tracker = FrequencyTracker()
        max_length = 0
        n = len(s)
        if n == 1:
            return 1

        i = j = 0
        while j < n:
            # Add character to current substring
            tracker.increment(s[j])
            substr_length = j + 1 - i
            replacements = substr_length - tracker.get_max()
            # Check if we have enough replacements
            while replacements > k:
                # Remove the character from substring until we have the next replacements
                tracker.decrement(s[i])
                i += 1
                substr_length = j - i
                replacements = substr_length - tracker.get_max()
            max_length = max(max_length, j + 1 - i)
            j += 1
        
        return max_length
        


        
    
            

