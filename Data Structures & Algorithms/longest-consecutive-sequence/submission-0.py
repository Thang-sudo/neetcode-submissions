class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Turn the list num into a set for O(1) look up
        # Iterate the list and check with the set if num - 1 in the set
        # If not, this would be the candidate for the sequence.
        # Keep checking num + 1 until it isn't in the set
        # Return the longest sequence
        nums_set = set(nums)
        max_length = 0
        for i in nums:
            # find the start of sequence
            if (i - 1) not in nums_set:
                sequence_length = 0;
                while (i in nums_set):
                    i += 1
                    sequence_length += 1
                if sequence_length > max_length:
                    max_length = sequence_length
        return max_length
        