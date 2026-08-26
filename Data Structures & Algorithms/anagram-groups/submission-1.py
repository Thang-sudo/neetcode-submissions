class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The main issue of this problem is to count frequency of characters in each string
        # Initialize "counts" dict, where key is a tuple of frequency and values is list of words
        # we use tuple because tuple is immutable and hashable, unlike a list
        # Iterate over the list of strings. For each, string count the frequency of characters. Save the frequency to list -> then turn to a tuple key in the dict
        # defaultdict: a dictionary automatically creates a default value when a key does not exist
        groups = defaultdict(list)
        for words in strs:
            counts = [0] * 26
            for i in words:
                counts[ord(i) - ord("a")] += 1
            groups[tuple(counts)].append(words)
        return list(groups.values())
